# AddonsEvaluationRowSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**section_color** | [**AddonsWidgetColor**](AddonsWidgetColor.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_evaluation_row_section import AddonsEvaluationRowSection

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsEvaluationRowSection from a JSON string
addons_evaluation_row_section_instance = AddonsEvaluationRowSection.from_json(json)
# print the JSON string representation of the object
print(AddonsEvaluationRowSection.to_json())

# convert the object into a dict
addons_evaluation_row_section_dict = addons_evaluation_row_section_instance.to_dict()
# create an instance of AddonsEvaluationRowSection from a dict
addons_evaluation_row_section_from_dict = AddonsEvaluationRowSection.from_dict(addons_evaluation_row_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


