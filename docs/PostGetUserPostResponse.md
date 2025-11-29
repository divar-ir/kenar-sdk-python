# PostGetUserPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_data** | [**PostGetUserPostResponseBusinessData**](PostGetUserPostResponseBusinessData.md) |  | [optional] 
**category_data** | **object** |  | [optional] 
**general_data** | [**PostPostGeneralData**](PostPostGeneralData.md) |  | [optional] 
**reject_reason** | **str** |  | [optional] 
**state** | [**OpenPlatformpostPostState**](OpenPlatformpostPostState.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.post_get_user_post_response import PostGetUserPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetUserPostResponse from a JSON string
post_get_user_post_response_instance = PostGetUserPostResponse.from_json(json)
# print the JSON string representation of the object
print(PostGetUserPostResponse.to_json())

# convert the object into a dict
post_get_user_post_response_dict = post_get_user_post_response_instance.to_dict()
# create an instance of PostGetUserPostResponse from a dict
post_get_user_post_response_from_dict = PostGetUserPostResponse.from_dict(post_get_user_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


