# AssetsGetBodyStatusesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body_status** | [**List[AssetsEnumOption]**](AssetsEnumOption.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.assets_get_body_statuses_response import AssetsGetBodyStatusesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsGetBodyStatusesResponse from a JSON string
assets_get_body_statuses_response_instance = AssetsGetBodyStatusesResponse.from_json(json)
# print the JSON string representation of the object
print(AssetsGetBodyStatusesResponse.to_json())

# convert the object into a dict
assets_get_body_statuses_response_dict = assets_get_body_statuses_response_instance.to_dict()
# create an instance of AssetsGetBodyStatusesResponse from a dict
assets_get_body_statuses_response_from_dict = AssetsGetBodyStatusesResponse.from_dict(assets_get_body_statuses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


