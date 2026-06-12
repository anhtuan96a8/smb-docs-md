# 1.1 Master Data

#### 1.1.1.    Chart of Account

SmartBooks provides a standard chart of accounts in accordance with Circular No. 200/TT-BTC issued by the Ministry of Finance on December 22, 2014.

In addition, SmartBooks allows users to create additional sub-accounts at level 2, level 3, and so on (up to level 5) based on the predefined main accounts

<figure><img src="../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

**Account Creation Guide**

·       Account Code: Enter the sub-account code. (\*)\
Note: SmartBooks uses a default 7-digit account code format.

·       Account Name (VN): Enter the account name in Vietnamese

·       Account Name (EN): Enter the account name in English.

·       Account Name (KR): Enter the account name in Korean or other languages

·       Account Type: Select the account type according to its nature: Asset, Liability, Income, or Expense

·       Account Group: Select the main account group (first 3 digits)

·       Status: Set the account status as Active or Inactive

Select **Save** to save the newly created account, **New** to create another account, or **Close** to exit the input window.

Delete an Existing Account

·       Select the account line you want to delete

·       Click the **Delete** button

Note: The setup of the chart of accounts directly affects the general ledger, detailed ledgers, and financial statements. Therefore, users should carefully review before deleting any account. If transactions related to the deleted account have already been recorded, it may affect the accuracy of reports.



#### 1.1.2    Account Class

SmartBooks provides a predefined list of level 1 and level 2 account groups in accordance with Circular No. 200/2014/TT-BTC dated December 22, 2014.\
Users may create additional level 1 and level 2 account groups after obtaining approval from the Ministry of Finance

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

**Account Class Creation Guide**

·       ClassID: Enter the code of the level 1 account to be created.

·       Description (VN): Enter the description in Vietnamese.

·       Description (EN): Enter the description in English.

·       Description (KR): Enter the description in Korean.

Select **Save** to save the newly created account class, **New** to create another account class, or **Close** to exit the input window.

&#x20;

#### 1.1.3    Setup Balance Sheet

SmartBooks provides predefined items displayed on the Balance Sheet (BS) in accordance with Circular No. 200/2014/TT-BTC dated December 22, 2014.\
Users can remove unnecessary items from the Balance Sheet by clicking the selection box.

<figure><img src="../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

·       **Step 1**: Set up the following information: Code, Description (VN, EN, KR), Total (using the sum function), and Status (to display or hide the item on the Balance Sheet).

·       **Step 2**: Assign account balances according to the corresponding codes on the Balance Sheet

&#x20;       o   **BalType**: two types (D – Debit balance; C – Credit balance)

&#x20;       o   Account: press F3 to select the account

&#x20;       o   Next Step: ndicates whether the balance on the Balance Sheet is calculated as a negative or positive value

&#x20;       o   Code: the code used on the Balance Sheet

&#x20;       o   **Beginning, Ending**: beginning and ending balances from the most recent Balance Sheet (can be used for data verification)

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

·       **Step 3**: Link the sub Balance Sheet codes to their corresponding higher-level Balance Sheet codes

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

·       **Step 4**: Link the total Balance Sheet codes to the highest-level summary Balance Sheet codes (these codes do not have balances from any accounts).

<figure><img src="../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>



#### 1.1.4    Closing Entry Delararion

This function allows users to set up the automatic closing entry method at the end of the accounting period.

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

**Setup Guide**

·       Account/ To Account: Enter the source account (press F3 to select or enter directly).

·       AmtType: Specify the transfer method for the source account balance (C – transfer the **credit** side, or D – transfer the **debit** side)

·       StepCode: Define the transfer steps (for example, transferring from accounts of type 5, 6, 7, 8 to 911 is step 1, and transferring from 911 to 4212 is step 2).

·       Description.
