# kenar_api_client.AssetsApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_get_body_statuses**](AssetsApi.md#assets_get_body_statuses) | **GET** /v1/open-platform/assets/body-status | دریافت گزینه‌های وضعیت بدنه موجود در دسته‌بندی‌های خودرو دیوار
[**assets_get_brand_models**](AssetsApi.md#assets_get_brand_models) | **GET** /v1/open-platform/assets/brand-model/{category} | دریافت مدل‌های برند در دسته‌بندی دیوار
[**assets_get_categories**](AssetsApi.md#assets_get_categories) | **GET** /v1/open-platform/assets/category | دریافت دسته‌بندی‌های دیوار
[**assets_get_cities**](AssetsApi.md#assets_get_cities) | **GET** /v1/open-platform/assets/city | دریافت شهرهای دیوار
[**assets_get_colors**](AssetsApi.md#assets_get_colors) | **GET** /v1/open-platform/assets/color/{category} | دریافت رنگ‌ها در دسته‌بندی دیوار
[**assets_get_districts**](AssetsApi.md#assets_get_districts) | **GET** /v1/open-platform/assets/district | دریافت مناطق دیوار
[**assets_get_districts2**](AssetsApi.md#assets_get_districts2) | **GET** /v1/open-platform/assets/district/{city_slug} | دریافت مناطق دیوار
[**assets_get_internal_storages**](AssetsApi.md#assets_get_internal_storages) | **GET** /v1/open-platform/assets/internal-storage | دریافت گزینه‌های حافظه داخلی موجود در دسته‌بندی‌های موبایل/تبلت/لپ‌تاپ دیوار
[**assets_get_o_auth_scopes**](AssetsApi.md#assets_get_o_auth_scopes) | **GET** /v1/open-platform/assets/oauth-scope | دریافت دامنه‌های OAuth کنار دیوار
[**assets_get_permissions**](AssetsApi.md#assets_get_permissions) | **GET** /v1/open-platform/assets/permission | دریافت مجوزهای کنار دیوار
[**assets_get_ram_memories**](AssetsApi.md#assets_get_ram_memories) | **GET** /v1/open-platform/assets/ram-memory | دریافت گزینه‌های حافظه رم موجود در دسته‌بندی‌های موبایل/تبلت/لپ‌تاپ دیوار
[**assets_get_service_types**](AssetsApi.md#assets_get_service_types) | **GET** /v1/open-platform/assets/service-type | دریافت انواع سرویس موجود در کنار دیوار
[**assets_get_submit_schema**](AssetsApi.md#assets_get_submit_schema) | **GET** /v1/open-platform/assets/submit-schema/{category_slug} | Get submit schema


# **assets_get_body_statuses**
> AssetsGetBodyStatusesResponse assets_get_body_statuses()

دریافت گزینه‌های وضعیت بدنه موجود در دسته‌بندی‌های خودرو دیوار

دریافت تمام گزینه‌های وضعیت بدنه موجود در دسته‌بندی‌های خودرو دیوار. این ترجمه فارسی برای هر گزینه وضعیت بدنه که در آگهی‌ها استفاده می‌شود، ارائه می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_body_statuses_response import AssetsGetBodyStatusesResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)

    try:
        # دریافت گزینه‌های وضعیت بدنه موجود در دسته‌بندی‌های خودرو دیوار
        api_response = api_instance.assets_get_body_statuses()
        print("The response of AssetsApi->assets_get_body_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_body_statuses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AssetsGetBodyStatusesResponse**](AssetsGetBodyStatusesResponse.md)

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

# **assets_get_brand_models**
> AssetsGetBrandModelsResponse assets_get_brand_models(category)

دریافت مدل‌های برند در دسته‌بندی دیوار

دریافت تمام مدل‌های برند دیوار در دسته‌بندی مشخص شده. این ترجمه فارسی برای هر مدل برند که در آگهی‌ها استفاده می‌شود، ارائه می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_brand_models_response import AssetsGetBrandModelsResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)
    category = 'category_example' # str | 

    try:
        # دریافت مدل‌های برند در دسته‌بندی دیوار
        api_response = api_instance.assets_get_brand_models(category)
        print("The response of AssetsApi->assets_get_brand_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_brand_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 

### Return type

[**AssetsGetBrandModelsResponse**](AssetsGetBrandModelsResponse.md)

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

# **assets_get_categories**
> AssetsGetCategoriesResponse assets_get_categories()

دریافت دسته‌بندی‌های دیوار

دریافت تمام دسته‌بندی‌های دیوار. این ترجمه فارسی برای هر دسته‌بندی که در آگهی‌ها استفاده می‌شود، ارائه می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_categories_response import AssetsGetCategoriesResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)

    try:
        # دریافت دسته‌بندی‌های دیوار
        api_response = api_instance.assets_get_categories()
        print("The response of AssetsApi->assets_get_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AssetsGetCategoriesResponse**](AssetsGetCategoriesResponse.md)

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

# **assets_get_cities**
> AssetsGetCitiesResponse assets_get_cities()

دریافت شهرهای دیوار

دریافت تمام شهرهای دیوار. این ترجمه فارسی برای هر شهر که در آگهی‌ها استفاده می‌شود، ارائه می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_cities_response import AssetsGetCitiesResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)

    try:
        # دریافت شهرهای دیوار
        api_response = api_instance.assets_get_cities()
        print("The response of AssetsApi->assets_get_cities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_cities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AssetsGetCitiesResponse**](AssetsGetCitiesResponse.md)

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

# **assets_get_colors**
> AssetsGetColorsResponse assets_get_colors(category)

دریافت رنگ‌ها در دسته‌بندی دیوار

دریافت تمام رنگ‌های دیوار در دسته‌بندی مشخص شده. این ترجمه فارسی برای هر رنگ که در آگهی‌ها استفاده می‌شود، ارائه می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_colors_response import AssetsGetColorsResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)
    category = 'category_example' # str | 

    try:
        # دریافت رنگ‌ها در دسته‌بندی دیوار
        api_response = api_instance.assets_get_colors(category)
        print("The response of AssetsApi->assets_get_colors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_colors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 

### Return type

[**AssetsGetColorsResponse**](AssetsGetColorsResponse.md)

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

# **assets_get_districts**
> AssetsGetDistrictsResponse assets_get_districts(city_slug=city_slug)

دریافت مناطق دیوار

دریافت تمام مناطق دیوار. این ترجمه فارسی برای هر منطقه که در آگهی‌ها استفاده می‌شود، ارائه می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_districts_response import AssetsGetDistrictsResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)
    city_slug = 'city_slug_example' # str |  (optional)

    try:
        # دریافت مناطق دیوار
        api_response = api_instance.assets_get_districts(city_slug=city_slug)
        print("The response of AssetsApi->assets_get_districts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_districts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city_slug** | **str**|  | [optional] 

### Return type

[**AssetsGetDistrictsResponse**](AssetsGetDistrictsResponse.md)

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

# **assets_get_districts2**
> AssetsGetDistrictsResponse assets_get_districts2(city_slug)

دریافت مناطق دیوار

دریافت تمام مناطق دیوار. این ترجمه فارسی برای هر منطقه که در آگهی‌ها استفاده می‌شود، ارائه می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_districts_response import AssetsGetDistrictsResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)
    city_slug = 'city_slug_example' # str | 

    try:
        # دریافت مناطق دیوار
        api_response = api_instance.assets_get_districts2(city_slug)
        print("The response of AssetsApi->assets_get_districts2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_districts2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city_slug** | **str**|  | 

### Return type

[**AssetsGetDistrictsResponse**](AssetsGetDistrictsResponse.md)

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

# **assets_get_internal_storages**
> AssetsGetInternalStoragesResponse assets_get_internal_storages()

دریافت گزینه‌های حافظه داخلی موجود در دسته‌بندی‌های موبایل/تبلت/لپ‌تاپ دیوار

دریافت تمام گزینه‌های حافظه داخلی موجود در دسته‌بندی‌های موبایل دیوار. این ترجمه فارسی برای هر گزینه حافظه داخلی که در آگهی‌ها استفاده می‌شود، ارائه می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_internal_storages_response import AssetsGetInternalStoragesResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)

    try:
        # دریافت گزینه‌های حافظه داخلی موجود در دسته‌بندی‌های موبایل/تبلت/لپ‌تاپ دیوار
        api_response = api_instance.assets_get_internal_storages()
        print("The response of AssetsApi->assets_get_internal_storages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_internal_storages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AssetsGetInternalStoragesResponse**](AssetsGetInternalStoragesResponse.md)

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

# **assets_get_o_auth_scopes**
> AssetsGetOAuthScopesResponse assets_get_o_auth_scopes()

دریافت دامنه‌های OAuth کنار دیوار

اینها دامنه‌های موجود برای OAuth2.0 کنار دیوار هستند.
از دامنه‌ها در جریان OAuth برای درخواست دسترسی به داده‌های کاربر یا انجام اقدامات از طرف آنها استفاده کنید.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_o_auth_scopes_response import AssetsGetOAuthScopesResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)

    try:
        # دریافت دامنه‌های OAuth کنار دیوار
        api_response = api_instance.assets_get_o_auth_scopes()
        print("The response of AssetsApi->assets_get_o_auth_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_o_auth_scopes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AssetsGetOAuthScopesResponse**](AssetsGetOAuthScopesResponse.md)

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

# **assets_get_permissions**
> AssetsGetPermissionsResponse assets_get_permissions()

دریافت مجوزهای کنار دیوار

این مجوزها برای کنترل دسترسی در اپلیکیشن‌های کنار دیوار استفاده می‌شوند. آنها را با دامنه‌های OAuth اشتباه نگیرید.
انتظار می‌رود اپلیکیشن‌ها نسبت به این مجوزها کور باشند. اینها فقط برای استفاده‌های داخلی ایجاد شده‌اند، اما در صورت نیاز آزادانه درخواست فعال‌سازی برای اپلیکیشن خود را ارائه دهید.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_permissions_response import AssetsGetPermissionsResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)

    try:
        # دریافت مجوزهای کنار دیوار
        api_response = api_instance.assets_get_permissions()
        print("The response of AssetsApi->assets_get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_permissions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AssetsGetPermissionsResponse**](AssetsGetPermissionsResponse.md)

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

# **assets_get_ram_memories**
> AssetsGetRamMemoriesResponse assets_get_ram_memories()

دریافت گزینه‌های حافظه رم موجود در دسته‌بندی‌های موبایل/تبلت/لپ‌تاپ دیوار

دریافت تمام گزینه‌های حافظه رم موجود در دسته‌بندی‌های موبایل/تبلت/لپ‌تاپ دیوار. این ترجمه فارسی برای هر گزینه حافظه رم که در آگهی‌ها استفاده می‌شود، ارائه می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_ram_memories_response import AssetsGetRamMemoriesResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)

    try:
        # دریافت گزینه‌های حافظه رم موجود در دسته‌بندی‌های موبایل/تبلت/لپ‌تاپ دیوار
        api_response = api_instance.assets_get_ram_memories()
        print("The response of AssetsApi->assets_get_ram_memories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_ram_memories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AssetsGetRamMemoriesResponse**](AssetsGetRamMemoriesResponse.md)

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

# **assets_get_service_types**
> AssetsGetServiceTypesResponse assets_get_service_types()

دریافت انواع سرویس موجود در کنار دیوار

این انواع سرویس برای گروه‌بندی سرویس‌های مشابه در کنار دیوار استفاده می‌شود.
هر ایده جدید با انواع سرویس جدید خوشامد است. در صورت نیاز آزادانه درخواست دهید.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_service_types_response import AssetsGetServiceTypesResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)

    try:
        # دریافت انواع سرویس موجود در کنار دیوار
        api_response = api_instance.assets_get_service_types()
        print("The response of AssetsApi->assets_get_service_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_service_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AssetsGetServiceTypesResponse**](AssetsGetServiceTypesResponse.md)

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

# **assets_get_submit_schema**
> AssetsGetSubmitSchemaResponse assets_get_submit_schema(category_slug)

Get submit schema

This API allows you to get the submit schema for a given category slug. Response is in JSON Schema format.

The schema defines the structure and validation rules for form fields when submitting posts in a specific category. Each field in the schema can have one of the following types:

**Basic Types:**
- `string`: Text input fields (e.g., titles, descriptions, time values)
- `integer`: Numeric input fields for whole numbers (e.g., prices, counts, sizes)
- `float`: Numeric input fields for decimal numbers
- `boolean`: True/false checkbox fields
- `array`: Multi-select fields that allow multiple values

**Enum Fields:**
Fields with predefined options use `enum` and `enumNames` properties:
- `enum`: Array of internal values used for API communication
- `enumNames`: Array of display labels shown to users (usually in Persian)
- These are used for single-select dropdowns (e.g., floor selection, parking availability)

**Array Fields with Enums:**
Multi-select fields combine `type: "array"` with enum properties:
- `items.enum`: Available options for selection
- `items.enumNames`: Display labels for each option
- Users can select multiple values (e.g., comfort amenities, heating systems)

**Field Properties:**
- `title`: Persian display name for the field
- `required`: Array of field names that must be provided
- `type`: Data type of the field

**Example Usage:**
```json
{
  "properties": {
    "size": {
      "title": "متراژ (متر مربع)",
      "type": "integer"
    },
    "elevator": {
      "enum": ["دارد", "ندارد"],
      "enumNames": ["دارد", "ندارد"],
      "title": "آسانسور",
      "type": "string"
    },
    "comfort_amenities": {
      "items": {
        "enum": ["اینترنت_پرسرعت", "تلویزیون"],
        "enumNames": ["اینترنت پرسرعت", "تلویزیون"],
        "type": "string"
      },
      "title": "امکانات رفاهی",
      "type": "array"
    }
  }
}
```

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.assets_get_submit_schema_response import AssetsGetSubmitSchemaResponse
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
    api_instance = kenar_api_client.AssetsApi(api_client)
    category_slug = 'category_slug_example' # str | 

    try:
        # Get submit schema
        api_response = api_instance.assets_get_submit_schema(category_slug)
        print("The response of AssetsApi->assets_get_submit_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_get_submit_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_slug** | **str**|  | 

### Return type

[**AssetsGetSubmitSchemaResponse**](AssetsGetSubmitSchemaResponse.md)

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

