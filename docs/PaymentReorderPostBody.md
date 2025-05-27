# PaymentReorderPostBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_details** | **str** | جزئیات اضافی که می‌خواهید به سمت کنار ارسال کنید. این فیلد اختیاری است و می‌تواند برای حل ناسازگاری‌ها در تراکنش استفاده شود. | [optional] 
**id** | **str** | یک uuid نسخه 4 که باید برای هر پرداخت منحصر به فرد باشد. این uuid باید در سمت شما تولید شده و در درخواست ارسال شود. اگر id ای ارسال شود که تراکنش موفق یا نیمه موفقی در سمت کنار داشته باشد، خطا دریافت خواهید کرد. | [optional] 

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


