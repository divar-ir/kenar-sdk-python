# AddonsEvaluationRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indicator_text** | **str** |  | [optional] 
**indicator_percentage** | **int** |  | [optional] 
**icon_name** | [**DivarIconsIconName**](DivarIconsIconName.md) |  | [optional] 
**left** | [**AddonsEvaluationRowSection**](AddonsEvaluationRowSection.md) |  | [optional] 
**middle** | [**AddonsEvaluationRowSection**](AddonsEvaluationRowSection.md) |  | [optional] 
**right** | [**AddonsEvaluationRowSection**](AddonsEvaluationRowSection.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_evaluation_row import AddonsEvaluationRow

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsEvaluationRow from a JSON string
addons_evaluation_row_instance = AddonsEvaluationRow.from_json(json)
# print the JSON string representation of the object
print(AddonsEvaluationRow.to_json())

# convert the object into a dict
addons_evaluation_row_dict = addons_evaluation_row_instance.to_dict()
# create an instance of AddonsEvaluationRow from a dict
addons_evaluation_row_from_dict = AddonsEvaluationRow.from_dict(addons_evaluation_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


