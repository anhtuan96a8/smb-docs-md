# 1.1 Setup section

### 1.GENERAL LEDGER MODULE

General ledger (abbreviated as GL) is the main module in any bookkeeping record in this software. All the transactions that user input in the system in terms of cash receivable, cash payable, fixed assets, inventories are posted into the ledger (recorded as a tracking journal). From this program, the user may set up, input account information, posting journal entry and Export financial statements.

GL module includes 5 categories: Setup, Input, Process, All Journal Entry Detail and Report.

### 1.1 Setup Section

Includes 4 items:

#### a) Chart of Account

Smartbook software provides an available main chart of Account regulated under circular no—200/TT-BTC issued by the Ministry of Finance on 22/12/201&#x34;**.**

Smartbook also let user’s setup additional sub-account level 2, level 3… (maximum is level 5) based on the main chart of Account.

![](<../.gitbook/assets/0 (24).png>)

**Note**: Smartbook’s default account code is in 7 digits.

How to create new Account:

* Account name (VN): Input account description in Vietnamese.
* Account name (EN): Input account description in English.
* Account name (KR): Input account description in Korean or other languages (Chinese, Japanese, Cambodian …)
* Account type: Select account type under characteristic: Asset, Liability\&Equite, Income, and Expense.
* Account group: Select the main account group (Account’s first 3 digits)
* Status: setup Account status: Active, Inactive
* Click Save to record the new Account.
* Click New to add another new account.
* Click Close to finish adding Account.
* To delete Account:

&#x20;\+ Click on the Account needed to be removed

&#x20;\+ Hit Delete button.

**Note:** Setting up a chart of Account may have a direct influence on General journal, ledgers and financial statements. Hence users need to consider carefully before deleting any account. This refers to cases where transactions arise related to the removed Account leading to the inaccuracy of reports.

#### b) List of account group:

Smartbook provides an available list of account groups level 1 and level 2 under circular no.200/2014/TT-BTC on 22/12/2014.

User may add more account groups level 1 and level 2 after being approved by the Ministry of Finance.

![](<../.gitbook/assets/1 (10).png>)

Adding account group:

* Group code: Enter account code level 1.
* Group name (VN): Description in Vietnamese.
* Group name (EN): Description in English.
* Group name (KR): Description in Korean or other languages (Chinese, Japanese, Cambodian …)
* Click Save to record the new Account.
* Click New to add another new account.
* Click Close to finish.

#### c) Setting up the Balance Sheet:

Smartbook setups available all items shown on the Balance sheet under circular 200/2014/TT-BTC on 22/12/2014.

User may remove unnecessary items on the Balance sheet by ticking into checkbox.

* **Step 1**: setup information: code, description (VN, EN, KR or other languages (Chinese, Japanese, Cambodian …), IsTotal (is the total code), InActive (let Account shown in the Balance sheet or not).

![](<../.gitbook/assets/2 (12).png>)

**Step 2**: Indicate accounts’ balance following codes presented on the Balance sheet

* Bal Type: there are two types

\+ D: Balance on Debit side

\+ C: Balance on the Credit side

* Acct: hit the F3 key to choose accounts
* AmtType: balances presented on the Balance sheet may in - or +
* Code: The Balance sheet’s code
* BegAmt, EndAmt: opening balance, closing balance of the last view on the Balance sheet (may use to check figures).

![](<../.gitbook/assets/3 (3).png>)

**Step 3**: Setup subordinate Codes on the Balance sheet for the higher-level codes

![](<../.gitbook/assets/4 (8).png>)

**Step 4**: Setup total Codes on the Balance sheet over grand total Codes (these codes must have a null balance)

![](<../.gitbook/assets/5 (14).png>)

#### d) The affirmation on entries transferring ending account balance:

These function support users in setting up entries that automatically transfer account balance at the end of the period.

![](<../.gitbook/assets/6 (8).png>)

Setup instruction:

\- Acct: Input source account (Hit F3 key and choose accounts or directly key in Account)

\- AmtType: Balance transferred method of source account

\+ C: record Credit for source account

\+ D: record Debit for source account

\- Step Code: transferring steps (for example for account type 5, 6, 7, 8 transfer into account 911 is the first transferring step and from account 911 transfer into account 4212 is the second transferring step).
