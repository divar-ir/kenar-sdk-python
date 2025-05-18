# AddonsOpenServerLink

An action to pass complete session data and retrieve redirect location from your server on each user action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | A data that you can set and will be returned to you upon user click to recognize the action | [optional] 

## Example

```python
from kenar_api_client.models.addons_open_server_link import AddonsOpenServerLink

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsOpenServerLink from a JSON string
addons_open_server_link_instance = AddonsOpenServerLink.from_json(json)
# print the JSON string representation of the object
print(AddonsOpenServerLink.to_json())

# convert the object into a dict
addons_open_server_link_dict = addons_open_server_link_instance.to_dict()
# create an instance of AddonsOpenServerLink from a dict
addons_open_server_link_from_dict = AddonsOpenServerLink.from_dict(addons_open_server_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


