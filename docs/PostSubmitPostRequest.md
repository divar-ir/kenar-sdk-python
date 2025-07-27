# PostSubmitPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_enabled** | **bool** | Whether to enable chat | [optional] 
**city** | **str** | City of the post | [optional] 
**description** | **str** | Description of the post | [optional] 
**district** | **str** | District of the post | [optional] 
**hide_phone** | **bool** | Whether to hide the phone number from demand users | [optional] 
**images** | **List[str]** |  | [optional] 
**latitude** | **float** | Latitude of the post | [optional] 
**longitude** | **float** | Longitude of the post | [optional] 
**temporary_residence** | [**PostTemporaryResidenceFields**](PostTemporaryResidenceFields.md) |  | [optional] 
**title** | **str** | Title of the post | [optional] 

## Example

```python
from kenar_api_client.models.post_submit_post_request import PostSubmitPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSubmitPostRequest from a JSON string
post_submit_post_request_instance = PostSubmitPostRequest.from_json(json)
# print the JSON string representation of the object
print(PostSubmitPostRequest.to_json())

# convert the object into a dict
post_submit_post_request_dict = post_submit_post_request_instance.to_dict()
# create an instance of PostSubmitPostRequest from a dict
post_submit_post_request_from_dict = PostSubmitPostRequest.from_dict(post_submit_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


