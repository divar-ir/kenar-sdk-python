# kenar_api_client.ChatAPIApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_api_chat_bot_send_message**](ChatAPIApi.md#chat_api_chat_bot_send_message) | **POST** /v1/open-platform/chat/bot/conversations/{conversation_id}/messages | ارسال پیام به مکالمه ChatBot
[**chat_api_chat_bot_send_message2**](ChatAPIApi.md#chat_api_chat_bot_send_message2) | **POST** /v1/open-platform/chat/bot/users/{user_id}/messages | ارسال پیام به مکالمه ChatBot
[**chat_api_chat_bot_send_message3**](ChatAPIApi.md#chat_api_chat_bot_send_message3) | **POST** /experimental/open-platform/chatbot-conversations/{conversation_id}/messages | ارسال پیام به مکالمه ChatBot
[**chat_api_chat_bot_send_message4**](ChatAPIApi.md#chat_api_chat_bot_send_message4) | **POST** /experimental/open-platform/chat/bot/users/{user_id}/messages | ارسال پیام به مکالمه ChatBot
[**chat_api_chat_bot_send_message5**](ChatAPIApi.md#chat_api_chat_bot_send_message5) | **POST** /experimental/open-platform/chat/bot/conversations/{conversation_id}/messages | ارسال پیام به مکالمه ChatBot
[**chat_api_conversation_send_message**](ChatAPIApi.md#chat_api_conversation_send_message) | **POST** /v2/open-platform/conversations/{conversation_id}/messages | ارسال پیام به مکالمه
[**chat_api_generate_upload_token**](ChatAPIApi.md#chat_api_generate_upload_token) | **POST** /experimental/open-platform/chat/upload | تولید توکن آپلود
[**chat_api_get_conversation**](ChatAPIApi.md#chat_api_get_conversation) | **GET** /v1/open-platform/chat/conversations/{conversation_id} | دریافت مکالمه با شناسه آن


# **chat_api_chat_bot_send_message**
> ChatapiChatBotSendMessageResponse chat_api_chat_bot_send_message(conversation_id, chat_api_chat_bot_send_message_body)

ارسال پیام به مکالمه ChatBot

می‌توانید این API را با conversation_id یا user_id فراخوانی کنید.
فراخوانی با user_id نیاز به access_token با دامنه CHAT_BOT_USER_MESSAGE_SEND دارد. این به شما امکان شروع مکالمه با کاربر از ChatBot را می‌دهد.

مجوزهای مورد نیاز: CHAT_BOT_SEND_MESSAGE.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.chat_api_chat_bot_send_message_body import ChatAPIChatBotSendMessageBody
from kenar_api_client.models.chatapi_chat_bot_send_message_response import ChatapiChatBotSendMessageResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    conversation_id = 'conversation_id_example' # str | شناسه منحصر به فرد برای مکالمه
    chat_api_chat_bot_send_message_body = kenar_api_client.ChatAPIChatBotSendMessageBody() # ChatAPIChatBotSendMessageBody | 

    try:
        # ارسال پیام به مکالمه ChatBot
        api_response = api_instance.chat_api_chat_bot_send_message(conversation_id, chat_api_chat_bot_send_message_body)
        print("The response of ChatAPIApi->chat_api_chat_bot_send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_chat_bot_send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| شناسه منحصر به فرد برای مکالمه | 
 **chat_api_chat_bot_send_message_body** | [**ChatAPIChatBotSendMessageBody**](ChatAPIChatBotSendMessageBody.md)|  | 

### Return type

[**ChatapiChatBotSendMessageResponse**](ChatapiChatBotSendMessageResponse.md)

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

# **chat_api_chat_bot_send_message2**
> ChatapiChatBotSendMessageResponse chat_api_chat_bot_send_message2(user_id, chat_api_chat_bot_send_message_body)

ارسال پیام به مکالمه ChatBot

می‌توانید این API را با conversation_id یا user_id فراخوانی کنید.
فراخوانی با user_id نیاز به access_token با دامنه CHAT_BOT_USER_MESSAGE_SEND دارد. این به شما امکان شروع مکالمه با کاربر از ChatBot را می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.chat_api_chat_bot_send_message_body import ChatAPIChatBotSendMessageBody
from kenar_api_client.models.chatapi_chat_bot_send_message_response import ChatapiChatBotSendMessageResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    user_id = 'user_id_example' # str | شناسه منحصر به فرد کاربر برای شروع یا ادامه مکالمه
    chat_api_chat_bot_send_message_body = kenar_api_client.ChatAPIChatBotSendMessageBody() # ChatAPIChatBotSendMessageBody | 

    try:
        # ارسال پیام به مکالمه ChatBot
        api_response = api_instance.chat_api_chat_bot_send_message2(user_id, chat_api_chat_bot_send_message_body)
        print("The response of ChatAPIApi->chat_api_chat_bot_send_message2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_chat_bot_send_message2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| شناسه منحصر به فرد کاربر برای شروع یا ادامه مکالمه | 
 **chat_api_chat_bot_send_message_body** | [**ChatAPIChatBotSendMessageBody**](ChatAPIChatBotSendMessageBody.md)|  | 

### Return type

[**ChatapiChatBotSendMessageResponse**](ChatapiChatBotSendMessageResponse.md)

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

# **chat_api_chat_bot_send_message3**
> ChatapiChatBotSendMessageResponse chat_api_chat_bot_send_message3(conversation_id, chat_api_chat_bot_send_message_body)

ارسال پیام به مکالمه ChatBot

می‌توانید این API را با conversation_id یا user_id فراخوانی کنید.
فراخوانی با user_id نیاز به access_token با دامنه CHAT_BOT_USER_MESSAGE_SEND دارد. این به شما امکان شروع مکالمه با کاربر از ChatBot را می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.chat_api_chat_bot_send_message_body import ChatAPIChatBotSendMessageBody
from kenar_api_client.models.chatapi_chat_bot_send_message_response import ChatapiChatBotSendMessageResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    conversation_id = 'conversation_id_example' # str | شناسه منحصر به فرد برای مکالمه
    chat_api_chat_bot_send_message_body = kenar_api_client.ChatAPIChatBotSendMessageBody() # ChatAPIChatBotSendMessageBody | 

    try:
        # ارسال پیام به مکالمه ChatBot
        api_response = api_instance.chat_api_chat_bot_send_message3(conversation_id, chat_api_chat_bot_send_message_body)
        print("The response of ChatAPIApi->chat_api_chat_bot_send_message3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_chat_bot_send_message3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| شناسه منحصر به فرد برای مکالمه | 
 **chat_api_chat_bot_send_message_body** | [**ChatAPIChatBotSendMessageBody**](ChatAPIChatBotSendMessageBody.md)|  | 

### Return type

[**ChatapiChatBotSendMessageResponse**](ChatapiChatBotSendMessageResponse.md)

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

# **chat_api_chat_bot_send_message4**
> ChatapiChatBotSendMessageResponse chat_api_chat_bot_send_message4(user_id, chat_api_chat_bot_send_message_body)

ارسال پیام به مکالمه ChatBot

می‌توانید این API را با conversation_id یا user_id فراخوانی کنید.
فراخوانی با user_id نیاز به access_token با دامنه CHAT_BOT_USER_MESSAGE_SEND دارد. این به شما امکان شروع مکالمه با کاربر از ChatBot را می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.chat_api_chat_bot_send_message_body import ChatAPIChatBotSendMessageBody
from kenar_api_client.models.chatapi_chat_bot_send_message_response import ChatapiChatBotSendMessageResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    user_id = 'user_id_example' # str | شناسه منحصر به فرد کاربر برای شروع یا ادامه مکالمه
    chat_api_chat_bot_send_message_body = kenar_api_client.ChatAPIChatBotSendMessageBody() # ChatAPIChatBotSendMessageBody | 

    try:
        # ارسال پیام به مکالمه ChatBot
        api_response = api_instance.chat_api_chat_bot_send_message4(user_id, chat_api_chat_bot_send_message_body)
        print("The response of ChatAPIApi->chat_api_chat_bot_send_message4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_chat_bot_send_message4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| شناسه منحصر به فرد کاربر برای شروع یا ادامه مکالمه | 
 **chat_api_chat_bot_send_message_body** | [**ChatAPIChatBotSendMessageBody**](ChatAPIChatBotSendMessageBody.md)|  | 

### Return type

[**ChatapiChatBotSendMessageResponse**](ChatapiChatBotSendMessageResponse.md)

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

# **chat_api_chat_bot_send_message5**
> ChatapiChatBotSendMessageResponse chat_api_chat_bot_send_message5(conversation_id, chat_api_chat_bot_send_message_body)

ارسال پیام به مکالمه ChatBot

می‌توانید این API را با conversation_id یا user_id فراخوانی کنید.
فراخوانی با user_id نیاز به access_token با دامنه CHAT_BOT_USER_MESSAGE_SEND دارد. این به شما امکان شروع مکالمه با کاربر از ChatBot را می‌دهد.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.chat_api_chat_bot_send_message_body import ChatAPIChatBotSendMessageBody
from kenar_api_client.models.chatapi_chat_bot_send_message_response import ChatapiChatBotSendMessageResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    conversation_id = 'conversation_id_example' # str | شناسه منحصر به فرد برای مکالمه
    chat_api_chat_bot_send_message_body = kenar_api_client.ChatAPIChatBotSendMessageBody() # ChatAPIChatBotSendMessageBody | 

    try:
        # ارسال پیام به مکالمه ChatBot
        api_response = api_instance.chat_api_chat_bot_send_message5(conversation_id, chat_api_chat_bot_send_message_body)
        print("The response of ChatAPIApi->chat_api_chat_bot_send_message5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_chat_bot_send_message5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| شناسه منحصر به فرد برای مکالمه | 
 **chat_api_chat_bot_send_message_body** | [**ChatAPIChatBotSendMessageBody**](ChatAPIChatBotSendMessageBody.md)|  | 

### Return type

[**ChatapiChatBotSendMessageResponse**](ChatapiChatBotSendMessageResponse.md)

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

# **chat_api_conversation_send_message**
> ChatapiConversationSendMessageResponse chat_api_conversation_send_message(conversation_id, chat_api_conversation_send_message_body)

ارسال پیام به مکالمه

این API برای ارسال پیام به مکالمه استفاده می‌شود.
برای فراخوانی این API به یکی از دامنه‌های زیر نیاز دارید:
- CONVERSATION_SEND_MESSAGE.{conversation_id}
- CHAT_SUPPLIER_ALL_CONVERSATIONS_MESSAGE_SEND
- CHAT_POST_CONVERSATIONS_MESSAGE_SEND.{post_token}


مجوزهای مورد نیاز: CHAT_SEND_MESSAGE_OAUTH.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.chat_api_conversation_send_message_body import ChatAPIConversationSendMessageBody
from kenar_api_client.models.chatapi_conversation_send_message_response import ChatapiConversationSendMessageResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    conversation_id = 'conversation_id_example' # str | شناسه منحصر به فرد برای مکالمه
    chat_api_conversation_send_message_body = kenar_api_client.ChatAPIConversationSendMessageBody() # ChatAPIConversationSendMessageBody | 

    try:
        # ارسال پیام به مکالمه
        api_response = api_instance.chat_api_conversation_send_message(conversation_id, chat_api_conversation_send_message_body)
        print("The response of ChatAPIApi->chat_api_conversation_send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_conversation_send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| شناسه منحصر به فرد برای مکالمه | 
 **chat_api_conversation_send_message_body** | [**ChatAPIConversationSendMessageBody**](ChatAPIConversationSendMessageBody.md)|  | 

### Return type

[**ChatapiConversationSendMessageResponse**](ChatapiConversationSendMessageResponse.md)

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

# **chat_api_generate_upload_token**
> ChatapiGenerateUploadTokenResponse chat_api_generate_upload_token(body)

تولید توکن آپلود

این API برای تولید توکن آپلود برای آپلود فایل‌های رسانه‌ای استفاده می‌شود.

مجوزهای مورد نیاز: CHAT_UPLOAD_MEDIA.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.chatapi_generate_upload_token_response import ChatapiGenerateUploadTokenResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    body = None # object | 

    try:
        # تولید توکن آپلود
        api_response = api_instance.chat_api_generate_upload_token(body)
        print("The response of ChatAPIApi->chat_api_generate_upload_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_generate_upload_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**ChatapiGenerateUploadTokenResponse**](ChatapiGenerateUploadTokenResponse.md)

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

# **chat_api_get_conversation**
> ChatapiGetConversationResponse chat_api_get_conversation(conversation_id)

دریافت مکالمه با شناسه آن

این API برای دریافت مکالمه و پیام‌های یک مکالمه با شناسه آن استفاده می‌شود. این API توکن دسترسی با دامنه `CHAT_CONVERSATION_READ` را انتظار دارد.

مجوزهای مورد نیاز: CHAT_READ_CONVERSATION.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.chatapi_get_conversation_response import ChatapiGetConversationResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    conversation_id = 'conversation_id_example' # str | شناسه منحصر به فرد برای مکالمه

    try:
        # دریافت مکالمه با شناسه آن
        api_response = api_instance.chat_api_get_conversation(conversation_id)
        print("The response of ChatAPIApi->chat_api_get_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_get_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| شناسه منحصر به فرد برای مکالمه | 

### Return type

[**ChatapiGetConversationResponse**](ChatapiGetConversationResponse.md)

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

