# kenar_api_client.PostApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_can_user_submit_post**](PostApi.md#post_can_user_submit_post) | **GET** /experimental/open-platform/user-posts/can-submit | Check if user can submit post
[**post_edit_post**](PostApi.md#post_edit_post) | **PUT** /v1/open-platform/post/{post_token} | ویرایش آگهی
[**post_get_image_upload_url**](PostApi.md#post_get_image_upload_url) | **GET** /v1/open-platform/post/image-upload-url | دریافت URL آپلود تصویر
[**post_get_post_stats**](PostApi.md#post_get_post_stats) | **GET** /experimental/open-platform/posts/{post_token}/stats | دریافت آمارهای آگهی
[**post_submit_post**](PostApi.md#post_submit_post) | **POST** /experimental/open-platform/posts/new | ثبت آگهی
[**post_submit_post_v2**](PostApi.md#post_submit_post_v2) | **POST** /experimental/open-platform/posts/new-v2 | ثبت آگهی با استفاده از اعتبارسنجی قالب JSON
[**post_submit_user_post**](PostApi.md#post_submit_user_post) | **POST** /experimental/open-platform/user-posts/new | ثبت آگهی به عنوان کاربر


# **post_can_user_submit_post**
> PostCanUserSubmitPostResponse post_can_user_submit_post()

Check if user can submit post

This API allows you to check if a user can submit a post.This API expects the user's access token in the request headers with the `SUBMIT_USER_POST` OAuth scope.

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
        # Check if user can submit post
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

# **post_edit_post**
> object post_edit_post(post_token, post_edit_post_body)

ویرایش آگهی

این API به شما امکان ویرایش آگهی را می‌دهد. این نیاز به دامنه OAuth `POST_EDIT.{post_token}` دارد.
در حال حاضر فقط می‌توانید عنوان، توضیحات و تصاویر آگهی را ویرایش کنید.

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

# **post_get_image_upload_url**
> PostGetImageUploadURLResponse post_get_image_upload_url()

دریافت URL آپلود تصویر

این API به شما امکان دریافت URL آپلود برای آپلود تصاویر آگهی را می‌دهد.
می‌توانید تصاویر را با استفاده از درخواست POST با کدگذاری باینری به URL برگشتی آپلود کنید.

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
        # دریافت URL آپلود تصویر
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

# **post_submit_post**
> PostSubmitPostResponse post_submit_post(post_submit_post_request)

ثبت آگهی

این API به شما امکان ثبت آگهی را می‌دهد. این نیاز به دامنه OAuth `POST_SUBMIT` دارد.
می‌توانید آگهی را با عنوان، توضیحات، تصاویر و سایر فیلدها ثبت کنید. فیلدهای عمومی و فیلدهای مخصوص دسته‌بندی وجود دارند.

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

این API به شما امکان ثبت آگهی با استفاده از اعتبارسنجی قالب JSON را می‌دهد. این به مجوز `POST_SUBMIT` نیاز دارد.
شما داده‌های کامل آگهی را به عنوان یک رشته JSON ارائه می‌دهید که با احترام به قالب ثبت برای دسته‌بندی مشخص شده موجود در دارایی‌ها اعتبارسنجی خواهد شد.

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

