# 1.2 Input section

#### a) General journal entry

GL module let users input Journal Ledger or other particular transaction directly.

Data input instruction:

_Transaction details part:_

* Module: GL (General Ledger)
* Batch no.: Leave blank, the program will automatically run the entry’s sequential order number. (Hit F3 key to review inputted entries)
* Voucher date: must be in the accounting month
* Voucher no.: the program automatically run sequential order number
* Status: Always keep hold status
* Accounting month: Choose bookkeeping month

(For example, record in June 2015 is present as 06-2015)

* Description (VN): Transaction details in Vietnamese
* Description (EN): Transaction details in English
* Description (KR): Transaction details in Korean or other languages (Chinese, Japanese, Cambodian …)

![](<../.gitbook/assets/0 (111).png>)

_**Transaction entry part:**_

Users may choose data value required to be displayed: Description, tax, cost centres, profit centres, group.

* Debit account: Hit the F3 key to select account or input directly system will auto-completed
* Credit account: Hit F3 key to select account or input directly system will auto-completed
* Currency unit: Choose currency type (VNĐ, USD, KOR…)
* Foreign exchange rate: Input accounting foreign exchange rate for currencies other than VNĐ.
* Amount: Input amount in VND or foreign Amount for currencies other than VND
* Converted Amount: matching with Amount in VND or equal to foreign Amount multiplied by foreign exchange rate. The software automatically calculates.
* Description (VN), (EN) and (KR or other languages: Chinese, Japanese, Cambodian …) Automatically appear following the description key in transaction details part. Users may alter description detail by directly type in.
* Employee code, supplier code, customer code: User hit F3 key to select or input directly system will auto-completed, corresponding codes being set up in:

\+ Employee list (Cash management module)

\+ Supplier list (Account payable)

\+ Customer list (Account receivable)

#### b) Offset account payable against Account receivable

To be used in the case where the user wishes to offset Account payable against Account receivable

![](<../.gitbook/assets/1 (76).png>)
