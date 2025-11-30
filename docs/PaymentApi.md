# kenar_api_client.PaymentApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_commit_wallet_transaction**](PaymentApi.md#payment_commit_wallet_transaction) | **POST** /experimental/open-platform/wallet/payments/commit | تایید تراکنش کیف پول
[**payment_create_wallet_payment**](PaymentApi.md#payment_create_wallet_payment) | **POST** /experimental/open-platform/wallet/payments/create | ایجاد پرداخت کیف پول
[**payment_get_balance**](PaymentApi.md#payment_get_balance) | **GET** /experimental/open-platform/balance | دریافت موجودی اپلیکیشن
[**payment_get_post_pricing**](PaymentApi.md#payment_get_post_pricing) | **GET** /v1/open-platform/post/{post_token}/pricing | Retrieve the cost of the service
[**payment_get_transaction**](PaymentApi.md#payment_get_transaction) | **GET** /experimental/open-platform/transactions/{id} | دریافت جزئیات تراکنش
[**payment_list_transactions**](PaymentApi.md#payment_list_transactions) | **GET** /experimental/open-platform/transactions | لیست تراکنش‌ها
[**payment_publish_user_post**](PaymentApi.md#payment_publish_user_post) | **POST** /experimental/open-platform/post/{post_token}/publish | Pay for user post submission on behalf of provider
[**payment_renew_post**](PaymentApi.md#payment_renew_post) | **POST** /experimental/open-platform/post/{post_token}/renew | تمدید آگهی
[**payment_reorder_post**](PaymentApi.md#payment_reorder_post) | **POST** /experimental/open-platform/post/{post_token}/reorder | نردبان آگهی
[**payment_retrieve_wallet_transaction**](PaymentApi.md#payment_retrieve_wallet_transaction) | **GET** /experimental/open-platform/wallet/payments/{token} | بازیابی تراکنش کیف پول
[**payment_submit_user_payment**](PaymentApi.md#payment_submit_user_payment) | **POST** /v1/open-platform/user-payments | Submit a user payment


# **payment_commit_wallet_transaction**
> PaymentCommitWalletTransactionResponse payment_commit_wallet_transaction(payment_commit_wallet_transaction_request)

تایید تراکنش کیف پول

(Limited) Using this API you can commit a successful payment. This API is idempotent and you can call it multiple times.

مجوزهای مورد نیاز: WALLET_PAYMENT.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.payment_commit_wallet_transaction_request import PaymentCommitWalletTransactionRequest
from kenar_api_client.models.payment_commit_wallet_transaction_response import PaymentCommitWalletTransactionResponse
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
    api_instance = kenar_api_client.PaymentApi(api_client)
    payment_commit_wallet_transaction_request = kenar_api_client.PaymentCommitWalletTransactionRequest() # PaymentCommitWalletTransactionRequest | 

    try:
        # تایید تراکنش کیف پول
        api_response = api_instance.payment_commit_wallet_transaction(payment_commit_wallet_transaction_request)
        print("The response of PaymentApi->payment_commit_wallet_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_commit_wallet_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_commit_wallet_transaction_request** | [**PaymentCommitWalletTransactionRequest**](PaymentCommitWalletTransactionRequest.md)|  | 

### Return type

[**PaymentCommitWalletTransactionResponse**](PaymentCommitWalletTransactionResponse.md)

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

# **payment_create_wallet_payment**
> PaymentCreateWalletPaymentResponse payment_create_wallet_payment(payment_create_wallet_payment_request)

ایجاد پرداخت کیف پول

(Limited) Using this API you can start a payment transaction from the users wallet.

مجوزهای مورد نیاز: WALLET_PAYMENT.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.payment_create_wallet_payment_request import PaymentCreateWalletPaymentRequest
from kenar_api_client.models.payment_create_wallet_payment_response import PaymentCreateWalletPaymentResponse
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
    api_instance = kenar_api_client.PaymentApi(api_client)
    payment_create_wallet_payment_request = kenar_api_client.PaymentCreateWalletPaymentRequest() # PaymentCreateWalletPaymentRequest | 

    try:
        # ایجاد پرداخت کیف پول
        api_response = api_instance.payment_create_wallet_payment(payment_create_wallet_payment_request)
        print("The response of PaymentApi->payment_create_wallet_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_create_wallet_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_create_wallet_payment_request** | [**PaymentCreateWalletPaymentRequest**](PaymentCreateWalletPaymentRequest.md)|  | 

### Return type

[**PaymentCreateWalletPaymentResponse**](PaymentCreateWalletPaymentResponse.md)

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

# **payment_get_balance**
> PaymentGetBalanceResponse payment_get_balance()

دریافت موجودی اپلیکیشن

(Limited) Using this API you can retrieve current balance of your app.

مجوزهای مورد نیاز: BALANCE_RETRIEVE.

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
    api_instance = kenar_api_client.PaymentApi(api_client)

    try:
        # دریافت موجودی اپلیکیشن
        api_response = api_instance.payment_get_balance()
        print("The response of PaymentApi->payment_get_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_get_balance: %s\n" % e)
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

Retrieve the cost of the service

Using this API and with user permission, you can get the price of various services like Reorder, Renew, and Submit.The price of this API is not necessarily the same as the price on Divar, and pricing may vary.Use this API to get the price before applying services (such as reordering a post, renewing a post, or submitting a post).

مجوزهای مورد نیاز: POST_PRICING_RETRIEVE.

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
    api_instance = kenar_api_client.PaymentApi(api_client)
    post_token = 'post_token_example' # str | شناسه منحصر به فرد 8-9 کاراکتری برای آگهی

    try:
        # Retrieve the cost of the service
        api_response = api_instance.payment_get_post_pricing(post_token)
        print("The response of PaymentApi->payment_get_post_pricing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_get_post_pricing: %s\n" % e)
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

دریافت جزئیات تراکنش

(Limited) Using this API you can retrieve transaction details.

مجوزهای مورد نیاز: TRANSACTION_RETRIEVE.

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
    api_instance = kenar_api_client.PaymentApi(api_client)
    id = 'id_example' # str | شناسه منحصر به فرد برای تراکنش، همان id در درخواست

    try:
        # دریافت جزئیات تراکنش
        api_response = api_instance.payment_get_transaction(id)
        print("The response of PaymentApi->payment_get_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_get_transaction: %s\n" % e)
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

لیست تراکنش‌ها

(Limited) Using this API you can retrieve a list of transactions. Follow pages till you get an empty list.

مجوزهای مورد نیاز: TRANSACTION_LIST.

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
    api_instance = kenar_api_client.PaymentApi(api_client)
    page_size = 56 # int | تعداد تراکنش‌ها برای برگرداندن در هر صفحه (optional)
    page_token = 'page_token_example' # str | توکن برای صفحه بعدی نتایج (optional)

    try:
        # لیست تراکنش‌ها
        api_response = api_instance.payment_list_transactions(page_size=page_size, page_token=page_token)
        print("The response of PaymentApi->payment_list_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_list_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| تعداد تراکنش‌ها برای برگرداندن در هر صفحه | [optional] 
 **page_token** | **str**| توکن برای صفحه بعدی نتایج | [optional] 

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

# **payment_publish_user_post**
> PaymentPublishUserPostResponse payment_publish_user_post(post_token, payment_publish_user_post_body)

Pay for user post submission on behalf of provider

This API allows providers to pay for user post submission costs. The post_token should be obtained from the SubmitUserPost API in post collection.

مجوزهای مورد نیاز: PUBLISH_USER_POST.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.payment_publish_user_post_body import PaymentPublishUserPostBody
from kenar_api_client.models.payment_publish_user_post_response import PaymentPublishUserPostResponse
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
    api_instance = kenar_api_client.PaymentApi(api_client)
    post_token = 'post_token_example' # str | توکن آگهی دریافت شده از RPC SubmitUserPost. شناسه منحصر به فرد 8-9 کاراکتری برای آگهی ثبت شده توسط کاربر.
    payment_publish_user_post_body = kenar_api_client.PaymentPublishUserPostBody() # PaymentPublishUserPostBody | 

    try:
        # Pay for user post submission on behalf of provider
        api_response = api_instance.payment_publish_user_post(post_token, payment_publish_user_post_body)
        print("The response of PaymentApi->payment_publish_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_publish_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_token** | **str**| توکن آگهی دریافت شده از RPC SubmitUserPost. شناسه منحصر به فرد 8-9 کاراکتری برای آگهی ثبت شده توسط کاربر. | 
 **payment_publish_user_post_body** | [**PaymentPublishUserPostBody**](PaymentPublishUserPostBody.md)|  | 

### Return type

[**PaymentPublishUserPostResponse**](PaymentPublishUserPostResponse.md)

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

# **payment_renew_post**
> PaymentRenewPostResponse payment_renew_post(post_token, payment_renew_post_body)

تمدید آگهی

(Limited) Use this API to renew a post, which extends its visibility period. Use GetPostPricing API to get the cost of the service before calling this API.

مجوزهای مورد نیاز: POST_RENEW.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.payment_renew_post_body import PaymentRenewPostBody
from kenar_api_client.models.payment_renew_post_response import PaymentRenewPostResponse
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
    api_instance = kenar_api_client.PaymentApi(api_client)
    post_token = 'post_token_example' # str | 
    payment_renew_post_body = kenar_api_client.PaymentRenewPostBody() # PaymentRenewPostBody | 

    try:
        # تمدید آگهی
        api_response = api_instance.payment_renew_post(post_token, payment_renew_post_body)
        print("The response of PaymentApi->payment_renew_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_renew_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_token** | **str**|  | 
 **payment_renew_post_body** | [**PaymentRenewPostBody**](PaymentRenewPostBody.md)|  | 

### Return type

[**PaymentRenewPostResponse**](PaymentRenewPostResponse.md)

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

# **payment_reorder_post**
> PaymentReorderPostResponse payment_reorder_post(post_token, payment_reorder_post_body)

نردبان آگهی

(Limited) Use GetPostPricing API to get the cost of the service before calling this API.

مجوزهای مورد نیاز: POST_REORDER.

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
    api_instance = kenar_api_client.PaymentApi(api_client)
    post_token = 'post_token_example' # str | 
    payment_reorder_post_body = kenar_api_client.PaymentReorderPostBody() # PaymentReorderPostBody | 

    try:
        # نردبان آگهی
        api_response = api_instance.payment_reorder_post(post_token, payment_reorder_post_body)
        print("The response of PaymentApi->payment_reorder_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_reorder_post: %s\n" % e)
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

# **payment_retrieve_wallet_transaction**
> PaymentRetrieveWalletTransactionResponse payment_retrieve_wallet_transaction(token)

بازیابی تراکنش کیف پول

(Limited) Using this API you can retrieve a transaction and its status. Use this API to validate the payment before committing.

مجوزهای مورد نیاز: WALLET_PAYMENT.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.payment_retrieve_wallet_transaction_response import PaymentRetrieveWalletTransactionResponse
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
    api_instance = kenar_api_client.PaymentApi(api_client)
    token = 'token_example' # str | توکن تراکنشی که می‌خواهید بازیابی کنید

    try:
        # بازیابی تراکنش کیف پول
        api_response = api_instance.payment_retrieve_wallet_transaction(token)
        print("The response of PaymentApi->payment_retrieve_wallet_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_retrieve_wallet_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| توکن تراکنشی که می‌خواهید بازیابی کنید | 

### Return type

[**PaymentRetrieveWalletTransactionResponse**](PaymentRetrieveWalletTransactionResponse.md)

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

# **payment_submit_user_payment**
> object payment_submit_user_payment(payment_submit_user_payment_request)

Submit a user payment

Using this API, you should submit a user payment. It is imperative you use this API to submit a user payment along with the received amount. This API requires an access token with the `SUBMIT_USER_PAYMENT` OAuth scope.

مجوزهای مورد نیاز: SUBMIT_USER_PAYMENT.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.payment_submit_user_payment_request import PaymentSubmitUserPaymentRequest
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
    api_instance = kenar_api_client.PaymentApi(api_client)
    payment_submit_user_payment_request = kenar_api_client.PaymentSubmitUserPaymentRequest() # PaymentSubmitUserPaymentRequest | 

    try:
        # Submit a user payment
        api_response = api_instance.payment_submit_user_payment(payment_submit_user_payment_request)
        print("The response of PaymentApi->payment_submit_user_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_submit_user_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_submit_user_payment_request** | [**PaymentSubmitUserPaymentRequest**](PaymentSubmitUserPaymentRequest.md)|  | 

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

