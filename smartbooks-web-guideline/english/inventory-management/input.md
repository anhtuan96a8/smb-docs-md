# 6.2 Process

#### 6.2.1    Warehouse process: enter price processing period

Choose Fromdate…Todate

Includes 5 steps

·       Step 1: Release batches

·       Step 2: Input unit price of raw material

·       Step 3: Input unit price of raw material

·       Step 4: Input cost of goods sold

·       Step 5: Post to the general ledger

&#x20;

Release batches

This function is used to release all entries entered in the period in the Input section.

Note: all entries must be released for accurate calculation of production cost and cost of goods sold.

&#x20;

Input unit price of raw material

Raw material issued cost is calculated by two methods:

·       Periodic average method,

·       Raw material movement average method

Press Load to get all the released transactions or Choose to import transactuons directly

<figure><img src="../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

Input unit price of raw material

_Installation finished goods stock in cost:_ This form is used when the company does not wish to use the software for finished goods cost calculation, yet it wishes to track finish goods movement and calculate cost of goods sold by the software.

&#x20;

_Calculate finished goods stock in cost:_ this function is used to calculate inventory production cost in the period. Smartbook integrates 5 methods for inventory production cost, including

·       Phrased method

·       Selling price

·       Coefficient

·       Simple method

·       BOM method

&#x20;

a. Inventory production cost calculated by raw material, labour, and overhead expense norm (BOM).

Applied conditions: the company is capable of establishing norms for the usage of direct raw material, labour and overhead expense.

Operation steps:

Step 1: Declaration for BOM

·       Setup production procedures,

·       Setup usage norms for account 621, 622, 627 comparable to each process,

·       Enter expense account 622, 627 incurred in the period, expense account 621 calculated in the step of setup raw material cost issued for production.

<figure><img src="../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

Step 2: Inventory production cost

Input the beginning balance and closing balance of WIP

<figure><img src="../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

Step 3: Inventory unit cost

This form is used to transfer the mentioned different amount into cost of goods sold account (632)

<figure><img src="../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

Step 4: Costing

·       Following established BOM and quantities of finished goods produced in the period as well as WIP at the end of the period, the software automatically calculates expense account 621,622,627 as required.  &#x20;

·       Comparing actual cost with cost calculated under BOM method.

&#x20;       o   In the event cost calculated under BOM method > actual cost (621, 622, 627), the software will allocate actual cost following optional criteria.

&#x20;       o   In the event cost calculated under BOM method < actual cost (621, 622, 627), inventory production cost must be under BOM method, the different Amount is optional (record in account 154 or transfer in cost of goods sold in the period).

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

Input cost of goods sold

Cost of goods sold calculation is determined by 2 methods:

·       Average by period

·       Average by each output material.

<figure><img src="../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

Post to the general ledger

Alll the transaction in the Inventory module in the particular period, which haved calculated, will be input in the GL.

<figure><img src="../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

#### 6.2.2    Released batches

It is the first step in the COGS or selling price calculation.

This form is separated in case the users do not need to use COGS calculation, only change the voucher status and record them into GL

<figure><img src="../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>
