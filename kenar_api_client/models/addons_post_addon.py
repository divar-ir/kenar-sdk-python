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
from kenar_api_client.models.addons_addon_linkage import AddonsAddonLinkage
from kenar_api_client.models.addons_addon_meta_data import AddonsAddonMetaData
from kenar_api_client.models.addons_addon_secondary_links import AddonsAddonSecondaryLinks
from kenar_api_client.models.addons_addon_selector import AddonsAddonSelector
from kenar_api_client.models.addons_addon_semantic import AddonsAddonSemantic
from kenar_api_client.models.apps_app import AppsApp
from typing import Optional, Set
from typing_extensions import Self

class AddonsPostAddon(BaseModel):
    """
    AddonsPostAddon
    """ # noqa: E501
    app: Optional[AppsApp] = None
    linkage: Optional[AddonsAddonLinkage] = None
    meta_data: Optional[AddonsAddonMetaData] = None
    score: Optional[StrictStr] = None
    secondary_links: Optional[AddonsAddonSecondaryLinks] = None
    selector: Optional[AddonsAddonSelector] = None
    semantic: Optional[Dict[str, StrictStr]] = None
    semantic_data: Optional[AddonsAddonSemantic] = None
    semantic_sensitives: Optional[List[StrictStr]] = None
    sensitive_semantic: Optional[Dict[str, StrictStr]] = None
    token: Optional[StrictStr] = None
    widgets: Optional[Dict[str, Any]] = None
    widgets_semantic: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["app", "linkage", "meta_data", "score", "secondary_links", "selector", "semantic", "semantic_data", "semantic_sensitives", "sensitive_semantic", "token", "widgets", "widgets_semantic"]

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
        """Create an instance of AddonsPostAddon from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of app
        if self.app:
            _dict['app'] = self.app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of meta_data
        if self.meta_data:
            _dict['meta_data'] = self.meta_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary_links
        if self.secondary_links:
            _dict['secondary_links'] = self.secondary_links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of selector
        if self.selector:
            _dict['selector'] = self.selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of semantic_data
        if self.semantic_data:
            _dict['semantic_data'] = self.semantic_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddonsPostAddon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app": AppsApp.from_dict(obj["app"]) if obj.get("app") is not None else None,
            "linkage": obj.get("linkage"),
            "meta_data": AddonsAddonMetaData.from_dict(obj["meta_data"]) if obj.get("meta_data") is not None else None,
            "score": obj.get("score"),
            "secondary_links": AddonsAddonSecondaryLinks.from_dict(obj["secondary_links"]) if obj.get("secondary_links") is not None else None,
            "selector": AddonsAddonSelector.from_dict(obj["selector"]) if obj.get("selector") is not None else None,
            "semantic": obj.get("semantic"),
            "semantic_data": AddonsAddonSemantic.from_dict(obj["semantic_data"]) if obj.get("semantic_data") is not None else None,
            "semantic_sensitives": obj.get("semantic_sensitives"),
            "sensitive_semantic": obj.get("sensitive_semantic"),
            "token": obj.get("token"),
            "widgets": obj.get("widgets"),
            "widgets_semantic": obj.get("widgets_semantic")
        })
        return _obj


