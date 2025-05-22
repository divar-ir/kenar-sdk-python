# AddonsAddonSemantic

This is the message extracted by OpenPlatform from service provider semantics. Guidelines:  - Always check to see if an appropriate enum field or value exists before  adding one.  - Zero value of every enum should be {ENUM_NAME}_UNSPECIFIED.  - Enum values should not correspond to any specific post or person  attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**car_verification_failure_reason** | [**AddonSemanticCarVerificationStage**](AddonSemanticCarVerificationStage.md) |  | [optional] 
**car_verification_last_successful_stage** | [**AddonSemanticCarVerificationStage**](AddonSemanticCarVerificationStage.md) |  | [optional] 
**identity_verification_failure_reason** | [**AddonSemanticIdentityVerificationStage**](AddonSemanticIdentityVerificationStage.md) |  | [optional] 
**identity_verification_last_successful_stage** | [**AddonSemanticIdentityVerificationStage**](AddonSemanticIdentityVerificationStage.md) |  | [optional] 
**identity_verification_result** | [**AddonSemanticIdentityVerificationResult**](AddonSemanticIdentityVerificationResult.md) |  | [optional] 
**inspection_result** | [**AddonSemanticInspectionResult**](AddonSemanticInspectionResult.md) |  | [optional] 
**new_face_verification_result** | [**AddonSemanticNewFaceVerificationResult**](AddonSemanticNewFaceVerificationResult.md) |  | [optional] 
**ownership_result** | [**AddonSemanticOwnershipResult**](AddonSemanticOwnershipResult.md) |  | [optional] 
**payment_method** | [**AddonsAddonSemanticPaymentMethod**](AddonsAddonSemanticPaymentMethod.md) |  | [optional] 
**post_verification_result** | [**AddonSemanticPostVerificationResult**](AddonSemanticPostVerificationResult.md) |  | [optional] 
**status** | [**AddonsAddonSemanticStatus**](AddonsAddonSemanticStatus.md) |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_addon_semantic import AddonsAddonSemantic

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsAddonSemantic from a JSON string
addons_addon_semantic_instance = AddonsAddonSemantic.from_json(json)
# print the JSON string representation of the object
print(AddonsAddonSemantic.to_json())

# convert the object into a dict
addons_addon_semantic_dict = addons_addon_semantic_instance.to_dict()
# create an instance of AddonsAddonSemantic from a dict
addons_addon_semantic_from_dict = AddonsAddonSemantic.from_dict(addons_addon_semantic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


