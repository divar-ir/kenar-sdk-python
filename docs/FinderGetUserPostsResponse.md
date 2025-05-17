# FinderGetUserPostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts** | [**List[FinderGetUserPostsResponsePost]**](FinderGetUserPostsResponsePost.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.finder_get_user_posts_response import FinderGetUserPostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FinderGetUserPostsResponse from a JSON string
finder_get_user_posts_response_instance = FinderGetUserPostsResponse.from_json(json)
# print the JSON string representation of the object
print(FinderGetUserPostsResponse.to_json())

# convert the object into a dict
finder_get_user_posts_response_dict = finder_get_user_posts_response_instance.to_dict()
# create an instance of FinderGetUserPostsResponse from a dict
finder_get_user_posts_response_from_dict = FinderGetUserPostsResponse.from_dict(finder_get_user_posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


