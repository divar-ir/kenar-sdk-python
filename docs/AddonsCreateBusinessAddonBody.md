# AddonsCreateBusinessAddonBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widgets** | [**List[AddonsWidget]**](AddonsWidget.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_create_business_addon_body import AddonsCreateBusinessAddonBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsCreateBusinessAddonBody from a JSON string
addons_create_business_addon_body_instance = AddonsCreateBusinessAddonBody.from_json(json)
# print the JSON string representation of the object
print(AddonsCreateBusinessAddonBody.to_json())

# convert the object into a dict
addons_create_business_addon_body_dict = addons_create_business_addon_body_instance.to_dict()
# create an instance of AddonsCreateBusinessAddonBody from a dict
addons_create_business_addon_body_from_dict = AddonsCreateBusinessAddonBody.from_dict(addons_create_business_addon_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


