# GetPostStatsResponsePostStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily** | [**List[GetPostStatsResponseDailyStats]**](GetPostStatsResponseDailyStats.md) | Daily value the metric over the last seven days | [optional] 
**total** | **int** | Total number of the metric (e.g. view) | [optional] 

## Example

```python
from kenar_api_client.models.get_post_stats_response_post_stats import GetPostStatsResponsePostStats

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostStatsResponsePostStats from a JSON string
get_post_stats_response_post_stats_instance = GetPostStatsResponsePostStats.from_json(json)
# print the JSON string representation of the object
print(GetPostStatsResponsePostStats.to_json())

# convert the object into a dict
get_post_stats_response_post_stats_dict = get_post_stats_response_post_stats_instance.to_dict()
# create an instance of GetPostStatsResponsePostStats from a dict
get_post_stats_response_post_stats_from_dict = GetPostStatsResponsePostStats.from_dict(get_post_stats_response_post_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


