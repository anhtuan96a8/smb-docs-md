# 2.2 Input section

**Vendor’s Voucher**

**-** Vouchers that require tracking stocks movement are entered in Inventory management when these vouchers are processed they will be linked to account payable module.

\- Payable vouchers obtained from using material, supplies and other services expenses (such as electricity, water, telephone, office rental,): These vouchers are entered in Account payable module.

![](<../.gitbook/assets/0 (159).png>)

Details in the voucher process procedure from vendors

Data input form contains two parts:

**General area**: General information of vouchers and normally positioned in upper part.

*
  * Batch no.: Leave blank, the software will automatically run the sequential order number.
  * Accounting period:(for example Voucher in July 2015 is presented as: 07-2015) Voucher arises in Month
  * Voucher no.: Key in voucher number.
  * Voucher date: must be within the accounting period.
  * Voucher type: select Voucher.
  * Vendor: Press F3 to select the Vendor.
  * Description (VN - EN): Key in description
  * Purchase order number: (input any PO number)
  * Payment date: Auto fill based on payment term .
  * Payment term: Press F3 to select.
  * AP account: Press F3 to select.

**Detail area:** refers to the detail information of vouchers, each particular is a line within the grid

*
  * Account: Press F3 and select expense account
  * Advance payment: If any advance payment was made for this purchase order in foreign currency, user must select the advance note to get the foreign exchange rate at the advance date as well as the advanced Amount. The remaining Amount is recorded following selling rate prevailed on the payable date
  * Currency Type: Select currency type used for payment
  * Conversion rate: Key in the exchange rate of the Currency against VND
* For example: For USD, the exchange rate on voucher date is 21500: key in 21500
* For VND: exchange rate is 1
  * Amount: Input amount before tax or foreign Amount
  * Converted Amount: Is the Amount after multiplied by exchange rate
  * Tax rate: Hit F3 key to select a comparable tax rate.
  * Tax amount should be actually incurred tax amount. The converted tax amount is the Amount after multiplied by the exchange rate (if any).
  * Description (VN - EN): will be automatically retrieved from description inputted in the general area.
  * Input voucher number
  * Input voucher date

**Other buttons : if have permission**

![](<../.gitbook/assets/1 (91).png>)

*
  * Previous: Previous Voucher
  * Next: Next Voucher
  * Un-release: Change voucher status from Posted to Hold (this function only apply with users have access right)
  * Vendor: In case have no Vendor code. User can register directly (no need back to Vendor List form)

![](<../.gitbook/assets/2 (61).png>)
