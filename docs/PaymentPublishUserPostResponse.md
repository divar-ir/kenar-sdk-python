# PaymentPublishUserPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**PaymentTransaction**](PaymentTransaction.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.payment_publish_user_post_response import PaymentPublishUserPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPublishUserPostResponse from a JSON string
payment_publish_user_post_response_instance = PaymentPublishUserPostResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentPublishUserPostResponse.to_json())

# convert the object into a dict
payment_publish_user_post_response_dict = payment_publish_user_post_response_instance.to_dict()
# create an instance of PaymentPublishUserPostResponse from a dict
payment_publish_user_post_response_from_dict = PaymentPublishUserPostResponse.from_dict(payment_publish_user_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


