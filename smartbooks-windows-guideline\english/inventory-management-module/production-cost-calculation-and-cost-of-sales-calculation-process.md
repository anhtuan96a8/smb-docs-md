# 6.3 Production cost calculation & Cost of sales calculation (Process)

## This section comprises of 5 steps

* **Step 1: Release batches**
* **Step 2: Setup raw material cost issued for production**
* **Step 3: Setup finished goods stock in cost/ Calculate finish goods stock in cost**
* **Step 4: Setup cost of goods sold**
* **Step 5: Posting into the general ledger**

#### a) Release batches

This function is used to release all entries entered in the period in the Input section. Notice: all entries must be released for accurate calculation of production cost and cost of goods sold.

#### b) Setup raw material cost issued for production

Raw material issued cost is calculated by two methods:

\+ Periodic average method,

\+ Raw material movement average method

#### c) Setup finished goods stock in cost/ Calculate finished goods stock in cost

* _Installation finished goods stock in cost_: This form is used when the company does not wish to use the software for finished goods cost calculation, yet it wishes to track finish goods movement and calculate cost of goods sold by the software.
* _Calculate finished goods stock in cost_: this function is used to calculate inventory production cost in the period. Smartbook integrates 5 methods for inventory production cost, including:
* Inventory production cost calculated by raw material, labour, and overhead expense norm (BOM).

Applied in the event: The Company is capable of establishing norms for the usage of direct raw material, labour and overhead expense.

Operation steps:

#### **c-1/ Declaration for BOM**

\- Setup production procedures,

\- Setup usage norms for account 621, 622, 627 comparable to each process,

\- Enter expense account 622, 627 incurred in the period, expense account 621 calculated in the step of setup raw material cost issued for production.

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### **c-2/ Inventory production cost:**

\- Following established BOM and quantities of finished goods produced in the period as well as WIP at the end of the period, the software automatically calculates expense account 621,622,627 as required.

\- Comparing actual cost with cost calculated under BOM method.

&#x20;\+ In the event cost calculated under BOM method > actual cost (621, 622, 627), the software will allocate actual cost following optional criteria.

&#x20;\+ In the event cost calculated under BOM method < actual cost (621, 622, 627), inventory production cost must be under BOM method, the different Amount is optional (record in account 154 or transfer in cost of goods sold in the period).

![](<../.gitbook/assets/1 (89).png>)

#### &#x20;**c-3/ Inventory unit cost**

&#x20;This form is used to transfer the mentioned different Amount into cost of goods sold Account.

![](<../.gitbook/assets/2 (50).png>)

&#x20;Note: Remember to click the update button when finished

#### d) The setup cost of goods sold

Cost of goods sold calculation is determined by 2 methods: Periodic average method and inventory movement average method.

![](<../.gitbook/assets/3 (44).png>)

#### e) Posting into the general ledger

![](<../.gitbook/assets/4 (36).png>)

Final processing: click Post to General Ledger

All transactions in inventory module with the selected period which calculated value would be posted to GL
