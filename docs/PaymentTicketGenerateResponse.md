# PaymentTicketGenerateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_uuid** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.payment_ticket_generate_response import PaymentTicketGenerateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTicketGenerateResponse from a JSON string
payment_ticket_generate_response_instance = PaymentTicketGenerateResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentTicketGenerateResponse.to_json())

# convert the object into a dict
payment_ticket_generate_response_dict = payment_ticket_generate_response_instance.to_dict()
# create an instance of PaymentTicketGenerateResponse from a dict
payment_ticket_generate_response_from_dict = PaymentTicketGenerateResponse.from_dict(payment_ticket_generate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


