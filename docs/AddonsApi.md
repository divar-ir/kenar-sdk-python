# kenar_api_client.AddonsApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addons_create_post_addon_v2**](AddonsApi.md#addons_create_post_addon_v2) | **POST** /v2/open-platform/addons/post/{token} | Attach a new Addon to a post
[**addons_create_user_addon_v2**](AddonsApi.md#addons_create_user_addon_v2) | **POST** /v2/open-platform/addons/user/{phone} | Attach a new Addon to a user
[**addons_create_user_addon_v22**](AddonsApi.md#addons_create_user_addon_v22) | **POST** /v2/open-platform/addons/users/{divar_user_id} | Attach a new Addon to a user
[**addons_delete_post_addon**](AddonsApi.md#addons_delete_post_addon) | **DELETE** /v1/open-platform/add-ons/post/{token} | Delete an Addon from a post
[**addons_delete_post_addon2**](AddonsApi.md#addons_delete_post_addon2) | **DELETE** /v1/open-platform/addons/post/{token} | Delete an Addon from a post
[**addons_delete_user_addon**](AddonsApi.md#addons_delete_user_addon) | **DELETE** /v1/open-platform/addons/user/{id} | Delete an UserAddon
[**addons_get_user_addons**](AddonsApi.md#addons_get_user_addons) | **GET** /v1/open-platform/addons/user/{phone} | Retrieve all UserAddons
[**addons_get_user_addons2**](AddonsApi.md#addons_get_user_addons2) | **GET** /v2/open-platform/addons/users/{divar_user_id} | Retrieve all UserAddons


# **addons_create_post_addon_v2**
> object addons_create_post_addon_v2(token, addons_create_post_addon_v2_body)

Attach a new Addon to a post

Using this API and with user permission, you can attach a new AD to a post.
You can use available widgets to design your Addon.
This API need access token having one of the following scopes:
- USER_POSTS_ADDON_CREATE
- POST_ADDON_CREATE.{post_token}

### Example


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


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.AddonsApi(api_client)
    token = 'token_example' # str | 
    addons_create_post_addon_v2_body = kenar_api_client.AddonsCreatePostAddonV2Body() # AddonsCreatePostAddonV2Body | 

    try:
        # Attach a new Addon to a post
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_create_user_addon_v2**
> AddonsCreateUserAddonResponseV2 addons_create_user_addon_v2(phone, addons_create_user_addon_v2_body)

Attach a new Addon to a user

Using this API and with user permission, you can create a UserAddon.
UserAddon will attach to all user posts in future and also back fills last 30 posts in the past.
You can use available widgets to design your UserAddon.
This API need access token having `USER_ADDON_CREATE` scope

### Example


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


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.AddonsApi(api_client)
    phone = 'phone_example' # str | 
    addons_create_user_addon_v2_body = kenar_api_client.AddonsCreateUserAddonV2Body() # AddonsCreateUserAddonV2Body | 

    try:
        # Attach a new Addon to a user
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_create_user_addon_v22**
> AddonsCreateUserAddonResponseV2 addons_create_user_addon_v22(divar_user_id, addons_create_user_addon_v2_body)

Attach a new Addon to a user

Using this API and with user permission, you can create a UserAddon.
UserAddon will attach to all user posts in future and also back fills last 30 posts in the past.
You can use available widgets to design your UserAddon.
This API need access token having `USER_ADDON_CREATE` scope

### Example


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


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.AddonsApi(api_client)
    divar_user_id = 'divar_user_id_example' # str | 
    addons_create_user_addon_v2_body = kenar_api_client.AddonsCreateUserAddonV2Body() # AddonsCreateUserAddonV2Body | 

    try:
        # Attach a new Addon to a user
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_delete_post_addon**
> object addons_delete_post_addon(token)

Delete an Addon from a post

You can only delete addons which are created by your app.

### Example


```python
import kenar_api_client
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.AddonsApi(api_client)
    token = 'token_example' # str | 

    try:
        # Delete an Addon from a post
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_delete_post_addon2**
> object addons_delete_post_addon2(token)

Delete an Addon from a post

You can only delete addons which are created by your app.

### Example


```python
import kenar_api_client
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.AddonsApi(api_client)
    token = 'token_example' # str | 

    try:
        # Delete an Addon from a post
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_delete_user_addon**
> object addons_delete_user_addon(id)

Delete an UserAddon

This will delete all correlated Addons to all user posts.
You can only delete Addons which are created by your app.

### Example


```python
import kenar_api_client
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://open-api.divar.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "https://open-api.divar.ir"
)


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.AddonsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete an UserAddon
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_get_user_addons**
> AddonsGetUserAddonsResponse addons_get_user_addons(phone, divar_user_id=divar_user_id)

Retrieve all UserAddons

Retrieve all UserAddons of a user.

### Example


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


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.AddonsApi(api_client)
    phone = 'phone_example' # str | 
    divar_user_id = 'divar_user_id_example' # str |  (optional)

    try:
        # Retrieve all UserAddons
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_get_user_addons2**
> AddonsGetUserAddonsResponse addons_get_user_addons2(divar_user_id, phone=phone)

Retrieve all UserAddons

Retrieve all UserAddons of a user.

### Example


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


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.AddonsApi(api_client)
    divar_user_id = 'divar_user_id_example' # str | 
    phone = 'phone_example' # str |  (optional)

    try:
        # Retrieve all UserAddons
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

