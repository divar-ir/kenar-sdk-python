# PostSubmitPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_enabled** | **bool** | امکان چت فعال باشد | [optional] 
**city** | **str** | شهر آگهی | [optional] 
**description** | **str** | توضیحات آگهی | [optional] 
**district** | **str** | محله آگهی | [optional] 
**hide_phone** | **bool** | عدم نمایش شماره تماس به کاربران | [optional] 
**images** | **List[str]** |  | [optional] 
**landline_numbers** | **List[str]** | Landline numbers to be added to the post | [optional] 
**latitude** | **float** | عرض جغرافیایی آگهی | [optional] 
**location_type** | [**SubmitPostRequestLocationType**](SubmitPostRequestLocationType.md) |  | [optional] 
**longitude** | **float** | طول جغرافیایی آگهی | [optional] 
**services** | [**OpenPlatformpostServicesFields**](OpenPlatformpostServicesFields.md) |  | [optional] 
**temporary_residence** | [**PostTemporaryResidenceFields**](PostTemporaryResidenceFields.md) |  | [optional] 
**title** | **str** | عنوان آگهی | [optional] 

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


