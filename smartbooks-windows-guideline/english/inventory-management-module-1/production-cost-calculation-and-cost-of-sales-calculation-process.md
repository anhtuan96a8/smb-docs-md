# 7.3 Coefficient

## COEFFICIENT

**Steps of Costing calculation under Coefficient Method**

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/U_XmtlpyI5LWAmpkdflgsw5v0Lssz_U4bIx-CIiOtGBr3v-uo4OmSUaZ_lfWxg5-yiy7RLL1IPmsm2BrTcT1nwtiFWKZkk-IOuf4N0wvud9nBbIC8lHkpUXADEv_Ky-67Q4HfmrTEik7a1GZx9P-1Fa-fr8MV25o" alt=""><figcaption></figcaption></figure>

### Step 1: Choose 1 product as a standard product

The coefficient method will be applied to enterprises that is only manufacturing of identical products, only size different . For example: the enterprise manufactures glass of bottles and jars. There are many sizes such as 1litle (1l), 0.5 litle (0.5l), 250ml…....

At that time, it is necessary to choose a product as a standard product to convert other products. For example, in the above case, a glass bottle with size 1l will be selected as the standard product.

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption></figcaption></figure>

At this step, SB needs to set up an initial product coefficient declaration table for users to declare on the software. Should have the form.

<figure><img src="../.gitbook/assets/image (103).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/SSyV9aUfx3mOYl8IFRdylOQ9E_Jv0ZXah26MBc5jlM4TDvtXqGiQbSgAhsBSgeEq50cnxkOYvoNjntBA_DBeXUEB3tVuHQK3uxHpuC2JkMb4e6vRVebzc0YswHNC5_ryrTD9dUGHxducXV3jORTtXCJobLexIuzS" alt=""><figcaption></figcaption></figure>

### Step 2: Total quantity of finished goods manufacturing during the period (same as BOM)

At this step, data is only entered into SB through finished goods import vouchers

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/RyopTmIYJC4VPQUe9XMk5l6aVMYt1BRdHTpP7C0dTo_0mI-Xuea9sz4HXWogBDwtYidTFXI01cIIaLeDxaelBBumxJkgFIiJD9KXl8vJbjYiIeJwRRm_Ut3iVT85mzmfxASBPmG5tH92MuOvgXYy8GI4Ql-DXgn1" alt=""><figcaption></figcaption></figure>

### Step 3: The total of unfinished goods and convert to finished products (same as BOM)

The software will create a separate section related to enter unfinished goods and completion rate. At the same time, It sets up the formula to convert from unfinished goods into equivalent finished goods.

Noted: A product can have many unfinished ratio. Because, it can be at the beginning, middle or ending of manufacturing process.

For example :

| Code     | Name                          | WIP qty a          | Ratio \_b | FG equivalent \_c =a\*b |
| -------- | ----------------------------- | ------------------ | --------- | ----------------------- |
| DUOI DEN | Plastic lamp holder (NLH100)  |                250 | 65%       |                162.50   |
| DUOI DEN | Plastic lamp holder  (NLH100) |                150 | 80%       |                120.00   |
| DUOI DEN | Plastic lamp holder  (NLH100) |             6,816  | 50%       |             3,408.00    |
| DUOI DEN | Plastic lamp holder  (NLH100) |                538 | 70%       |                376.60   |
| DUOI DEN | Plastic lamp holder  (NLH100) |             9,346  | 35%       |             3,271.10    |

After calculating the equivalent products with different unfinished rates, the software will collect each of product code which is converted to the equivalent product. As in the above example, after calculating unfinished goods with different percentages, the total of equivalent finished goods of this code will be collected as follows:   &#x20;

| Code     |   | Name                          | WIP qty a | Ratio | FG equivalent                |
| -------- | - | ----------------------------- | --------- | ----- | ---------------------------- |
| DUOI DEN |   | Plastic lamp holder  (NLH100) | 17,100.00 |       |                     7,338.20 |
|          |   |                               |           |       |                              |

Each unfinished good code is needed collection into each line and show the total of final equivalent converted product, because the result of this part will be used to calculated the value of unfinished goods in next Step.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure>

&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/omRD58WGq-Wgn-wMO4DFFY4HKTFDV5uz1xuwyvU93dN5CqmKaystnyg3OeAKsYgZRUAqRuqDuHeI1KYOii2Kl2hqoPuokksGhaEha5jLou-9RHyUrjbPgP2kM2mGWTE2hQq_8sNA-VMRmbfpwV6VtX_lmwiH6iX1" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/RvF4_z9t7r3LcOyFk-aD8IvzSYTtDJu1sK4HxDKnySTdasV_kY5YnQQRrPyaN8Mbs8qOHyo2oqPIUUlc-mBsFniwaO7JxAcyJaqSEjAnA9E07lAjNImMFvn5JjVHeI7g7baqCN5es3HfMH2-RqL4vIyjCzOBCb8W" alt=""><figcaption></figcaption></figure>

