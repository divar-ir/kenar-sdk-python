# kenar_api_client.SemanticApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**semantic_create_post_semantic**](SemanticApi.md#semantic_create_post_semantic) | **POST** /experimental/open-platform/semantic/post/{token} | Create Post Semantic
[**semantic_create_user_semantic**](SemanticApi.md#semantic_create_user_semantic) | **POST** /v1/open-platform/semantic/user/{phone} | Create User Semantic
[**semantic_create_user_semantic2**](SemanticApi.md#semantic_create_user_semantic2) | **POST** /v1/open-platform/semantic/users/{divar_user_id} | Create User Semantic
[**semantic_delete_user_semantic**](SemanticApi.md#semantic_delete_user_semantic) | **DELETE** /v1/open-platform/semantic/user/{phone} | Delete User Semantic
[**semantic_delete_user_semantic2**](SemanticApi.md#semantic_delete_user_semantic2) | **DELETE** /v1/open-platform/semantic/users/{divar_user_id} | Delete User Semantic


# **semantic_create_post_semantic**
> object semantic_create_post_semantic(token, semantic_create_post_semantic_body)

Create Post Semantic

In some cases, it is necessary to store information about the post in Divar without adding an addon.
This API expects access token having `POST_SEMANTIC_CREATE` scope.


### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.SemanticApi(api_client)
    token = 'token_example' # str | 
    semantic_create_post_semantic_body = kenar_api_client.SemanticCreatePostSemanticBody() # SemanticCreatePostSemanticBody | 

    try:
        # Create Post Semantic
        api_response = api_instance.semantic_create_post_semantic(token, semantic_create_post_semantic_body)
        print("The response of SemanticApi->semantic_create_post_semantic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticApi->semantic_create_post_semantic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **semantic_create_post_semantic_body** | [**SemanticCreatePostSemanticBody**](SemanticCreatePostSemanticBody.md)|  | 

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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **semantic_create_user_semantic**
> SemanticCreateUserSemanticResponse semantic_create_user_semantic(phone, semantic_create_user_semantic_body)

Create User Semantic

In some cases, it is necessary to store information about the user in Divar without adding an addon.
The username in Divar is the same as the mobile number.
This API expects access token having `USER_VERIFICATION_CREATE` scope.
Use the User Semantic APIs for this purpose.This service allows sending semantic information and an optional payment ticket.

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.SemanticApi(api_client)
    phone = 'phone_example' # str | 
    semantic_create_user_semantic_body = kenar_api_client.SemanticCreateUserSemanticBody() # SemanticCreateUserSemanticBody | 

    try:
        # Create User Semantic
        api_response = api_instance.semantic_create_user_semantic(phone, semantic_create_user_semantic_body)
        print("The response of SemanticApi->semantic_create_user_semantic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticApi->semantic_create_user_semantic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 
 **semantic_create_user_semantic_body** | [**SemanticCreateUserSemanticBody**](SemanticCreateUserSemanticBody.md)|  | 

### Return type

[**SemanticCreateUserSemanticResponse**](SemanticCreateUserSemanticResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **semantic_create_user_semantic2**
> SemanticCreateUserSemanticResponse semantic_create_user_semantic2(divar_user_id, semantic_create_user_semantic_body)

Create User Semantic

In some cases, it is necessary to store information about the user in Divar without adding an addon.
The username in Divar is the same as the mobile number.
This API expects access token having `USER_VERIFICATION_CREATE` scope.
Use the User Semantic APIs for this purpose.This service allows sending semantic information and an optional payment ticket.

### Example

* Api Key Authentication (APIKey):

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

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.SemanticApi(api_client)
    divar_user_id = 'divar_user_id_example' # str | 
    semantic_create_user_semantic_body = kenar_api_client.SemanticCreateUserSemanticBody() # SemanticCreateUserSemanticBody | 

    try:
        # Create User Semantic
        api_response = api_instance.semantic_create_user_semantic2(divar_user_id, semantic_create_user_semantic_body)
        print("The response of SemanticApi->semantic_create_user_semantic2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticApi->semantic_create_user_semantic2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **divar_user_id** | **str**|  | 
 **semantic_create_user_semantic_body** | [**SemanticCreateUserSemanticBody**](SemanticCreateUserSemanticBody.md)|  | 

### Return type

[**SemanticCreateUserSemanticResponse**](SemanticCreateUserSemanticResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **semantic_delete_user_semantic**
> object semantic_delete_user_semantic(phone, divar_user_id=divar_user_id)

Delete User Semantic

You can delete the semantic information of a user by calling this API.

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
    phone = 'phone_example' # str | 
    divar_user_id = 'divar_user_id_example' # str |  (optional)

    try:
        # Delete User Semantic
        api_response = api_instance.semantic_delete_user_semantic(phone, divar_user_id=divar_user_id)
        print("The response of SemanticApi->semantic_delete_user_semantic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticApi->semantic_delete_user_semantic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 
 **divar_user_id** | **str**|  | [optional] 

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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **semantic_delete_user_semantic2**
> object semantic_delete_user_semantic2(divar_user_id, phone=phone)

Delete User Semantic

You can delete the semantic information of a user by calling this API.

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
    divar_user_id = 'divar_user_id_example' # str | 
    phone = 'phone_example' # str |  (optional)

    try:
        # Delete User Semantic
        api_response = api_instance.semantic_delete_user_semantic2(divar_user_id, phone=phone)
        print("The response of SemanticApi->semantic_delete_user_semantic2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SemanticApi->semantic_delete_user_semantic2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **divar_user_id** | **str**|  | 
 **phone** | **str**|  | [optional] 

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
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

