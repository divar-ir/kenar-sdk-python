# OpenPlatformpostServicesFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**ServicesFieldsCategory**](ServicesFieldsCategory.md) |  | 
**expertise_ids** | **List[str]** | فهرست شناسه‌های تخصص | 
**work_hours_end** | **int** | ساعت پایان کار به فرمت 24 ساعته (مثلاً 18 برای 18:00). فقط در صورتی اعمال می‌شود که &#x60;works_24_7&#x60; false باشد. | 
**work_hours_start** | **int** | ساعت شروع کار به فرمت 24 ساعته (مثلاً 9 برای 9:00). فقط در صورتی اعمال می‌شود که &#x60;works_24_7&#x60; false باشد. | 
**work_on_holidays** | **bool** | آیا ارائه‌دهنده سرویس در تعطیلات کار می‌کند | 
**works_24_7** | **bool** | آیا ارائه‌دهنده سرویس به صورت 24/7 در دسترس است. اگر true باشد، &#x60;work_hours_start&#x60; و &#x60;work_hours_end&#x60; نادیده گرفته می‌شوند. | 

## Example

```python
from kenar_api_client.models.open_platformpost_services_fields import OpenPlatformpostServicesFields

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPlatformpostServicesFields from a JSON string
open_platformpost_services_fields_instance = OpenPlatformpostServicesFields.from_json(json)
# print the JSON string representation of the object
print(OpenPlatformpostServicesFields.to_json())

# convert the object into a dict
open_platformpost_services_fields_dict = open_platformpost_services_fields_instance.to_dict()
# create an instance of OpenPlatformpostServicesFields from a dict
open_platformpost_services_fields_from_dict = OpenPlatformpostServicesFields.from_dict(open_platformpost_services_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


