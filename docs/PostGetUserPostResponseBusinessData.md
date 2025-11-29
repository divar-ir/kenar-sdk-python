# PostGetUserPostResponseBusinessData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_name** | **str** |  | [optional] 
**business_type** | [**PremiumPanelBusinessDataSubBusinessType**](PremiumPanelBusinessDataSubBusinessType.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.post_get_user_post_response_business_data import PostGetUserPostResponseBusinessData

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetUserPostResponseBusinessData from a JSON string
post_get_user_post_response_business_data_instance = PostGetUserPostResponseBusinessData.from_json(json)
# print the JSON string representation of the object
print(PostGetUserPostResponseBusinessData.to_json())

# convert the object into a dict
post_get_user_post_response_business_data_dict = post_get_user_post_response_business_data_instance.to_dict()
# create an instance of PostGetUserPostResponseBusinessData from a dict
post_get_user_post_response_business_data_from_dict = PostGetUserPostResponseBusinessData.from_dict(post_get_user_post_response_business_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


