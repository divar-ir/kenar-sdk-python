# PaymentReorderPostBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A Version 4 uuid that must be unique for each payment. This uuid must be generated on your side and sent in the request. If an id is sent that has a successful or semi-successful transaction on the Kenar side, you will receive an error. | [optional] 
**extra_details** | **str** | Additional details that you want to send to the Kenar side. This field is optional and can be used to solve inconsistencies in the transaction. | [optional] 

## Example

```python
from kenar_api_client.models.payment_reorder_post_body import PaymentReorderPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentReorderPostBody from a JSON string
payment_reorder_post_body_instance = PaymentReorderPostBody.from_json(json)
# print the JSON string representation of the object
print(PaymentReorderPostBody.to_json())

# convert the object into a dict
payment_reorder_post_body_dict = payment_reorder_post_body_instance.to_dict()
# create an instance of PaymentReorderPostBody from a dict
payment_reorder_post_body_from_dict = PaymentReorderPostBody.from_dict(payment_reorder_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


