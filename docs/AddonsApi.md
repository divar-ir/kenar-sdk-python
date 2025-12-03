# kenar_api_client.AddonsApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addons_create_business_addon**](AddonsApi.md#addons_create_business_addon) | **POST** /v1/open-platform/addons/business/{business_token} | ایجاد افزونه کسب‌وکار
[**addons_create_post_addon_v2**](AddonsApi.md#addons_create_post_addon_v2) | **POST** /v2/open-platform/addons/post/{token} | ایجاد افزونه آگهی
[**addons_create_user_addon_v2**](AddonsApi.md#addons_create_user_addon_v2) | **POST** /v2/open-platform/addons/user/{phone} | ایجاد افزونه کاربر
[**addons_create_user_addon_v22**](AddonsApi.md#addons_create_user_addon_v22) | **POST** /v2/open-platform/addons/users/{divar_user_id} | ایجاد افزونه کاربر
[**addons_delete_post_addon**](AddonsApi.md#addons_delete_post_addon) | **DELETE** /v1/open-platform/add-ons/post/{token} | حذف افزونه آگهی
[**addons_delete_post_addon2**](AddonsApi.md#addons_delete_post_addon2) | **DELETE** /v1/open-platform/addons/post/{token} | حذف افزونه آگهی
[**addons_delete_user_addon**](AddonsApi.md#addons_delete_user_addon) | **DELETE** /v1/open-platform/addons/user/{id} | حذف افزونه کاربر


# **addons_create_business_addon**
> AddonsCreateBusinessAddonResponse addons_create_business_addon(business_token, addons_create_business_addon_body)

ایجاد افزونه کسب‌وکار

این API امکان ایجاد افزونه کسب‌وکار را فراهم می‌کند که روی تمام آگهی‌های منتشر شده یک کسب‌وکار نمایش داده می‌شود.

**نکات مهم**:
- ویجت‌ها باید معتبر بوده و از مشخصات فرمت ویجت پیروی کنند
- مالکیت کسب‌وکار قبل از ایجاد افزونه بررسی می‌شود

#### دسترسی‌ها:

##### مجوزهای API Key مورد نیاز:

- `BUSINESS_ADDON_CREATE`

##### OAuth اسکوپ موردنیاز:

- `BUSINESS_ADDON_CREATE.business_token`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.AddonsApi(api_client)
    business_token = 'business_token_example' # str | 
    addons_create_business_addon_body = kenar_api_client.AddonsCreateBusinessAddonBody() # AddonsCreateBusinessAddonBody | 

    try:
        # ایجاد افزونه کسب‌وکار
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

# **addons_create_post_addon_v2**
> object addons_create_post_addon_v2(token, addons_create_post_addon_v2_body)

ایجاد افزونه آگهی

این API امکان ایجاد افزونه متصل به یک آگهی خاص را فراهم می‌کند. افزونه در صفحه جزئیات آگهی نمایش داده می‌شود.

**نکات مهم**:
- ویجت‌ها باید معتبر بوده و از مشخصات فرمت ویجت پیروی کنند
- مسیرهای معنایی از ویجت‌ها برای دسته‌بندی استخراج می‌شوند

#### دسترسی‌ها:

##### مجوزهای API Key مورد نیاز:

- `ADD_ON_CREATE`

##### OAuth اسکوپ موردنیاز:

- `POST_ADDON_CREATE.post_token` یا `USER_POSTS_ADDON_CREATE`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.AddonsApi(api_client)
    token = 'token_example' # str | 
    addons_create_post_addon_v2_body = kenar_api_client.AddonsCreatePostAddonV2Body() # AddonsCreatePostAddonV2Body | 

    try:
        # ایجاد افزونه آگهی
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

# **addons_create_user_addon_v2**
> AddonsCreateUserAddonResponseV2 addons_create_user_addon_v2(phone, addons_create_user_addon_v2_body)

ایجاد افزونه کاربر

این API امکان ایجاد افزونه کاربر را فراهم می‌کند که به صورت خودکار به تمام آگهی‌های کاربر متصل می‌شود. افزونه برای آگهی‌های آینده اعمال شده و همچنین تا 30 آگهی اخیر به عقب برمی‌گردد.

**نکات مهم**:
- می‌توان دسته‌بندی‌ها را برای فیلتر کردن آگهی‌هایی که افزونه دریافت می‌کنند مشخص کرد
- ویجت‌ها باید معتبر بوده و از مشخصات فرمت ویجت پیروی کنند

#### دسترسی‌ها:

##### مجوزهای API Key مورد نیاز:

- `USER_ADDON_CREATE`

##### OAuth اسکوپ موردنیاز:

- `USER_ADDON_CREATE`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.AddonsApi(api_client)
    phone = 'phone_example' # str | 
    addons_create_user_addon_v2_body = kenar_api_client.AddonsCreateUserAddonV2Body() # AddonsCreateUserAddonV2Body | 

    try:
        # ایجاد افزونه کاربر
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

# **addons_create_user_addon_v22**
> AddonsCreateUserAddonResponseV2 addons_create_user_addon_v22(divar_user_id, addons_create_user_addon_v2_body)

ایجاد افزونه کاربر

این API امکان ایجاد افزونه کاربر را فراهم می‌کند که به صورت خودکار به تمام آگهی‌های کاربر متصل می‌شود. افزونه برای آگهی‌های آینده اعمال شده و همچنین تا 30 آگهی اخیر به عقب برمی‌گردد.

**نکات مهم**:
- می‌توان دسته‌بندی‌ها را برای فیلتر کردن آگهی‌هایی که افزونه دریافت می‌کنند مشخص کرد
- ویجت‌ها باید معتبر بوده و از مشخصات فرمت ویجت پیروی کنند

#### دسترسی‌ها:

##### OAuth اسکوپ موردنیاز:

- `USER_ADDON_CREATE`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.AddonsApi(api_client)
    divar_user_id = 'divar_user_id_example' # str | 
    addons_create_user_addon_v2_body = kenar_api_client.AddonsCreateUserAddonV2Body() # AddonsCreateUserAddonV2Body | 

    try:
        # ایجاد افزونه کاربر
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

# **addons_delete_post_addon**
> object addons_delete_post_addon(token)

حذف افزونه آگهی

این API امکان حذف افزونه از یک آگهی را فراهم می‌کند. تمام افزونه‌های ایجاد شده توسط اپلیکیشن شما برای توکن آگهی مشخص شده حذف می‌شوند.

**نکات مهم**:
- فقط افزونه‌های ایجاد شده توسط اپلیکیشن شما قابل حذف هستند


#### دسترسی‌ها:

##### مجوزهای API Key مورد نیاز:

- `ADD_ON_DELETE`

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
        # حذف افزونه آگهی
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

حذف افزونه آگهی

این API امکان حذف افزونه از یک آگهی را فراهم می‌کند. تمام افزونه‌های ایجاد شده توسط اپلیکیشن شما برای توکن آگهی مشخص شده حذف می‌شوند.

**نکات مهم**:
- فقط افزونه‌های ایجاد شده توسط اپلیکیشن شما قابل حذف هستند


#### دسترسی‌ها:

##### مجوزهای API Key مورد نیاز:

- `ADD_ON_DELETE`

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
        # حذف افزونه آگهی
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

این API امکان حذف افزونه کاربر با شناسه را فراهم می‌کند. این کار افزونه کاربر و تمام افزونه‌های آگهی مرتبط را حذف می‌کند.

**نکات مهم**:
- فقط افزونه‌های کاربر ایجاد شده توسط اپلیکیشن شما قابل حذف هستند


#### دسترسی‌ها:

##### مجوزهای API Key مورد نیاز:

- `USER_ADDON_DELETE`

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

