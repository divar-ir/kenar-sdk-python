# PaymentSubmitUserPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_rials** | **str** | مبلغ کل پرداختی کاربر به ریال | 
**profit_rials** | **str** | سود یا کمیسیون شما از این تراکنش، به ریال. اگر چنین مفهومی در فرایند پرداخت شما وجود ندارد، مقدار این پارامتر را برابر amount_rials قرار دهید. | 
**reference_id** | **str** | شناسه منحصر به فرد بین دیوار و ارائه‌دهنده برای فاکتور یا تراکنش. این شناسه مرجع درگاه پرداخت نیست. | 
**services** | **List[str]** | لیست slug خدماتی که کاربر برای آنها پرداخت کرده (مثلاً &#39;banner&#39;، &#39;title_refinement&#39;) | 

## Example

```python
from kenar_api_client.models.payment_submit_user_payment_request import PaymentSubmitUserPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSubmitUserPaymentRequest from a JSON string
payment_submit_user_payment_request_instance = PaymentSubmitUserPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentSubmitUserPaymentRequest.to_json())

# convert the object into a dict
payment_submit_user_payment_request_dict = payment_submit_user_payment_request_instance.to_dict()
# create an instance of PaymentSubmitUserPaymentRequest from a dict
payment_submit_user_payment_request_from_dict = PaymentSubmitUserPaymentRequest.from_dict(payment_submit_user_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


