import boto3
import json

dynamodb_client = boto3.client('dynamodb')
ssm_client = boto3.client('ssm')
sns_client = boto3.client('sns')
step_functions_client = boto3.client('stepfunctions')
def ddb_get_item(table: str,
                 primary_key: dict):
    item = dynamodb_client.get_item(TableName=table,
                                    Key=primary_key)
    return item


def ddb_put_item(table: str,
                 item_values: dict):
    response = dynamodb_client.put_item(TableName=table,
                                        Item=item_values)
    return response


def ddb_update_item(table: str,
                    primary_key: dict,
                    update_attribute: str,
                    value_dict: dict,
                    increment: bool = False,
                    return_values: str = "UPDATED_NEW"):
    if increment:
        update_expression = f"set {update_attribute} = :value + {update_attribute}"
    else:
        update_expression = f"set {update_attribute} = :value"

    expression_attribute_values = {':value': value_dict}

    print(f"update_expression: {update_expression}")
    print(f"expression_attribute_values: {expression_attribute_values}")

    updated_val = dynamodb_client.update_item(TableName=table,
                                              Key=primary_key,
                                              UpdateExpression=update_expression,
                                              ExpressionAttributeValues=expression_attribute_values,
                                              ReturnValues=return_values)

    return updated_val


def ddb_delete_item(table: str,
                    primary_key: dict):
    deleted_val = dynamodb_client.delete_item(TableName=table,
                                              Key=primary_key)
    return deleted_val

def sms_get_parameter_value(key):
    parameter = ssm_client.get_parameter(Name=key, WithDecryption=True)
    value = parameter['Parameter']['Value']
    return value
def sns_publish(email_sns_topic: str,
                email_subject: str,
                email_message: str):

    response = sns_client.publish(TopicArn = email_sns_topic,
                       Subject = email_subject,
                       Message = email_message)
    return response

def redirect_to_step_functions(lambda_arn, state_machine_name, execution_name):
    lambda_arn_tokens = lambda_arn.split(':')
    print(f"lambdaArnTokens: {lambda_arn_tokens}")

    partition = lambda_arn_tokens[1]
    region = lambda_arn_tokens[3]
    account_id = lambda_arn_tokens[4]
    print(f"partition: {partition}")
    print(f"region: {region}")
    print(f"accountId: {account_id}")

    execution_arn = f"arn:{partition}:states:{region}:{account_id}:execution:{state_machine_name}:{execution_name}"
    print(f"execution_arn: {execution_arn}")

    url = f"https://console.aws.amazon.com/states/home?region={region}#/executions/details/{execution_arn}"

    return {'statusCode': 303,
            'headers': {'Location': url}}

def step_function_send_success(output: dict,
                               task_token: str,
                               invoked_function_arn: str,
                               state_machine_name: str,
                               execution_name: str):
    output_json = json.dumps(output)
    try:
        step_functions_client.send_task_success(taskToken=task_token, output=output_json)
    except Exception as e:
        return f"error: {e}"

    return redirect_to_step_functions(invoked_function_arn, state_machine_name, execution_name)
