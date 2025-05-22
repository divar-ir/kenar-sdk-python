# kenar_api_client.LimitedApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_get_balance**](LimitedApi.md#payment_get_balance) | **GET** /experimental/open-platform/balance | 
[**payment_get_post_pricing**](LimitedApi.md#payment_get_post_pricing) | **GET** /v1/open-platform/post/{post_token}/pricing | Retrieve the cost of the service
[**payment_get_transaction**](LimitedApi.md#payment_get_transaction) | **GET** /experimental/open-platform/transactions/{id} | 
[**payment_reorder_post**](LimitedApi.md#payment_reorder_post) | **POST** /experimental/open-platform/post/{post_token}/reorder | 


# **payment_get_balance**
> PaymentGetBalanceResponse payment_get_balance()

Using this API you can retrieve current balance of your app.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.payment_get_balance_response import PaymentGetBalanceResponse
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
    api_instance = kenar_api_client.LimitedApi(api_client)

    try:
        api_response = api_instance.payment_get_balance()
        print("The response of LimitedApi->payment_get_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LimitedApi->payment_get_balance: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PaymentGetBalanceResponse**](PaymentGetBalanceResponse.md)

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

# **payment_get_post_pricing**
> PaymentGetPostPricingResponse payment_get_post_pricing(post_token)

Retrieve the cost of the service

Using this API and with user permission, you can get the price of various services like Reorder.The price of this API is not necessarily the same as the price on Divar, and pricing may vary.Use this API to get the price before applying services (such as reordering a post).

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.payment_get_post_pricing_response import PaymentGetPostPricingResponse
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
    api_instance = kenar_api_client.LimitedApi(api_client)
    post_token = 'post_token_example' # str | An 8-9 character unique identifier for the post

    try:
        # Retrieve the cost of the service
        api_response = api_instance.payment_get_post_pricing(post_token)
        print("The response of LimitedApi->payment_get_post_pricing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LimitedApi->payment_get_post_pricing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_token** | **str**| An 8-9 character unique identifier for the post | 

### Return type

[**PaymentGetPostPricingResponse**](PaymentGetPostPricingResponse.md)

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

# **payment_get_transaction**
> PaymentGetTransactionResponse payment_get_transaction(id)

Using this API you can retrieve transaction details.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.payment_get_transaction_response import PaymentGetTransactionResponse
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
    api_instance = kenar_api_client.LimitedApi(api_client)
    id = 'id_example' # str | The unique identifier for the transaction, same as the id in the request

    try:
        api_response = api_instance.payment_get_transaction(id)
        print("The response of LimitedApi->payment_get_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LimitedApi->payment_get_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the transaction, same as the id in the request | 

### Return type

[**PaymentGetTransactionResponse**](PaymentGetTransactionResponse.md)

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

# **payment_reorder_post**
> PaymentReorderPostResponse payment_reorder_post(post_token, payment_reorder_post_body)

Use GetPostPricing API to get the cost of the service before calling this API.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.payment_reorder_post_body import PaymentReorderPostBody
from kenar_api_client.models.payment_reorder_post_response import PaymentReorderPostResponse
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
    api_instance = kenar_api_client.LimitedApi(api_client)
    post_token = 'post_token_example' # str | 
    payment_reorder_post_body = kenar_api_client.PaymentReorderPostBody() # PaymentReorderPostBody | 

    try:
        api_response = api_instance.payment_reorder_post(post_token, payment_reorder_post_body)
        print("The response of LimitedApi->payment_reorder_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LimitedApi->payment_reorder_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_token** | **str**|  | 
 **payment_reorder_post_body** | [**PaymentReorderPostBody**](PaymentReorderPostBody.md)|  | 

### Return type

[**PaymentReorderPostResponse**](PaymentReorderPostResponse.md)

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

