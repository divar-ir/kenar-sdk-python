# PaymentTicketValidateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Deprecated. Use divar_user_id. | [optional] 
**service_cost** | **int** |  | [optional] 
**ticket_uuid** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.payment_ticket_validate_request import PaymentTicketValidateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTicketValidateRequest from a JSON string
payment_ticket_validate_request_instance = PaymentTicketValidateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentTicketValidateRequest.to_json())

# convert the object into a dict
payment_ticket_validate_request_dict = payment_ticket_validate_request_instance.to_dict()
# create an instance of PaymentTicketValidateRequest from a dict
payment_ticket_validate_request_from_dict = PaymentTicketValidateRequest.from_dict(payment_ticket_validate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


