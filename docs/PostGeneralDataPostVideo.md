# PostGeneralDataPostVideo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | زمان ویدیو به ثانیه | 
**name** | **str** | نام ویدیو (از فیلد &#x60;video_name&#x60; در پاسخ آپلود) | 
**thumbnail_name** | **str** | کاور ویدیو (از فیلد &#x60;thumbnail_name&#x60; در پاسخ آپلود). فریم اول ویدیوی آپلود‌شده است. | 

## Example

```python
from kenar_api_client.models.post_general_data_post_video import PostGeneralDataPostVideo

# TODO update the JSON string below
json = "{}"
# create an instance of PostGeneralDataPostVideo from a JSON string
post_general_data_post_video_instance = PostGeneralDataPostVideo.from_json(json)
# print the JSON string representation of the object
print(PostGeneralDataPostVideo.to_json())

# convert the object into a dict
post_general_data_post_video_dict = post_general_data_post_video_instance.to_dict()
# create an instance of PostGeneralDataPostVideo from a dict
post_general_data_post_video_from_dict = PostGeneralDataPostVideo.from_dict(post_general_data_post_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


