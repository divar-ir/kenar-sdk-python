# coding: utf-8

"""
    Kenar API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kenar_api_client.models.apps_app_status import AppsAppStatus
from kenar_api_client.models.apps_service_tag import AppsServiceTag
from kenar_api_client.models.apps_service_type import AppsServiceType
from typing import Optional, Set
from typing_extensions import Self

class AppsApp(BaseModel):
    """
    AppsApp
    """ # noqa: E501
    avatar: Optional[StrictStr] = None
    display: Optional[StrictStr] = None
    divar_identification_key: Optional[StrictStr] = None
    service_tags: Optional[List[AppsServiceTag]] = None
    service_type: Optional[AppsServiceType] = None
    slug: Optional[StrictStr] = None
    status: Optional[AppsAppStatus] = None
    __properties: ClassVar[List[str]] = ["avatar", "display", "divar_identification_key", "service_tags", "service_type", "slug", "status"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AppsApp from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppsApp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avatar": obj.get("avatar"),
            "display": obj.get("display"),
            "divar_identification_key": obj.get("divar_identification_key"),
            "service_tags": obj.get("service_tags"),
            "service_type": obj.get("service_type"),
            "slug": obj.get("slug"),
            "status": AppsAppStatus.from_dict(obj["status"]) if obj.get("status") is not None else None
        })
        return _obj


