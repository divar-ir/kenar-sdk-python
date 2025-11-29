# PostGeneralDataPostVideo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | زمان ویدیو به ثانیه | 
**name** | **str** | Name of the video, retrieved from &#x60;video_name&#x60; field in the response of upload video endpoint | 
**thumbnail_name** | **str** | کاور ویدیو. این مقدار را از روی فیلد &#x60;thumbnail_name&#x60; در پاسخ به درخواست آپلود ویدیو پر کنید. این تصویر، فریم اول ویدیو‌ی آپلود شده است. | 

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


