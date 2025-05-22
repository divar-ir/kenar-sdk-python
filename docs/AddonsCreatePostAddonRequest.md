# AddonsCreatePostAddonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_in_spec** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**selector** | [**AddonsAddonSelector**](AddonsAddonSelector.md) |  | [optional] 
**semantic** | **Dict[str, str]** |  | [optional] 
**semantic_sensitives** | **List[str]** |  | [optional] 
**token** | **str** |  | [optional] 
**widgets** | **object** |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_create_post_addon_request import AddonsCreatePostAddonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsCreatePostAddonRequest from a JSON string
addons_create_post_addon_request_instance = AddonsCreatePostAddonRequest.from_json(json)
# print the JSON string representation of the object
print(AddonsCreatePostAddonRequest.to_json())

# convert the object into a dict
addons_create_post_addon_request_dict = addons_create_post_addon_request_instance.to_dict()
# create an instance of AddonsCreatePostAddonRequest from a dict
addons_create_post_addon_request_from_dict = AddonsCreatePostAddonRequest.from_dict(addons_create_post_addon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


