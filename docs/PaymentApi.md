# kenar_api_client.PaymentApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_commit_wallet_transaction**](PaymentApi.md#payment_commit_wallet_transaction) | **POST** /experimental/open-platform/wallet/payments/commit | نهایی کردن تراکنش کیف پول
[**payment_create_wallet_payment**](PaymentApi.md#payment_create_wallet_payment) | **POST** /experimental/open-platform/wallet/payments/create | ایجاد پرداخت کیف پول
[**payment_get_balance**](PaymentApi.md#payment_get_balance) | **GET** /experimental/open-platform/balance | دریافت موجودی اپلیکیشن
[**payment_get_post_pricing**](PaymentApi.md#payment_get_post_pricing) | **GET** /v1/open-platform/post/{post_token}/pricing | دریافت قیمت خدمات آگهی
[**payment_get_transaction**](PaymentApi.md#payment_get_transaction) | **GET** /experimental/open-platform/transactions/{id} | دریافت جزئیات تراکنش
[**payment_list_transactions**](PaymentApi.md#payment_list_transactions) | **GET** /experimental/open-platform/transactions | لیست تراکنش‌ها
[**payment_publish_user_post**](PaymentApi.md#payment_publish_user_post) | **POST** /experimental/open-platform/post/{post_token}/publish | انتشار آگهی کاربر (پرداخت توسط ارائه‌دهنده)
[**payment_renew_post**](PaymentApi.md#payment_renew_post) | **POST** /experimental/open-platform/post/{post_token}/renew | تمدید آگهی
[**payment_reorder_post**](PaymentApi.md#payment_reorder_post) | **POST** /experimental/open-platform/post/{post_token}/reorder | نردبان آگهی
[**payment_retrieve_wallet_transaction**](PaymentApi.md#payment_retrieve_wallet_transaction) | **GET** /experimental/open-platform/wallet/payments/{token} | دریافت تراکنش کیف پول
[**payment_submit_user_payment**](PaymentApi.md#payment_submit_user_payment) | **POST** /v1/open-platform/user-payments | ثبت رکورد پرداخت کاربر


# **payment_commit_wallet_transaction**
> PaymentCommitWalletTransactionResponse payment_commit_wallet_transaction(payment_commit_wallet_transaction_request)

نهایی کردن تراکنش کیف پول

این API تراکنش پرداخت کیف پول را پس از پرداخت موفق نهایی می‌کند.

**نکات مهم**:
- این قابلیت آزمایشی است و فقط برای اپلیکیشن‌های تایید شده در دسترس است
- فقط تراکنش‌هایی که در وضعیت PAID هستند را نهایی کنید

مجوزهای مورد نیاز: `WALLET_PAYMENT`. OAuth scope موردنیاز: `CREATE_WALLET_PAYMENT`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PaymentApi(api_client)
    payment_commit_wallet_transaction_request = kenar_api_client.PaymentCommitWalletTransactionRequest() # PaymentCommitWalletTransactionRequest | 

    try:
        # نهایی کردن تراکنش کیف پول
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

# **payment_create_wallet_payment**
> PaymentCreateWalletPaymentResponse payment_create_wallet_payment(payment_create_wallet_payment_request)

ایجاد پرداخت کیف پول

این API امکان شروع تراکنش پرداخت از کیف پول دیوار کاربر را فراهم می‌کند. کاربر برای تکمیل پرداخت هدایت می‌شود و می‌توانید وضعیت تراکنش را پیگیری کنید.

**نکات مهم**:
- این قابلیت آزمایشی است و فقط برای اپلیکیشن‌های تایید شده در دسترس است
- کاربر برای تکمیل تراکنش به آدرس پرداخت هدایت می‌شود
- پس از پرداخت، کاربر به `redirect_url` مشخص شده شما هدایت می‌شود
- از `RetrieveWalletTransaction` برای بررسی وضعیت پرداخت استفاده کنید
- از `CommitWalletTransaction` برای نهایی کردن تراکنش پس از پرداخت موفق استفاده کنید


مجوزهای مورد نیاز: `WALLET_PAYMENT`. OAuth scope موردنیاز: `CREATE_WALLET_PAYMENT`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

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

# **payment_get_balance**
> PaymentGetBalanceResponse payment_get_balance()

دریافت موجودی اپلیکیشن

این API امکان دریافت موجودی فعلی اپلیکیشن شما به ریال را فراهم می‌کند. برای نظارت بر موجودی حساب قبل از انجام عملیات‌های پولی استفاده کنید.

**نکات مهم**:
- این قابلیت فقط برای اپلیکیشن‌های تایید شده در دسترس است
- موجودی به ریال ایران برگردانده می‌شود

مجوزهای مورد نیاز: `BALANCE_RETRIEVE`

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

دریافت قیمت خدمات آگهی

این API امکان دریافت اطلاعات قیمت‌گذاری برای خدمات مرتبط با آگهی را فراهم می‌کند. قبل از انجام عملیات‌های پولی مانند نردبان، تمدید یا ثبت آگهی از این برای بررسی هزینه‌ها استفاده کنید.

**نکات مهم**:
- قیمت‌گذاری مختص اپلیکیشن شما است و ممکن است با قیمت‌گذاری استاندارد دیوار متفاوت باشد
- قیمت‌ها ممکن است بر اساس دسته‌بندی و شهر آگهی متفاوت باشند
- فلگ `available` نشان می‌دهد که آیا سرویس برای این آگهی قابل اعمال است

مجوزهای مورد نیاز: `POST_PRICING_RETRIEVE`. OAuth scope موردنیاز: `PAYMENT_ALL_POSTS_PRICING_READ`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PaymentApi(api_client)
    post_token = 'post_token_example' # str | شناسه منحصر به فرد 8-9 کاراکتری برای آگهی

    try:
        # دریافت قیمت خدمات آگهی
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

# **payment_get_transaction**
> PaymentGetTransactionResponse payment_get_transaction(id)

دریافت جزئیات تراکنش

این API امکان دریافت اطلاعات دقیق یک تراکنش خاص با شناسه آن را فراهم می‌کند. برای پیگیری وضعیت تراکنش، هزینه‌ها و متادیتا استفاده کنید.

**نکات مهم**:
- این قابلیت فقط برای اپلیکیشن‌های تایید شده در دسترس است
- شناسه تراکنش همان UUID است که هنگام ایجاد تراکنش ارسال کردید
- وضعیت‌های تراکنش: PENDING، COMPLETED، FAILED، REFUNDED
- انواع تراکنش: REORDER، SUBMIT، RENEW
- برای تایید تکمیل تراکنش پس از عملیات‌های پولی استفاده کنید

مجوزهای مورد نیاز: `TRANSACTION_RETRIEVE`

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

این API امکان دریافت لیست صفحه‌بندی شده از تراکنش‌های اپلیکیشن شما را فراهم می‌کند. برای تاریخچه تراکنش، ممیزی و تسویه حساب استفاده کنید.

**نکات مهم**:
- این قابلیت فقط برای اپلیکیشن‌های تایید شده در دسترس است
- نتایج صفحه‌بندی شده هستند - از `page_size` برای کنترل تعداد آیتم‌ها در هر صفحه استفاده کنید
- از `page_token` در پاسخ برای دریافت صفحه بعدی استفاده کنید
- تراکنش‌ها بر اساس زمان ایجاد مرتب می‌شوند (جدیدترین اول)

مجوزهای مورد نیاز: `TRANSACTION_LIST`

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
    page_size = 56 # int | تعداد تراکنش‌ها در هر صفحه (optional)
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
 **page_size** | **int**| تعداد تراکنش‌ها در هر صفحه | [optional] 
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

انتشار آگهی کاربر (پرداخت توسط ارائه‌دهنده)

این API امکان پرداخت هزینه انتشار آگهی ثبت شده توسط کاربر از طرف اپلیکیشن شما را فراهم می‌کند. هزینه از موجودی اپلیکیشن شما کسر می‌شود و آگهی منتشر می‌شود.

**نکات مهم**:
- ابتدا آگهی باید با API `SubmitUserPost` ایجاد شده باشد
- یک `id` منحصر به فرد (UUID v4) برای جلوگیری از تکرار ارسال کنید
- آگهی باید در وضعیت نیازمند پرداخت (WAITING_FOR_PAYMENT) باشد
- از کافی بودن موجودی اپلیکیشن خود اطمینان حاصل کنید
- هزینه‌ها بر اساس دسته‌بندی و شهر آگهی متفاوت است

مجوزهای مورد نیاز: `PUBLISH_USER_POST`. OAuth scope موردنیاز: `SUBMIT_USER_POST`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PaymentApi(api_client)
    post_token = 'post_token_example' # str | توکن آگهی دریافت شده از RPC SubmitUserPost. شناسه منحصر به فرد 8-9 کاراکتری برای آگهی ثبت شده توسط کاربر.
    payment_publish_user_post_body = kenar_api_client.PaymentPublishUserPostBody() # PaymentPublishUserPostBody | 

    try:
        # انتشار آگهی کاربر (پرداخت توسط ارائه‌دهنده)
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

# **payment_renew_post**
> PaymentRenewPostResponse payment_renew_post(post_token, payment_renew_post_body)

تمدید آگهی

این API امکان تمدید آگهی را فراهم می‌کند که دوره نمایش آن در دیوار را افزایش می‌دهد. هزینه از موجودی اپلیکیشن شما کسر می‌شود.

**نکات مهم**:
- این قابلیت فقط برای اپلیکیشن‌های تایید شده در دسترس است
- قبل از تمدید، از `GetPostPricing` برای بررسی هزینه استفاده کنید
- یک `id` منحصر به فرد (UUID v4) برای جلوگیری از تکرار ارسال کنید
- آگهی باید در وضعیت PUBLISHED و واجد شرایط تمدید باشد
- از کافی بودن موجودی اپلیکیشن خود اطمینان حاصل کنید
- هزینه‌ها بر اساس دسته‌بندی و شهر آگهی متفاوت است
- تمدید، نمایش آگهی را افزایش داده و عمر آن را بازنشانی می‌کند

مجوزهای مورد نیاز: `POST_RENEW`. OAuth scope موردنیاز: `PAYMENT_ALL_POSTS_RENEW`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

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

# **payment_reorder_post**
> PaymentReorderPostResponse payment_reorder_post(post_token, payment_reorder_post_body)

نردبان آگهی

این API امکان نردبان کردن آگهی به بالای لیست را فراهم می‌کند. هزینه از موجودی اپلیکیشن شما کسر می‌شود.

**نکات مهم**:
- این قابلیت فقط برای اپلیکیشن‌های تایید شده در دسترس است
- قبل از نردبان، از `GetPostPricing` برای بررسی هزینه استفاده کنید
- یک `id` منحصر به فرد (UUID v4) برای جلوگیری از تکرار ارسال کنید
- آگهی باید در وضعیت PUBLISHED باشد
- از کافی بودن موجودی اپلیکیشن خود اطمینان حاصل کنید
- هزینه‌ها بر اساس دسته‌بندی و شهر آگهی متفاوت است

مجوزهای مورد نیاز: `POST_REORDER`. OAuth scope موردنیاز: `PAYMENT_ALL_POSTS_REORDER`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

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

# **payment_retrieve_wallet_transaction**
> PaymentRetrieveWalletTransactionResponse payment_retrieve_wallet_transaction(token)

دریافت تراکنش کیف پول

این API امکان دریافت وضعیت فعلی و جزئیات تراکنش پرداخت کیف پول را فراهم می‌کند. برای تایید تکمیل پرداخت قبل از commit کردن تراکنش استفاده کنید.

**نکات مهم**:
- این قابلیت آزمایشی است و فقط برای اپلیکیشن‌های تایید شده در دسترس است
- وضعیت‌های تراکنش: UNKNOWN، CREATED، EXPIRED، PAID، COMMITTED

مجوزهای مورد نیاز: `WALLET_PAYMENT`. OAuth scope موردنیاز: `CREATE_WALLET_PAYMENT`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PaymentApi(api_client)
    token = 'token_example' # str | توکن تراکنشی که می‌خواهید دریافت کنید

    try:
        # دریافت تراکنش کیف پول
        api_response = api_instance.payment_retrieve_wallet_transaction(token)
        print("The response of PaymentApi->payment_retrieve_wallet_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->payment_retrieve_wallet_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| توکن تراکنشی که می‌خواهید دریافت کنید | 

### Return type

[**PaymentRetrieveWalletTransactionResponse**](PaymentRetrieveWalletTransactionResponse.md)

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

# **payment_submit_user_payment**
> object payment_submit_user_payment(payment_submit_user_payment_request)

ثبت رکورد پرداخت کاربر

این API امکان گزارش پرداخت انجام شده توسط کاربر به سرویس شما را فراهم می‌کند. از این برای اطلاع‌رسانی دیوار درباره تراکنش‌هایی که کاربران از طریق پلتفرم شما پرداخت می‌کنند استفاده کنید.

**نکات مهم**:
- باید پرداخت‌ها را در بازه زمانی توافق شده گزارش دهید
- `reference_id` باید برای هر تراکنش منحصر به فرد باشد (برای تسویه حساب استفاده می‌شود)
- شناسه خدماتی که کاربر برای آنها پرداخت کرده را لیست کنید (مثلاً 'banner', 'title_refinement')
- این داده‌ها برای تقسیم درآمد و گزارش مالی استفاده می‌شوند


مجوزهای مورد نیاز: `SUBMIT_USER_PAYMENT`. OAuth scope موردنیاز: `SUBMIT_USER_PAYMENT`

### Example

* Api Key Authentication (APIKey):
* OAuth Authentication (OAuth):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with kenar_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kenar_api_client.PaymentApi(api_client)
    payment_submit_user_payment_request = kenar_api_client.PaymentSubmitUserPaymentRequest() # PaymentSubmitUserPaymentRequest | 

    try:
        # ثبت رکورد پرداخت کاربر
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

