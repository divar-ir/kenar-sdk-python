# AssetsGetDistrictsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**districts** | [**List[AssetsEnumOption]**](AssetsEnumOption.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_districts_response import AssetsGetDistrictsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetDistrictsResponse from a JSON string
assets_get_districts_response_instance = AssetsGetDistrictsResponse.from_json(json)
# print the JSON string representation of the object
print(AssetsGetDistrictsResponse.to_json())

# convert the object into a dict
assets_get_districts_response_dict = assets_get_districts_response_instance.to_dict()
# create an instance of AssetsGetDistrictsResponse from a dict
assets_get_districts_response_from_dict = AssetsGetDistrictsResponse.from_dict(assets_get_districts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


