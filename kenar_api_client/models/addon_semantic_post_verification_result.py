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


class AddonSemanticPostVerificationResult(str, Enum):
    """
    AddonSemanticPostVerificationResult
    """

    """
    allowed enum values
    """
    POST_INFORMATION_MATCHED = 'POST_INFORMATION_MATCHED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AddonSemanticPostVerificationResult from a JSON string"""
        return cls(json.loads(json_str))


