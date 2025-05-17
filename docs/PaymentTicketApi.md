# kenar_api_client.PaymentTicketApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_ticket_validate**](PaymentTicketApi.md#payment_ticket_validate) | **POST** /v1/open-platform/payment-ticket/validate | Validate a payment ticket


# **payment_ticket_validate**
> PaymentTicketValidateResponse payment_ticket_validate(payment_ticket_validate_request)

Validate a payment ticket

Payment tickets are designed to integrate Kenar apps with Divar internal teams.
Using this API you can validate a payment ticket and get the issuer payload.

### Example


```python
import kenar_api_client
from kenar_api_client.models.payment_ticket_validate_request import PaymentTicketValidateRequest
from kenar_api_client.models.payment_ticket_validate_response import PaymentTicketValidateResponse
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

