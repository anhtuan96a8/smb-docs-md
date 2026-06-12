# 7.2 Simple Method

## SIMPLE METHOD

Steps of Costing calculation under Simple method

This is the simplest method of costing calculation methods, and currently very few businesses use this method.

<figure><img src="../.gitbook/assets/image (93).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/VPYD-29nkJIiKs04oV2tzNA0wg0NQcQzv_1OvHZs_0L1HdCUWlrCbvlttBuRkBYNP5K8vVvqa_iN7ljfNyjtj2Xrfga2P4FJYBWB4TObOLFMNB72VsHSTotC5yv_s50B3D8Ix2DdfOfy-dDP7Du0_2bpAIz6lgHN" alt=""><figcaption></figcaption></figure>

### Step 1: Summary of FG manufactoring during the period (same as BOM)

In this step , just input the data into the SB on the FG warehouse receipt

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/ZIZh-TgBSg-qMNP6Zf8_X7wKqNIO2wO_zd5Dw_i4lYkHi3V-9IqK7uV4f-d5kBYUQwewtnNI_m-t0-xTrS_F4BtQ6SvhpQCL9OAis25RrNT2N3D_taH404xgnSXt6B0vMeGH-XR-i1bfeX-GI7Ovq5SwpjtxgrEp" alt=""><figcaption></figcaption></figure>

### Step 2: Summary of WIP and convert to FG (same as BOM)

The software will create a separate section for importing WIP and completion rate. At the same time, set up the formula to converted from WIP into equivalent FG.

Note: A product can have many completion rates. Because, it can be at the beginning, middle or ending stage of manufacturing process.

For example:

| Code     | Name                         | WIP qty (a) | Ratio (b) | FG equivalent  (c =a\*b) |
| -------- | ---------------------------- | ----------- | --------- | ------------------------ |
| DUOI DEN | Plastic lamp holder (NLH100) | 250         | 65%       | 162.50                   |
| DUOI DEN | Plastic lamp holder (NLH100) | 150         | 80%       | 120.00                   |
| DUOI DEN | Plastic lamp holder (NLH100) | 6,816       | 50%       | 3,408.00                 |
| DUOI DEN | Plastic lamp holder (NLH100) | 538         | 70%       | 376.60                   |
| DUOI DEN | Plastic lamp holder (NLH100) | 9,346       | 35%       | 3,271.10                 |

After calculating the equivalent products with different completion rates, the software will sum up each of product code which converted to the equivalent product. As in the above example, after calculating WIP with different percentages, the total of equivalent FG of this code will be shown as follows :&#x20;

| Code     | Name                         | WIP qty a | Ratio | FG equivalent |
| -------- | ---------------------------- | --------- | ----- | ------------- |
| DUOI DEN | Plastic lamp holder (NLH100) | 17,100.00 |       | 7,338.20      |

Each WIP code is assembled into each line and show the total of final equivalent converted product, because the result of this step will use to calculate the value of WIP in next step.

<figure><img src="../.gitbook/assets/image (95).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/ZhlqsXQDJUS-Cq_OuUWdIyBbai8bQQwP0Cza4kXwRpxFWp4y6eYWEzUM40x38mCTxH_MCrKc-x76W_1YOydZQTeMX6ljCc_fVOhpcBHhCZ65pw4ULLl4trP1JwDa4jGwGkisr6-7DOgkfuTCw12NCmdP7pRVJf20" alt=""><figcaption></figcaption></figure>

### Step 3 : Calculate the number of products manufacturing during the period

There is always a logic in the manufacturing as follows :

WIP at the beginning of the period + the product manufacturing during the period -> manufacturing -> FG + WIP at the ending of the period.

Therefore , the formula of the manufacturing process:

WIP at the beginning of the period + the product manufacturing during the period = FG + WIP at the ending of the period.&#x20;

Therefore, knowing the 3 factors of this equation will calculate the remaining factors. And 3 values are always defined as:

1\. Quantity of WIP at the beginning of the period (from the previous the period forward),

2\. FG manufactured during the period, and

3\. WIP at the ending of the period (provided by the customer's inventory)

🡺 Products manufactured during the period = FG + WIP at the ending of the period – WIP at the beginning of the period

On the SB will be setup to calculate the amount of these products

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/LC1Jju31Te9SV62Ir7EAw-qDCg_QzZ_8yTz4QU3pqB-QREmRwXh9HJ8YjX9iOAuHhlxUpnJMPQZP2z_8E6kYEhbO5MJ-ScxbdoYQ71R5JrySiUGtAmLjtrrK7xo5s7EI3GTR8QfrrsRdeQiOrXcPQR3oautwnI7v" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (97).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/Q8nwDpFwx9b_CHGZsJQJHHXmjV_yqyMjllHtNwaK1kEEb0Uyyy6iCjdnrqEt9Q7NY-z0q_ooVgplWJXTb8d1-Z81jLNbokwMKT5aNa2k5CASjLVz5b4Sz5bDg-IDKTvLTlt8CP82C8a50RMogtuZKoy5ChaLwZMQ" alt=""><figcaption></figcaption></figure>

### Step 4 : Calculate the costing for products&#x20;

This step is the allocation of direct material costs, labor costs and manufacturing overhead costs to each product according to the total of products which manufactured.

<figure><img src="../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/HBQWik_B24FO5OBlqTnIvmWjVGgnFbnW5ytjzHeImcsdflVETL7yumNAMdPOuyVafM3rRedCMXzCm9-9uQn_7V_3AzlkZh6mGldcVdgP48oy9gItEgkYt2dmwY9IDoQP7R4F9zJjMS8jMD6_KOkieuBocpbV3QlI" alt=""><figcaption></figcaption></figure>

This step is simply taking the total expenses divided the total product and multiplied the number of products of each type.

### Step 5: Calculate the value of WIP at the ending of the period

The value of WIP at the ending of the period is calculated according to the formula:

The equivalent FG \* unit cost

The equivalent FG are determined at step 2, the unit cost is determined at step 4

<figure><img src="../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/J1p6Hwk8eMj25BZcw5PQ5JTeptFhiIq_BkwCJUolFEcoCQWMWvU9DW3xf_7tCp77FpORbKeiCSZxPX16YeQEoK61c8jpOthmp1a62KQ4aEXAt51nRFBmbOZw17CRyiz-kjWYIMotIxgEzTeudY84CJ3-OcMMX55G" alt=""><figcaption></figcaption></figure>

### Step 6: Determine the value of FG input during the period

At this step, the manufacturing equilibrium equation is used to determine the value of FG input during the period .

The value of FG input during the period = Value of WIP at the beginning of the period + incurred manufacturing costs during the period – Value of WIP at the ending of the period

After calculating the value of input product-> determining the unit cost of products = total value of input product / total quantity of input finished products (determined at step 1 )

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>
