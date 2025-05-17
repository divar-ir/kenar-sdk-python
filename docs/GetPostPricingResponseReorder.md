# GetPostPricingResponseReorder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_rials** | **str** | The cost of reordering in rials | [optional] 
**available** | **bool** | Indicates if the post can be reordered. If false, the reorder API will return an error | [optional] 

## Example

```python
from kenar_api_client.models.get_post_pricing_response_reorder import GetPostPricingResponseReorder

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostPricingResponseReorder from a JSON string
get_post_pricing_response_reorder_instance = GetPostPricingResponseReorder.from_json(json)
# print the JSON string representation of the object
print(GetPostPricingResponseReorder.to_json())

# convert the object into a dict
get_post_pricing_response_reorder_dict = get_post_pricing_response_reorder_instance.to_dict()
# create an instance of GetPostPricingResponseReorder from a dict
get_post_pricing_response_reorder_from_dict = GetPostPricingResponseReorder.from_dict(get_post_pricing_response_reorder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


