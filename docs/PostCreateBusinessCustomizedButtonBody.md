# PostCreateBusinessCustomizedButtonBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customized_button** | [**PostCustomizedButton**](PostCustomizedButton.md) |  | 

## Example

```python
from kenar_api_client.models.post_create_business_customized_button_body import PostCreateBusinessCustomizedButtonBody

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateBusinessCustomizedButtonBody from a JSON string
post_create_business_customized_button_body_instance = PostCreateBusinessCustomizedButtonBody.from_json(json)
# print the JSON string representation of the object
print(PostCreateBusinessCustomizedButtonBody.to_json())

# convert the object into a dict
post_create_business_customized_button_body_dict = post_create_business_customized_button_body_instance.to_dict()
# create an instance of PostCreateBusinessCustomizedButtonBody from a dict
post_create_business_customized_button_body_from_dict = PostCreateBusinessCustomizedButtonBody.from_dict(post_create_business_customized_button_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


