# PaymentCommitWalletTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token of the transaction you want to commit | [optional] 

## Example

```python
from kenar_api_client.models.payment_commit_wallet_transaction_request import PaymentCommitWalletTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCommitWalletTransactionRequest from a JSON string
payment_commit_wallet_transaction_request_instance = PaymentCommitWalletTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentCommitWalletTransactionRequest.to_json())

# convert the object into a dict
payment_commit_wallet_transaction_request_dict = payment_commit_wallet_transaction_request_instance.to_dict()
# create an instance of PaymentCommitWalletTransactionRequest from a dict
payment_commit_wallet_transaction_request_from_dict = PaymentCommitWalletTransactionRequest.from_dict(payment_commit_wallet_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


