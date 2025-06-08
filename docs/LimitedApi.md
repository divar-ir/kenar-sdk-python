# kenar_api_client.LimitedApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_get_balance**](LimitedApi.md#payment_get_balance) | **GET** /experimental/open-platform/balance | 
[**payment_get_post_pricing**](LimitedApi.md#payment_get_post_pricing) | **GET** /v1/open-platform/post/{post_token}/pricing | دریافت هزینه سرویس
[**payment_get_transaction**](LimitedApi.md#payment_get_transaction) | **GET** /experimental/open-platform/transactions/{id} | 
[**payment_list_transactions**](LimitedApi.md#payment_list_transactions) | **GET** /experimental/open-platform/transactions | 
[**payment_reorder_post**](LimitedApi.md#payment_reorder_post) | **POST** /experimental/open-platform/post/{post_token}/reorder | 


# **payment_get_balance**
> PaymentGetBalanceResponse payment_get_balance()

با استفاده از این API می‌توانید موجودی فعلی اپلیکیشن خود را دریافت کنید.

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
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_get_post_pricing**
> PaymentGetPostPricingResponse payment_get_post_pricing(post_token)

دریافت هزینه سرویس

با استفاده از این API و با مجوز کاربر، می‌توانید قیمت سرویس‌های مختلف مانند نردبان را دریافت کنید. قیمت این API لزوماً با قیمت روی دیوار یکسان نیست و قیمت‌گذاری ممکن است متفاوت باشد. از این API برای دریافت قیمت قبل از اعمال سرویس‌ها (مانند نردبان آگهی) استفاده کنید.

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
    post_token = 'post_token_example' # str | شناسه منحصر به فرد 8-9 کاراکتری برای آگهی

    try:
        # دریافت هزینه سرویس
        api_response = api_instance.payment_get_post_pricing(post_token)
        print("The response of LimitedApi->payment_get_post_pricing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LimitedApi->payment_get_post_pricing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_token** | **str**| شناسه منحصر به فرد 8-9 کاراکتری برای آگهی | 

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
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_get_transaction**
> PaymentGetTransactionResponse payment_get_transaction(id)

با استفاده از این API می‌توانید جزئیات تراکنش را دریافت کنید.

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
    id = 'id_example' # str | شناسه منحصر به فرد برای تراکنش، همان id در درخواست

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
 **id** | **str**| شناسه منحصر به فرد برای تراکنش، همان id در درخواست | 

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
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_list_transactions**
> PaymentListTransactionsResponse payment_list_transactions(page_size=page_size, page_token=page_token)

با استفاده از این api میتوانید لیست تراکنش‌های اپ را مشاهده کنید. برای مشاهده‌ی تمام تراکنش‌ها، صفحات را دنبال کنید.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.payment_list_transactions_response import PaymentListTransactionsResponse
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
    page_size = 56 # int | Number of transactions to return per page (optional)
    page_token = 'page_token_example' # str | Token for the next page of results (optional)

    try:
        api_response = api_instance.payment_list_transactions(page_size=page_size, page_token=page_token)
        print("The response of LimitedApi->payment_list_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LimitedApi->payment_list_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of transactions to return per page | [optional] 
 **page_token** | **str**| Token for the next page of results | [optional] 

### Return type

[**PaymentListTransactionsResponse**](PaymentListTransactionsResponse.md)

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

# **payment_reorder_post**
> PaymentReorderPostResponse payment_reorder_post(post_token, payment_reorder_post_body)

قبل از فراخوانی این API، از API GetPostPricing برای دریافت هزینه سرویس استفاده کنید.

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
**200** | پاسخ موفقیت‌آمیز. |  -  |
**0** | پاسخ خطای غیرمنتظره. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

