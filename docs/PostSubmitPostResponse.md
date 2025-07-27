# PostSubmitPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_token** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.post_submit_post_response import PostSubmitPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostSubmitPostResponse from a JSON string
post_submit_post_response_instance = PostSubmitPostResponse.from_json(json)
# print the JSON string representation of the object
print(PostSubmitPostResponse.to_json())

# convert the object into a dict
post_submit_post_response_dict = post_submit_post_response_instance.to_dict()
# create an instance of PostSubmitPostResponse from a dict
post_submit_post_response_from_dict = PostSubmitPostResponse.from_dict(post_submit_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


