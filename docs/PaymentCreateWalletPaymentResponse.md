# PaymentCreateWalletPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_url** | **str** | آدرسی که باید کاربر را به آن هدایت کنید | [optional] 
**token** | **str** | توکن تراکنش. برای عملیات‌های بعدی استفاده می‌شود | [optional] 

## Example

```python
from kenar_api_client.models.payment_create_wallet_payment_response import PaymentCreateWalletPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCreateWalletPaymentResponse from a JSON string
payment_create_wallet_payment_response_instance = PaymentCreateWalletPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentCreateWalletPaymentResponse.to_json())

# convert the object into a dict
payment_create_wallet_payment_response_dict = payment_create_wallet_payment_response_instance.to_dict()
# create an instance of PaymentCreateWalletPaymentResponse from a dict
payment_create_wallet_payment_response_from_dict = PaymentCreateWalletPaymentResponse.from_dict(payment_create_wallet_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


