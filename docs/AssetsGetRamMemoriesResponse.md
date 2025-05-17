# AssetsGetRamMemoriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ram_memories** | [**List[AssetsEnumOption]**](AssetsEnumOption.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_ram_memories_response import AssetsGetRamMemoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetRamMemoriesResponse from a JSON string
assets_get_ram_memories_response_instance = AssetsGetRamMemoriesResponse.from_json(json)
# print the JSON string representation of the object
print(AssetsGetRamMemoriesResponse.to_json())

# convert the object into a dict
assets_get_ram_memories_response_dict = assets_get_ram_memories_response_instance.to_dict()
# create an instance of AssetsGetRamMemoriesResponse from a dict
assets_get_ram_memories_response_from_dict = AssetsGetRamMemoriesResponse.from_dict(assets_get_ram_memories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


