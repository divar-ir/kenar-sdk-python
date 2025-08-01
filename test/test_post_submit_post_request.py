# coding: utf-8

"""
    Kenar API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kenar_api_client.models.post_submit_post_request import PostSubmitPostRequest

class TestPostSubmitPostRequest(unittest.TestCase):
    """PostSubmitPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostSubmitPostRequest:
        """Test PostSubmitPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostSubmitPostRequest`
        """
        model = PostSubmitPostRequest()
        if include_optional:
            return PostSubmitPostRequest(
                chat_enabled = True,
                city = 'tehran',
                description = 'I'm available only in chat.',
                district = 'abshar',
                hide_phone = True,
                images = [
                    ''
                    ],
                latitude = 35.7152,
                longitude = 51.4043,
                temporary_residence = kenar_api_client.models.post_temporary_residence_fields.postTemporaryResidenceFields(
                    area = 100, 
                    extra_person_capacity = 2, 
                    has_own_image = True, 
                    price_cost_per_extra_person = '150000', 
                    price_regular_days = '1000000', 
                    price_special_days = '1500000', 
                    price_weekends = '1200000', 
                    regular_person_capacity = 4, 
                    rooms_count = 'ROOMS_COUNT_0', ),
                title = 'Temporary Residence for Rent in Tehran'
            )
        else:
            return PostSubmitPostRequest(
        )
        """

    def testPostSubmitPostRequest(self):
        """Test PostSubmitPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
