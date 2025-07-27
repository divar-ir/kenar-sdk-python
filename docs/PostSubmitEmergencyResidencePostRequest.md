# PostSubmitEmergencyResidencePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**images** | **List[str]** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.post_submit_emergency_residence_post_request import PostSubmitEmergencyResidencePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSubmitEmergencyResidencePostRequest from a JSON string
post_submit_emergency_residence_post_request_instance = PostSubmitEmergencyResidencePostRequest.from_json(json)
# print the JSON string representation of the object
print(PostSubmitEmergencyResidencePostRequest.to_json())

# convert the object into a dict
post_submit_emergency_residence_post_request_dict = post_submit_emergency_residence_post_request_instance.to_dict()
# create an instance of PostSubmitEmergencyResidencePostRequest from a dict
post_submit_emergency_residence_post_request_from_dict = PostSubmitEmergencyResidencePostRequest.from_dict(post_submit_emergency_residence_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


