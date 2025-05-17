# PaymentTicketValidateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_payload** | **object** |  | [optional] 

## Example

```python
from kenar_api_client.models.payment_ticket_validate_response import PaymentTicketValidateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTicketValidateResponse from a JSON string
payment_ticket_validate_response_instance = PaymentTicketValidateResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentTicketValidateResponse.to_json())

# convert the object into a dict
payment_ticket_validate_response_dict = payment_ticket_validate_response_instance.to_dict()
# create an instance of PaymentTicketValidateResponse from a dict
payment_ticket_validate_response_from_dict = PaymentTicketValidateResponse.from_dict(payment_ticket_validate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


