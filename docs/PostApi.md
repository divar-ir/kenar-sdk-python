# kenar_api_client.PostApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_edit_post**](PostApi.md#post_edit_post) | **PUT** /v1/open-platform/post/{post_token} | Edit a post
[**post_get_image_upload_url**](PostApi.md#post_get_image_upload_url) | **GET** /v1/open-platform/post/image-upload-url | Get image upload URL


# **post_edit_post**
> object post_edit_post(post_token, post_edit_post_body)

Edit a post

This API allows you to edit a post. This needs `POST_EDIT.{post_token}` OAuth scope.
By now you can only edit title, description, and images of a post.

### Example


```python
import kenar_api_client
from kenar_api_client.models.post_edit_post_body import PostEditPostBody
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
    api_instance = kenar_api_client.PostApi(api_client)
    post_token = 'post_token_example' # str | 
    post_edit_post_body = kenar_api_client.PostEditPostBody() # PostEditPostBody | 

    try:
        # Edit a post
        api_response = api_instance.post_edit_post(post_token, post_edit_post_body)
        print("The response of PostApi->post_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_token** | **str**|  | 
 **post_edit_post_body** | [**PostEditPostBody**](PostEditPostBody.md)|  | 

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

# **post_get_image_upload_url**
> PostGetImageUploadURLResponse post_get_image_upload_url()

Get image upload URL

This API allows you to get an upload URL for uploading images of a post.
You can upload images to the returned URL using a POST request with binary encoding.

### Example


```python
import kenar_api_client
from kenar_api_client.models.post_get_image_upload_url_response import PostGetImageUploadURLResponse
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
    api_instance = kenar_api_client.PostApi(api_client)

    try:
        # Get image upload URL
        api_response = api_instance.post_get_image_upload_url()
        print("The response of PostApi->post_get_image_upload_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->post_get_image_upload_url: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PostGetImageUploadURLResponse**](PostGetImageUploadURLResponse.md)

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

