# kenar_api_client.FinderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finder_get_post**](FinderApi.md#finder_get_post) | **GET** /v1/open-platform/finder/post/{token} | Get a Divar post
[**finder_get_user**](FinderApi.md#finder_get_user) | **POST** /v1/open-platform/users | Get user information
[**finder_get_user2**](FinderApi.md#finder_get_user2) | **GET** /v1/open-platform/users | Get user information
[**finder_get_user_posts**](FinderApi.md#finder_get_user_posts) | **GET** /v1/open-platform/finder/user-posts | Get user posts
[**finder_search_post_v2**](FinderApi.md#finder_search_post_v2) | **POST** /v2/open-platform/finder/post | Search Divar posts with some filters


# **finder_get_post**
> FinderGetPostResponse finder_get_post(token)

Get a Divar post

This API allows you to get details about Divar post by its token.
You can use the token to get the post data and its state in order to implement your service.


### Example


```python
import kenar_api_client
from kenar_api_client.models.finder_get_post_response import FinderGetPostResponse
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.FinderApi(api_client)
    token = 'token_example' # str | 

    try:
        # Get a Divar post
        api_response = api_instance.finder_get_post(token)
        print("The response of FinderApi->finder_get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinderApi->finder_get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**FinderGetPostResponse**](FinderGetPostResponse.md)

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

# **finder_get_user**
> FinderUser finder_get_user(body)

Get user information

After gaining an access token, you can use this API to get user information.
With scope `USER_PHONE` you can get user phone number.
With scope `USER_ID` you can get user id and you can rely on uniqueness of this id.


### Example


```python
import kenar_api_client
from kenar_api_client.models.finder_user import FinderUser
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.FinderApi(api_client)
    body = None # object | 

    try:
        # Get user information
        api_response = api_instance.finder_get_user(body)
        print("The response of FinderApi->finder_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinderApi->finder_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**FinderUser**](FinderUser.md)

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

# **finder_get_user2**
> FinderUser finder_get_user2()

Get user information

After gaining an access token, you can use this API to get user information.
With scope `USER_PHONE` you can get user phone number.
With scope `USER_ID` you can get user id and you can rely on uniqueness of this id.


### Example


```python
import kenar_api_client
from kenar_api_client.models.finder_user import FinderUser
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.FinderApi(api_client)

    try:
        # Get user information
        api_response = api_instance.finder_get_user2()
        print("The response of FinderApi->finder_get_user2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinderApi->finder_get_user2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FinderUser**](FinderUser.md)

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

# **finder_get_user_posts**
> FinderGetUserPostsResponse finder_get_user_posts()

Get user posts

This API allows you to get all posts of a user.
You can use this API to show user posts in your service.

### Example


```python
import kenar_api_client
from kenar_api_client.models.finder_get_user_posts_response import FinderGetUserPostsResponse
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.FinderApi(api_client)

    try:
        # Get user posts
        api_response = api_instance.finder_get_user_posts()
        print("The response of FinderApi->finder_get_user_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinderApi->finder_get_user_posts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FinderGetUserPostsResponse**](FinderGetUserPostsResponse.md)

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

# **finder_search_post_v2**
> FinderSearchPostV2Response finder_search_post_v2(finder_search_posts_v2_request)

Search Divar posts with some filters

This API allows you to search Divar posts with some filters.
You can search posts by category, city, district, and some other filters.
Posts will be sorted by their timestamp.


### Example


```python
import kenar_api_client
from kenar_api_client.models.finder_search_post_v2_response import FinderSearchPostV2Response
from kenar_api_client.models.finder_search_posts_v2_request import FinderSearchPostsV2Request
from kenar_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kenar_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.FinderApi(api_client)
    finder_search_posts_v2_request = kenar_api_client.FinderSearchPostsV2Request() # FinderSearchPostsV2Request | 

    try:
        # Search Divar posts with some filters
        api_response = api_instance.finder_search_post_v2(finder_search_posts_v2_request)
        print("The response of FinderApi->finder_search_post_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinderApi->finder_search_post_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finder_search_posts_v2_request** | [**FinderSearchPostsV2Request**](FinderSearchPostsV2Request.md)|  | 

### Return type

[**FinderSearchPostV2Response**](FinderSearchPostV2Response.md)

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

