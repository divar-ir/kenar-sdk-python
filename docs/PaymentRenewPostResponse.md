# PaymentRenewPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**PaymentTransaction**](PaymentTransaction.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.payment_renew_post_response import PaymentRenewPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRenewPostResponse from a JSON string
payment_renew_post_response_instance = PaymentRenewPostResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentRenewPostResponse.to_json())

# convert the object into a dict
payment_renew_post_response_dict = payment_renew_post_response_instance.to_dict()
# create an instance of PaymentRenewPostResponse from a dict
payment_renew_post_response_from_dict = PaymentRenewPostResponse.from_dict(payment_renew_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


