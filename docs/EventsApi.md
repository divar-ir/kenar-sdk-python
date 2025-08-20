# kenar_api_client.EventsApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_register_event_subscription**](EventsApi.md#events_register_event_subscription) | **POST** /v1/open-platform/events/subscriptions | اشتراک در رویداد
[**events_send_event**](EventsApi.md#events_send_event) | **POST** /experimental/open-platform/events/send | Send an event to a user


# **events_register_event_subscription**
> object events_register_event_subscription(events_register_event_subscription_request)

اشتراک در رویداد

این درخواست به شما امکان اشتراک در رویداد را می‌دهد.
باید access-token را در این API ارسال کنید تا دسترسی شما بررسی شود.
برای اشتراک در `NEW_MESSAGE_ON_POST` به یکی از این دامنه‌ها نیاز دارید:
- CHAT_POST_CONVERSATIONS_READ.{post_token}
- CHAT_SUPPLIER_ALL_CONVERSATIONS_READ
برای اشتراک در `POST_UPDATE` به دامنه `USER_POSTS_GET` نیاز دارید.
پس از فراخوانی این API، هنگام وقوع رویداد مربوطه در webhook خود مطلع خواهید شد.
مطمئن شوید URL webhook در پنل ارائه‌دهندگان برای اپلیکیشن شما تنظیم شده است.
برخی رویدادها به طور پیش‌فرض فعال هستند و نیازی به اشتراک ندارند (مثل پیام‌های chatbot).

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.events_register_event_subscription_request import EventsRegisterEventSubscriptionRequest
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
    api_instance = kenar_api_client.EventsApi(api_client)
    events_register_event_subscription_request = kenar_api_client.EventsRegisterEventSubscriptionRequest() # EventsRegisterEventSubscriptionRequest | 

    try:
        # اشتراک در رویداد
        api_response = api_instance.events_register_event_subscription(events_register_event_subscription_request)
        print("The response of EventsApi->events_register_event_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_register_event_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **events_register_event_subscription_request** | [**EventsRegisterEventSubscriptionRequest**](EventsRegisterEventSubscriptionRequest.md)|  | 

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

# **events_send_event**
> object events_send_event(primary_button_action_open_post_page_post_token, primary_button_action_open_post_manage_page_post_token, message=message, primary_button_title=primary_button_title, primary_button_action_open_direct_link=primary_button_action_open_direct_link, primary_button_action_open_server_link_data=primary_button_action_open_server_link_data, primary_button_action_get_dynamic_action_data=primary_button_action_get_dynamic_action_data, target_type=target_type, target_resource_id=target_resource_id)

Send an event to a user

Using this API, you can send an event to a user. The event can be specific to a post or general. The event can include buttons with custom actions allowing users to interact with your app.

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
    api_instance = kenar_api_client.EventsApi(api_client)
    primary_button_action_open_post_page_post_token = 'primary_button_action_open_post_page_post_token_example' # str | Token of the post to open
    primary_button_action_open_post_manage_page_post_token = 'primary_button_action_open_post_manage_page_post_token_example' # str | Token of the post to redirect to its management page
    message = 'message_example' # str | The event message to display to the user (optional)
    primary_button_title = 'primary_button_title_example' # str | The text to display on the button (optional)
    primary_button_action_open_direct_link = 'primary_button_action_open_direct_link_example' # str | An action to send user to your URL directly with just a resource id (if applicable) (optional)
    primary_button_action_open_server_link_data = None # object | A data that you can set and will be returned to you upon user click to recognize the action (optional)
    primary_button_action_get_dynamic_action_data = None # object | A data that you can set and will be returned to you upon user click to recognize the action (optional)
    target_type = 'target_type_example' # str | Target of the event; USER or POST (optional)
    target_resource_id = 'target_resource_id_example' # str | id of the target. When target type is USER, it should be the Divar User ID of that user and when target type is POST, it should be the post token.  (optional)

    try:
        # Send an event to a user
        api_response = api_instance.events_send_event(primary_button_action_open_post_page_post_token, primary_button_action_open_post_manage_page_post_token, message=message, primary_button_title=primary_button_title, primary_button_action_open_direct_link=primary_button_action_open_direct_link, primary_button_action_open_server_link_data=primary_button_action_open_server_link_data, primary_button_action_get_dynamic_action_data=primary_button_action_get_dynamic_action_data, target_type=target_type, target_resource_id=target_resource_id)
        print("The response of EventsApi->events_send_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_send_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **primary_button_action_open_post_page_post_token** | **str**| Token of the post to open | 
 **primary_button_action_open_post_manage_page_post_token** | **str**| Token of the post to redirect to its management page | 
 **message** | **str**| The event message to display to the user | [optional] 
 **primary_button_title** | **str**| The text to display on the button | [optional] 
 **primary_button_action_open_direct_link** | **str**| An action to send user to your URL directly with just a resource id (if applicable) | [optional] 
 **primary_button_action_open_server_link_data** | [**object**](.md)| A data that you can set and will be returned to you upon user click to recognize the action | [optional] 
 **primary_button_action_get_dynamic_action_data** | [**object**](.md)| A data that you can set and will be returned to you upon user click to recognize the action | [optional] 
 **target_type** | **str**| Target of the event; USER or POST | [optional] 
 **target_resource_id** | **str**| id of the target. When target type is USER, it should be the Divar User ID of that user and when target type is POST, it should be the post token.  | [optional] 

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

