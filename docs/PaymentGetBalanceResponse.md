# PaymentGetBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_rials** | **str** | The balance of the app in rials | [optional] 

## Example

```python
from kenar_api_client.models.payment_get_balance_response import PaymentGetBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentGetBalanceResponse from a JSON string
payment_get_balance_response_instance = PaymentGetBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentGetBalanceResponse.to_json())

# convert the object into a dict
payment_get_balance_response_dict = payment_get_balance_response_instance.to_dict()
# create an instance of PaymentGetBalanceResponse from a dict
payment_get_balance_response_from_dict = PaymentGetBalanceResponse.from_dict(payment_get_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


