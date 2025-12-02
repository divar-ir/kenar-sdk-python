# AddonsGetDynamicAction

نمایانگر یک Action پویا که می‌تواند در دستگاه کاربر دریافت و اجرا شود

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | داده‌ای که می‌توانید مقداردهی کنید و هنگام کلیک کاربر به شما برگردانده می‌شود | [optional] 

## Example

```python
from kenar_api_client.models.addons_get_dynamic_action import AddonsGetDynamicAction

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsGetDynamicAction from a JSON string
addons_get_dynamic_action_instance = AddonsGetDynamicAction.from_json(json)
# print the JSON string representation of the object
print(AddonsGetDynamicAction.to_json())

# convert the object into a dict
addons_get_dynamic_action_dict = addons_get_dynamic_action_instance.to_dict()
# create an instance of AddonsGetDynamicAction from a dict
addons_get_dynamic_action_from_dict = AddonsGetDynamicAction.from_dict(addons_get_dynamic_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


