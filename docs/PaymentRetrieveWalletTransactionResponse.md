# PaymentRetrieveWalletTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**PaymentWalletTransaction**](PaymentWalletTransaction.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.payment_retrieve_wallet_transaction_response import PaymentRetrieveWalletTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRetrieveWalletTransactionResponse from a JSON string
payment_retrieve_wallet_transaction_response_instance = PaymentRetrieveWalletTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentRetrieveWalletTransactionResponse.to_json())

# convert the object into a dict
payment_retrieve_wallet_transaction_response_dict = payment_retrieve_wallet_transaction_response_instance.to_dict()
# create an instance of PaymentRetrieveWalletTransactionResponse from a dict
payment_retrieve_wallet_transaction_response_from_dict = PaymentRetrieveWalletTransactionResponse.from_dict(payment_retrieve_wallet_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


