# kenar_api_client.FinderApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finder_get_post**](FinderApi.md#finder_get_post) | **GET** /v1/open-platform/finder/post/{token} | دریافت آگهی دیوار
[**finder_get_user**](FinderApi.md#finder_get_user) | **POST** /v1/open-platform/users | دریافت اطلاعات کاربر
[**finder_get_user2**](FinderApi.md#finder_get_user2) | **GET** /v1/open-platform/users | دریافت اطلاعات کاربر
[**finder_get_user_posts**](FinderApi.md#finder_get_user_posts) | **GET** /v1/open-platform/finder/user-posts | دریافت آگهی‌های کاربر
[**finder_search_post_v2**](FinderApi.md#finder_search_post_v2) | **POST** /v2/open-platform/finder/post | جستجو آگهی‌های دیوار با فیلترهایی


# **finder_get_post**
> FinderGetPostResponse finder_get_post(token)

دریافت آگهی دیوار

This API allows you to get details about Divar post by its token.
You can use the token to get the post data and its state 

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.finder_get_post_response import FinderGetPostResponse
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
    api_instance = kenar_api_client.FinderApi(api_client)
    token = 'token_example' # str | 

    try:
        # دریافت آگهی دیوار
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

# **finder_get_user**
> FinderUser finder_get_user(body)

دریافت اطلاعات کاربر

پس از دریافت توکن دسترسی، می‌توانید از این API برای دریافت اطلاعات کاربر استفاده کنید.
با scope `USER_PHONE` می‌توانید شماره تلفن کاربر را دریافت کنید.
با scope `USER_ID` می‌توانید شناسه کاربر را دریافت کرده و می‌توانید روی منحصر به فرد بودن این شناسه تکیه کنید.


### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.finder_user import FinderUser
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
    api_instance = kenar_api_client.FinderApi(api_client)
    body = None # object | 

    try:
        # دریافت اطلاعات کاربر
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

# **finder_get_user2**
> FinderUser finder_get_user2()

دریافت اطلاعات کاربر

پس از دریافت توکن دسترسی، می‌توانید از این API برای دریافت اطلاعات کاربر استفاده کنید.
با scope `USER_PHONE` می‌توانید شماره تلفن کاربر را دریافت کنید.
با scope `USER_ID` می‌توانید شناسه کاربر را دریافت کرده و می‌توانید روی منحصر به فرد بودن این شناسه تکیه کنید.


### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.finder_user import FinderUser
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
    api_instance = kenar_api_client.FinderApi(api_client)

    try:
        # دریافت اطلاعات کاربر
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

# **finder_get_user_posts**
> FinderGetUserPostsResponse finder_get_user_posts()

دریافت آگهی‌های کاربر

این API به شما امکان دریافت تمام آگهی‌های یک کاربر را می‌دهد.
می‌توانید از این API برای نمایش آگهی‌های کاربر در سرویس خود استفاده کنید.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.finder_get_user_posts_response import FinderGetUserPostsResponse
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
    api_instance = kenar_api_client.FinderApi(api_client)

    try:
        # دریافت آگهی‌های کاربر
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

# **finder_search_post_v2**
> FinderSearchPostV2Response finder_search_post_v2(finder_search_posts_v2_request)

جستجو آگهی‌های دیوار با فیلترهایی

این API به شما امکان جستجو آگهی‌های دیوار با برخی فیلترها را می‌دهد.
می‌توانید آگهی‌ها را بر اساس دسته‌بندی، شهر، منطقه و برخی فیلترهای دیگر جستجو کنید.
آگهی‌ها بر اساس زمان آنها مرتب می‌شوند.


### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.finder_search_post_v2_response import FinderSearchPostV2Response
from kenar_api_client.models.finder_search_posts_v2_request import FinderSearchPostsV2Request
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
    api_instance = kenar_api_client.FinderApi(api_client)
    finder_search_posts_v2_request = kenar_api_client.FinderSearchPostsV2Request() # FinderSearchPostsV2Request | 

    try:
        # جستجو آگهی‌های دیوار با فیلترهایی
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

