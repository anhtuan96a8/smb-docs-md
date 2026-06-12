# 4.2 Input

#### 4.2.1    Cash Payment/ Cash Receipt

Cash management is carried out through the Cash Accounting module. All transactions related to cash within the company are created, recorded, and processed in this module

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure>

Select **New** to open the data entry window.

·       **General Information**

&#x20;       o   Voucher No: Enter the payment voucher number, or the system will automatically generate it in sequential order.

&#x20;       o   PO Date: Enter the transaction date

&#x20;       o   Period: Automatically assigned by the system based on the transaction month

&#x20;       o   Receiver: Press F3 to select from the list.

&#x20;       o   Cash Account: Press F3 to select or enter the corresponding account number

&#x20;       o   Specific Exchange Rate: Select if using the specific exchange rate method.

&#x20;       o   Currency/ Currency ID: Depending on the currency type, the system will apply the corresponding exchange rate to VND

&#x20;       o   AP Voucher: Press F3 to select the invoices to be paid to the vendor

&#x20;       o   Origin Voucher: Enter the original document information (contract, purchase order, etc.).

&#x20;       o   Address/ Reason

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

·       **Detail Information**

&#x20;       o   Account: Press F3 to select or enter the corresponding account number.

&#x20;       o   Description (VN-EN-KR): Automatically linked from the description entered in the general information section.

&#x20;       o   Currency/ Cury Rate: Default values are taken from the general information section.

&#x20;       o   Unit Price/ Domestic Unit Price: Enter the amount; the converted amount is calculated based on the entered exchange rate

&#x20;       o   Tax ID

&#x20;       o   Tax Amount/ Domestic Tax Amount: Enter the tax amount; the converted tax amount is calculated based on the entered exchange rate.

&#x20;       o   Serial No/ Invoice No/ Invoice Date: Enter the invoice information.

&#x20;       o   Employee ID/ Prepayment Voucher: Information related to employee payment vouchers.

&#x20;       o   Vendor ID/ Address/ Tax ID: Automatically retrieved from the vendor list.

&#x20;       o   JobCentor/ Cost ID/ Profit ID

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

In the case of making a payment for a vendor invoice.

·       In the **Payable** field: Press F3 to search for and select the invoices to be paid.

·       You can select one or multiple payable invoices by checking the selection column.

·       Once selected, the invoice data will be automatically entered into the data grid.

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>

The selected invoice information will be displayed in the detailed information grid, including:

·       Account

·       Description

·       Unit Price/ Domestic Unit Price

·       Tax ID/ Tax Amount/ Domestic Tax Amount

·       Invoice Information

·       Vendor Information

<figure><img src="../.gitbook/assets/image (109).png" alt=""><figcaption></figcaption></figure>

#### 1.1.1.    Cash Receipt/ Bank Receipt

Select **New** to open the data entry window.

·       **General Information**

&#x20;       o   Voucher No: Enter the receipt voucher number, or the system will automatically generate it in sequential order.

&#x20;       o   PO Date: Enter the transaction date

&#x20;       o   Period: Automatically assigned by the system based on the transaction month

&#x20;       o   Payer: Press F3 to select from the list

&#x20;       o   Cash Account: Press F3 to select or enter the corresponding account number

&#x20;       o   Currency/Cury Rate: Depending on the currency type, the system will apply the corresponding exchange rate to VND

&#x20;       o   AR Voucher: Press F3 to select the invoices to be collected

&#x20;       o   Origin Voucher: Enter the original document information (contract, purchase order, etc.).

&#x20;       o   Adress/ Reason

<figure><img src="../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

·    **Detail Information**

&#x20;       o   Account: Press F3 to select or enter the corresponding account.

&#x20;       o   Description (VN-EN): Automatically linked from the description entered in the general information section.

&#x20;       o   Currency/ Cury Rate: Default values are taken from the general information section

&#x20;       o   SubToal/ Domestic Amount: Enter the amount; the converted amount is calculated based on the entered exchange rate

&#x20;       o   Tax ID

&#x20;       o   Tax Amount/ Domestic Tax Amount: Enter the tax amount; the converted tax amount is calculated based on the entered exchange rate

&#x20;       o   Serial No/ Invoice No/ Invoice date: Enter invoice information

&#x20;       o   Employee ID/ Phiếu phải thu: Information on the employee receipt voucher

&#x20;       o   Customer Code ID/ Address/ Tax ID: Automatically retrieved from the customer list.

&#x20;       o   Job Center/ Cost ID/ Profit ID

<figure><img src="../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

Similar to the **Payment Voucher**, in the case of collecting payments from customer invoices:

·       In the **Receivable** field: Press F3 to search for and select the invoices to be collected

·       You can select one or multiple invoices by checking the selection column.

·       Once selected, the invoice data will be automatically entered into the data grid

&#x20;

**Note**

When entering expenses with input VAT or recording cash revenue with output VAT, two lines should be entered in the detail section:

·       **Line 1:** Enter the transaction amount excluding VAT

·       **Line 2:** Enter the corresponding VAT — input tax (133) or output tax (333). The VAT amount must be manually calculated and entered by the user



#### 4.2.3   Voucher Released

This function is used to lock recorded cash receipt and payment entries and post them to the ledger.\
The procedure is the same as in the Accounts Receivable and Accounts Payable modules.

·       **Released** a single voucher

&#x20;       o   Select the voucher to be **Released** from the voucher list

&#x20;       o   Click **Released**

·       **Released** multiple vouchers

&#x20;       o   In the voucher list, filter vouchers that have not yet been **Released** (status: _Hold_)

&#x20;       o   Select the vouchers to be **Released**

&#x20;       o   Click **Released**

<figure><img src="../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>
