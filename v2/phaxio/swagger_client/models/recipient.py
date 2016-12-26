# coding: utf-8

"""
    Phaxio API

    API Definition for Phaxio

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Recipient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, phone_number=None, status=None, completed_at=None, error_type=None, error_message=None, error_id=None):
        """
        Recipient - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'phone_number': 'str',
            'status': 'str',
            'completed_at': 'str',
            'error_type': 'str',
            'error_message': 'str',
            'error_id': 'int'
        }

        self.attribute_map = {
            'phone_number': 'phone_number',
            'status': 'status',
            'completed_at': 'completed_at',
            'error_type': 'error_type',
            'error_message': 'error_message',
            'error_id': 'error_id'
        }

        self._phone_number = phone_number
        self._status = status
        self._completed_at = completed_at
        self._error_type = error_type
        self._error_message = error_message
        self._error_id = error_id

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Recipient.

        :return: The phone_number of this Recipient.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Recipient.

        :param phone_number: The phone_number of this Recipient.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def status(self):
        """
        Gets the status of this Recipient.

        :return: The status of this Recipient.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Recipient.

        :param status: The status of this Recipient.
        :type: str
        """
        allowed_values = ["queued", "pendingbatch", "inprogress", "success", "failure", "partialsuccess"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def completed_at(self):
        """
        Gets the completed_at of this Recipient.

        :return: The completed_at of this Recipient.
        :rtype: str
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """
        Sets the completed_at of this Recipient.

        :param completed_at: The completed_at of this Recipient.
        :type: str
        """

        self._completed_at = completed_at

    @property
    def error_type(self):
        """
        Gets the error_type of this Recipient.

        :return: The error_type of this Recipient.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """
        Sets the error_type of this Recipient.

        :param error_type: The error_type of this Recipient.
        :type: str
        """

        self._error_type = error_type

    @property
    def error_message(self):
        """
        Gets the error_message of this Recipient.

        :return: The error_message of this Recipient.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this Recipient.

        :param error_message: The error_message of this Recipient.
        :type: str
        """

        self._error_message = error_message

    @property
    def error_id(self):
        """
        Gets the error_id of this Recipient.

        :return: The error_id of this Recipient.
        :rtype: int
        """
        return self._error_id

    @error_id.setter
    def error_id(self, error_id):
        """
        Sets the error_id of this Recipient.

        :param error_id: The error_id of this Recipient.
        :type: int
        """

        self._error_id = error_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other