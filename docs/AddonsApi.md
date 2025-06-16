# kenar_api_client.AddonsApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addons_create_business_addon**](AddonsApi.md#addons_create_business_addon) | **POST** /v1/open-platform/addons/business/{business_token} | افزودن افزونه جدید به آگهی‌های کسب‌و‌کار
[**addons_create_post_addon_v2**](AddonsApi.md#addons_create_post_addon_v2) | **POST** /v2/open-platform/addons/post/{token} | افزودن افزونه جدید به آگهی
[**addons_create_user_addon_v2**](AddonsApi.md#addons_create_user_addon_v2) | **POST** /v2/open-platform/addons/user/{phone} | افزودن افزونه جدید به کاربر
[**addons_create_user_addon_v22**](AddonsApi.md#addons_create_user_addon_v22) | **POST** /v2/open-platform/addons/users/{divar_user_id} | افزودن افزونه جدید به کاربر
[**addons_delete_post_addon**](AddonsApi.md#addons_delete_post_addon) | **DELETE** /v1/open-platform/add-ons/post/{token} | حذف افزونه از آگهی
[**addons_delete_post_addon2**](AddonsApi.md#addons_delete_post_addon2) | **DELETE** /v1/open-platform/addons/post/{token} | حذف افزونه از آگهی
[**addons_delete_user_addon**](AddonsApi.md#addons_delete_user_addon) | **DELETE** /v1/open-platform/addons/user/{id} | حذف افزونه کاربر
[**addons_get_user_addons**](AddonsApi.md#addons_get_user_addons) | **GET** /v1/open-platform/addons/user/{phone} | دریافت تمام افزونه‌های کاربر
[**addons_get_user_addons2**](AddonsApi.md#addons_get_user_addons2) | **GET** /v2/open-platform/addons/users/{divar_user_id} | دریافت تمام افزونه‌های کاربر


# **addons_create_business_addon**
> AddonsCreateBusinessAddonResponse addons_create_business_addon(business_token, addons_create_business_addon_body)

افزودن افزونه جدید به آگهی‌های کسب‌و‌کار

با استفاده از این API و با مجوز کاربر، می‌توانید افزونه جدیدی به آگهی‌های کسب‌و‌کار متصل کنید.
می‌توانید از ویجت‌های موجود برای طراحی افزونه خود استفاده کنید.
این API به توکن دسترسی با یکی از دامنه‌های زیر نیاز دارد:
- BUSINESS_ADDON_CREATE.{business_token}

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.addons_create_business_addon_body import AddonsCreateBusinessAddonBody
from kenar_api_client.models.addons_create_business_addon_response import AddonsCreateBusinessAddonResponse
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
    api_instance = kenar_api_client.AddonsApi(api_client)
    business_token = 'business_token_example' # str | 
    addons_create_business_addon_body = kenar_api_client.AddonsCreateBusinessAddonBody() # AddonsCreateBusinessAddonBody | 

    try:
        # افزودن افزونه جدید به آگهی‌های کسب‌و‌کار
        api_response = api_instance.addons_create_business_addon(business_token, addons_create_business_addon_body)
        print("The response of AddonsApi->addons_create_business_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_create_business_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_token** | **str**|  | 
 **addons_create_business_addon_body** | [**AddonsCreateBusinessAddonBody**](AddonsCreateBusinessAddonBody.md)|  | 

### Return type

[**AddonsCreateBusinessAddonResponse**](AddonsCreateBusinessAddonResponse.md)

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

# **addons_create_post_addon_v2**
> object addons_create_post_addon_v2(token, addons_create_post_addon_v2_body)

افزودن افزونه جدید به آگهی

با استفاده از این API و با مجوز کاربر، می‌توانید افزونه جدیدی به آگهی متصل کنید.
می‌توانید از ویجت‌های موجود برای طراحی افزونه خود استفاده کنید.
این API به توکن دسترسی با یکی از دامنه‌های زیر نیاز دارد:
- USER_POSTS_ADDON_CREATE
- POST_ADDON_CREATE.{post_token}

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.addons_create_post_addon_v2_body import AddonsCreatePostAddonV2Body
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
    api_instance = kenar_api_client.AddonsApi(api_client)
    token = 'token_example' # str | 
    addons_create_post_addon_v2_body = kenar_api_client.AddonsCreatePostAddonV2Body() # AddonsCreatePostAddonV2Body | 

    try:
        # افزودن افزونه جدید به آگهی
        api_response = api_instance.addons_create_post_addon_v2(token, addons_create_post_addon_v2_body)
        print("The response of AddonsApi->addons_create_post_addon_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_create_post_addon_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **addons_create_post_addon_v2_body** | [**AddonsCreatePostAddonV2Body**](AddonsCreatePostAddonV2Body.md)|  | 

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

# **addons_create_user_addon_v2**
> AddonsCreateUserAddonResponseV2 addons_create_user_addon_v2(phone, addons_create_user_addon_v2_body)

افزودن افزونه جدید به کاربر

با استفاده از این API و با مجوز کاربر، می‌توانید افزونه کاربر ایجاد کنید.
افزونه کاربر به تمام آگهی‌های آینده کاربر متصل می‌شود و همچنین 30 آگهی آخر گذشته را پر می‌کند.
می‌توانید از ویجت‌های موجود برای طراحی افزونه کاربر خود استفاده کنید.
این API به توکن دسترسی با دامنه `USER_ADDON_CREATE` نیاز دارد

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.addons_create_user_addon_response_v2 import AddonsCreateUserAddonResponseV2
from kenar_api_client.models.addons_create_user_addon_v2_body import AddonsCreateUserAddonV2Body
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
    api_instance = kenar_api_client.AddonsApi(api_client)
    phone = 'phone_example' # str | 
    addons_create_user_addon_v2_body = kenar_api_client.AddonsCreateUserAddonV2Body() # AddonsCreateUserAddonV2Body | 

    try:
        # افزودن افزونه جدید به کاربر
        api_response = api_instance.addons_create_user_addon_v2(phone, addons_create_user_addon_v2_body)
        print("The response of AddonsApi->addons_create_user_addon_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_create_user_addon_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 
 **addons_create_user_addon_v2_body** | [**AddonsCreateUserAddonV2Body**](AddonsCreateUserAddonV2Body.md)|  | 

### Return type

[**AddonsCreateUserAddonResponseV2**](AddonsCreateUserAddonResponseV2.md)

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

# **addons_create_user_addon_v22**
> AddonsCreateUserAddonResponseV2 addons_create_user_addon_v22(divar_user_id, addons_create_user_addon_v2_body)

افزودن افزونه جدید به کاربر

با استفاده از این API و با مجوز کاربر، می‌توانید افزونه کاربر ایجاد کنید.
افزونه کاربر به تمام آگهی‌های آینده کاربر متصل می‌شود و همچنین 30 آگهی آخر گذشته را پر می‌کند.
می‌توانید از ویجت‌های موجود برای طراحی افزونه کاربر خود استفاده کنید.
این API به توکن دسترسی با دامنه `USER_ADDON_CREATE` نیاز دارد

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.addons_create_user_addon_response_v2 import AddonsCreateUserAddonResponseV2
from kenar_api_client.models.addons_create_user_addon_v2_body import AddonsCreateUserAddonV2Body
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
    api_instance = kenar_api_client.AddonsApi(api_client)
    divar_user_id = 'divar_user_id_example' # str | 
    addons_create_user_addon_v2_body = kenar_api_client.AddonsCreateUserAddonV2Body() # AddonsCreateUserAddonV2Body | 

    try:
        # افزودن افزونه جدید به کاربر
        api_response = api_instance.addons_create_user_addon_v22(divar_user_id, addons_create_user_addon_v2_body)
        print("The response of AddonsApi->addons_create_user_addon_v22:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_create_user_addon_v22: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **divar_user_id** | **str**|  | 
 **addons_create_user_addon_v2_body** | [**AddonsCreateUserAddonV2Body**](AddonsCreateUserAddonV2Body.md)|  | 

### Return type

[**AddonsCreateUserAddonResponseV2**](AddonsCreateUserAddonResponseV2.md)

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

# **addons_delete_post_addon**
> object addons_delete_post_addon(token)

حذف افزونه از آگهی

فقط می‌توانید افزونه‌هایی را حذف کنید که توسط اپلیکیشن شما ایجاد شده‌اند.

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
    api_instance = kenar_api_client.AddonsApi(api_client)
    token = 'token_example' # str | 

    try:
        # حذف افزونه از آگهی
        api_response = api_instance.addons_delete_post_addon(token)
        print("The response of AddonsApi->addons_delete_post_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_delete_post_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

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

# **addons_delete_post_addon2**
> object addons_delete_post_addon2(token)

حذف افزونه از آگهی

فقط می‌توانید افزونه‌هایی را حذف کنید که توسط اپلیکیشن شما ایجاد شده‌اند.

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
    api_instance = kenar_api_client.AddonsApi(api_client)
    token = 'token_example' # str | 

    try:
        # حذف افزونه از آگهی
        api_response = api_instance.addons_delete_post_addon2(token)
        print("The response of AddonsApi->addons_delete_post_addon2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_delete_post_addon2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

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

# **addons_delete_user_addon**
> object addons_delete_user_addon(id)

حذف افزونه کاربر

این تمام افزونه‌های مرتبط با تمام آگهی‌های کاربر را حذف می‌کند.
فقط می‌توانید افزونه‌هایی را حذف کنید که توسط اپلیکیشن شما ایجاد شده‌اند.

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
    api_instance = kenar_api_client.AddonsApi(api_client)
    id = 'id_example' # str | 

    try:
        # حذف افزونه کاربر
        api_response = api_instance.addons_delete_user_addon(id)
        print("The response of AddonsApi->addons_delete_user_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_delete_user_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **addons_get_user_addons**
> AddonsGetUserAddonsResponse addons_get_user_addons(phone, divar_user_id=divar_user_id)

دریافت تمام افزونه‌های کاربر

دریافت تمام افزونه‌های کاربر یک کاربر.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.addons_get_user_addons_response import AddonsGetUserAddonsResponse
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
    api_instance = kenar_api_client.AddonsApi(api_client)
    phone = 'phone_example' # str | 
    divar_user_id = 'divar_user_id_example' # str |  (optional)

    try:
        # دریافت تمام افزونه‌های کاربر
        api_response = api_instance.addons_get_user_addons(phone, divar_user_id=divar_user_id)
        print("The response of AddonsApi->addons_get_user_addons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_get_user_addons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 
 **divar_user_id** | **str**|  | [optional] 

### Return type

[**AddonsGetUserAddonsResponse**](AddonsGetUserAddonsResponse.md)

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

# **addons_get_user_addons2**
> AddonsGetUserAddonsResponse addons_get_user_addons2(divar_user_id, phone=phone)

دریافت تمام افزونه‌های کاربر

دریافت تمام افزونه‌های کاربر یک کاربر.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.addons_get_user_addons_response import AddonsGetUserAddonsResponse
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
    api_instance = kenar_api_client.AddonsApi(api_client)
    divar_user_id = 'divar_user_id_example' # str | 
    phone = 'phone_example' # str |  (optional)

    try:
        # دریافت تمام افزونه‌های کاربر
        api_response = api_instance.addons_get_user_addons2(divar_user_id, phone=phone)
        print("The response of AddonsApi->addons_get_user_addons2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_get_user_addons2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **divar_user_id** | **str**|  | 
 **phone** | **str**|  | [optional] 

### Return type

[**AddonsGetUserAddonsResponse**](AddonsGetUserAddonsResponse.md)

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

