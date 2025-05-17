# AssetsGetBrandModelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_models** | [**List[AssetsEnumOption]**](AssetsEnumOption.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_brand_models_response import AssetsGetBrandModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetBrandModelsResponse from a JSON string
assets_get_brand_models_response_instance = AssetsGetBrandModelsResponse.from_json(json)
# print the JSON string representation of the object
print(AssetsGetBrandModelsResponse.to_json())

# convert the object into a dict
assets_get_brand_models_response_dict = assets_get_brand_models_response_instance.to_dict()
# create an instance of AssetsGetBrandModelsResponse from a dict
assets_get_brand_models_response_from_dict = AssetsGetBrandModelsResponse.from_dict(assets_get_brand_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


