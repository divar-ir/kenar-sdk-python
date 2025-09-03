# PaymentWalletTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_rials** | **str** |  | [optional] 
**status** | [**PaymentWalletTransactionStatus**](PaymentWalletTransactionStatus.md) |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.payment_wallet_transaction import PaymentWalletTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentWalletTransaction from a JSON string
payment_wallet_transaction_instance = PaymentWalletTransaction.from_json(json)
# print the JSON string representation of the object
print(PaymentWalletTransaction.to_json())

# convert the object into a dict
payment_wallet_transaction_dict = payment_wallet_transaction_instance.to_dict()
# create an instance of PaymentWalletTransaction from a dict
payment_wallet_transaction_from_dict = PaymentWalletTransaction.from_dict(payment_wallet_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


