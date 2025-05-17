# GetPostResponseBusinessData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_type** | [**PremiumPanelBusinessDataSubBusinessType**](PremiumPanelBusinessDataSubBusinessType.md) |  | [optional] 
**business_name** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.get_post_response_business_data import GetPostResponseBusinessData

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostResponseBusinessData from a JSON string
get_post_response_business_data_instance = GetPostResponseBusinessData.from_json(json)
# print the JSON string representation of the object
print(GetPostResponseBusinessData.to_json())

# convert the object into a dict
get_post_response_business_data_dict = get_post_response_business_data_instance.to_dict()
# create an instance of GetPostResponseBusinessData from a dict
get_post_response_business_data_from_dict = GetPostResponseBusinessData.from_dict(get_post_response_business_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


