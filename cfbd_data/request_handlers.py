import boto3
import urllib
import request_utilities.aws_integration as aws_integration

def ddb_interface(event, context):
    print(event)

    tableKey = event['data_type'] + 'Table'
    print(f"tableKey: {tableKey}")
    table = aws_integration.sms_get_parameter_value(key=tableKey)

    key = event['key']
    request_type = event['request_type']

    print(f"table: {table}")
    print(f"key: {key}")
    print(f"request_type: {request_type}")

    if request_type == 'getItem':
        item = aws_integration.ddb_get_item(table=table, primary_key=key)
        return item

    if request_type == 'putItem':
        added_item = aws_integration.ddb_put_item(table=table, item_values=key)
        return added_item

    if request_type == 'updateItem':
        update_attribute = event['update_attribute']
        value_dict = event['value_dict']
        increment = True if event['increment'] == 'True' else False
        print(f"update_attribute: {update_attribute}")
        print(f"value_dict: {value_dict}")
        print(f"increment: {increment}")

        update_val = aws_integration.ddb_update_item(table=table,
                                     primary_key=key,
                                     update_attribute=update_attribute,
                                     value_dict=value_dict,
                                     increment=increment)
        return update_val

    if request_type == 'deleteItem':
        delete_val = aws_integration.ddb_delete_item(table=table, primary_key=key)
        return delete_val

def sns_publish(event, context):
    print('Loading function')

    print(f"event: {event}")
    print(f"context: {context}")
    execution_context = event['ExecutionContext']
    print(f"executionContext: {execution_context}")
    user_id = execution_context['Execution']['Input']['userId']['S']
    amount = execution_context['Execution']['Input']['amount']['N']
    reason = execution_context['Execution']['Input']['message']['S']
    print(f"user_id: {user_id}")
    print(f"amount: {amount}")
    print(f"reason: {reason}")

    execution_name = execution_context['Execution']['Name']
    print(f"execution_name: {execution_name}")

    state_machine_name = execution_context['StateMachine']['Name']
    print(f"state_machine_name: {state_machine_name}")

    task_token = execution_context['Task']['Token']
    print(f"task_token: {task_token}")

    email_sns_topic = event['SnsTopic']
    print(f"email_sns_topic: {email_sns_topic}")

    api_gw_endpoint = event['APIGatewayEndpoint']
    print(f"api_gw_endpoint: {api_gw_endpoint}")

    parsed_task_token = urllib.parse.quote(task_token, safe='()*!\'')

    approve_endpoint = f"{api_gw_endpoint}/execution?action=approve&ex={execution_name}&sm={state_machine_name}&taskToken={parsed_task_token}"
    print(f"approve_endpoint: {approve_endpoint}")

    reject_endpoint = f"{api_gw_endpoint}/execution?action=reject&ex={execution_name}&sm={state_machine_name}&taskToken={parsed_task_token}"
    print(f"reject_endpoint: {reject_endpoint}")

    email_subject = "Required approval for OST Funding Request"

    email_message = f"Welcome! \n\n"
    email_message += f"Approval has been requested for an OST Analytics Funding Request. \n\n"
    email_message += f"Please check the following information and click \"Approve\" link if you want to approve. \n\n"
    email_message += f"Execution Name -> {execution_name} \n\n"
    email_message += f"Requested Token Amount: {amount} \n\n"
    email_message += f"Request Reason: {reason} \n\n"
    email_message += f"Approve {approve_endpoint} \n\n"
    email_message += f"Reject {reject_endpoint} \n\n"
    email_message += f"Thanks for using Step functions!"

    sns_response = aws_integration.sns_publish(email_sns_topic = email_sns_topic,
                                       email_subject = email_subject,
                                       email_message = email_message)

    print(f"sns_response: {sns_response}")

    return sns_response


def request_approval(event, context):
    print(f"event: {event}")
    action = event['query']['action']
    task_token = event['query']['taskToken']
    state_machine_name = event['query']['sm']
    execution_name = event['query']['ex']
    invoked_function_arn = context.invoked_function_arn

    if action == 'approve':
        message = {"Status": "Approved! Task approved"}
    elif action == 'reject':
        message = {"Status": "Rejected! Task rejected"}
    else:
        print(f"Unrecognized action. Expected: approve, reject.")
        return {"Status": "Failed to process the request. Unrecognized Action."}

    response = aws_integration.step_function_send_success(output=message,
                                               task_token=task_token,
                                               invoked_function_arn=invoked_function_arn,
                                               state_machine_name=state_machine_name,
                                               execution_name=execution_name)
    print(f"response: {response}")

    return response



