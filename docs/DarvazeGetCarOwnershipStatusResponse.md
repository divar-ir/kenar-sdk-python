# DarvazeGetCarOwnershipStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**status** | [**DarvazeGetCarOwnershipStatusResponseStatus**](DarvazeGetCarOwnershipStatusResponseStatus.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.darvaze_get_car_ownership_status_response import DarvazeGetCarOwnershipStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DarvazeGetCarOwnershipStatusResponse from a JSON string
darvaze_get_car_ownership_status_response_instance = DarvazeGetCarOwnershipStatusResponse.from_json(json)
# print the JSON string representation of the object
print(DarvazeGetCarOwnershipStatusResponse.to_json())

# convert the object into a dict
darvaze_get_car_ownership_status_response_dict = darvaze_get_car_ownership_status_response_instance.to_dict()
# create an instance of DarvazeGetCarOwnershipStatusResponse from a dict
darvaze_get_car_ownership_status_response_from_dict = DarvazeGetCarOwnershipStatusResponse.from_dict(darvaze_get_car_ownership_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


