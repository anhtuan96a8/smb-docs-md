# 7.1 BOM

Select method from Company Information

<figure><img src="../.gitbook/assets/image (136).png" alt=""><figcaption></figcaption></figure>

## BOM

### **Steps of Costing calculation under BOM**

<figure><img src="../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/BTS-L92GXGtMLtJVobx6Uy_CxLHqgLzAVGZrQbcqICS-BZSQlfNG1ofKDF7XwXWwVmrYUUjyEPs7SVwgCF56UL2cXxCliLomZdUAtZmkubnBEOcM8ZL6qtnS-D8-ssOIiWHrLMofDQ-hLtfwoKrC57fkALicDug4" alt=""><figcaption></figcaption></figure>

### Step 1: Setting up the norms table for each product

What are the marterials making the A product?, How much quantity of each material do a product needed to make?).

Each product can use from 1 -> 100 materials (Can be customized if the number of materials is more than 100). Materials can set up according to kg, pcs , metre, bottles ( depending on each type of product )

In this step, when setting up on smart book will create the registration section for norm of each product and create Excel file to import in cases where the company has a lot of the product code .

Check the figure below for details

For example: 1 product needs to use 4 main material and the norm of each type of material is detailed in kg.

| FGCode     | Material code           | Norms/Quota kg |
| ---------- | ----------------------- | -------------- |
| NIBA-07-CT | 7W LED PCB              | 0.570          |
| NIBA-07-CT | LED E27 CAP             | 0.758          |
| NIBA-07-CT | LED BULB A60 HOUSING 7W | 0.852          |
| NIBA-07-CT | LED DRIVER 7W           | 0.570          |

&#x20;![](<../.gitbook/assets/image (81).png>)

<figure><img src="https://lh7-us.googleusercontent.com/NHBr3ernKDhBhN0LjBSpTWzqgcIE_dWYe7ujT_pRtVIexCW2d7FAzg2Lgp4sd3tF855eyK1P1PeDps8QqXKq0qtbXbcX-EuXXQH2PW0mU-_3vZYNSdqsHU6hODXojbxQ_FyJurux64iauVTohvw_tCN_gtPmW7nP" alt=""><figcaption></figcaption></figure>

### Step 2: Summary of finished goods (FG) import to the warehouse during the period

In this step, input the data into the SB on the finished goods import voucher.

<figure><img src="../.gitbook/assets/image (82).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/yJtc34-kPL6mG3BJMyjIk0zh-IYk1b6O5hjOafQX2kVLy1_m0Y9YNl6C8SpY_genwNPr1x231tLP9yCadOh--O8qQ54Y7ih8ERlmewxsuALlgTgoYvZEdmv7Lo_pBZkLy2h6FDIBBbmkTkvctBN5IIFtFJoqHSLU" alt=""><figcaption></figcaption></figure>

### Step 3: Summary of work-in- progress (WIP) and convert to finished goods

The software will create a separate section for importing unfinished goods and completion rate and set up the formula to converted from unfinished goods into equivalent finished goods.

Note: A product can have many completion rates. Because, it can be at the beginning, middle or ending stage of manufacturing process.

For example :

| Code     | Name                         | WIP qty (a) | Ratio (b) | FG equivalent (c =a\*b) |
| -------- | ---------------------------- | ----------- | --------- | ----------------------- |
| DUOI DEN | Plastic lamp holder (NLH100) |       250   | 65%       |       162.50            |
| DUOI DEN | Plastic lamp holder (NLH100) |       150   | 80%       |       120.00            |
| DUOI DEN | Plastic lamp holder (NLH100) |       6,816 | 50%       |       3,408.00          |
| DUOI DEN | Plastic lamp holder (NLH100) |       538   | 70%       |       376.60            |
| DUOI DEN | Plastic lamp holder (NLH100) |       9,346 | 35%       |       3,271.10          |

<br>

After calculating the equivalent products with different unfinished rates, the software will sum up each of product code which converted to the equivalent product. As in the above example, after calculating WIP with different percentages, the total of equivalent FG of this code will be shown as follows: &#x20;

| Code     | Name                         | WIP qty a | Ratio | FG equivalent      |
| -------- | ---------------------------- | --------- | ----- | ------------------ |
| DUOI DEN | Plastic lamp holder (NLH100) | 17,100.00 |       |           7,338.20 |

&#x20;

Each WIP code is assembled into each line and show the total of final equivalent converted FG, because the result of this step will be used to calculate the value of WIP in Step 9.&#x20;

