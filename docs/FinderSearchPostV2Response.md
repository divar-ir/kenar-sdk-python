# FinderSearchPostV2Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts** | [**List[FinderSearchPostItem]**](FinderSearchPostItem.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.finder_search_post_v2_response import FinderSearchPostV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of FinderSearchPostV2Response from a JSON string
finder_search_post_v2_response_instance = FinderSearchPostV2Response.from_json(json)
# print the JSON string representation of the object
print(FinderSearchPostV2Response.to_json())

# convert the object into a dict
finder_search_post_v2_response_dict = finder_search_post_v2_response_instance.to_dict()
# create an instance of FinderSearchPostV2Response from a dict
finder_search_post_v2_response_from_dict = FinderSearchPostV2Response.from_dict(finder_search_post_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


