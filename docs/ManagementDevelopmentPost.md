# ManagementDevelopmentPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preset** | [**ManagementPreset**](ManagementPreset.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**token** | **str** |  | [optional] 
**mng_token** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.management_development_post import ManagementDevelopmentPost

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementDevelopmentPost from a JSON string
management_development_post_instance = ManagementDevelopmentPost.from_json(json)
# print the JSON string representation of the object
print(ManagementDevelopmentPost.to_json())

# convert the object into a dict
management_development_post_dict = management_development_post_instance.to_dict()
# create an instance of ManagementDevelopmentPost from a dict
management_development_post_from_dict = ManagementDevelopmentPost.from_dict(management_development_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


