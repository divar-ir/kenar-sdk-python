# PaymentReorderPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_rials** | **str** | هزینه تراکنش به ریال برای اپلیکیشن شما | [optional] 
**id** | **str** | همان uuid هنگام ایجاد تراکنش | [optional] 

## Example

```python
from kenar_api_client.models.payment_reorder_post_response import PaymentReorderPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReorderPostResponse from a JSON string
payment_reorder_post_response_instance = PaymentReorderPostResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentReorderPostResponse.to_json())

# convert the object into a dict
payment_reorder_post_response_dict = payment_reorder_post_response_instance.to_dict()
# create an instance of PaymentReorderPostResponse from a dict
payment_reorder_post_response_from_dict = PaymentReorderPostResponse.from_dict(payment_reorder_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


