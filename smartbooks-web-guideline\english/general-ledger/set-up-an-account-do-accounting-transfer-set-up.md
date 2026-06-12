# 1.2 Input

#### 1.2.1    General Journal Entry

The GL module allows users to directly enter general journal entries or other specific accounting transactions.

Data Entry Guide

.       Select **New** to open the data entry window

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

·       Journal Information Section

&#x20;       o   Subsystem: GL (General Ledger)

&#x20;       o   Voucher No: Leave blank; the system will automatically assign a sequential number to the journal entry. (Press F3 to view previously entered entries)

&#x20;       o   PO date: Must fall within the accounting month

&#x20;       o   Period: Select the posting month (for example, posting for June 2015: 062015)

&#x20;       o   Description (VN): Transaction details in Vietnamese

&#x20;       o   Description (EN): Transaction details in English

&#x20;       o   Description (KR): Transaction details in Korean

&#x20;       o   Voucher Status: Hold – temporarily saved; Released – processed and posted to the ledger

&#x20;

·       Posting Section

Users can choose which fields to display, such as Description, Tax, Cost Code, Profit Code, Process Code, etc.

&#x20;       o   Select **New** to open the data entry window

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>

&#x20;       o   Debit: Press F3 to select an account or enter it directly.

&#x20;       o   Credit: Press F3 to select an account or enter it directly

&#x20;       o   Currency: Select the currency type (VND, USD, KOR, etc.).

&#x20;       o   Cury Rate: Enter the posting Cury rate if the currency is other than VND.

&#x20;       o   Amount: Enter the original amount

&#x20;       o   Domestic Amount: The system will automatically calculate this value, or users can input it manually

&#x20;       o   Description (VN), (EN) and (KR): Automatically appears based on the journal information section. Users can modify the detailed description by entering it directly.

&#x20;       o   Employee ID/ Vendor ID/ Customer Code: Users can input or press F3 to select the corresponding code from:

&#x20;             §  Employee List (Cash Management module),

&#x20;             §  Vendor List,

&#x20;             §  Customer List (Accounts Receivable module)

&#x20;       o   Invoice No./ Invoice Date/ Serial No: Enter invoice information (if applicable) so the system can generate the corresponding input or output VAT report.

&#x20;       o   Cost ID/ Profit ID/ JobCenter: Used for internal reporting or cost calculation purposes.

Select **Save** to store the entered information, **Delete** to remove redundant lines, **Copy** to duplicate all details from an existing voucher, and **Process** to change the voucher status to _Released_.



#### 1.2.2    Offset Journal Entry

Used in cases where it is necessary to offset accounts receivable and accounts payable.\
Select New to open the data entry window.\
The Journal Information section and the Data Entry Grid are performed in the same way as for General Journal entries.

Note: It is necessary to enter the Supplier, Customer Code, or Employee information so that the Detailed Account Balance Report reflects accurate figures for each entity

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>
