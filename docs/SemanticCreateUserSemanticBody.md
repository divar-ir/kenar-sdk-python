# SemanticCreateUserSemanticBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **int** |  | [optional] 
**phone** | **str** |  | [optional] 
**semantic** | **Dict[str, str]** |  | [optional] 
**ticket_uuid** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.semantic_create_user_semantic_body import SemanticCreateUserSemanticBody

# TODO update the JSON string below
json = "{}"
# create an instance of SemanticCreateUserSemanticBody from a JSON string
semantic_create_user_semantic_body_instance = SemanticCreateUserSemanticBody.from_json(json)
# print the JSON string representation of the object
print(SemanticCreateUserSemanticBody.to_json())

# convert the object into a dict
semantic_create_user_semantic_body_dict = semantic_create_user_semantic_body_instance.to_dict()
# create an instance of SemanticCreateUserSemanticBody from a dict
semantic_create_user_semantic_body_from_dict = SemanticCreateUserSemanticBody.from_dict(semantic_create_user_semantic_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


