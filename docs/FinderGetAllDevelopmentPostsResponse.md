# FinderGetAllDevelopmentPostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**development_posts** | [**List[ManagementDevelopmentPost]**](ManagementDevelopmentPost.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.finder_get_all_development_posts_response import FinderGetAllDevelopmentPostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FinderGetAllDevelopmentPostsResponse from a JSON string
finder_get_all_development_posts_response_instance = FinderGetAllDevelopmentPostsResponse.from_json(json)
# print the JSON string representation of the object
print(FinderGetAllDevelopmentPostsResponse.to_json())

# convert the object into a dict
finder_get_all_development_posts_response_dict = finder_get_all_development_posts_response_instance.to_dict()
# create an instance of FinderGetAllDevelopmentPostsResponse from a dict
finder_get_all_development_posts_response_from_dict = FinderGetAllDevelopmentPostsResponse.from_dict(finder_get_all_development_posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


