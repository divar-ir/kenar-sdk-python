# AddonsImageCarouselRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ImageCarouselRowImageItem]**](ImageCarouselRowImageItem.md) |  | [optional] 
**has_divider** | **bool** |  | [optional] 

## Example

```python
from kenar_api_client.models.addons_image_carousel_row import AddonsImageCarouselRow

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsImageCarouselRow from a JSON string
addons_image_carousel_row_instance = AddonsImageCarouselRow.from_json(json)
# print the JSON string representation of the object
print(AddonsImageCarouselRow.to_json())

# convert the object into a dict
addons_image_carousel_row_dict = addons_image_carousel_row_instance.to_dict()
# create an instance of AddonsImageCarouselRow from a dict
addons_image_carousel_row_from_dict = AddonsImageCarouselRow.from_dict(addons_image_carousel_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


