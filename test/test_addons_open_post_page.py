# coding: utf-8

"""
    Kenar API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kenar_api_client.models.addons_open_post_page import AddonsOpenPostPage

class TestAddonsOpenPostPage(unittest.TestCase):
    """AddonsOpenPostPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddonsOpenPostPage:
        """Test AddonsOpenPostPage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddonsOpenPostPage`
        """
        model = AddonsOpenPostPage()
        if include_optional:
            return AddonsOpenPostPage(
                post_token = 'AJIEWcw'
            )
        else:
            return AddonsOpenPostPage(
                post_token = 'AJIEWcw',
        )
        """

    def testAddonsOpenPostPage(self):
        """Test AddonsOpenPostPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
