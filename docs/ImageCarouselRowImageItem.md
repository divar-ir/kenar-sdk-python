# ImageCarouselRowImageItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from kenar_api_client.models.image_carousel_row_image_item import ImageCarouselRowImageItem

# TODO update the JSON string below
json = "{}"
# create an instance of ImageCarouselRowImageItem from a JSON string
image_carousel_row_image_item_instance = ImageCarouselRowImageItem.from_json(json)
# print the JSON string representation of the object
print(ImageCarouselRowImageItem.to_json())

# convert the object into a dict
image_carousel_row_image_item_dict = image_carousel_row_image_item_instance.to_dict()
# create an instance of ImageCarouselRowImageItem from a dict
image_carousel_row_image_item_from_dict = ImageCarouselRowImageItem.from_dict(image_carousel_row_image_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


