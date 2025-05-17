# AppsApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**display** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**divar_identification_key** | **str** |  | [optional] 
**status** | [**AppsAppStatus**](AppsAppStatus.md) |  | [optional] 
**service_type** | [**AppsServiceType**](AppsServiceType.md) |  | [optional] 
**service_tags** | [**List[AppsServiceTag]**](AppsServiceTag.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.apps_app import AppsApp

# TODO update the JSON string below
json = "{}"
# create an instance of AppsApp from a JSON string
apps_app_instance = AppsApp.from_json(json)
# print the JSON string representation of the object
print(AppsApp.to_json())

# convert the object into a dict
apps_app_dict = apps_app_instance.to_dict()
# create an instance of AppsApp from a dict
apps_app_from_dict = AppsApp.from_dict(apps_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


