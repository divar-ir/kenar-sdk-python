# AddonsCreatePostAddonV2Body


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widgets** | [**List[AddonsWidget]**](AddonsWidget.md) |  | [optional] 
**semantic** | **Dict[str, str]** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_create_post_addon_v2_body import AddonsCreatePostAddonV2Body

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsCreatePostAddonV2Body from a JSON string
addons_create_post_addon_v2_body_instance = AddonsCreatePostAddonV2Body.from_json(json)
# print the JSON string representation of the object
print(AddonsCreatePostAddonV2Body.to_json())

# convert the object into a dict
addons_create_post_addon_v2_body_dict = addons_create_post_addon_v2_body_instance.to_dict()
# create an instance of AddonsCreatePostAddonV2Body from a dict
addons_create_post_addon_v2_body_from_dict = AddonsCreatePostAddonV2Body.from_dict(addons_create_post_addon_v2_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


