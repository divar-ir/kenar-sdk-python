# ProtobufAny

`Any` شامل یک پیام protocol buffer سریالایز شده دلخواه همراه با URL که نوع پیام سریالایز شده را توضیح می‌دهد.  کتابخانه Protobuf پشتیبانی برای pack/unpack مقادیر Any را به شکل توابع کاربردی یا متدهای اضافی تولید شده نوع Any ارائه می‌دهد.  مثال 1: Pack و unpack پیام در C++.      Foo foo = ...;     Any any;     any.PackFrom(foo);     ...     if (any.UnpackTo(&foo)) {       ...     }  مثال 2: Pack و unpack پیام در Java.      Foo foo = ...;     Any any = Any.pack(foo);     ...     if (any.is(Foo.class)) {       foo = any.unpack(Foo.class);     }  مثال 3: Pack و unpack پیام در Python.      foo = Foo(...)     any = Any()     any.Pack(foo)     ...     if any.Is(Foo.DESCRIPTOR):       any.Unpack(foo)       ...  مثال 4: Pack و unpack پیام در Go       foo := &pb.Foo{...}      any, err := anypb.New(foo)      if err != nil {        ...      }      ...      foo := &pb.Foo{}      if err := any.UnmarshalTo(foo); err != nil {        ...      }  متدهای pack ارائه شده توسط کتابخانه protobuf به طور پیش‌فرض از 'type.googleapis.com/full.type.name' به عنوان URL نوع استفاده می‌کنند و متدهای unpack فقط از نام نوع کاملاً واجد شرایط پس از آخرین '/' در URL نوع استفاده می‌کنند، مثلاً \"foo.bar.com/x/y.z\" نام نوع \"y.z\" را ایجاد می‌کند.   JSON  نمایش JSON یک مقدار `Any` از نمایش معمولی پیام deserialize شده و جاسازی شده، با یک فیلد اضافی `@type` که شامل URL نوع است، استفاده می‌کند. مثال:      package google.profile;     message Person {       string first_name = 1;       string last_name = 2;     }      {       \"@type\": \"type.googleapis.com/google.profile.Person\",       \"firstName\": <string>,       \"lastName\": <string>     }  اگر نوع پیام جاسازی شده شناخته شده باشد و نمایش JSON سفارشی داشته باشد، آن نمایش با افزودن فیلد `value` که JSON سفارشی را علاوه بر فیلد `@type` نگه می‌دارد، جاسازی می‌شود. مثال (برای پیام [google.protobuf.Duration][]):      {       \"@type\": \"type.googleapis.com/google.protobuf.Duration\",       \"value\": \"1.212s\"     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | یک URL/نام منبع که نوع پیام protocol buffer سریالایز شده را به طور منحصر به فرد شناسایی می‌کند. این رشته باید حداقل یک کاراکتر \&quot;/\&quot; داشته باشد. آخرین بخش مسیر URL باید نام کاملاً واجد شرایط نوع را نمایش دهد (مانند &#x60;path/google.protobuf.Duration&#x60;). نام باید در فرم کانونیکال باشد (مثلاً، \&quot;.\&quot; ابتدایی پذیرفته نیست).  در عمل، تیم‌ها معمولاً تمام انواعی که انتظار دارند در زمینه Any استفاده شود را به صورت پیش‌کامپایل در باینری قرار می‌دهند. با این حال، برای URL هایی که از طرح &#x60;http&#x60;، &#x60;https&#x60; یا بدون طرح استفاده می‌کنند، می‌توان به طور اختیاری یک سرور نوع تنظیم کرد که URL های نوع را به تعاریف پیام نگاشت می‌کند:  * اگر طرحی ارائه نشود، &#x60;https&#x60; فرض می‌شود. * یک HTTP GET روی URL باید مقدار [google.protobuf.Type][] را   به فرمت باینری ارائه دهد، یا خطا تولید کند. * برنامه‌ها مجاز هستند نتایج جستجو را بر اساس   URL کش کنند، یا آنها را در باینری پیش‌کامپایل کنند تا از هر   جستجویی جلوگیری کنند. بنابراین، سازگاری باینری باید در   تغییرات انواع حفظ شود. (از نام‌های نوع نسخه‌دار برای مدیریت   تغییرات شکست‌آور استفاده کنید.)  توجه: این قابلیت در حال حاضر در نسخه رسمی protobuf در دسترس نیست، و برای URL های نوع که با type.googleapis.com شروع می‌شوند استفاده نمی‌شود.  طرح‌های غیر از &#x60;http&#x60;، &#x60;https&#x60; (یا طرح خالی) ممکن است با معناشناسی خاص پیاده‌سازی استفاده شوند. | [optional] 

## Example

```python
from kenar_api_client.models.protobuf_any import ProtobufAny

# TODO update the JSON string below
json = "{}"
# create an instance of ProtobufAny from a JSON string
protobuf_any_instance = ProtobufAny.from_json(json)
# print the JSON string representation of the object
print(ProtobufAny.to_json())

# convert the object into a dict
protobuf_any_dict = protobuf_any_instance.to_dict()
# create an instance of ProtobufAny from a dict
protobuf_any_from_dict = ProtobufAny.from_dict(protobuf_any_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


