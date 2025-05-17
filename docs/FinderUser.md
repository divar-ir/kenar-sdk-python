# FinderUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_numbers** | **List[str]** | deprecated | [optional] 
**phone_number** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.finder_user import FinderUser

# TODO update the JSON string below
json = "{}"
# create an instance of FinderUser from a JSON string
finder_user_instance = FinderUser.from_json(json)
# print the JSON string representation of the object
print(FinderUser.to_json())

# convert the object into a dict
finder_user_dict = finder_user_instance.to_dict()
# create an instance of FinderUser from a dict
finder_user_from_dict = FinderUser.from_dict(finder_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


