# AddonsGetBusinessAddonsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**List[AddonsBusinessAddon]**](AddonsBusinessAddon.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_get_business_addons_response import AddonsGetBusinessAddonsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsGetBusinessAddonsResponse from a JSON string
addons_get_business_addons_response_instance = AddonsGetBusinessAddonsResponse.from_json(json)
# print the JSON string representation of the object
print(AddonsGetBusinessAddonsResponse.to_json())

# convert the object into a dict
addons_get_business_addons_response_dict = addons_get_business_addons_response_instance.to_dict()
# create an instance of AddonsGetBusinessAddonsResponse from a dict
addons_get_business_addons_response_from_dict = AddonsGetBusinessAddonsResponse.from_dict(addons_get_business_addons_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


