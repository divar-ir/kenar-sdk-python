# kenar_api_client.PostApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_can_user_submit_post**](PostApi.md#post_can_user_submit_post) | **GET** /experimental/open-platform/user-posts/can-submit | بررسی اینکه آیا کاربر می‌تواند آگهی ارسال کند
[**post_create_business_customized_button**](PostApi.md#post_create_business_customized_button) | **POST** /experimental/open-platform/business/{business_token}/customized-button | ایجاد دکمه اختصاصی برای آگهی‌های کسب‌و‌کار
[**post_delete_business_customized_button**](PostApi.md#post_delete_business_customized_button) | **DELETE** /experimental/open-platform/business/{business_token}/customized-button | حذف دکمه اختصاصی از آگهی‌های کسب‌و‌کار
[**post_delete_post_customized_button**](PostApi.md#post_delete_post_customized_button) | **DELETE** /experimental/open-platform/posts/{post_token}/customized-button | حذف دکمه اختصاصی از آگهی
[**post_delete_user_post**](PostApi.md#post_delete_user_post) | **DELETE** /v1/open-platform/post/{post_token} | حذف آگهی
[**post_edit_post**](PostApi.md#post_edit_post) | **PUT** /v1/open-platform/post/{post_token} | ویرایش آگهی
[**post_edit_post_v2**](PostApi.md#post_edit_post_v2) | **PUT** /v2/open-platform/post/{post_token} | ویرایش آگهی با پشتیبانی از فیلد ماسک
[**post_get_image_upload_url**](PostApi.md#post_get_image_upload_url) | **GET** /v1/open-platform/post/image-upload-url | دریافت آدرس اپلود تصاویر آگهی (منسوخ شده)
[**post_get_post_stats**](PostApi.md#post_get_post_stats) | **GET** /experimental/open-platform/posts/{post_token}/stats | دریافت آمارهای آگهی
[**post_get_upload_urls_v2**](PostApi.md#post_get_upload_urls_v2) | **GET** /v2/open-platform/post/upload-urls | دریافت آدرس آپلود برای تصاویر و ویدیو‌ی آگهی‌ها
[**post_get_user_post**](PostApi.md#post_get_user_post) | **GET** /v1/open-platform/user-post/{token} | دریافت آگهی با توکن
[**post_set_post_customized_button**](PostApi.md#post_set_post_customized_button) | **POST** /experimental/open-platform/posts/{post_token}/customized-button | تنظیم دکمه اختصاصی بر روی آگهی ثبت شده
[**post_submit_post**](PostApi.md#post_submit_post) | **POST** /experimental/open-platform/posts/new | ثبت آگهی
[**post_submit_post_v2**](PostApi.md#post_submit_post_v2) | **POST** /experimental/open-platform/posts/new-v2 | ثبت آگهی با استفاده از اعتبارسنجی قالب JSON
[**post_submit_user_post**](PostApi.md#post_submit_user_post) | **POST** /experimental/open-platform/user-posts/new | ثبت آگهی به عنوان کاربر


# **post_can_user_submit_post**
> PostCanUserSubmitPostResponse post_can_user_submit_post()

بررسی اینکه آیا کاربر می‌تواند آگهی ارسال کند

با این API میتوانید بررسی کنید آیا کاربر می‌تواند آگهی ارسال کند یا خیر.این API انتظار دارد توکن کاربر در درخواست با اسکوپ `SUBMIT_USER_POST` موجود باشد.

مجوزهای مورد نیاز: CAN_USER_SUBMIT_POST.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.post_can_user_submit_post_response import PostCanUserSubmitPostResponse
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)

    try:
        # بررسی اینکه آیا کاربر می‌تواند آگهی ارسال کند
        api_response = api_instance.post_can_user_submit_post()
        print("The response of PostApi->post_can_user_submit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_can_user_submit_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PostCanUserSubmitPostResponse**](PostCanUserSubmitPostResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_business_customized_button**
> object post_create_business_customized_button(business_token, post_create_business_customized_button_body)

ایجاد دکمه اختصاصی برای آگهی‌های کسب‌و‌کار

این API برای ایجاد دکمه اختصاصی برای تمام آگهی‌های کسب‌وکار استفاده می‌شود.
این API به مجوز `BUSINESS_CUSTOMIZED_BUTTON_CREATE` و دامنه OAuth `BUSINESS_CREATE_CUSTOMIZED_BUTTON.{business_ref}` نیاز دارد.


مجوزهای مورد نیاز: BUSINESS_CUSTOMIZED_BUTTON_CREATE.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.post_create_business_customized_button_body import PostCreateBusinessCustomizedButtonBody
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)
    business_token = 'business_token_example' # str | 
    post_create_business_customized_button_body = kenar_api_client.PostCreateBusinessCustomizedButtonBody() # PostCreateBusinessCustomizedButtonBody | 

    try:
        # ایجاد دکمه اختصاصی برای آگهی‌های کسب‌و‌کار
        api_response = api_instance.post_create_business_customized_button(business_token, post_create_business_customized_button_body)
        print("The response of PostApi->post_create_business_customized_button:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_create_business_customized_button: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_token** | **str**|  | 
 **post_create_business_customized_button_body** | [**PostCreateBusinessCustomizedButtonBody**](PostCreateBusinessCustomizedButtonBody.md)|  | 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_delete_business_customized_button**
> object post_delete_business_customized_button(business_token)

حذف دکمه اختصاصی از آگهی‌های کسب‌و‌کار

این API دکمه اختصاصی را از تمام آگهی‌های کسب‌وکار حذف می‌کند. این API به مجوز `BUSINESS_CUSTOMIZED_BUTTON_CREATE` نیاز دارد.


مجوزهای مورد نیاز: BUSINESS_CUSTOMIZED_BUTTON_CREATE.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)
    business_token = 'business_token_example' # str | 

    try:
        # حذف دکمه اختصاصی از آگهی‌های کسب‌و‌کار
        api_response = api_instance.post_delete_business_customized_button(business_token)
        print("The response of PostApi->post_delete_business_customized_button:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_delete_business_customized_button: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_token** | **str**|  | 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_delete_post_customized_button**
> object post_delete_post_customized_button(post_token)

حذف دکمه اختصاصی از آگهی

این API دکمه اختصاصی را از آگهی ثبت شده توسط سرویس شما حذف می‌کند. این API نیاز به مجوز `SET_CUSTOMIZED_BUTTON` دارد.


مجوزهای مورد نیاز: SET_CUSTOMIZED_BUTTON.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)
    post_token = 'post_token_example' # str | 

    try:
        # حذف دکمه اختصاصی از آگهی
        api_response = api_instance.post_delete_post_customized_button(post_token)
        print("The response of PostApi->post_delete_post_customized_button:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_delete_post_customized_button: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_token** | **str**|  | 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_delete_user_post**
> object post_delete_user_post(post_token)

حذف آگهی

این API به شما امکان حذف آگهی را می‌دهد. این نیاز به اسکوپ OAuth `DELETE_USER_POST` دارد.

مجوزهای مورد نیاز: DELETE_USER_POST.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)
    post_token = 'post_token_example' # str | توکن آگهی برای حذف

    try:
        # حذف آگهی
        api_response = api_instance.post_delete_user_post(post_token)
        print("The response of PostApi->post_delete_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_delete_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_token** | **str**| توکن آگهی برای حذف | 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_edit_post**
> object post_edit_post(post_token, post_edit_post_body)

ویرایش آگهی

این API به شما امکان ویرایش آگهی را می‌دهد. این نیاز به دامنه OAuth `POST_EDIT.{post_token}` دارد.
در حال حاضر فقط می‌توانید عنوان، توضیحات و تصاویر آگهی را ویرایش کنید.

مجوزهای مورد نیاز: EDIT_POST.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.post_edit_post_body import PostEditPostBody
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)
    post_token = 'post_token_example' # str | 
    post_edit_post_body = kenar_api_client.PostEditPostBody() # PostEditPostBody | 

    try:
        # ویرایش آگهی
        api_response = api_instance.post_edit_post(post_token, post_edit_post_body)
        print("The response of PostApi->post_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_token** | **str**|  | 
 **post_edit_post_body** | [**PostEditPostBody**](PostEditPostBody.md)|  | 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_edit_post_v2**
> object post_edit_post_v2(post_token, post_edit_post_v2_body)

ویرایش آگهی با پشتیبانی از فیلد ماسک

این API به شما امکان ویرایش آگهی با استفاده از احراز هویت OAuth را می‌دهد.
توکن دسترسی از یک کاربر با اسکوپ OAuth `POST_EDIT.{post_token}` یا `EDIT_USER_POST` مورد نیاز است.

می‌توانید عنوان، توضیحات، تصاویر، موقعیت، فیلدهای مخصوص دسته‌بندی و سایر ویژگی‌های آگهی را ویرایش کنید. فیلدهای مخصوص دسته‌بندی باید از قالب دسته‌بندی آگهی پیروی کنند. قالب را از اینجا دریافت کنید: https://kenar.divar.dev/openapi-doc/assets-get-submit-schema/

از فیلد update_mask برای مشخص کردن فیلدهایی که می‌خواهید به‌روزرسانی کنید استفاده کنید.

مجوزهای مورد نیاز: EDIT_POST.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.post_edit_post_v2_body import PostEditPostV2Body
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)
    post_token = 'post_token_example' # str | توکن آگهی
    post_edit_post_v2_body = kenar_api_client.PostEditPostV2Body() # PostEditPostV2Body | 

    try:
        # ویرایش آگهی با پشتیبانی از فیلد ماسک
        api_response = api_instance.post_edit_post_v2(post_token, post_edit_post_v2_body)
        print("The response of PostApi->post_edit_post_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_edit_post_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_token** | **str**| توکن آگهی | 
 **post_edit_post_v2_body** | [**PostEditPostV2Body**](PostEditPostV2Body.md)|  | 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_image_upload_url**
> PostGetImageUploadURLResponse post_get_image_upload_url()

دریافت آدرس اپلود تصاویر آگهی (منسوخ شده)

این API به شما اجازه می‌دهد یک آدرس اینترنتی برای بارگذاری تصاویر یک پست دریافت کنید.
می‌توانید تصاویر را با یک درخواست POST و رمزگذاری باینری به آدرس برگشتی بارگذاری کنید.
به جای آن از https://kenar.divar.dev/openapi-doc/post-get-upload-urls-v2/ استفاده کنید

مجوزهای مورد نیاز: UPLOAD_POST_IMAGE.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.post_get_image_upload_url_response import PostGetImageUploadURLResponse
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)

    try:
        # دریافت آدرس اپلود تصاویر آگهی (منسوخ شده)
        api_response = api_instance.post_get_image_upload_url()
        print("The response of PostApi->post_get_image_upload_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_get_image_upload_url: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PostGetImageUploadURLResponse**](PostGetImageUploadURLResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_post_stats**
> PostGetPostStatsResponse post_get_post_stats(post_token)

دریافت آمارهای آگهی

از این api برای مشاهده‌ی آمارهای یک آگهی (مانند تعداد بازدید‌های آگهی) استفاده کنید. 

مجوزهای مورد نیاز: POST_STATS_RETRIEVE.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.post_get_post_stats_response import PostGetPostStatsResponse
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)
    post_token = 'post_token_example' # str | توکن آگهی

    try:
        # دریافت آمارهای آگهی
        api_response = api_instance.post_get_post_stats(post_token)
        print("The response of PostApi->post_get_post_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_get_post_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_token** | **str**| توکن آگهی | 

### Return type

[**PostGetPostStatsResponse**](PostGetPostStatsResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_upload_urls_v2**
> PostGetUploadURLsV2Response post_get_upload_urls_v2()

دریافت آدرس آپلود برای تصاویر و ویدیو‌ی آگهی‌ها

این API به شما امکان دریافت URL آپلود برای آپلود تصاویر و ویدیوهای آگهی را می‌دهد.
می‌توانید تصاویر/ویدیوها را با استفاده از درخواست POST یا PUT با کدگذاری باینری به URL برگشتی آپلود کنید. آدرس برگشتی این API به api-key شما برای آپلود نیاز دارد. لطفاً توجه داشته باشید که آدرس برگشتی ممکن است بدون اطلاع قبلی تغییر کند.

مجوزهای مورد نیاز: UPLOAD_POST_IMAGE.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.post_get_upload_urls_v2_response import PostGetUploadURLsV2Response
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)

    try:
        # دریافت آدرس آپلود برای تصاویر و ویدیو‌ی آگهی‌ها
        api_response = api_instance.post_get_upload_urls_v2()
        print("The response of PostApi->post_get_upload_urls_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_get_upload_urls_v2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PostGetUploadURLsV2Response**](PostGetUploadURLsV2Response.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_user_post**
> PostGetUserPostResponse post_get_user_post(token)

دریافت آگهی با توکن

این API به شما امکان دریافت اطلاعات دقیق درباره یک آگهی خاص با استفاده از توکن آن را می‌دهد.
این نقطه پایانی آگهی‌های ثبت شده توسط کاربران احراز هویت شده از طریق پلتفرم باز را برمی‌گرداند، شامل داده‌های کسب‌وکار، وضعیت و دلایل رد.
این API به مجوز `GET_USER_POST` نیاز دارد.
این API به دامنه OAuth `USER_POSTS_GET` نیاز دارد.

مجوزهای مورد نیاز: GET_USER_POST.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.post_get_user_post_response import PostGetUserPostResponse
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)
    token = 'token_example' # str | 

    try:
        # دریافت آگهی با توکن
        api_response = api_instance.post_get_user_post(token)
        print("The response of PostApi->post_get_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_get_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**PostGetUserPostResponse**](PostGetUserPostResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_set_post_customized_button**
> object post_set_post_customized_button(post_token, post_set_post_customized_button_body)

تنظیم دکمه اختصاصی بر روی آگهی ثبت شده

این API برای تنظیم دکمه اختصاصی برای یک آگهی استفاده می‌شود. اگر دکمه‌ای وجود نداشته باشد، ایجاد خواهد شد. اگر از قبل وجود داشته باشد، داده‌های آن به‌روزرسانی خواهد شد. این API به مجوز `SET_CUSTOMIZED_BUTTON` نیاز دارد.
اگر این آگهی توسط کاربر ثبت شده باشد، این API به توکن دسترسی کاربر در هدرهای درخواست با دامنه OAuth `USER_SET_CUSTOMIZED_BUTTON` نیاز دارد.

مجوزهای مورد نیاز: SET_CUSTOMIZED_BUTTON.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.post_set_post_customized_button_body import PostSetPostCustomizedButtonBody
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)
    post_token = 'post_token_example' # str | 
    post_set_post_customized_button_body = kenar_api_client.PostSetPostCustomizedButtonBody() # PostSetPostCustomizedButtonBody | 

    try:
        # تنظیم دکمه اختصاصی بر روی آگهی ثبت شده
        api_response = api_instance.post_set_post_customized_button(post_token, post_set_post_customized_button_body)
        print("The response of PostApi->post_set_post_customized_button:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_set_post_customized_button: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_token** | **str**|  | 
 **post_set_post_customized_button_body** | [**PostSetPostCustomizedButtonBody**](PostSetPostCustomizedButtonBody.md)|  | 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_submit_post**
> PostSubmitPostResponse post_submit_post(post_submit_post_request)

ثبت آگهی

این API به شما امکان ثبت آگهی را می‌دهد. این نیاز به دامنه OAuth `SUBMIT_POST` دارد.
می‌توانید آگهی را با عنوان، توضیحات، تصاویر و سایر فیلدها ثبت کنید. فیلدهای عمومی و فیلدهای مخصوص دسته‌بندی وجود دارند.

مجوزهای مورد نیاز: SUBMIT_POST.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.post_submit_post_request import PostSubmitPostRequest
from kenar_api_client.models.post_submit_post_response import PostSubmitPostResponse
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)
    post_submit_post_request = kenar_api_client.PostSubmitPostRequest() # PostSubmitPostRequest | 

    try:
        # ثبت آگهی
        api_response = api_instance.post_submit_post(post_submit_post_request)
        print("The response of PostApi->post_submit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_submit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_submit_post_request** | [**PostSubmitPostRequest**](PostSubmitPostRequest.md)|  | 

### Return type

[**PostSubmitPostResponse**](PostSubmitPostResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_submit_post_v2**
> PostSubmitPostResponse post_submit_post_v2(post_submit_post_v2_request)

ثبت آگهی با استفاده از اعتبارسنجی قالب JSON

این API به شما امکان ثبت آگهی با استفاده از اعتبارسنجی قالب JSON را می‌دهد. این به مجوز `SUBMIT_POST` نیاز دارد.
شما داده‌های کامل آگهی را به عنوان یک رشته JSON ارائه می‌دهید که با احترام به قالب ثبت برای دسته‌بندی مشخص شده موجود در دارایی‌ها اعتبارسنجی خواهد شد.

مجوزهای مورد نیاز: SUBMIT_POST.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.post_submit_post_response import PostSubmitPostResponse
from kenar_api_client.models.post_submit_post_v2_request import PostSubmitPostV2Request
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)
    post_submit_post_v2_request = kenar_api_client.PostSubmitPostV2Request() # PostSubmitPostV2Request | 

    try:
        # ثبت آگهی با استفاده از اعتبارسنجی قالب JSON
        api_response = api_instance.post_submit_post_v2(post_submit_post_v2_request)
        print("The response of PostApi->post_submit_post_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_submit_post_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_submit_post_v2_request** | [**PostSubmitPostV2Request**](PostSubmitPostV2Request.md)|  | 

### Return type

[**PostSubmitPostResponse**](PostSubmitPostResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_submit_user_post**
> PostSubmitPostResponse post_submit_user_post(post_submit_user_post_request)

ثبت آگهی به عنوان کاربر

این API به شما امکان ثبت آگهی از طرف یک کاربر احراز هویت شده با استفاده از اعتبارسنجی قالب JSON را می‌دهد. این به احراز هویت OAuth با توکن دسترسی معتبر و دامنه OAuth `SUBMIT_USER_POST` نیاز دارد.
بر خلاف SubmitPostV2 که آگهی‌ها را به عنوان ارائه‌دهنده ثبت می‌کند، این نقطه پایانی آگهی‌ها را به عنوان کاربر مرتبط با توکن دسترسی ارائه شده ثبت می‌کند. آگهی متعلق به کاربر احراز هویت شده خواهد بود.
شما داده‌های کامل آگهی را به عنوان یک رشته JSON ارائه می‌دهید که با احترام به قالب ثبت برای دسته‌بندی مشخص شده موجود در دارایی‌ها اعتبارسنجی خواهد شد.

مجوزهای مورد نیاز: SUBMIT_USER_POST.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.post_submit_post_response import PostSubmitPostResponse
from kenar_api_client.models.post_submit_user_post_request import PostSubmitUserPostRequest
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration.api_key['APIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PostApi(api_client)
    post_submit_user_post_request = kenar_api_client.PostSubmitUserPostRequest() # PostSubmitUserPostRequest | 

    try:
        # ثبت آگهی به عنوان کاربر
        api_response = api_instance.post_submit_user_post(post_submit_user_post_request)
        print("The response of PostApi->post_submit_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_submit_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_submit_user_post_request** | [**PostSubmitUserPostRequest**](PostSubmitUserPostRequest.md)|  | 

### Return type

[**PostSubmitPostResponse**](PostSubmitPostResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

