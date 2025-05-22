# kenar_api_client.PaymentTicketApi

All URIs are relative to *https://open-api.divar.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_ticket_validate**](PaymentTicketApi.md#payment_ticket_validate) | **POST** /v1/open-platform/payment-ticket/validate | Validate a payment ticket


# **payment_ticket_validate**
> PaymentTicketValidateResponse payment_ticket_validate(payment_ticket_validate_request)

Validate a payment ticket

Payment tickets are designed to integrate Kenar apps with Divar internal teams.
Using this API you can validate a payment ticket and get the issuer payload.

### Example

* Api Key Authentication (APIKey):

```python
import kenar_api_client
from kenar_api_client.models.payment_ticket_validate_request import PaymentTicketValidateRequest
from kenar_api_client.models.payment_ticket_validate_response import PaymentTicketValidateResponse
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
    api_instance = kenar_api_client.PaymentTicketApi(api_client)
    payment_ticket_validate_request = kenar_api_client.PaymentTicketValidateRequest() # PaymentTicketValidateRequest | 

    try:
        # Validate a payment ticket
        api_response = api_instance.payment_ticket_validate(payment_ticket_validate_request)
        print("The response of PaymentTicketApi->payment_ticket_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTicketApi->payment_ticket_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_ticket_validate_request** | [**PaymentTicketValidateRequest**](PaymentTicketValidateRequest.md)|  | 

### Return type

[**PaymentTicketValidateResponse**](PaymentTicketValidateResponse.md)

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

