# kenar_api_client.EventsApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_register_event_subscription**](EventsApi.md#events_register_event_subscription) | **POST** /v1/open-platform/events/subscriptions | اشتراک در رویداد
[**events_send_event**](EventsApi.md#events_send_event) | **POST** /experimental/open-platform/events/send | ارسال رویداد به کاربر


# **events_register_event_subscription**
> object events_register_event_subscription(events_register_event_subscription_request)

اشتراک در رویداد

این API امکان اشتراک در رویدادها برای دریافت اعلان‌ها از طریق webhook هنگام وقوع رویدادها را فراهم می‌کند. پس از اشتراک، هنگام وقوع رویداد مربوطه در آدرس webhook شما مطلع خواهید شد.

**نکات مهم**:
- برای رویداد `NEW_MESSAGE_ON_POST`: نیاز به scope `CHAT_POST_CONVERSATIONS_READ.post_token` یا `CHAT_SUPPLIER_ALL_CONVERSATIONS_READ`
- برای رویداد `POST_UPDATE`: نیاز به scope `USER_POSTS_GET`
- آدرس webhook باید در پنل ارائه‌دهندگان برای اپلیکیشن شما تنظیم شده باشد
- برخی رویدادها به صورت پیش‌فرض فعال هستند و نیازی به اشتراک ندارند (مثل پیام‌های ربات چت)

مجوزهای مورد نیاز: `EVENTS_REGISTER_SUBSCRIPTION`. OAuth scope موردنیاز: `CHAT_POST_CONVERSATIONS_READ.post_token` یا `CHAT_SUPPLIER_ALL_CONVERSATIONS_READ` یا `USER_POSTS_GET`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

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

# **events_send_event**
> object events_send_event(message=message, target_type=target_type, target_resource_id=target_resource_id)

ارسال رویداد به کاربر

این API امکان ارسال اعلان رویداد به یک کاربر را فراهم می‌کند. رویداد می‌تواند به یک کاربر خاص یا یک آگهی هدف‌گیری شود. رویدادها می‌توانند شامل دکمه‌هایی با اقدامات سفارشی باشند که به کاربران امکان تعامل با اپلیکیشن شما را می‌دهند.

**نکات مهم**:
- عنوان دکمه‌ها باید بین 5 تا 50 کاراکتر باشد
- هنگام هدف‌گیری کاربر، target_resource_id باید با شناسه مبهم شده کاربر احراز هویت شده مطابقت داشته باشد
- هنگام هدف‌گیری آگهی، آگهی باید متعلق به کاربر احراز هویت شده باشد

مجوزهای مورد نیاز: `EVENTS_SEND`. OAuth scope موردنیاز: `SEND_EVENT`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.EventsApi(api_client)
    message = 'message_example' # str | پیام رویداد برای نمایش به کاربر (optional)
    target_type = 'target_type_example' # str | هدف رویداد؛ USER یا POST (optional)
    target_resource_id = 'target_resource_id_example' # str | شناسه هدف. اگر نوع هدف USER است، باید شناسه کاربر دیوار باشد و اگر POST است، باید توکن آگهی باشد. (optional)

    try:
        # ارسال رویداد به کاربر
        api_response = api_instance.events_send_event(message=message, target_type=target_type, target_resource_id=target_resource_id)
        print("The response of EventsApi->events_send_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_send_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| پیام رویداد برای نمایش به کاربر | [optional] 
 **target_type** | **str**| هدف رویداد؛ USER یا POST | [optional] 
 **target_resource_id** | **str**| شناسه هدف. اگر نوع هدف USER است، باید شناسه کاربر دیوار باشد و اگر POST است، باید توکن آگهی باشد. | [optional] 

### Return type

**object**

### Authorization

[APIKey](../README.md#APIKey), [OAuth](../README.md#OAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

