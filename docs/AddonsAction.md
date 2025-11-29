# AddonsAction

نمایان‌گر یک عملیات که می‌تواند انجام شود

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**get_dynamic_action** | [**AddonsGetDynamicAction**](AddonsGetDynamicAction.md) |  | [optional] 
**open_direct_link** | **str** | عملیاتی برای ارسال کاربر به URL شما به صورت مستقیم با فقط یک شناسه منبع (در صورت وجود) | [optional] 
**open_post_manage_page** | [**AddonsOpenPostManagePage**](AddonsOpenPostManagePage.md) |  | [optional] 
**open_post_page** | [**AddonsOpenPostPage**](AddonsOpenPostPage.md) |  | [optional] 
**open_server_link** | [**AddonsOpenServerLink**](AddonsOpenServerLink.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_action import AddonsAction

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsAction from a JSON string
addons_action_instance = AddonsAction.from_json(json)
# print the JSON string representation of the object
print(AddonsAction.to_json())

# convert the object into a dict
addons_action_dict = addons_action_instance.to_dict()
# create an instance of AddonsAction from a dict
addons_action_from_dict = AddonsAction.from_dict(addons_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


