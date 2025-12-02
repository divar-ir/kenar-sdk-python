# PaymentReorderPostBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_details** | **str** | اطلاعات تکمیلی که می‌خواهید به کنار ارسال کنید. این فیلد اختیاری است و برای رفع مغایرت‌های احتمالی در تراکنش کاربرد دارد. | [optional] 
**id** | **str** | یک UUID نسخه ۴ که باید برای هر پرداخت یکتا باشد. این UUID باید در سمت شما ساخته شده و در درخواست ارسال شود. اگر id ارسال‌شده قبلاً تراکنش موفق یا نیمه‌موفقی در کنار داشته باشد، خطا دریافت می‌کنید. | [optional] 

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


