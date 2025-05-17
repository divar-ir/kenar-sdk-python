# FinderSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_model** | **List[str]** |  | [optional] 
**production_year** | [**FinderSearchQueryNumberRange**](FinderSearchQueryNumberRange.md) |  | [optional] 
**usage** | [**FinderSearchQueryNumberRange**](FinderSearchQueryNumberRange.md) |  | [optional] 
**rooms** | **List[str]** |  | [optional] 
**rent** | [**FinderSearchQueryNumberRange**](FinderSearchQueryNumberRange.md) |  | [optional] 
**credit** | [**FinderSearchQueryNumberRange**](FinderSearchQueryNumberRange.md) |  | [optional] 
**size** | [**FinderSearchQueryNumberRange**](FinderSearchQueryNumberRange.md) |  | [optional] 
**only_with_parking** | **bool** |  | [optional] 

## Example

```python
from kenar_api_client.models.finder_search_query import FinderSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of FinderSearchQuery from a JSON string
finder_search_query_instance = FinderSearchQuery.from_json(json)
# print the JSON string representation of the object
print(FinderSearchQuery.to_json())

# convert the object into a dict
finder_search_query_dict = finder_search_query_instance.to_dict()
# create an instance of FinderSearchQuery from a dict
finder_search_query_from_dict = FinderSearchQuery.from_dict(finder_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


