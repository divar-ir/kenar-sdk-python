# DarvazeIranianCarPlate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_code** | **int** |  | [optional] 
**province_code** | **int** |  | [optional] 
**serial_letter** | **str** |  | [optional] 
**serial_number** | **int** |  | [optional] 

## Example

```python
from kenar_api_client.models.darvaze_iranian_car_plate import DarvazeIranianCarPlate

# TODO update the JSON string below
json = "{}"
# create an instance of DarvazeIranianCarPlate from a JSON string
darvaze_iranian_car_plate_instance = DarvazeIranianCarPlate.from_json(json)
# print the JSON string representation of the object
print(DarvazeIranianCarPlate.to_json())

# convert the object into a dict
darvaze_iranian_car_plate_dict = darvaze_iranian_car_plate_instance.to_dict()
# create an instance of DarvazeIranianCarPlate from a dict
darvaze_iranian_car_plate_from_dict = DarvazeIranianCarPlate.from_dict(darvaze_iranian_car_plate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


