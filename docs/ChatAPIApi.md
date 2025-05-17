# kenar_api_client.ChatAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_api_chat_bot_send_message**](ChatAPIApi.md#chat_api_chat_bot_send_message) | **POST** /experimental/open-platform/chatbot-conversations/{conversation_id}/messages | Send a message to a ChatBot conversation
[**chat_api_chat_bot_send_message2**](ChatAPIApi.md#chat_api_chat_bot_send_message2) | **POST** /experimental/open-platform/chat/bot/users/{user_id}/messages | Send a message to a ChatBot conversation
[**chat_api_chat_bot_send_message3**](ChatAPIApi.md#chat_api_chat_bot_send_message3) | **POST** /experimental/open-platform/chat/bot/conversations/{conversation_id}/messages | Send a message to a ChatBot conversation
[**chat_api_conversation_send_message**](ChatAPIApi.md#chat_api_conversation_send_message) | **POST** /v2/open-platform/conversations/{conversation_id}/messages | Send a message to a conversation
[**chat_api_generate_upload_token**](ChatAPIApi.md#chat_api_generate_upload_token) | **POST** /experimental/open-platform/chat/upload | Generate an upload token
[**chat_api_get_conversation**](ChatAPIApi.md#chat_api_get_conversation) | **GET** /v1/open-platform/chat/conversations/{conversation_id} | Get Conversation by it&#39;s ID


# **chat_api_chat_bot_send_message**
> ChatapiChatBotSendMessageResponse chat_api_chat_bot_send_message(conversation_id, chat_api_chat_bot_send_message_body)

Send a message to a ChatBot conversation

You can call this API with either conversation_id or user_id.
Calling with user_id needs a access_token having CHAT_BOT_USER_MESSAGE_SEND scope.This enables you to start conversation with user from ChatBot.

### Example


```python
import kenar_api_client
from kenar_api_client.models.chat_api_chat_bot_send_message_body import ChatAPIChatBotSendMessageBody
from kenar_api_client.models.chatapi_chat_bot_send_message_response import ChatapiChatBotSendMessageResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    chat_api_chat_bot_send_message_body = kenar_api_client.ChatAPIChatBotSendMessageBody() # ChatAPIChatBotSendMessageBody | 

    try:
        # Send a message to a ChatBot conversation
        api_response = api_instance.chat_api_chat_bot_send_message(conversation_id, chat_api_chat_bot_send_message_body)
        print("The response of ChatAPIApi->chat_api_chat_bot_send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_chat_bot_send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **chat_api_chat_bot_send_message_body** | [**ChatAPIChatBotSendMessageBody**](ChatAPIChatBotSendMessageBody.md)|  | 

### Return type

[**ChatapiChatBotSendMessageResponse**](ChatapiChatBotSendMessageResponse.md)

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

# **chat_api_chat_bot_send_message2**
> ChatapiChatBotSendMessageResponse chat_api_chat_bot_send_message2(user_id, chat_api_chat_bot_send_message_body)

Send a message to a ChatBot conversation

You can call this API with either conversation_id or user_id.
Calling with user_id needs a access_token having CHAT_BOT_USER_MESSAGE_SEND scope.This enables you to start conversation with user from ChatBot.

### Example


```python
import kenar_api_client
from kenar_api_client.models.chat_api_chat_bot_send_message_body import ChatAPIChatBotSendMessageBody
from kenar_api_client.models.chatapi_chat_bot_send_message_response import ChatapiChatBotSendMessageResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    user_id = 'user_id_example' # str | 
    chat_api_chat_bot_send_message_body = kenar_api_client.ChatAPIChatBotSendMessageBody() # ChatAPIChatBotSendMessageBody | 

    try:
        # Send a message to a ChatBot conversation
        api_response = api_instance.chat_api_chat_bot_send_message2(user_id, chat_api_chat_bot_send_message_body)
        print("The response of ChatAPIApi->chat_api_chat_bot_send_message2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_chat_bot_send_message2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **chat_api_chat_bot_send_message_body** | [**ChatAPIChatBotSendMessageBody**](ChatAPIChatBotSendMessageBody.md)|  | 

### Return type

[**ChatapiChatBotSendMessageResponse**](ChatapiChatBotSendMessageResponse.md)

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

# **chat_api_chat_bot_send_message3**
> ChatapiChatBotSendMessageResponse chat_api_chat_bot_send_message3(conversation_id, chat_api_chat_bot_send_message_body)

Send a message to a ChatBot conversation

You can call this API with either conversation_id or user_id.
Calling with user_id needs a access_token having CHAT_BOT_USER_MESSAGE_SEND scope.This enables you to start conversation with user from ChatBot.

### Example


```python
import kenar_api_client
from kenar_api_client.models.chat_api_chat_bot_send_message_body import ChatAPIChatBotSendMessageBody
from kenar_api_client.models.chatapi_chat_bot_send_message_response import ChatapiChatBotSendMessageResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    chat_api_chat_bot_send_message_body = kenar_api_client.ChatAPIChatBotSendMessageBody() # ChatAPIChatBotSendMessageBody | 

    try:
        # Send a message to a ChatBot conversation
        api_response = api_instance.chat_api_chat_bot_send_message3(conversation_id, chat_api_chat_bot_send_message_body)
        print("The response of ChatAPIApi->chat_api_chat_bot_send_message3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_chat_bot_send_message3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **chat_api_chat_bot_send_message_body** | [**ChatAPIChatBotSendMessageBody**](ChatAPIChatBotSendMessageBody.md)|  | 

### Return type

[**ChatapiChatBotSendMessageResponse**](ChatapiChatBotSendMessageResponse.md)

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

# **chat_api_conversation_send_message**
> ChatapiConversationSendMessageResponse chat_api_conversation_send_message(conversation_id, chat_api_conversation_send_message_body)

Send a message to a conversation

This API is used to send a message to a conversation.
You need one of the following scopes to call this API:
- CONVERSATION_SEND_MESSAGE.{conversation_id}
- CHAT_SUPPLIER_ALL_CONVERSATIONS_MESSAGE_SEND
- CHAT_POST_CONVERSATIONS_MESSAGE_SEND.{post_token}


### Example


```python
import kenar_api_client
from kenar_api_client.models.chat_api_conversation_send_message_body import ChatAPIConversationSendMessageBody
from kenar_api_client.models.chatapi_conversation_send_message_response import ChatapiConversationSendMessageResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    chat_api_conversation_send_message_body = kenar_api_client.ChatAPIConversationSendMessageBody() # ChatAPIConversationSendMessageBody | 

    try:
        # Send a message to a conversation
        api_response = api_instance.chat_api_conversation_send_message(conversation_id, chat_api_conversation_send_message_body)
        print("The response of ChatAPIApi->chat_api_conversation_send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_conversation_send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **chat_api_conversation_send_message_body** | [**ChatAPIConversationSendMessageBody**](ChatAPIConversationSendMessageBody.md)|  | 

### Return type

[**ChatapiConversationSendMessageResponse**](ChatapiConversationSendMessageResponse.md)

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

# **chat_api_generate_upload_token**
> ChatapiGenerateUploadTokenResponse chat_api_generate_upload_token(body)

Generate an upload token

This API is used to generate an upload token for uploading media files.

### Example


```python
import kenar_api_client
from kenar_api_client.models.chatapi_generate_upload_token_response import ChatapiGenerateUploadTokenResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    body = None # object | 

    try:
        # Generate an upload token
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

# **chat_api_get_conversation**
> ChatapiGetConversationResponse chat_api_get_conversation(conversation_id)

Get Conversation by it's ID

This API is used to get the conversation and messages of a conversation by it's ID.This API expects access token with `CHAT_CONVERSATION_READ` scope.

### Example


```python
import kenar_api_client
from kenar_api_client.models.chatapi_get_conversation_response import ChatapiGetConversationResponse
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
    api_instance = kenar_api_client.ChatAPIApi(api_client)
    conversation_id = 'conversation_id_example' # str | 

    try:
        # Get Conversation by it's ID
        api_response = api_instance.chat_api_get_conversation(conversation_id)
        print("The response of ChatAPIApi->chat_api_get_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatAPIApi->chat_api_get_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 

### Return type

[**ChatapiGetConversationResponse**](ChatapiGetConversationResponse.md)

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