<figure><img src="../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/jCDrMEWcszazXw9jjF_PRT6psgFb30GG8q3Pm-9yK_i_9b-47I7ChUbwlv6ote9zzdopy8X7OjxoOZ295QfJStxC_fUdAX69d2B5euyASkebI0C86Nnz2VZFY6IndUeXWzEkM3plI1tVm0PSbYGHtGHNNf4YkCVp" alt=""><figcaption></figcaption></figure>

### Step 4 : Calculate the number of products manufacturing during the period

There is always a logic in the manufacturing as follows :

WIP at the beginning of the period + the product manufacturing during the period -> manufacturing -> FG + WIP at the ending of the period.

Therefore , the formula of the manufacturing process:

WIP at the beginning of the period + the product manufacturing during the period = FG + WIP at the ending of the period.&#x20;

Then, knowing the 3 factors of this equation will calculate the remaining factors. And here, 3 values are always defined as:

1\. Quantity of WIP at the beginning the period (from the previous the period forward),

2\. FG manufactured during the period and

3\. WIP at the end of the period (provided by the customer's inventory)

🡺 Products manufactured during the period = FG + WIP at the ending of the period – WIP at the beginning of the period

On the SB will be setup to calculate the amount of manufactured products

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/0rqAwovnT984B4k4DIe9FxVnim1z5KA8MmSdflhcYjpwX7Wu5U2kTNbQbwXnHDQ0umDL01EuWYBVK-aAsfqyP283txlF0lprz68dqR3of4QOrh9Lm4JCqww3HvfpaFtMhQDy2dLylrDv-G4RWpBmR8plhlurhHA0" alt=""><figcaption></figcaption></figure>

### Step 5: Calculate the amount of material according to the BOM for the number of manufactured products

At this step, SB will setup the formula to calculate the number of material according to norms (already set up in Step 1) for the products manufacturing during the period ( already calculated in Step 4)

| FGCode     | RMCode                  | Norms kg (a) | Qty products (b) | Material used by BOM (c)=(a)\*(b) |
| ---------- | ----------------------- | ------------ | ---------------- | --------------------------------- |
| NIBA-07-CT | 7W LED PCB              | 0.570        |       58,315     |     33.230                        |
| NIBA-07-CT | LED E27 CAP             | 0.758        |       58,315     |     44.225                        |
| NIBA-07-CT | LED BULB A60 HOUSING 7W | 0.852        |       58,315     |     49,697                        |
| NIBA-07-CT | LED DRIVER 7W           | 0.570        |       58,315     |     33.230                        |
| NIBA-07-WT | 7W LED PCB              | 1,000 yen    |       26,366     |     26,366                        |
| NIBA-07-WT | LED E27 CAP             | 1,000 yen    |       26,366     |     26,366                        |
| NIBA-07-WT | LED BULB A60 HOUSING 7W | 1,000 yen    |       26,366     |     26,366                        |
| NIBA-07-WT | LED DRIVER 7W           | 1,000 yen    |       26,366     |     26,366                        |

&#x20;

Note: A product will use many materials for manufacturing so the formula will set up to fully calculate all the materials codes which are used to manufacture a finished goods code.

### Step 6: Summary of output materials in practice by product code

This step is quite similar to the step of setting up materials for each specific product code, because this data is the actual output materials of customer.

SB should have an import form because with many finished goods, it will not be possible to input manually.

| RMCode                  | Output material in practice  |
| ----------------------- | ---------------------------- |
| 7W LED PCB              |               34,918.19      |
| LED E27 CAP             |               45,909.50      |
| LED BULB A60 HOUSING 7W |               51,385.13      |

&#x20;![](<../.gitbook/assets/image (86).png>)

<figure><img src="https://lh7-us.googleusercontent.com/c1Y90kulZwGjouwcefDV_4fFYGh1dhN1uG5YXm9JrhDUjU1k--M-LMq_RyQYSXx5ZDAAD-99lXjkTfTatwmEtmIlMu4sCabTWF5MbmjLC4O5LjJ8UcFJA1coY7M9JHv1CcK0eVTXKnBrt8dymylDyn9GF82D5KPf" alt=""><figcaption></figcaption></figure>

### Step 7: Compare the difference between the output materials in actual and the norm of materials&#x20;

After obtaining the quantity of output material in actual and output warehouse according to the norm. This step needs to determine the difference in the quantity of materials between the actual and norm.

In fact, there is always a difference between the actual quantity of output material and the material built on the norm.

#### Case 1: output material in actual > material according to the norm.

In terms of accounting regulations: in case the output materials in actual > the output materials according to BOM. The difference will be recorded in the cost of goods sold

For example: Actual output materials is 100, norm is 75. The difference of 25 will be recorded directly in cost of goods sold (Account No. 632)

The accouting entry on SB when output materials for this case as follows:

1 / The output materials according to norms:

Debit 621 / Credit 152: 100

2 / Materials that SB calculate according to BOM: 75

3 / Transfer material to calculate the costing

Debit 154: 75

Debit 632: 25

Credit 621: 100

#### Case 2: Output material in actual < the norms

In addition, in case of the output material in actual is smaller than the material norm, in this case the accountant can go back to step 1 to adjust the material norm for each product.

Therefore, SB needs to set up 2 formulas to handle these 2 cases. Because there will be output material > material norm and output material < material norm in some material codes.

🡺Check the excel file for details&#x20;

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/z6cTrVU5xSLQS4diLIrHNxlMpzFNUHP9QTzXOu-dlk2PDgfCwtoetZEMKvJ3WdbroPpyBJO7PoQDo_EKvJPTYKy-lMkAt4CFL_tHrYTQ4KL0hnrJ7elzFv0aPw6nt-HcMWkdfBV8chZ0S2LSC_PGnstM4TC1-Z0k" alt=""><figcaption></figcaption></figure>

### Step 8: Determine the number of materials to calculate the costing&#x20;

After completing step 7, the amount of materials to calculate cost of goods manufactured will be the actual or norm materials depending on each materials code.&#x20;

### Step 9 : Calculate cost for each product

This step will allocate the labor cost and overheads cost to each product according to the cost of material. The labor cost and overheads cost are collected and uploaded in the costing section as the table below:

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/war31YTlWBTIZ9bCxL8dwkjwFdb389nSkl57UPC9MTF5UuoGrFxBzxeH5Kjv-FBj-SnL5Jv5qWxGSF6HZ3xMW4-9s3zqDFh73R-ICSoYz9u9N-X2mo73coxezMGeTW1SyRao4yEZxNidIL9Mifyp5Ki-w4DX53OS" alt=""><figcaption></figcaption></figure>

Note: the formula to calculate unit cost for each product code ( final column\_unit cost )

When calculating the unit cost for 1 product, it will average for the whole WIP at the beginning of the period.

The reason: the WIP at the beginning of the period is still manufacture this the period. Averaging will make the unit cost of the product less fluctuated.

When setting up on SB, the IT team should note this formula.

<figure><img src="https://lh7-us.googleusercontent.com/p2hKUv5QG9TXw6Lk9YnG1Fc5i-_UyGqTcPP4Cd_TeXALo_6Dlqu7KLRRTemkrrraP-oys2hsEQPtSUQtSoIh_h6SsE3FD9g6O_McwO9lg1u-bKCGy18Sq48BSFyY6Ne8VEJo_-alHQMOczN5UogLyzRclYMCa0LE" alt=""><figcaption></figcaption></figure>

### Step 10: Calculate the value of WIP at the ending of the period

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/a9eARm4v2vIaIoFHAzFT3j7gAP8u-Nk6ftd6kY2wXNZfz8Tdlf_R742BWir9g65pia5vX88dW14i_aE5bZ47a9hqquySazfsyko3tBSh29dRb1XoMLWldhDCJ29FRBLseKo6s0NeuF113emILrReN-JzIcuTnNjZ" alt=""><figcaption></figcaption></figure>

The value of WIP at the ending of the period is calculated according to the formula:

The equivalent FG \* unit cost

The equivalent FG are determined at step 3, the unit cost is determined at step 9

### Step 11: Determine the value of FG input during the period

<figure><img src="../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/d-azR4IYi_kf4VTqyVcWNDOUtXz6uN9kfltSDAdvMkYHl8QsKHNdeVhA9tSxt4eqa1FZI5hZjL0ihbVO2IDZ5dE15NgZEFn1DuRjWVCgkZECBEbVtVBa0XJ18d7VvisH8-HsMsKp71osj-BOIwlf5kbNNak4zaDB" alt=""><figcaption></figcaption></figure>

At this step, the manufacturing equilibrium equation is used to determine the value of finished goods input warehouse during the period .

The value of FG input during the period = Value of WIP at the beginning of the period + incurred manufacturing costs during the period - Value WIP at the ending of the period

After calculating the value of input warehouse product-> determining the unit cost of products = total value of input product / total quantity of input finished products (determined at step 2)&#x20;

<figure><img src="../.gitbook/assets/image (91).png" alt=""><figcaption></figcaption></figure>
