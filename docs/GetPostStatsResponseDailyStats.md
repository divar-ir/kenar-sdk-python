# GetPostStatsResponseDailyStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | تعداد روزانه آمار (مثلاً بازدید) | [optional] 
**var_date** | **str** | تاریخ به فرمت YYYY-MM-DD | [optional] 

## Example

```python
from kenar_api_client.models.get_post_stats_response_daily_stats import GetPostStatsResponseDailyStats

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostStatsResponseDailyStats from a JSON string
get_post_stats_response_daily_stats_instance = GetPostStatsResponseDailyStats.from_json(json)
# print the JSON string representation of the object
print(GetPostStatsResponseDailyStats.to_json())

# convert the object into a dict
get_post_stats_response_daily_stats_dict = get_post_stats_response_daily_stats_instance.to_dict()
# create an instance of GetPostStatsResponseDailyStats from a dict
get_post_stats_response_daily_stats_from_dict = GetPostStatsResponseDailyStats.from_dict(get_post_stats_response_daily_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


