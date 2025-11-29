# GetPostPricingResponseRenew


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | نشان می‌دهد که آیا آگهی قابل تمدید است. اگر false باشد، API تمدید خطا برمی‌گرداند | [optional] 
**cost_rials** | **str** | هزینه تمدید به ریال | [optional] 

## Example

```python
from kenar_api_client.models.get_post_pricing_response_renew import GetPostPricingResponseRenew

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostPricingResponseRenew from a JSON string
get_post_pricing_response_renew_instance = GetPostPricingResponseRenew.from_json(json)
# print the JSON string representation of the object
print(GetPostPricingResponseRenew.to_json())

# convert the object into a dict
get_post_pricing_response_renew_dict = get_post_pricing_response_renew_instance.to_dict()
# create an instance of GetPostPricingResponseRenew from a dict
get_post_pricing_response_renew_from_dict = GetPostPricingResponseRenew.from_dict(get_post_pricing_response_renew_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


