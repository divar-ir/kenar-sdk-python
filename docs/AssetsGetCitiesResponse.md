# AssetsGetCitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cities** | [**List[AssetsEnumOption]**](AssetsEnumOption.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_cities_response import AssetsGetCitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetCitiesResponse from a JSON string
assets_get_cities_response_instance = AssetsGetCitiesResponse.from_json(json)
# print the JSON string representation of the object
print(AssetsGetCitiesResponse.to_json())

# convert the object into a dict
assets_get_cities_response_dict = assets_get_cities_response_instance.to_dict()
# create an instance of AssetsGetCitiesResponse from a dict
assets_get_cities_response_from_dict = AssetsGetCitiesResponse.from_dict(assets_get_cities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


