# PaymentGetPostPricingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reorder** | [**GetPostPricingResponseReorder**](GetPostPricingResponseReorder.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.payment_get_post_pricing_response import PaymentGetPostPricingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentGetPostPricingResponse from a JSON string
payment_get_post_pricing_response_instance = PaymentGetPostPricingResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentGetPostPricingResponse.to_json())

# convert the object into a dict
payment_get_post_pricing_response_dict = payment_get_post_pricing_response_instance.to_dict()
# create an instance of PaymentGetPostPricingResponse from a dict
payment_get_post_pricing_response_from_dict = PaymentGetPostPricingResponse.from_dict(payment_get_post_pricing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


