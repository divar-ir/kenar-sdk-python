# AppsAppStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**AppsAppStatusStatus**](AppsAppStatusStatus.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.apps_app_status import AppsAppStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AppsAppStatus from a JSON string
apps_app_status_instance = AppsAppStatus.from_json(json)
# print the JSON string representation of the object
print(AppsAppStatus.to_json())

# convert the object into a dict
apps_app_status_dict = apps_app_status_instance.to_dict()
# create an instance of AppsAppStatus from a dict
apps_app_status_from_dict = AppsAppStatus.from_dict(apps_app_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


