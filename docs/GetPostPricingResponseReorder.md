# GetPostPricingResponseReorder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | نشان می‌دهد که آیا آگهی قابل نردبان است. اگر false باشد، API نردبان خطا برمی‌گرداند | [optional] 
**cost_rials** | **str** | هزینه نردبان به ریال | [optional] 

## Example

```python
from kenar_api_client.models.get_post_pricing_response_reorder import GetPostPricingResponseReorder

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostPricingResponseReorder from a JSON string
get_post_pricing_response_reorder_instance = GetPostPricingResponseReorder.from_json(json)
# print the JSON string representation of the object
print(GetPostPricingResponseReorder.to_json())

# convert the object into a dict
get_post_pricing_response_reorder_dict = get_post_pricing_response_reorder_instance.to_dict()
# create an instance of GetPostPricingResponseReorder from a dict
get_post_pricing_response_reorder_from_dict = GetPostPricingResponseReorder.from_dict(get_post_pricing_response_reorder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


