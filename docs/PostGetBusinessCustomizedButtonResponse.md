# PostGetBusinessCustomizedButtonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**app_slug** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**type** | [**PostCustomizedButtonType**](PostCustomizedButtonType.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.post_get_business_customized_button_response import PostGetBusinessCustomizedButtonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetBusinessCustomizedButtonResponse from a JSON string
post_get_business_customized_button_response_instance = PostGetBusinessCustomizedButtonResponse.from_json(json)
# print the JSON string representation of the object
print(PostGetBusinessCustomizedButtonResponse.to_json())

# convert the object into a dict
post_get_business_customized_button_response_dict = post_get_business_customized_button_response_instance.to_dict()
# create an instance of PostGetBusinessCustomizedButtonResponse from a dict
post_get_business_customized_button_response_from_dict = PostGetBusinessCustomizedButtonResponse.from_dict(post_get_business_customized_button_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


