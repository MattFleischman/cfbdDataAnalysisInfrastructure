# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.11
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class PlayerSearchResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'team': 'str',
        'name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'weight': 'int',
        'height': 'int',
        'jersey': 'int',
        'position': 'str',
        'hometown': 'str',
        'team_color': 'str',
        'team_color_secondary': 'str'
    }

    attribute_map = {
        'id': 'id',
        'team': 'team',
        'name': 'name',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'weight': 'weight',
        'height': 'height',
        'jersey': 'jersey',
        'position': 'position',
        'hometown': 'hometown',
        'team_color': 'teamColor',
        'team_color_secondary': 'teamColorSecondary'
    }

    def __init__(self, id=None, team=None, name=None, first_name=None, last_name=None, weight=None, height=None, jersey=None, position=None, hometown=None, team_color=None, team_color_secondary=None, _configuration=None):  # noqa: E501
        """PlayerSearchResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._team = None
        self._name = None
        self._first_name = None
        self._last_name = None
        self._weight = None
        self._height = None
        self._jersey = None
        self._position = None
        self._hometown = None
        self._team_color = None
        self._team_color_secondary = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if team is not None:
            self.team = team
        if name is not None:
            self.name = name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if weight is not None:
            self.weight = weight
        if height is not None:
            self.height = height
        if jersey is not None:
            self.jersey = jersey
        if position is not None:
            self.position = position
        if hometown is not None:
            self.hometown = hometown
        if team_color is not None:
            self.team_color = team_color
        if team_color_secondary is not None:
            self.team_color_secondary = team_color_secondary

    @property
    def id(self):
        """Gets the id of this PlayerSearchResult.  # noqa: E501


        :return: The id of this PlayerSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlayerSearchResult.


        :param id: The id of this PlayerSearchResult.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def team(self):
        """Gets the team of this PlayerSearchResult.  # noqa: E501


        :return: The team of this PlayerSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PlayerSearchResult.


        :param team: The team of this PlayerSearchResult.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def name(self):
        """Gets the name of this PlayerSearchResult.  # noqa: E501


        :return: The name of this PlayerSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerSearchResult.


        :param name: The name of this PlayerSearchResult.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def first_name(self):
        """Gets the first_name of this PlayerSearchResult.  # noqa: E501


        :return: The first_name of this PlayerSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PlayerSearchResult.


        :param first_name: The first_name of this PlayerSearchResult.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this PlayerSearchResult.  # noqa: E501


        :return: The last_name of this PlayerSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PlayerSearchResult.


        :param last_name: The last_name of this PlayerSearchResult.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def weight(self):
        """Gets the weight of this PlayerSearchResult.  # noqa: E501


        :return: The weight of this PlayerSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this PlayerSearchResult.


        :param weight: The weight of this PlayerSearchResult.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def height(self):
        """Gets the height of this PlayerSearchResult.  # noqa: E501


        :return: The height of this PlayerSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this PlayerSearchResult.


        :param height: The height of this PlayerSearchResult.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def jersey(self):
        """Gets the jersey of this PlayerSearchResult.  # noqa: E501


        :return: The jersey of this PlayerSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._jersey

    @jersey.setter
    def jersey(self, jersey):
        """Sets the jersey of this PlayerSearchResult.


        :param jersey: The jersey of this PlayerSearchResult.  # noqa: E501
        :type: int
        """

        self._jersey = jersey

    @property
    def position(self):
        """Gets the position of this PlayerSearchResult.  # noqa: E501


        :return: The position of this PlayerSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PlayerSearchResult.


        :param position: The position of this PlayerSearchResult.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def hometown(self):
        """Gets the hometown of this PlayerSearchResult.  # noqa: E501


        :return: The hometown of this PlayerSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        """Sets the hometown of this PlayerSearchResult.


        :param hometown: The hometown of this PlayerSearchResult.  # noqa: E501
        :type: str
        """

        self._hometown = hometown

    @property
    def team_color(self):
        """Gets the team_color of this PlayerSearchResult.  # noqa: E501


        :return: The team_color of this PlayerSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._team_color

    @team_color.setter
    def team_color(self, team_color):
        """Sets the team_color of this PlayerSearchResult.


        :param team_color: The team_color of this PlayerSearchResult.  # noqa: E501
        :type: str
        """

        self._team_color = team_color

    @property
    def team_color_secondary(self):
        """Gets the team_color_secondary of this PlayerSearchResult.  # noqa: E501


        :return: The team_color_secondary of this PlayerSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._team_color_secondary

    @team_color_secondary.setter
    def team_color_secondary(self, team_color_secondary):
        """Sets the team_color_secondary of this PlayerSearchResult.


        :param team_color_secondary: The team_color_secondary of this PlayerSearchResult.  # noqa: E501
        :type: str
        """

        self._team_color_secondary = team_color_secondary

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PlayerSearchResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PlayerSearchResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlayerSearchResult):
            return True

        return self.to_dict() != other.to_dict()
