# PaymentWalletTransactionStatus

وضعیت‌های مختلفی که یک تراکنش کیف پول می‌تواند در طول چرخه حیات خود داشته باشد. UNKNOWN: وضعیت پیش‌فرض/مقداردهی اولیه نشده - نباید در عملیات عادی استفاده شود. CREATED: تراکنش ایجاد شده و در انتظار پرداخت یا پردازش بیشتر است. EXPIRED: تراکنش ایجاد شد اما قبل از تکمیل منقضی شد (مثل timeout پرداخت). PAID: تراکنش پرداخت/تامین مالی شده و هنوز در انتظار تایید نهایی است. COMMITTED: تراکنش با موفقیت commit و نهایی شده در سیستم.

## Enum

* `CREATED` (value: `'CREATED'`)

* `EXPIRED` (value: `'EXPIRED'`)

* `PAID` (value: `'PAID'`)

* `COMMITTED` (value: `'COMMITTED'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


