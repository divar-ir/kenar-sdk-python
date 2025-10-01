# PaymentSubmitUserPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_rials** | **str** | کل مبلغ پرداختی توسط کاربر، به ریال | 
**profit_rials** | **str** | بخشی از مبلغ پرداختی که به شما تعلق می‌گیرد (سود یا کمیسیون)، به ریال | 
**reference_id** | **str** | شناسه مرجع فاکتور یا تراکنش | 
**services** | **List[str]** | لیست شناسه خدماتی که کاربر برای آنها پرداخت انجام داده است (مثلاً «banner»، «title_refinement» و ...). توصیه می‌شود از نام‌های انگلیسی کوتاه و توصیفی به‌عنوان شناسه خدمت استفاده شود. | 

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


