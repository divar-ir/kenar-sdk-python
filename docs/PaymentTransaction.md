# PaymentTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_rials** | **str** | The cost of the transaction in rials for your application | [optional] 
**extra_details** | **str** | Same Additional details which you sent in the request | [optional] 
**id** | **str** | Same uuid when creating transaction | [optional] 
**state** | [**PaymentTransactionState**](PaymentTransactionState.md) |  | [optional] 
**type** | [**PaymentTransactionType**](PaymentTransactionType.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.payment_transaction import PaymentTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTransaction from a JSON string
payment_transaction_instance = PaymentTransaction.from_json(json)
# print the JSON string representation of the object
print(PaymentTransaction.to_json())

# convert the object into a dict
payment_transaction_dict = payment_transaction_instance.to_dict()
# create an instance of PaymentTransaction from a dict
payment_transaction_from_dict = PaymentTransaction.from_dict(payment_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


