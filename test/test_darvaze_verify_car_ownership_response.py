# coding: utf-8

"""
    Kenar API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kenar_api_client.models.darvaze_verify_car_ownership_response import DarvazeVerifyCarOwnershipResponse

class TestDarvazeVerifyCarOwnershipResponse(unittest.TestCase):
    """DarvazeVerifyCarOwnershipResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DarvazeVerifyCarOwnershipResponse:
        """Test DarvazeVerifyCarOwnershipResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DarvazeVerifyCarOwnershipResponse`
        """
        model = DarvazeVerifyCarOwnershipResponse()
        if include_optional:
            return DarvazeVerifyCarOwnershipResponse(
                id = ''
            )
        else:
            return DarvazeVerifyCarOwnershipResponse(
        )
        """

    def testDarvazeVerifyCarOwnershipResponse(self):
        """Test DarvazeVerifyCarOwnershipResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