### Step 4 : Calculating the number of manufactured products during the period (same as BOM)

There is always a logic in the manufacturing as follows :

Unfinished goods at beginning period + the products are manufactured during the period -> manufacturing -> finished goods + unfinished goods at ending period.

Therefore , the formula of the manufacturing process:

Unfinished goods  at beginning period + the product are manufactured during the period = finished goods + unfinished goods at ending period.&#x20;

Then, If knowing the 3 factors of this equation, it can be calculated the remaining factors. And, there are some value always defined as:

1\. Quantity of unfinished goods at beginning period (from the previous period forward),

2\. Finished goods manufactured during the period and

3\. Unfinished goods at the end of the period (provided by the customer's inventory)

🡺 Products manufactured during the period = Finished goods + unfinished goods at ending period – unfinished goods at beginning period

&#x20;

On the SB, It will be setup to calculate the quantity of this products manufactured.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/0rqAwovnT984B4k4DIe9FxVnim1z5KA8MmSdflhcYjpwX7Wu5U2kTNbQbwXnHDQ0umDL01EuWYBVK-aAsfqyP283txlF0lprz68dqR3of4QOrh9Lm4JCqww3HvfpaFtMhQDy2dLylrDv-G4RWpBmR8plhlurhHA0" alt=""><figcaption></figcaption></figure>

### Step 5: Convert the products manufactured during the period to standard products based on the ratio which was determined in step 1

After determining the number of products manufactured in the period according to the above formula, it is necessary to convert these products into standard products.

Using the standard product ratio established in step 1 multiplies the number of products manufactured during the period in order to convert to the standard product

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/AKkrQ7aEL9XHlRR7C4AWMrR61kbkhIAxPZ1c5Xjcktpjx9Mcul_A2B_I4wo4hwMff2_RcCLQVP-kbd_gLyStW-YY5lEEcUuN_yUbgNVwLUpxwJgdOagXZXWAHH010mjYYVjNjCggLRLZwtNNZ9-KzJlH13ljdio7" alt=""><figcaption></figcaption></figure>

### Step 6: Calculate costing of the standard products&#x20;

When calculation costing for the standard product, It is noted that in this case, the value of unfinished goods at the beginning of the period  as well as the quantity of unfinished goods at the beginning of the period will be added to calculate the average unit price for the standard product.

This step is simply as below:

(the value of unfinished goods at the beginning of the period + incurred expenses in the period)

&#x20;/ ( the number of products in the period + the number of unfinished goods at the beginning of the period)



### Step 7: Re-Calculate the costing for each type of the product

Use the costing  of standard product calculated in step 6 and the standard product ratio converted in step 1.

SB will set up the costing re-calculation table for each type of product, as the table below :

<figure><img src="../.gitbook/assets/image (109).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/sK62jOaFOCvYUacH4cMbh0iOSOqr4kZ7kRhHccC8DcL0QxK5-aMBpBUKZkK_P9_WWFI7SeZ2YT-KMvE5BQC1ZqldAUJS6JMoVvfhe9yWyc0FvQyL_vHuXz3BO_jw_bj6MjHoRFulz1dokmh4mQGeI7jADJ4dYLQw" alt=""><figcaption></figcaption></figure>

&#x20;

### Step 8: Calculate the value of unfinished goods at ending period

The value of unfinished goods at the end of the period is calculated according to the formula:

The equivalent finished goods \* unit cost

The equivalent finished goods are determined at step 3, the unit cost is determined at step 6

<figure><img src="../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/tpWJqO54kUPLLjxHzFqcVjLuKb3lwz1zIAAH1_LeuQo6sBgyUk0o8jI61H4XpA2JAWwzsqDq5_PQOFgdqk08pnJHoP5nt5r2FUCrl_hKidnNPdcXlJLqHh-2rMKXTPloJjZAhDSnRdX7GndLHr2MdjjAGoOfBJJS" alt=""><figcaption></figcaption></figure>

&#x20;

### Step 9: Determine the value of finished goods input warehouse during the period

At this step, the manufacturing equilibrium equation is used to determine the value of finished goods input warehouse during the period .

The value of finished goods input warehouse during the period = Value of unfinished goods at beginning period + incurred manufacturing costs during the period - Value unfinished goods at the end of the period

After calculating the value of input warehouse product-> determining the unit cost of products = total value of input product / total quantity of input finished products (determined at step 2)

<figure><img src="../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/n2u-k4I6e8t9L4R70M28B0XnI27BG6Qadv8YpCiiRP2QXnqasrXAyRfb9cwUX27GI5jb1qYBJbqTEXKc2SgewLqHPziCGtU6s_AcQfOi5JeKgnPMudXFhW8Y1VflsEWKbeC5UuvoCug9ypCJpaix6tCE8nYpPAoF" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>
