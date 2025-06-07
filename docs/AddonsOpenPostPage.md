# AddonsOpenPostPage

An action to open a post page in the app

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_token** | **str** | Token of the post to open | 

## Example

```python
from kenar_api_client.models.addons_open_post_page import AddonsOpenPostPage

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsOpenPostPage from a JSON string
addons_open_post_page_instance = AddonsOpenPostPage.from_json(json)
# print the JSON string representation of the object
print(AddonsOpenPostPage.to_json())

# convert the object into a dict
addons_open_post_page_dict = addons_open_post_page_instance.to_dict()
# create an instance of AddonsOpenPostPage from a dict
addons_open_post_page_from_dict = AddonsOpenPostPage.from_dict(addons_open_post_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


