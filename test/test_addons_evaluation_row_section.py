# coding: utf-8

"""
    Kenar API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kenar_api_client.models.addons_evaluation_row_section import AddonsEvaluationRowSection

class TestAddonsEvaluationRowSection(unittest.TestCase):
    """AddonsEvaluationRowSection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddonsEvaluationRowSection:
        """Test AddonsEvaluationRowSection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddonsEvaluationRowSection`
        """
        model = AddonsEvaluationRowSection()
        if include_optional:
            return AddonsEvaluationRowSection(
                section_color = 'WARNING_SECONDARY',
                text = ''
            )
        else:
            return AddonsEvaluationRowSection(
        )
        """

    def testAddonsEvaluationRowSection(self):
        """Test AddonsEvaluationRowSection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
