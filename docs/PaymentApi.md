# kenar_api_client.PaymentApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_commit_wallet_transaction**](PaymentApi.md#payment_commit_wallet_transaction) | **POST** /experimental/open-platform/wallet/payments/commit | 
[**payment_create_wallet_payment**](PaymentApi.md#payment_create_wallet_payment) | **POST** /experimental/open-platform/wallet/payments/create | 
[**payment_get_balance**](PaymentApi.md#payment_get_balance) | **GET** /experimental/open-platform/balance | 
[**payment_get_post_pricing**](PaymentApi.md#payment_get_post_pricing) | **GET** /v1/open-platform/post/{post_token}/pricing | دریافت هزینه سرویس
[**payment_get_transaction**](PaymentApi.md#payment_get_transaction) | **GET** /experimental/open-platform/transactions/{id} | 
[**payment_list_transactions**](PaymentApi.md#payment_list_transactions) | **GET** /experimental/open-platform/transactions | 
[**payment_reorder_post**](PaymentApi.md#payment_reorder_post) | **POST** /experimental/open-platform/post/{post_token}/reorder | 
[**payment_retrieve_wallet_transaction**](PaymentApi.md#payment_retrieve_wallet_transaction) | **GET** /experimental/open-platform/wallet/payments/{token} | 
[**payment_submit_user_payment**](PaymentApi.md#payment_submit_user_payment) | **POST** /v1/open-platform/user-payments | ثبت پرداخت کاربر


# **payment_commit_wallet_transaction**
> PaymentCommitWalletTransactionResponse payment_commit_wallet_transaction(payment_commit_wallet_transaction_request)

(محدود) با استفاده از این API می‌توانید یک پرداخت موفق را commit کنید. این API idempotent است و می‌توانید چندین بار آن را فراخوانی کنید.

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

(محدود) با استفاده از این API می‌توانید یک تراکنش پرداخت از کیف پول کاربران شروع کنید.

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

(محدود) با استفاده از این API می‌توانید موجودی فعلی اپلیکیشن خود را دریافت کنید.

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

دریافت هزینه سرویس

Using this API and with user permission, you can get the price of various services like Reorder and Submit.The price of this API is not necessarily the same as the price on Divar, and pricing may vary.Use this API to get the price before applying services (such as reordering a post or submitting a post).

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
        # دریافت هزینه سرویس
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

(محدود) با استفاده از این API می‌توانید جزئیات تراکنش را دریافت کنید.

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

(محدود) با استفاده از این api میتوانید لیست تراکنش‌های اپ را مشاهده کنید. برای مشاهده‌ی تمام تراکنش‌ها، صفحات را دنبال کنید.

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
    page_size = 56 # int | Number of transactions to return per page (optional)
    page_token = 'page_token_example' # str | Token for the next page of results (optional)

    try:
        api_response = api_instance.payment_list_transactions(page_size=page_size, page_token=page_token)
        print("The response of PaymentApi->payment_list_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_list_transactions: %s\n" % e)
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

(محدود) قبل از فراخوانی این API، از API GetPostPricing برای دریافت هزینه سرویس استفاده کنید.

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

(محدود) با استفاده از این API می‌توانید یک تراکنش و وضعیت آن را بازیابی کنید. از این API برای اعتبارسنجی پرداخت قبل از commit استفاده کنید.

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
> object payment_submit_user_payment(amount_rials=amount_rials, profit_rials=profit_rials, services=services, reference_id=reference_id)

ثبت پرداخت کاربر

باید با استفاده از این API پرداخت کاربران را ثبت کنید. ضروری است که از این API برای ثبت هر پرداخت کاربر به همراه مبلغ دریافتی استفاده کنید. انتظار می‌رود این API با توکن دسترسی دارای دامنه SUBMIT_USER_PAYMENT فراخوانی شود.

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
    api_instance = kenar_api_client.PaymentApi(api_client)
    amount_rials = 'amount_rials_example' # str | کل مبلغ پرداختی توسط کاربر، به ریال (optional)
    profit_rials = 'profit_rials_example' # str | بخشی از مبلغ پرداختی که به شما تعلق می‌گیرد (سود یا کمیسیون)، به ریال (optional)
    services = ['services_example'] # List[str] | لیست شناسه سرویس‌هایی که کاربر برای آنها پرداخت انجام داده است (مثلاً «banner»، «title_refinement» و ...). توصیه می‌شود از نام‌های انگلیسی کوتاه و توصیفی به‌عنوان شناسه سرویس استفاده شود. (optional)
    reference_id = 'reference_id_example' # str | شناسه مرجع فاکتور یا تراکنش (optional)

    try:
        # ثبت پرداخت کاربر
        api_response = api_instance.payment_submit_user_payment(amount_rials=amount_rials, profit_rials=profit_rials, services=services, reference_id=reference_id)
        print("The response of PaymentApi->payment_submit_user_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_submit_user_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount_rials** | **str**| کل مبلغ پرداختی توسط کاربر، به ریال | [optional] 
 **profit_rials** | **str**| بخشی از مبلغ پرداختی که به شما تعلق می‌گیرد (سود یا کمیسیون)، به ریال | [optional] 
 **services** | [**List[str]**](str.md)| لیست شناسه سرویس‌هایی که کاربر برای آنها پرداخت انجام داده است (مثلاً «banner»، «title_refinement» و ...). توصیه می‌شود از نام‌های انگلیسی کوتاه و توصیفی به‌عنوان شناسه سرویس استفاده شود. | [optional] 
 **reference_id** | **str**| شناسه مرجع فاکتور یا تراکنش | [optional] 

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

