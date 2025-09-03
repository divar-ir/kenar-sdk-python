# PaymentCommitWalletTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**PaymentWalletTransaction**](PaymentWalletTransaction.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.payment_commit_wallet_transaction_response import PaymentCommitWalletTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCommitWalletTransactionResponse from a JSON string
payment_commit_wallet_transaction_response_instance = PaymentCommitWalletTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentCommitWalletTransactionResponse.to_json())

# convert the object into a dict
payment_commit_wallet_transaction_response_dict = payment_commit_wallet_transaction_response_instance.to_dict()
# create an instance of PaymentCommitWalletTransactionResponse from a dict
payment_commit_wallet_transaction_response_from_dict = PaymentCommitWalletTransactionResponse.from_dict(payment_commit_wallet_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


