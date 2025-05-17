# AssetsGetCategoriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[AssetsEnumOption]**](AssetsEnumOption.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_categories_response import AssetsGetCategoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetCategoriesResponse from a JSON string
assets_get_categories_response_instance = AssetsGetCategoriesResponse.from_json(json)
# print the JSON string representation of the object
print(AssetsGetCategoriesResponse.to_json())

# convert the object into a dict
assets_get_categories_response_dict = assets_get_categories_response_instance.to_dict()
# create an instance of AssetsGetCategoriesResponse from a dict
assets_get_categories_response_from_dict = AssetsGetCategoriesResponse.from_dict(assets_get_categories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


