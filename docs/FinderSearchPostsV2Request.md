# FinderSearchPostsV2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**districts** | **List[str]** |  | [optional] 
**query** | [**FinderSearchQuery**](FinderSearchQuery.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.finder_search_posts_v2_request import FinderSearchPostsV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of FinderSearchPostsV2Request from a JSON string
finder_search_posts_v2_request_instance = FinderSearchPostsV2Request.from_json(json)
# print the JSON string representation of the object
print(FinderSearchPostsV2Request.to_json())

# convert the object into a dict
finder_search_posts_v2_request_dict = finder_search_posts_v2_request_instance.to_dict()
# create an instance of FinderSearchPostsV2Request from a dict
finder_search_posts_v2_request_from_dict = FinderSearchPostsV2Request.from_dict(finder_search_posts_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


