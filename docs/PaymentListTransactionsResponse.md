# PaymentListTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Token for the next page of results. | [optional] 
**transactions** | [**List[PaymentTransaction]**](PaymentTransaction.md) | شناسه مرجع فاکتور یا تراکنش | [optional] 

## Example

```python
from kenar_api_client.models.payment_list_transactions_response import PaymentListTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentListTransactionsResponse from a JSON string
payment_list_transactions_response_instance = PaymentListTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentListTransactionsResponse.to_json())

# convert the object into a dict
payment_list_transactions_response_dict = payment_list_transactions_response_instance.to_dict()
# create an instance of PaymentListTransactionsResponse from a dict
payment_list_transactions_response_from_dict = PaymentListTransactionsResponse.from_dict(payment_list_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


