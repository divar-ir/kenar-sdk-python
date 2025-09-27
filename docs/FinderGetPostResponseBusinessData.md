# FinderGetPostResponseBusinessData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_name** | **str** |  | [optional] 
**business_type** | [**PremiumPanelBusinessDataSubBusinessType**](PremiumPanelBusinessDataSubBusinessType.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.finder_get_post_response_business_data import FinderGetPostResponseBusinessData

# TODO update the JSON string below
json = "{}"
# create an instance of FinderGetPostResponseBusinessData from a JSON string
finder_get_post_response_business_data_instance = FinderGetPostResponseBusinessData.from_json(json)
# print the JSON string representation of the object
print(FinderGetPostResponseBusinessData.to_json())

# convert the object into a dict
finder_get_post_response_business_data_dict = finder_get_post_response_business_data_instance.to_dict()
# create an instance of FinderGetPostResponseBusinessData from a dict
finder_get_post_response_business_data_from_dict = FinderGetPostResponseBusinessData.from_dict(finder_get_post_response_business_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


