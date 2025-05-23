# coding: utf-8

"""
    Kenar API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kenar_api_client.models.payment_get_post_pricing_response import PaymentGetPostPricingResponse

class TestPaymentGetPostPricingResponse(unittest.TestCase):
    """PaymentGetPostPricingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentGetPostPricingResponse:
        """Test PaymentGetPostPricingResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentGetPostPricingResponse`
        """
        model = PaymentGetPostPricingResponse()
        if include_optional:
            return PaymentGetPostPricingResponse(
                reorder = kenar_api_client.models.get_post_pricing_response_reorder.GetPostPricingResponseReorder(
                    available = True, 
                    cost_rials = '', )
            )
        else:
            return PaymentGetPostPricingResponse(
        )
        """

    def testPaymentGetPostPricingResponse(self):
        """Test PaymentGetPostPricingResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
