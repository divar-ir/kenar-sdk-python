# PaymentGetTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**PaymentTransaction**](PaymentTransaction.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.payment_get_transaction_response import PaymentGetTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentGetTransactionResponse from a JSON string
payment_get_transaction_response_instance = PaymentGetTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentGetTransactionResponse.to_json())

# convert the object into a dict
payment_get_transaction_response_dict = payment_get_transaction_response_instance.to_dict()
# create an instance of PaymentGetTransactionResponse from a dict
payment_get_transaction_response_from_dict = PaymentGetTransactionResponse.from_dict(payment_get_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


