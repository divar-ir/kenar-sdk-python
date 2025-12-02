# PaymentTicketValidateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | شماره تلفن کاربر (به جای آن از user_id استفاده کنید) | [optional] 
**service_cost** | **int** | هزینه سرویس به ریال | 
**ticket_uuid** | **str** | شناسه منحصر به فرد تیکت پرداخت | 
**user_id** | **str** | شناسه منحصر به فرد کاربر | [optional] 

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


