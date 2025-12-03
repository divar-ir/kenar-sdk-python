# kenar_api_client.SemanticApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**semantic_create_post_semantic**](SemanticApi.md#semantic_create_post_semantic) | **POST** /experimental/open-platform/semantic/post/{token} | ایجاد اطلاعات معنایی آگهی
[**semantic_create_user_semantic**](SemanticApi.md#semantic_create_user_semantic) | **POST** /v1/open-platform/semantic/user/{phone} | ایجاد اطلاعات معنایی کاربر
[**semantic_create_user_semantic2**](SemanticApi.md#semantic_create_user_semantic2) | **POST** /v1/open-platform/semantic/users/{divar_user_id} | ایجاد اطلاعات معنایی کاربر
[**semantic_delete_user_semantic**](SemanticApi.md#semantic_delete_user_semantic) | **DELETE** /v1/open-platform/semantic/user/{phone} | حذف اطلاعات معنایی کاربر
[**semantic_delete_user_semantic2**](SemanticApi.md#semantic_delete_user_semantic2) | **DELETE** /v1/open-platform/semantic/users/{divar_user_id} | حذف اطلاعات معنایی کاربر


# **semantic_create_post_semantic**
> object semantic_create_post_semantic(token, semantic_create_post_semantic_body)

ایجاد اطلاعات معنایی آگهی

این API امکان ذخیره اطلاعات درباره یک آگهی در دیوار بدون افزودن افزونه را فراهم می‌کند.

#### دسترسی‌ها:

##### مجوزهای API Key مورد نیاز:

- `POST_SEMANTIC_CREATE`

##### OAuth اسکوپ موردنیاز:

- `POST_SEMANTIC_CREATE.post_token`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

```python
import kenar_api_client
from kenar_api_client.models.semantic_create_post_semantic_body import SemanticCreatePostSemanticBody
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.SemanticApi(api_client)
    token = 'token_example' # str | توکن آگهی
    semantic_create_post_semantic_body = kenar_api_client.SemanticCreatePostSemanticBody() # SemanticCreatePostSemanticBody | 

    try:
        # ایجاد اطلاعات معنایی آگهی
        api_response = api_instance.semantic_create_post_semantic(token, semantic_create_post_semantic_body)
        print("The response of SemanticApi->semantic_create_post_semantic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticApi->semantic_create_post_semantic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| توکن آگهی | 
 **semantic_create_post_semantic_body** | [**SemanticCreatePostSemanticBody**](SemanticCreatePostSemanticBody.md)|  | 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **semantic_create_user_semantic**
> SemanticCreateUserSemanticResponse semantic_create_user_semantic(phone, semantic_create_user_semantic_body)

ایجاد اطلاعات معنایی کاربر

این API امکان ایجاد یا به‌روزرسانی semantic کاربر بدون افزودن افزونه را می‌دهد.

**نکات مهم**:
- امکان ارسال اطلاعات معنایی و تیکت پرداخت (اختیاری) وجود دارد

#### دسترسی‌ها:

##### مجوزهای API Key مورد نیاز:

- `USER_SEMANTIC_CREATE`

##### OAuth اسکوپ موردنیاز:

- `USER_VERIFICATION_CREATE`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

```python
import kenar_api_client
from kenar_api_client.models.semantic_create_user_semantic_body import SemanticCreateUserSemanticBody
from kenar_api_client.models.semantic_create_user_semantic_response import SemanticCreateUserSemanticResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.SemanticApi(api_client)
    phone = 'phone_example' # str | شماره موبایل کاربر
    semantic_create_user_semantic_body = kenar_api_client.SemanticCreateUserSemanticBody() # SemanticCreateUserSemanticBody | 

    try:
        # ایجاد اطلاعات معنایی کاربر
        api_response = api_instance.semantic_create_user_semantic(phone, semantic_create_user_semantic_body)
        print("The response of SemanticApi->semantic_create_user_semantic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticApi->semantic_create_user_semantic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| شماره موبایل کاربر | 
 **semantic_create_user_semantic_body** | [**SemanticCreateUserSemanticBody**](SemanticCreateUserSemanticBody.md)|  | 

### Return type

[**SemanticCreateUserSemanticResponse**](SemanticCreateUserSemanticResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **semantic_create_user_semantic2**
> SemanticCreateUserSemanticResponse semantic_create_user_semantic2(divar_user_id, semantic_create_user_semantic_body)

ایجاد اطلاعات معنایی کاربر

این API امکان ایجاد یا به‌روزرسانی semantic کاربر بدون افزودن افزونه را می‌دهد.

**نکات مهم**:
- امکان ارسال اطلاعات معنایی و تیکت پرداخت (اختیاری) وجود دارد

#### دسترسی‌ها:

##### مجوزهای API Key مورد نیاز:

- `USER_SEMANTIC_CREATE`

##### OAuth اسکوپ موردنیاز:

- `USER_VERIFICATION_CREATE`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

```python
import kenar_api_client
from kenar_api_client.models.semantic_create_user_semantic_body import SemanticCreateUserSemanticBody
from kenar_api_client.models.semantic_create_user_semantic_response import SemanticCreateUserSemanticResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.SemanticApi(api_client)
    divar_user_id = 'divar_user_id_example' # str | شناسه کاربر دیوار
    semantic_create_user_semantic_body = kenar_api_client.SemanticCreateUserSemanticBody() # SemanticCreateUserSemanticBody | 

    try:
        # ایجاد اطلاعات معنایی کاربر
        api_response = api_instance.semantic_create_user_semantic2(divar_user_id, semantic_create_user_semantic_body)
        print("The response of SemanticApi->semantic_create_user_semantic2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticApi->semantic_create_user_semantic2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **divar_user_id** | **str**| شناسه کاربر دیوار | 
 **semantic_create_user_semantic_body** | [**SemanticCreateUserSemanticBody**](SemanticCreateUserSemanticBody.md)|  | 

### Return type

[**SemanticCreateUserSemanticResponse**](SemanticCreateUserSemanticResponse.md)

### Authorization

[APIKey](../README.md#APIKey), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **semantic_delete_user_semantic**
> object semantic_delete_user_semantic(phone, divar_user_id=divar_user_id)

حذف اطلاعات معنایی کاربر

این API امکان حذف اطلاعات معنایی یک کاربر را فراهم می‌کند.

#### دسترسی‌ها:

##### مجوزهای API Key مورد نیاز:

- `USER_SEMANTIC_DELETE`

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
    api_instance = kenar_api_client.SemanticApi(api_client)
    phone = 'phone_example' # str | شماره موبایل کاربر
    divar_user_id = 'divar_user_id_example' # str | شناسه کاربر دیوار (optional)

    try:
        # حذف اطلاعات معنایی کاربر
        api_response = api_instance.semantic_delete_user_semantic(phone, divar_user_id=divar_user_id)
        print("The response of SemanticApi->semantic_delete_user_semantic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticApi->semantic_delete_user_semantic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| شماره موبایل کاربر | 
 **divar_user_id** | **str**| شناسه کاربر دیوار | [optional] 

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

# **semantic_delete_user_semantic2**
> object semantic_delete_user_semantic2(divar_user_id, phone)

حذف اطلاعات معنایی کاربر

این API امکان حذف اطلاعات معنایی یک کاربر را فراهم می‌کند.

#### دسترسی‌ها:

##### مجوزهای API Key مورد نیاز:

- `USER_SEMANTIC_DELETE`

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
    api_instance = kenar_api_client.SemanticApi(api_client)
    divar_user_id = 'divar_user_id_example' # str | شناسه کاربر دیوار
    phone = 'phone_example' # str | شماره موبایل کاربر

    try:
        # حذف اطلاعات معنایی کاربر
        api_response = api_instance.semantic_delete_user_semantic2(divar_user_id, phone)
        print("The response of SemanticApi->semantic_delete_user_semantic2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticApi->semantic_delete_user_semantic2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **divar_user_id** | **str**| شناسه کاربر دیوار | 
 **phone** | **str**| شماره موبایل کاربر | 

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

