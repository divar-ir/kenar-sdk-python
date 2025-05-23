# coding: utf-8

"""
    Kenar API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ManagementPreset(str, Enum):
    """
    ManagementPreset
    """

    """
    allowed enum values
    """
    LIGHT = 'LIGHT'
    CRAFTSMEN = 'CRAFTSMEN'
    MOBILE_PHONES = 'MOBILE_PHONES'
    APARTMENT_SELL = 'APARTMENT_SELL'
    SUITE_APARTMENT = 'SUITE_APARTMENT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ManagementPreset from a JSON string"""
        return cls(json.loads(json_str))


