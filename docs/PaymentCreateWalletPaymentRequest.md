# PaymentCreateWalletPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_rials** | **str** | Transaction amount in rials | 
**description** | **str** | A description of the transaction | 
**redirect_url** | **str** | The address user should be redirected to after paying the amount | 

## Example

```python
from kenar_api_client.models.payment_create_wallet_payment_request import PaymentCreateWalletPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCreateWalletPaymentRequest from a JSON string
payment_create_wallet_payment_request_instance = PaymentCreateWalletPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentCreateWalletPaymentRequest.to_json())

# convert the object into a dict
payment_create_wallet_payment_request_dict = payment_create_wallet_payment_request_instance.to_dict()
# create an instance of PaymentCreateWalletPaymentRequest from a dict
payment_create_wallet_payment_request_from_dict = PaymentCreateWalletPaymentRequest.from_dict(payment_create_wallet_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


