# PostSubmitPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apartment_sell** | [**PostApartmentSellFields**](PostApartmentSellFields.md) |  | [optional] 
**chat_enabled** | **bool** | فعال بودن چت | 
**city** | **str** | شهر آگهی | 
**description** | **str** | توضیحات آگهی | 
**district** | **str** | محله آگهی | [optional] 
**hide_phone** | **bool** | مخفی کردن شماره تماس از کاربران | 
**home_presell** | [**PostHomePresellFields**](PostHomePresellFields.md) |  | [optional] 
**images** | **List[str]** |  | 
**landline_numbers** | **List[str]** | شماره‌های ثابت برای افزودن به آگهی | [optional] 
**latitude** | **float** | عرض جغرافیایی آگهی | [optional] 
**location_type** | [**PostLocationType**](PostLocationType.md) |  | 
**longitude** | **float** | طول جغرافیایی آگهی | [optional] 
**services** | [**OpenPlatformpostServicesFields**](OpenPlatformpostServicesFields.md) |  | [optional] 
**temporary_residence** | [**PostTemporaryResidenceFields**](PostTemporaryResidenceFields.md) |  | [optional] 
**title** | **str** | عنوان آگهی | 

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


