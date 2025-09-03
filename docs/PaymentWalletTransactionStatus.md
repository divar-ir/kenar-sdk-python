# PaymentWalletTransactionStatus

Represents the various states a wallet transaction can be in during its lifecycle. UNKNOWN: Default/uninitialized status - should not be used in normal operation. CREATED: Transaction has been created and is awaiting payment or further processing. EXPIRED: Transaction was created but expired before completion (e.g., payment timeout). PAID: Transaction has been paid/funded and is still pending final confirmation. COMMITTED: Transaction has been successfully committed and finalized in the system.

## Enum

* `CREATED` (value: `'CREATED'`)

* `EXPIRED` (value: `'EXPIRED'`)

* `PAID` (value: `'PAID'`)

* `COMMITTED` (value: `'COMMITTED'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


