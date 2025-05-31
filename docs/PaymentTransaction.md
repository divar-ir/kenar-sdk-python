# PaymentTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_rials** | **str** | هزینه تراکنش به ریال برای اپلیکیشن شما | [optional] 
**created_at** | **datetime** | The time when the transaction was created | [optional] 
**extra_details** | **str** | همان جزئیات اضافی که در درخواست ارسال کردید | [optional] 
**id** | **str** | همان uuid هنگام ایجاد تراکنش | [optional] 
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


