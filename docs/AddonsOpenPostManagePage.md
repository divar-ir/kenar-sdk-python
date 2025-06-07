# AddonsOpenPostManagePage

An action to open a post management page in the app

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_token** | **str** | Token of the post to redirect to its management page | 

## Example

```python
from kenar_api_client.models.addons_open_post_manage_page import AddonsOpenPostManagePage

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsOpenPostManagePage from a JSON string
addons_open_post_manage_page_instance = AddonsOpenPostManagePage.from_json(json)
# print the JSON string representation of the object
print(AddonsOpenPostManagePage.to_json())

# convert the object into a dict
addons_open_post_manage_page_dict = addons_open_post_manage_page_instance.to_dict()
# create an instance of AddonsOpenPostManagePage from a dict
addons_open_post_manage_page_from_dict = AddonsOpenPostManagePage.from_dict(addons_open_post_manage_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


