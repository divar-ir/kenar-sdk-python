# AddonsCreateUserAddonV2Body


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** |  | [optional] 
**cost** | **int** |  | [optional] 
**phone** | **str** |  | [optional] 
**semantic** | **Dict[str, str]** |  | [optional] 
**ticket_uuid** | **str** |  | [optional] 
**widgets** | [**List[AddonsWidget]**](AddonsWidget.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_create_user_addon_v2_body import AddonsCreateUserAddonV2Body

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsCreateUserAddonV2Body from a JSON string
addons_create_user_addon_v2_body_instance = AddonsCreateUserAddonV2Body.from_json(json)
# print the JSON string representation of the object
print(AddonsCreateUserAddonV2Body.to_json())

# convert the object into a dict
addons_create_user_addon_v2_body_dict = addons_create_user_addon_v2_body_instance.to_dict()
# create an instance of AddonsCreateUserAddonV2Body from a dict
addons_create_user_addon_v2_body_from_dict = AddonsCreateUserAddonV2Body.from_dict(addons_create_user_addon_v2_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


