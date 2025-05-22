# kenar_api_client.AssetsApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_get_body_statuses**](AssetsApi.md#assets_get_body_statuses) | **GET** /v1/open-platform/assets/body-status | Get available body-status options in Divar vehicle categories
[**assets_get_brand_models**](AssetsApi.md#assets_get_brand_models) | **GET** /v1/open-platform/assets/brand-model/{category} | Get brand models in a Divar category
[**assets_get_categories**](AssetsApi.md#assets_get_categories) | **GET** /v1/open-platform/assets/category | Get Divar categories
[**assets_get_cities**](AssetsApi.md#assets_get_cities) | **GET** /v1/open-platform/assets/city | Get Divar cities
[**assets_get_colors**](AssetsApi.md#assets_get_colors) | **GET** /v1/open-platform/assets/color/{category} | Get colors in a Divar category
[**assets_get_districts**](AssetsApi.md#assets_get_districts) | **GET** /v1/open-platform/assets/district | Get Divar districts
[**assets_get_districts2**](AssetsApi.md#assets_get_districts2) | **GET** /v1/open-platform/assets/district/{city_slug} | Get Divar districts
[**assets_get_internal_storages**](AssetsApi.md#assets_get_internal_storages) | **GET** /v1/open-platform/assets/internal-storage | Get available internal-storage options in Divar mobile/tablet/laptop categories
[**assets_get_o_auth_scopes**](AssetsApi.md#assets_get_o_auth_scopes) | **GET** /v1/open-platform/assets/oauth-scope | Get KenarDivar OAuth scopes
[**assets_get_permissions**](AssetsApi.md#assets_get_permissions) | **GET** /v1/open-platform/assets/permission | Get KenarDivar permissions
[**assets_get_ram_memories**](AssetsApi.md#assets_get_ram_memories) | **GET** /v1/open-platform/assets/ram-memory | Get available ram-memory options in Divar mobile/tablet/laptop categories
[**assets_get_service_types**](AssetsApi.md#assets_get_service_types) | **GET** /v1/open-platform/assets/service-type | Get available service types in KenarDivar


# **assets_get_body_statuses**
> AssetsGetBodyStatusesResponse assets_get_body_statuses()

Get available body-status options in Divar vehicle categories

Get all available body-status options in Divar vehicle categories.This provides persian translations for each body-status options which used in posts.

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
        # Get available body-status options in Divar vehicle categories
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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_get_brand_models**
> AssetsGetBrandModelsResponse assets_get_brand_models(category)

Get brand models in a Divar category

Get all Divar brand models in specified category.This provides persian translations for each brand models which used in posts.

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
        # Get brand models in a Divar category
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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_get_categories**
> AssetsGetCategoriesResponse assets_get_categories()

Get Divar categories

Get all Divar categories. This provides persian translations for each category which used in posts.

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
        # Get Divar categories
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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_get_cities**
> AssetsGetCitiesResponse assets_get_cities()

Get Divar cities

Get all Divar cities. This provides persian translations for each city which used in posts.

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
        # Get Divar cities
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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_get_colors**
> AssetsGetColorsResponse assets_get_colors(category)

Get colors in a Divar category

Get all Divar colors in specified category.This provides persian translations for each color which used in posts.

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
        # Get colors in a Divar category
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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_get_districts**
> AssetsGetDistrictsResponse assets_get_districts(city_slug=city_slug)

Get Divar districts

Get all Divar districts. This provides persian translations for each district which used in posts.

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
        # Get Divar districts
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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_get_districts2**
> AssetsGetDistrictsResponse assets_get_districts2(city_slug)

Get Divar districts

Get all Divar districts. This provides persian translations for each district which used in posts.

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
        # Get Divar districts
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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_get_internal_storages**
> AssetsGetInternalStoragesResponse assets_get_internal_storages()

Get available internal-storage options in Divar mobile/tablet/laptop categories

Get all available internal-storage options in Divar mobile categories.This provides persian translations for each internal-storage options which used in posts.

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
        # Get available internal-storage options in Divar mobile/tablet/laptop categories
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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_get_o_auth_scopes**
> AssetsGetOAuthScopesResponse assets_get_o_auth_scopes()

Get KenarDivar OAuth scopes

These are available scopes for KenarDivar OAuth2.0.
Use scopes in OAuth flow to request access to user data or perform actions on their behalf.

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
        # Get KenarDivar OAuth scopes
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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_get_permissions**
> AssetsGetPermissionsResponse assets_get_permissions()

Get KenarDivar permissions

These permission are used to control access in KenarDivar Apps. Don't mistake them with OAuth scopes.
It's expected that apps be blind about these permissions.These are created for internal usages only, but feel free to request to be enabled for you app as needed.

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
        # Get KenarDivar permissions
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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_get_ram_memories**
> AssetsGetRamMemoriesResponse assets_get_ram_memories()

Get available ram-memory options in Divar mobile/tablet/laptop categories

Get all available ram-memory options in Divar mobile/tablet/laptop categories.This provides persian translations for each ram-memory options which used in posts.

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
        # Get available ram-memory options in Divar mobile/tablet/laptop categories
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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_get_service_types**
> AssetsGetServiceTypesResponse assets_get_service_types()

Get available service types in KenarDivar

These service types is used to group similar services in KenarDivar.
Any new idea with new service types are welcome. Feel free to request them as needed.

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
        # Get available service types in KenarDivar
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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

