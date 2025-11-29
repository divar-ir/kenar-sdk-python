# PostCustomizedButton


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AddonsAction**](AddonsAction.md) |  | 
**type** | [**PostCustomizedButtonType**](PostCustomizedButtonType.md) |  | 

## Example

```python
from kenar_api_client.models.post_customized_button import PostCustomizedButton

# TODO update the JSON string below
json = "{}"
# create an instance of PostCustomizedButton from a JSON string
post_customized_button_instance = PostCustomizedButton.from_json(json)
# print the JSON string representation of the object
print(PostCustomizedButton.to_json())

# convert the object into a dict
post_customized_button_dict = post_customized_button_instance.to_dict()
# create an instance of PostCustomizedButton from a dict
post_customized_button_from_dict = PostCustomizedButton.from_dict(post_customized_button_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


