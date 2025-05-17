# AssetsGetColorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colors** | [**List[AssetsEnumOption]**](AssetsEnumOption.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_colors_response import AssetsGetColorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetColorsResponse from a JSON string
assets_get_colors_response_instance = AssetsGetColorsResponse.from_json(json)
# print the JSON string representation of the object
print(AssetsGetColorsResponse.to_json())

# convert the object into a dict
assets_get_colors_response_dict = assets_get_colors_response_instance.to_dict()
# create an instance of AssetsGetColorsResponse from a dict
assets_get_colors_response_from_dict = AssetsGetColorsResponse.from_dict(assets_get_colors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


