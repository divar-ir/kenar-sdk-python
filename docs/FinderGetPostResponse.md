# FinderGetPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_data** | [**GetPostResponseBusinessData**](GetPostResponseBusinessData.md) |  | [optional] 
**category** | **str** |  | [optional] 
**chat_enabled** | **bool** |  | [optional] 
**city** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**district** | **str** |  | [optional] 
**first_published_at** | **datetime** |  | [optional] 
**state** | [**FinderPostExtState**](FinderPostExtState.md) |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.finder_get_post_response import FinderGetPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FinderGetPostResponse from a JSON string
finder_get_post_response_instance = FinderGetPostResponse.from_json(json)
# print the JSON string representation of the object
print(FinderGetPostResponse.to_json())

# convert the object into a dict
finder_get_post_response_dict = finder_get_post_response_instance.to_dict()
# create an instance of FinderGetPostResponse from a dict
finder_get_post_response_from_dict = FinderGetPostResponse.from_dict(finder_get_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


