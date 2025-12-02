# kenar_api_client.AssetsApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_get_body_statuses**](AssetsApi.md#assets_get_body_statuses) | **GET** /v1/open-platform/assets/body-status | لیست گزینه‌های وضعیت بدنه
[**assets_get_brand_models**](AssetsApi.md#assets_get_brand_models) | **GET** /v1/open-platform/assets/brand-model/{category} | لیست مدل برندها بر اساس دسته‌بندی
[**assets_get_categories**](AssetsApi.md#assets_get_categories) | **GET** /v1/open-platform/assets/category | لیست همه دسته‌بندی‌ها
[**assets_get_cities**](AssetsApi.md#assets_get_cities) | **GET** /v1/open-platform/assets/city | لیست همه شهرها
[**assets_get_colors**](AssetsApi.md#assets_get_colors) | **GET** /v1/open-platform/assets/color/{category} | لیست رنگ‌ها بر اساس دسته‌بندی
[**assets_get_districts**](AssetsApi.md#assets_get_districts) | **GET** /v1/open-platform/assets/district | لیست محله‌ها
[**assets_get_districts2**](AssetsApi.md#assets_get_districts2) | **GET** /v1/open-platform/assets/district/{city_slug} | لیست محله‌ها
[**assets_get_internal_storages**](AssetsApi.md#assets_get_internal_storages) | **GET** /v1/open-platform/assets/internal-storage | لیست گزینه‌های حافظه داخلی
[**assets_get_o_auth_scopes**](AssetsApi.md#assets_get_o_auth_scopes) | **GET** /v1/open-platform/assets/oauth-scope | لیست دامنه‌های OAuth
[**assets_get_permissions**](AssetsApi.md#assets_get_permissions) | **GET** /v1/open-platform/assets/permission | لیست مجوزهای کنار دیوار
[**assets_get_ram_memories**](AssetsApi.md#assets_get_ram_memories) | **GET** /v1/open-platform/assets/ram-memory | لیست گزینه‌های حافظه RAM
[**assets_get_service_types**](AssetsApi.md#assets_get_service_types) | **GET** /v1/open-platform/assets/service-type | لیست انواع سرویس
[**assets_get_submit_schema**](AssetsApi.md#assets_get_submit_schema) | **GET** /v1/open-platform/assets/submit-schema/{category_slug} | دریافت schema ثبت آگهی برای دسته‌بندی


# **assets_get_body_statuses**
> AssetsGetBodyStatusesResponse assets_get_body_statuses()

لیست گزینه‌های وضعیت بدنه

این API امکان دریافت گزینه‌های وضعیت بدنه موجود برای دسته‌بندی‌های خودرو را فراهم می‌کند.

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
        # لیست گزینه‌های وضعیت بدنه
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

لیست مدل برندها بر اساس دسته‌بندی

این API امکان دریافت مدل برندها برای یک دسته‌بندی خاص را فراهم می‌کند. دسته‌بندی‌های پشتیبانی شده: `light` (خودرو) و `mobile-phones`.

**نکات مهم**:
- مدل برندها با نام‌های فارسی برگردانده می‌شوند
- دسته‌بندی باید یکی از دسته‌بندی‌های پشتیبانی شده باشد، در غیر این صورت خطا برمی‌گردد

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
        # لیست مدل برندها بر اساس دسته‌بندی
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

لیست همه دسته‌بندی‌ها

این API امکان دریافت همه دسته‌بندی‌های دیوار را فراهم می‌کند. شناسه دسته‌بندی‌ها و نام‌های فارسی آنها برای استفاده در ثبت و جستجوی آگهی برمی‌گردد.

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
        # لیست همه دسته‌بندی‌ها
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

لیست همه شهرها

این API امکان دریافت همه شهرهای دیوار را فراهم می‌کند. شناسه شهرها و نام‌های فارسی آنها برای استفاده در ثبت و جستجوی آگهی برمی‌گردد.

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
        # لیست همه شهرها
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

لیست رنگ‌ها بر اساس دسته‌بندی

این API امکان دریافت رنگ‌های موجود برای یک دسته‌بندی خاص را فراهم می‌کند. دسته‌بندی‌های پشتیبانی شده: `light` (خودرو) و `mobile-phones`.

**نکات مهم**:
- رنگ‌ها با نام‌های فارسی برگردانده می‌شوند
- دسته‌بندی باید یکی از دسته‌بندی‌های پشتیبانی شده باشد، در غیر این صورت خطا برمی‌گردد

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
        # لیست رنگ‌ها بر اساس دسته‌بندی
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

لیست محله‌ها

این API امکان دریافت محله‌های دیوار را فراهم می‌کند. می‌توان بدون پارامتر برای دریافت همه محله‌ها یا با city_slug برای دریافت محله‌های یک شهر خاص فراخوانی کرد.

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
        # لیست محله‌ها
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

لیست محله‌ها

این API امکان دریافت محله‌های دیوار را فراهم می‌کند. می‌توان بدون پارامتر برای دریافت همه محله‌ها یا با city_slug برای دریافت محله‌های یک شهر خاص فراخوانی کرد.

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
        # لیست محله‌ها
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

لیست گزینه‌های حافظه داخلی

این API امکان دریافت گزینه‌های حافظه داخلی موجود برای دسته‌بندی‌های موبایل، تبلت و لپ‌تاپ را فراهم می‌کند.

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
        # لیست گزینه‌های حافظه داخلی
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

لیست دامنه‌های OAuth

این API لیست OAuth scopeهای موجود برای کنار دیوار را برمی‌گرداند. از این scopeها در جریان OAuth برای درخواست دسترسی به داده‌های کاربر استفاده کنید.

**نکات مهم**:
- هر scope شامل وضعیت چرخه حیات است (آزمایشی، فعال، در حال منسوخ شدن، منسوخ شده)
- برخی scopeها نیاز به resource id دارند (مثلاً توکن آگهی، شناسه مکالمه)

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
        # لیست دامنه‌های OAuth
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

لیست مجوزهای کنار دیوار

این API امکان دریافت مجوزهای موجود کنار دیوار را فراهم می‌کند. این مجوزها برای کنترل دسترسی در اپلیکیشن‌های کنار دیوار استفاده می‌شوند و با دامنه‌های OAuth متفاوت هستند.

**نکات مهم**:
- مجوزها برای استفاده داخلی هستند و اپلیکیشن‌ها نباید مستقیماً به آنها وابسته باشند
- هر مجوز شامل وضعیت چرخه حیات آن است (آزمایشی، فعال، در حال منسوخ شدن، منسوخ شده)

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
        # لیست مجوزهای کنار دیوار
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

لیست گزینه‌های حافظه RAM

این API امکان دریافت گزینه‌های حافظه RAM موجود برای دسته‌بندی‌های موبایل، تبلت و لپ‌تاپ را فراهم می‌کند.

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
        # لیست گزینه‌های حافظه RAM
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

لیست انواع سرویس

این API امکان دریافت انواع سرویس موجود در کنار دیوار را فراهم می‌کند. انواع سرویس برای گروه‌بندی سرویس‌های مشابه استفاده می‌شوند.

**نکات مهم**:
- می‌توان انواع سرویس جدید را در صورت نیاز درخواست داد

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
        # لیست انواع سرویس
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

دریافت schema ثبت آگهی برای دسته‌بندی

این API به شما امکان دریافت قالب ثبت آگهی برای یک دسته‌بندی مشخص را می‌دهد. پاسخ در قالب JSON Schema است.

قالب تعریف کننده ساختار و قوانین برای فیلدهای فرم زمانی که آگهی در یک دسته‌بندی مشخص ثبت می‌شود. هر فیلد در قالب می‌تواند یکی از انواع زیر را داشته باشد:

**انواع اصلی:**
- `string`: فیلدهای ورودی متنی (مانند عنوان، توضیحات، مقادیر زمانی)
- `integer`: فیلدهای ورودی عددی برای اعداد صحیح (مانند قیمت، تعداد، اندازه)
- `float`: فیلدهای ورودی عددی برای اعداد اعشاری
- `boolean`: فیلدهای ورودی بولین (صحیح/غلط)
- `array`: فیلدهای ورودی چندگانه که امکان انتخاب چند مقدار را دارند

**فیلدهای Enum:**
فیلدها با گزینه‌های پیش‌تعریف شده از `enum` و `enumNames` استفاده می‌کنند:
- `enum`: آرایه از مقادیر داخلی استفاده شده برای ارتباط API
- `enumNames`: آرایه از برچسب‌های نمایشی نشان داده شده به کاربر (معمولاً به زبان فارسی)
- اینها برای فیلدهای ورودی چندگانه (مانند انتخاب طبقه، امکان استفاده از پارکینگ) استفاده می‌شوند

**فیلدهای آرایه با Enum:**
فیلدهای ورودی چندگانه ترکیب `type: "array"` با کلید Enum را دارند:
- `items.enum`: گزینه‌های موجود برای انتخاب
- `items.enumNames`: برچسب‌های نمایشی برای هر گزینه
- کاربران می‌توانند چند مقدار را انتخاب کنند (مانند امکانات رفاهی، سیستم‌های گرمایش)

**ویژگی‌های فیلد:**
- `title`: نام نمایشی فارسی برای فیلد
- `required`: آرایه از نام فیلدهای اجباری که باید ارائه شوند
- `type`: نوع داده فیلد

**مثال استفاده:**
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
        # دریافت schema ثبت آگهی برای دسته‌بندی
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

