# PaymentPublishUserPostBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_details** | **str** | جزئیات اضافی که می‌خواهید به سمت کنار ارسال کنید. این فیلد اختیاری است و می‌تواند برای حل ناسازگاری‌ها در تراکنش استفاده شود. | [optional] 
**id** | **str** | یک uuid نسخه 4 که باید برای هر پرداخت منحصر به فرد باشد. این uuid باید در سمت شما تولید شده و در درخواست ارسال شود. اگر id ای ارسال شود که تراکنش موفق یا نیمه موفقی در سمت کنار داشته باشد، خطا دریافت خواهید کرد. | [optional] 

## Example

```python
from kenar_api_client.models.payment_publish_user_post_body import PaymentPublishUserPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPublishUserPostBody from a JSON string
payment_publish_user_post_body_instance = PaymentPublishUserPostBody.from_json(json)
# print the JSON string representation of the object
print(PaymentPublishUserPostBody.to_json())

# convert the object into a dict
payment_publish_user_post_body_dict = payment_publish_user_post_body_instance.to_dict()
# create an instance of PaymentPublishUserPostBody from a dict
payment_publish_user_post_body_from_dict = PaymentPublishUserPostBody.from_dict(payment_publish_user_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


