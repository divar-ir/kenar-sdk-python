# PostGetPostStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chats** | [**GetPostStatsResponsePostStats**](GetPostStatsResponsePostStats.md) |  | [optional] 
**impressions** | [**GetPostStatsResponsePostStats**](GetPostStatsResponsePostStats.md) |  | [optional] 
**views** | [**GetPostStatsResponsePostStats**](GetPostStatsResponsePostStats.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.post_get_post_stats_response import PostGetPostStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGetPostStatsResponse from a JSON string
post_get_post_stats_response_instance = PostGetPostStatsResponse.from_json(json)
# print the JSON string representation of the object
print(PostGetPostStatsResponse.to_json())

# convert the object into a dict
post_get_post_stats_response_dict = post_get_post_stats_response_instance.to_dict()
# create an instance of PostGetPostStatsResponse from a dict
post_get_post_stats_response_from_dict = PostGetPostStatsResponse.from_dict(post_get_post_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


