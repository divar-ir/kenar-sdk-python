# DarvazeGenerateOrderForPostCodeValidationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**status** | [**DarvazeGenerateOrderForPostCodeValidationResponseStatus**](DarvazeGenerateOrderForPostCodeValidationResponseStatus.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.darvaze_generate_order_for_post_code_validation_response import DarvazeGenerateOrderForPostCodeValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DarvazeGenerateOrderForPostCodeValidationResponse from a JSON string
darvaze_generate_order_for_post_code_validation_response_instance = DarvazeGenerateOrderForPostCodeValidationResponse.from_json(json)
# print the JSON string representation of the object
print(DarvazeGenerateOrderForPostCodeValidationResponse.to_json())

# convert the object into a dict
darvaze_generate_order_for_post_code_validation_response_dict = darvaze_generate_order_for_post_code_validation_response_instance.to_dict()
# create an instance of DarvazeGenerateOrderForPostCodeValidationResponse from a dict
darvaze_generate_order_for_post_code_validation_response_from_dict = DarvazeGenerateOrderForPostCodeValidationResponse.from_dict(darvaze_generate_order_for_post_code_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


