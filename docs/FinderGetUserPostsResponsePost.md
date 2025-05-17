# FinderGetUserPostsResponsePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**images** | **List[str]** |  | [optional] 
**category** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.finder_get_user_posts_response_post import FinderGetUserPostsResponsePost

# TODO update the JSON string below
json = "{}"
# create an instance of FinderGetUserPostsResponsePost from a JSON string
finder_get_user_posts_response_post_instance = FinderGetUserPostsResponsePost.from_json(json)
# print the JSON string representation of the object
print(FinderGetUserPostsResponsePost.to_json())

# convert the object into a dict
finder_get_user_posts_response_post_dict = finder_get_user_posts_response_post_instance.to_dict()
# create an instance of FinderGetUserPostsResponsePost from a dict
finder_get_user_posts_response_post_from_dict = FinderGetUserPostsResponsePost.from_dict(finder_get_user_posts_response_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


