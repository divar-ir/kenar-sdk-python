# GetPostPricingResponseSubmit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | نشان می‌دهد که آیا آگهی قابل ثبت است. اگر false باشد، API ثبت خطا برمی‌گرداند | [optional] 
**cost_rials** | **str** | هزینه ثبت آگهی به ریال | [optional] 

## Example

```python
from kenar_api_client.models.get_post_pricing_response_submit import GetPostPricingResponseSubmit

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostPricingResponseSubmit from a JSON string
get_post_pricing_response_submit_instance = GetPostPricingResponseSubmit.from_json(json)
# print the JSON string representation of the object
print(GetPostPricingResponseSubmit.to_json())

# convert the object into a dict
get_post_pricing_response_submit_dict = get_post_pricing_response_submit_instance.to_dict()
# create an instance of GetPostPricingResponseSubmit from a dict
get_post_pricing_response_submit_from_dict = GetPostPricingResponseSubmit.from_dict(get_post_pricing_response_submit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


