# Tính giá thành

## **Các Bước tính giá thành theo BOM**

<figure><img src="https://lh7-us.googleusercontent.com/Egck_YfNc6u-w-HOm-OJEOaJ7mrk3LuiawLhHrOsBZM9Z1_6qWSYj6uBvzOWPqf9XDYYth1ktS7bTLLkx-vRMHjhR8LSN11zHJOsp9M9mOCxdnQ6KUDE78ExX5w5MrtivoTsy5C3PrXT0Kx89-uRbmXugoodijnK" alt=""><figcaption></figcaption></figure>

### Bước 1: Xây dựng bảng định mức cho mỗi sản phẩm&#x20;

Sản phẩm A được làm từ những NVL nào, khối lượng mỗi NVL cần thiết để làm ra 1 sản phẩm là bao nhiêu).&#x20;

Mỗi sp có thể dùng từ 1-->100 nvl (lớn hơn customize riêng). NVL có thể xây dựng theo kg, chiếc, m, chai (tùy theo từng loại hình)

Phần này khi thiết lập trên smart book sẽ tạo trường khai báo phần định mức cho từng sản phẩm và tạo file excel để import trong trường hợp công ty có nhiều mã sản phẩm.

Chi tiết xem hình bên dưới

Ví dụ ở đây: 1 sản phẩm cần sử dụng 4 nguyên vật liệu chính và định mức từng loại nguyên vật liệu được chi tiết theo kg

| FGCode     | Material code           | Norms kg |
| ---------- | ----------------------- | -------- |
| NIBA-07-CT | 7W LED PCB              | 0.570    |
| NIBA-07-CT | LED E27 CAP             | 0.758    |
| NIBA-07-CT | LED BULB A60 HOUSING 7W | 0.852    |
| NIBA-07-CT | LED DRIVER 7W           | 0.570    |

<figure><img src="https://lh7-us.googleusercontent.com/Gc5W3PHAmc-3B7v_Estjk8x3DNz7kxpmPc-FmkQo0qROg-Q5_p0CwJ1O4bY2mOsXir5kTcMaOXALe4fGMGLIPpme2QrvawwvjVeSzR7M4mw8j4rgpIgi_G8D3rtfNMP6y85jU6V7DpTRttV3QQDqUlxdKvWRLTwv" alt=""><figcaption></figcaption></figure>

### Bước 2: Tổng hợp số lượng thành phẩm nhập kho trong kỳ

Tại bước này, chỉ nhập liệu vào SB trên phiếu nhập kho thành phẩm

<figure><img src="https://lh7-us.googleusercontent.com/VSpzcoPswTGrKDGJbuK2lWp1IOcyiEQjG8qKuwefztf4ph3hDCYd0PjszwYlYHwLNpWISI9SqlQOQwFrGF47kCmVVEm095l5jYWZh3-pZVO3uzCsPp5Cql2_bxmD4LayxUCgyU0kodk-XFcDqmB4rx8iECYUFTUh" alt=""><figcaption></figcaption></figure>

### Bước 3: Tổng hợp số lượng sản phẩm dở dang và quy đổi sp hoàn thành

Trong phần mềm sẽ tạo một trường riêng liên quan đến nhập liệu sản phẩm dở dang và tỷ lệ hoàn thành. Đồng thời setup công thức quy đổi sản phẩm dở dang ra thành sản phẩm hoàn thành tương đương

Lưu ý: Một sản phẩm có thể có nhiều tỷ lệ dở dang vì nó có thể ở đầu quy trình sản xuất, giữa quy trình hoặc cuối quy trình sản xuất

Ví dụ:&#x20;

| Code     | Name                   | WIP qty a          | Ratio\_b | FG equivalent\_c=a\*b |
| -------- | ---------------------- | ------------------ | -------- | --------------------- |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |               250  | 65%      |               162.50  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |               150  | 80%      |               120.00  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |             6,816  | 50%      |             3,408.00  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |               538  | 70%      |               376.60  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |             9,346  | 35%      |             3,271.10  |

Sau khi tính ra được sản phẩm tương đương với tỷ lệ dở dang khác nhau, thì phần mềm sẽ tập hợp theo từng mã sản phẩm đã quy đổi về sản phẩm tương đương. Như trong ví dụ trên thì  sau  khi tính được sản phẩm dở dang với các tỷ lệ khác nhau thì tổng sản phẩm hoàn thành tương đương của mã này sẽ được tập hợp lại như sau:

| Code     | Name                   | WIP qty a  | Ratio       | FG equivalent                 |
| -------- | ---------------------- | ---------- | ----------- | ----------------------------- |
| DUOI DEN | Đuôi đèn nhựa (NLH100) | 17,100.00  | <p><br></p> |                     7,338.20  |



Mỗi mã sản phẩm dở dang cần được tập hợp lại thành từng dòng và thể hiện số tổng sản phẩm quy đổi tương đương sau cùng, vì phần kết quả phần này sẽ được sử dụng để tính giá trị sản phẩm dở dang ở bước 9.

<figure><img src="https://lh7-us.googleusercontent.com/sYvs31y6jtj7S7S25zZlpwHTc9MeKgD6pj0OKzeOY5-jLXEo3V8DRan1-NveZ3xc_aEveKWYGQs_1HUQBwp5FWOOk97iVArH4eWEhswvB2uXemjJXegU9q7Door0PpHNFM8oUdP0zVYv_LXopDK_ylsQ5hVJcscW" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/6LwIFQ07R5gD06Pyplgb63HSgBq60KRTQzXrmyxeHDJ941IU7wTFwCF5cyB_1T-Oi-IbIi1JZcYkHZfDKh3FeUE9VB4VBGp5gyKeWVBSAQLO8_NIOzt4QNFYZS6_arfTgQeSTVNCb9aivK0Le77oiYIzpr0rheo2" alt=""><figcaption></figcaption></figure>

### Bước 4: Tính số lượng sp sản xuất trong kỳ&#x20;

Luôn có một logic trong sản xuất như sau:&#x20;

Sản phẩm dở dang đầu kỳ+sản phẩm đưa vào sản xuất trong kỳ -🡪 tạo ra được🡪 thành phẩm +sản phẩm dở dang cuối kỳ

Do đó, phương trình trong quá trình sản xuất

Sản phẩm dở dang đầu kỳ+ sản phẩm sản xuất trong kỳ = Thành phẩm + dở dang cuối kỳ

Khi đó, biết được 3 yếu tố của phương trình này sẽ tính được yếu tố còn lại. Và ở đây, 3 giá trị luôn được xác định là:&#x20;

1. Số lượng dở dang đầu kỳ (từ kỳ trước chuyển sang),&#x20;
2. Thành phẩm sản xuất trong kỳ và&#x20;
3. Dở dang cuối kỳ (do kiểm kê của khách hàng cung cấp)

* Sản phẩm sản xuất trong kỳ = Thành phẩm+dở dang CK-Dở dang ĐK

Trên SB sẽ setup để tính ra được số lượng sản phẩm sản xuất này

<figure><img src="https://lh7-us.googleusercontent.com/-T5z1WS2evTIUzmht4NPMhVCv8ozCDO2o3sjTM5EW1tH0yEDoOgAuqV_l_LJ63dY9SPAbJqeHD1SBHErW4GHMqslrYZqeX3wUxQIP_nlJQf5eYqHDnOyjm_sG6ee_xLH78hdRVfp7plldNOO_APNHVTpPSRfaIby" alt=""><figcaption></figcaption></figure>

### Bước 5: Tính toán lượng nguyên vật liệu theo BOM cho số lượng sản phẩm sản xuất

Tại bước này, SB sẽ setup công thức để tính toán số lượng nguyên vật liệu  theo định mức (đã được setup ở bước 1) cho những sản phẩm sản xuất trong kỳ ( đã được tính ở bước 4)

| FGCode     | RMCode                  | Norms kg (a) | Qty products (b)    | Material used by BOM (c)=(a)\*(b) |
| ---------- | ----------------------- | ------------ | ------------------- | --------------------------------- |
| NIBA-07-CT | 7W LED PCB              | 0.570        |             58,315  |           33,230                  |
| NIBA-07-CT | LED E27 CAP             | 0.758        |             58,315  |           44,225                  |
| NIBA-07-CT | LED BULB A60 HOUSING 7W | 0.852        |             58,315  |           49,697                  |
| NIBA-07-CT | LED DRIVER 7W           | 0.570        |             58,315  |           33,230                  |
| NIBA-07-WT | 7W LED PCB              | 1.000        |             26,366  |           26,366                  |
| NIBA-07-WT | LED E27 CAP             | 1.000        |             26,366  |           26,366                  |
| NIBA-07-WT | LED BULB A60 HOUSING 7W | 1.000        |             26,366  |           26,366                  |
| NIBA-07-WT | LED DRIVER 7W           | 1.000        |             26,366  |           26,366                  |



Lưu ý: Một sản phẩm sẽ sử dụng nhiều nguyên vật liệu để sản xuất do vậy, công thức sẽ setup để tính toán đầy đủ tất cả các mã nvl được sử dụng để sản xuất một mã thành phẩm.

### Bước 6: Tổng hợp nguyên vật liệu xuất kho thực tế theo từng mã sản phẩm

Tại bước này, khá giống với bước thiết lập nguyên vật liệu đích danh cho từng mã sản phẩm, vì số liệu ở đây là số liệu thực tế xuất kho của khách hàng.

SB nên có form để input vì với nhiều mã thành phẩm sẽ không thể nhập tay được

| RMCode                  | NVL xuất kho thực tế/ output material in practice |
| ----------------------- | ------------------------------------------------- |
| 7W LED PCB              |                               34,918.19           |
| LED E27 CAP             |                               45,909.50           |
| LED BULB A60 HOUSING 7W |                               51,385.13           |

<figure><img src="https://lh7-us.googleusercontent.com/emAn7cOpdKDB8wIZt5rJz20-fDBKysOOkDq2fDvAxPbQDKwgy5laQYewXnYsuZCdBISEXicEFWB2GeMwq7P2q8y4a-3J2W8IEwiIodTErPXQnZ_HOd9vwAfeBabhcyfhmXMBMhwPG4x50Di6wVUMC1V14IQKWrOU" alt=""><figcaption></figcaption></figure>

Note: Khi nhấn update sẽ tự động lấy dữ liệu từ phiếu xuất kho qua. Cần nhập thông tin bên phiếu xuất kho NVL (S1) và áp giá xuất kho NVL trước khi thực hiện bước này.

### Bước 7: So sánh chênh lệch giữa thực tế NVL xuất kho và định mức NVL

Sau khi có được số lượng nvl xuất kho theo thực tế và số lượng xuất kho theo định mức. Tại bước này, cần xác định số lượng nguyên vật liệu chênh lệch giữa số lượng thực tế và định mức.

Trong thực tế, luôn có sự chênh lệch giữa lượng xuất kho nvl thực tế và NVL xây dựng trên định mức.

TH 1: nvl xuất kho theo thực tế> NVL theo định mức

Về mặt quy định kế toán: trường hợp nvl xuất kho thực tế > NVL xuất kho theo BOM. Thì phần chênh lệch sẽ được ghi nhận vào giá vốn bán hàng

Ví dụ: NVL xuất kho thực tế là 100, nvl theo định mức là 75. Chênh lệch là 25 thì sẽ được ghi nhận trực tiếp vào giá vốn 632

Các bút toán trên SB khi xuất nvl cho trường hợp này sẽ như sau

#### 1/ NVL xuất kho theo định mức:

Nợ 621/Có 152: 100

#### 2/ Nguyên vật liệu mà SB tính toán theo BOM: 75

#### 3/ Kết chuyển nvl để tính giá thành

Nợ 154: 75

Nợ 632: 25

Có 621: 100

TH2: Nguyên vật liệu xuất kho thực tế< định mức

Ngoài ra, trường hợp số nvl thực tế xuất kho mà nhỏ hơn số nvl theo định mức, thì đối với trường hợp này kế toán có thể quay lại bước 1 để điều chỉnh lại định mức nvl cho từng sản phẩm.

Vì vậy, SB cần setup 2 công thức để xử lý cho 2 trường hợp này. Vì sẽ có những mã nvl xuất ra > Định mức và có những mã NVL xuất ra< định mức.

* Chi tiết xem file excel

<figure><img src="https://lh7-us.googleusercontent.com/7yCr6bu-93sLwbLjT4ZeWSmGDAEv_kCJFUA4cRBN9MoFmuLg9KcQ_JTfuLYLUbo-aBX4HGZReSFkgupa7gAr-AcdHhZcH2H9NRC4jbSVRbXfJvHJHUKfK0goTbFR5sqt3Swu-PQ-uBwjBTaKYCAdKkE-2CzkvwWK" alt=""><figcaption></figcaption></figure>

### Bước 8: Xác định số nvl để tính giá thành

Sau khi đã xử lý xong bước 7, thì giá trị nvl chạy vào tính giá thành sẽ là nvl thực tế hoặc định mức tùy theo từng mã nvl.&#x20;



### Bước 9: Tính giá thành cho từng sản phẩm

Bước này là bước phân bổ chi phí nhân công và sản xuất chung cho từng sản phẩm theo chi phí nguyên vật liệu. Phần chi phí nhân công và sản xuất chung được tập hợp và tải lên trong phần tính giá thành như bảng bên dưới:

<figure><img src="https://lh7-us.googleusercontent.com/BZhIlNm3zLzpsdwCDG-kB5fe1LHCFi-Kv4x_cWZsbd6ixOxHdXEaWCGY046ykEgDZ0mMXmT30BZhIIaQlSlVa-vhrI_wagQ78JR6tsIcKZ_zKYX2UO8BL5_CABnPe-HD7BdkCdRXMS8hKCOFcW5ACKTFPGHzCkj8" alt=""><figcaption></figcaption></figure>

Lưu ý: công thức khi tính giá thành đơn vị cho từng mã sản phẩm (cột cuối cùng\_unit cost)

Thì ở đây, khi tính đơn giá cho 1 đơn vị sản phẩm sẽ binh quân lai cho cả phần dở dang đầu kỳ.

Lý do: vì sp dở dang đầu kỳ vẫn tiếp tục sản xuất trong kỳ này, và khi binh quân lại như vậy, thì phần giá thành đơn vị sản phẩm sẽ ít bị biến động.

Khi thiết lập trên SB thì IT team lưu ý công thức này nhé

<figure><img src="https://lh7-us.googleusercontent.com/ONCOi2U-b3Z8icSY4nlACiupDB2nWDj9SN1CPHnLtI31aYZCRyPjLXoLGhWtYzNH7zskEEUOXNp5CMundYZvyN8LR-jqcZlV857cvafeoI59tWIqVkvu22BkSHwgV0Ew1ccPinhAWXuGailIGyTD3ekCnq1wY28Y" alt=""><figcaption></figcaption></figure>

### Bước 10: Tính toán giá trị sản phẩm dở dang cuối kỳ

<figure><img src="https://lh7-us.googleusercontent.com/PHM-Yq-cXaR_NZ0NoxPiPuI7kP5TWdzNPUD6lFg3SJC-Se9nD_xZ7c8mb6rbJ49sHwN04oqi5uit7a7DcdOPXZYzFvOlZ6E4kwhDgQS7QRkEOUjOZ9cm7UFeX2tk1V1XlMXES1HQSoPp9yU0A-wIaFCvZalo3ZEV" alt=""><figcaption></figcaption></figure>

Giá trị sản phẩm dở dang cuối kỳ được tính theo công thức

Sản phẩm hoàn thành tương đương \* unit cost

Sản phẩm hoàn thành tương đương được xác định tại bước 3, unit cost được xác định tại bước 9



### Bước 11: Xác định giá trị thành phẩm nhập kho trong kỳ

<figure><img src="https://lh7-us.googleusercontent.com/x3c9iNN7zBPfYtVPTlG2fq0qctL5g_4gfkh5wbuji6Koicmn6WJeWzrpm-nOMv5mfYlyO0KdMgZNAWwjNyhoNGR0wf5OTiQ6DpM5B-HU5KS1-1FQzN-C_HBDlkTyJlo-nhUBvHWxumE_V8K5NQXIaajuRmmO9DAf" alt=""><figcaption></figcaption></figure>

Tại bước này, phương trình cân bằng của sản xuất được dùng để xác định giá trị thành phẩm nhập kho trong kỳ

Giá trị sản phẩm nhập kho trong kỳ = Giá trị dở dang đầu kỳ+chi phí sản xuất phát sinh trong kỳ- giá trị sản phẩm dở dang cuối kỳ

Sau khi tính được giá trị sản phẩm nhập kho 🡪 xác định giá thành đơn vị sản phẩm = tổng giá trị sp nhập kho/ tổng số lượng thành phẩm nhập kho (được xác định ở bước 2)

<figure><img src="https://lh7-us.googleusercontent.com/Ko4WIo6OOg7QsZyGwRYJ0iKYoUfBtgKz1nxZpv7nuIsfqwIkDt4MM9tAT2TbTnWKpCiy3osnyVZoSl2Zd1zvKxdkwKLHFV0zmb5anrxHyDhOHm4sNeqMMUZVnNdppa1I1Tk_0hiDd4pAxnnWM_HhD9bqYjE3WJcG" alt=""><figcaption></figcaption></figure>

## Phương pháp giản đơn:

Các bước tính giá thành giản đơn/ simple method

Đây là phương pháp đơn giản nhất trong các phương pháp tính giá thành, và hiện tại rất ít doanh nghiệp sử dụng phương pháp này

<figure><img src="https://lh7-us.googleusercontent.com/fmdg0MwiCgYcX1TcLqD5HC-CFAzwlZDt9MutQyBiIlrXU-OYwT00v51sSskJNL_NOBVmbninMZuFrUE-tLBNv-X7xUKJe3s9ltJlj-AZjpBcRXsJVfeFXezsfjF5bZ5BRUJAmfC0iwX0iNB4z7K9eRVI_R4s69cH" alt=""><figcaption></figcaption></figure>

### Bước 1: Tổng hợp thành phẩm sản xuất trong kỳ (giống như BOM)

Tại bước này, chỉ nhập liệu vào SB trên phiếu nhập kho thành phẩm

<figure><img src="https://lh7-us.googleusercontent.com/ztTanKijaVkpST9GvGqVmF7wUr-jiPCEFqpg5X64O7vhibNn-Mfx2K13iROoLW_fdi-LAYBxpjL8IqhcfaiJg9C1Fw_PCj3RTTP8ByftPOpI9JutHzzZ5LMseyIIt3B7B0pgiJdG2xayF7FWx0qbBF4UAR3PiqHb" alt=""><figcaption></figcaption></figure>

### Bước 2: Tổng hợp số lượng sản phẩm dở dang và quy đổi sp hoàn thành (giống BOM)

Trong phần mềm sẽ tạo một trường riêng liên quan đến nhập liệu sản phẩm dở dang và tỷ lệ hoàn thành. Đồng thời setup công thức quy đổi sản phẩm dở dang ra thành sản phẩm hoàn thành tương đương

Lưu ý: Một sản phẩm có thể có nhiều tỷ lệ dở dang vì nó có thể ở đầu quy trình sản xuất, giữa quy trình hoặc cuối quy trình sản xuất

Ví dụ:&#x20;

| Code     | Name                   | WIP qty a          | Ratio\_b | FG equivalent\_c=a\*b |
| -------- | ---------------------- | ------------------ | -------- | --------------------- |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |               250  | 65%      |               162.50  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |               150  | 80%      |               120.00  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |             6,816  | 50%      |             3,408.00  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |               538  | 70%      |               376.60  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |             9,346  | 35%      |             3,271.10  |

Sau khi tính ra được sản phẩm tương đương với tỷ lệ dở dang khác nhau, thì phần mềm sẽ tập hợp theo từng mã sản phẩm đã quy đổi về sản phẩm tương đương. Như trong ví dụ trên thì  sau  khi tính được sản phẩm dở dang với các tỷ lệ khác nhau thì tổng sản phẩm hoàn thành tương đương của mã này sẽ được tập hợp lại như sau:

| Code     | Name                   | WIP qty a  | Ratio       | FG equivalent                 |
| -------- | ---------------------- | ---------- | ----------- | ----------------------------- |
| DUOI DEN | Đuôi đèn nhựa (NLH100) | 17,100.00  | <p><br></p> |                     7,338.20  |

Mỗi mã sản phẩm dở dang cần được tập hợp lại thành từng dòng và thể hiện số tổng sản phẩm quy đổi tương đương sau cùng, vì phần kết quả phần này sẽ được sử dụng để tính giá trị sản phẩm dở dang ở bước sau.

<figure><img src="https://lh7-us.googleusercontent.com/pNr5xWvr_NUpfX898TKGtvjUl_cYGQdVEXNAdfcewNbbWG1RBwhhuUL0DQxgb8qXMp5hKh6OLozjyqaTvf4T8lU0Y0rYCmokmYnIv06rTKM5NLYyHaoiVUGYhFIYw0VT80JrDSfE9dL6aDWzQxoGkHsiDP5xjwZh" alt=""><figcaption></figcaption></figure>

### Bước 3: Tính số lượng sp sản xuất trong kỳ&#x20;

Luôn có một logic trong sản xuất như sau:&#x20;

Sản phẩm dở dang đầu kỳ+sản phẩm đưa vào sản xuất trong kỳ -🡪 tạo ra được🡪 thành phẩm +sản phẩm dở dang cuối kỳ

Do đó, phương trình trong quá trình sản xuất

Sản phẩm dở dang đầu kỳ+ sản phẩm sản xuất trong kỳ = Thành phẩm + dở dang cuối kỳ

Khi đó, biết được 3 yếu tố của phương trình này sẽ tính được yếu tố còn lại. Và ở đây, 3 giá trị luôn được xác định là:&#x20;

4. Số lượng dở dang đầu kỳ (từ kỳ trước chuyển sang),&#x20;
5. Thành phẩm sản xuất trong kỳ và&#x20;
6. Dở dang cuối kỳ (do kiểm kê của khách hàng cung cấp)

* Sản phẩm sản xuất trong kỳ = Thành phẩm+dở dang CK-Dở dang ĐK

Trên SB sẽ setup để tính ra được số lượng sản phẩm sản xuất này

<figure><img src="https://lh7-us.googleusercontent.com/CuJJqaFK63Nbg_jZS-LKXkP2OkNX0osrOUkVI3ITvrm4-wAnhK2JdkPzW-PjUNj5PDR6vWscChsJC-67yj7KQNZ7Gy6LgNdWXjSGYQFRV6TukuS7qyvfA9q1WvMMDnglb7qBQSGL3qxOWNyJ1-dezeZY9NEyYVuZ" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/YkjbiTclhgOlvlPLnI47s_cnfCLKO3ftzjTBdZsqtI7s7IhA-s_4V8rzr1AvDRqVYKfZ64WB439co8UsGpnLC2nLyzZgi5atP-0X0Sww_RIYx8XNgCNgH-3KvVYxokV4W3xdNhPMNp4zNusnBRfeHtuln9pj1vc0" alt=""><figcaption></figcaption></figure>

### Bước 4:  Tính giá thành cho các sản phầm&#x20;

Bước này là bước phân bổ chi phí nvl trực tiếp, chi phí nhân công và sản xuất chung cho từng sản phẩm theo tổng số lượng sản xuất ra

<figure><img src="https://lh7-us.googleusercontent.com/xcXszFRwGhIHGVD3y83D9VKC_5-2ngtVnxN50J0kptY1wbQoy8bRLwRji24-bs-6cGVbGWq4T5iqeHsIqa5irIu5msQX51WSVO5C5emamFrRAAF17EJ28mWirfmBLHESLAC5KwbhkPWDd5BJR2Vw2_-hKzDDTFM6" alt=""><figcaption></figcaption></figure>

Bước này đơn giản là lấy tổng chi phí chia cho tổng sản phẩm sản xuất và nhân với số lượng sản phẩm của từng loại.

### Bước 5: Tính toán giá trị sản phẩm dở dang cuối kỳ

Giá trị sản phẩm dở dang cuối kỳ được tính theo công thức

Sản phẩm hoàn thành tương đương \* unit cost

Sản phẩm hoàn thành tương đương được xác định tại bước 2, unit cost được xác định tại bước 4

<figure><img src="https://lh7-us.googleusercontent.com/pFNWS8CKvzbKyOo5l0Q0-RETbYO9bSqMS1dF951ndYSPKN3OzNL75xGkMCm5OeaIUw3yKJd2zhct33b64Q1-B9P3DRY2-KQf2axyxE7N_E7dgAeMciMno391vFGovwsb0E4WAFnGm1pwgcyeGui3NVFBFOr5oGl6" alt=""><figcaption></figcaption></figure>

### Bước 6: Xác định giá trị thành phẩm nhập kho trong kỳ

Tại bước này, phương trình cân bằng của sản xuất được dùng để xác định giá trị thành phẩm nhập kho trong kỳ

Giá trị sản phẩm nhập kho trong kỳ = Giá trị dở dang đầu kỳ+chi phí sản xuất phát sinh trong kỳ- giá trị sản phẩm dở dang cuối kỳ

Sau khi tính được giá trị sản phẩm nhập kho 🡪 xác định giá thành đơn vị sản phẩm = tổng giá trị sp nhập kho/ tổng số lượng thành phẩm nhập kho (được xác định ở bước 1)

<figure><img src="https://lh7-us.googleusercontent.com/ejKwshZx-1O-Q16VrN4kAqcKTdz-Cun4oItrf4j-kNj7xc4YcAlHh0CXeBmXbk_UoQPkXI_Bq3xfcHgvY2VQY0ngNyZNue31JUjoL81TXtilIZgyLmckCMbYR5KG6ZzGIbm-gBP_bp_MsFxTQGPigYRSNKW79tcj" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/7Jkh4RDkkh924LLIRxpYb0ZQE8E-5XuXhyAfW1sC1U6ru7fRnlCgfSUKon_ia41ggErlJBBJIrLX5hrlYdkzMz_NSKHcMvczG-Y0He0md820hut66bvIIefgDVrF3r8N60lSu77p87NNIzZ-a9c0mJ_OyJQEZDmg" alt=""><figcaption></figcaption></figure>



## **Phương pháp hệ số:**

Các bước tính giá thành hệ số/ Coefficient method

<figure><img src="https://lh7-us.googleusercontent.com/kVS-nKwhzTy6a8m6pXT9k6kiWQcXV5j8-iQ-chAjL6SXH44FllBGWaw7uvaTdyQgRWks4bf_l7UbygQ_gtzT0xaVKKAW_5olS4SVDYCYxg0ir4IMLDjR_NNA_eO8YAH7uMsPosVBr1sGD6ee41NJVFXAMa7Fnxxh" alt=""><figcaption></figcaption></figure>

### Bước 1: Chọn 1 sản phẩm làm sản phẩm chuẩn

Phương pháp hệ số sẽ được áp dụng cho các doanh nghiệp mà chỉ sản xuất các sản phẩm mà có tính chất giống hệt nhau chỉ khác nhau về kích thước. Ví dụ: doanh nghiệp sản xuất chai, lọ thủy tinh.  Có nhiều kích cỡ như 1l, 0,5l, 250ml….

Khi đó, cần chọn một sản phẩm làm sản phẩm chuẩn để quy đổi các sản phẩm ví dụ, trong TH trên sẽ chọn chai thủy tinh có kích cỡ 1l là sản phẩm chuẩn.

<figure><img src="https://lh7-us.googleusercontent.com/0IpQumuGEYsU2AwlWvHNWcR4DDQ7BjHI3Rt0bJ2oxJpsByenTwAsQAYAN4DT9189rpIXBcYEH8hG2iQmz4kfTvxqwkpnPtap4Qhr4d7Y_QUuJkRctD4eFLiGDJlpTuxAS_lK_IHuJMKIl4JB7XW02vo0Ggu0wj16" alt=""><figcaption></figcaption></figure>

Tại bước này, SB cần thiết lập một bảng khai báo hệ số sản phẩm ban đầu để người dùng khai báo trên phần mềm. Nên thiết lập cả form&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/__m_t7udFwbkDoFYjWsGdsaJTUESQ3N4usuBf-uZjsdb7bLKslMxtoJMtCEh8eqHL4fWBYAUGmjBrf8y5tHew6LsIJQaXQbShROUdMglgZdBIua8Yi1yDUlSnSNaUtWfANpH-WMcirBkeEUuARxILHZYL8gJjxOu" alt=""><figcaption></figcaption></figure>

### Bước 2: Tổng hợp số lượng thành phẩm sản xuất trong kỳ (giống BOM)

Tại bước này, chỉ nhập liệu vào SB trên phiếu nhập kho thành phẩm

<figure><img src="https://lh7-us.googleusercontent.com/GXOZqa8_0Y_WqHMcRmFZcKwj0jCOOdHxigO2DaJ2z3DcBUs2NxO7wewDg80kz4msbuN_zRc6Puqy0lMAv74kmFcPDWIORcwphukqM01GLMLWnm0p4M1dWkZbhHx5dRLD6q6nM26cbKt5gGsnd6awmlQrk44VBb5w" alt=""><figcaption></figcaption></figure>

### Bước 3: Tổng hợp số lượng sản phẩm dở dang và quy đổi sp hoàn thành (giống BOM)

Trong phần mềm sẽ tạo một trường riêng liên quan đến nhập liệu sản phẩm dở dang và tỷ lệ hoàn thành. Đồng thời setup công thức quy đổi sản phẩm dở dang ra thành sản phẩm hoàn thành tương đương

Lưu ý: Một sản phẩm có thể có nhiều tỷ lệ dở dang vì nó có thể ở đầu quy trình sản xuất, giữa quy trình hoặc cuối quy trình sản xuất

Ví dụ:&#x20;

| Code     | Name                   | WIP qty a          | Ratio\_b | FG equivalent\_c=a\*b |
| -------- | ---------------------- | ------------------ | -------- | --------------------- |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |               250  | 65%      |               162.50  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |               150  | 80%      |               120.00  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |             6,816  | 50%      |             3,408.00  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |               538  | 70%      |               376.60  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |             9,346  | 35%      |             3,271.10  |

Sau khi tính ra được sản phẩm tương đương với tỷ lệ dở dang khác nhau, thì phần mềm sẽ tập hợp theo từng mã sản phẩm đã quy đổi về sản phẩm tương đương. Như trong ví dụ trên thì  sau  khi tính được sản phẩm dở dang với các tỷ lệ khác nhau thì tổng sản phẩm hoàn thành tương đương của mã này sẽ được tập hợp lại như sau:

| Code        | <p><br></p> | Name                   | WIP qty a   | Ratio       | FG equivalent                 |
| ----------- | ----------- | ---------------------- | ----------- | ----------- | ----------------------------- |
| DUOI DEN    | <p><br></p> | Đuôi đèn nhựa (NLH100) | 17,100.00   | <p><br></p> |                     7,338.20  |
| <p><br></p> | <p><br></p> | <p><br></p>            | <p><br></p> | <p><br></p> | <p><br></p>                   |

Mỗi mã sản phẩm dở dang cần được tập hợp lại thành từng dòng và thể hiện số tổng sản phẩm quy đổi tương đương sau cùng, vì phần kết quả phần này sẽ được sử dụng để tính giá trị sản phẩm dở dang ở bước sau.&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/QxdRuWAKIP37wTieP2PamjwfnNECDviTEY9neD5NKea9govx3dlSm_Zv-89deFKhjS0aWJoaLYVP7oaQWLbxWmh6ja1Zp7gKzq6Hqi1qgt997F_wBYWjBG_AIpd0-lKBxVw6KwDNSN19eswyUCM76FWaudq6I6pY" alt=""><figcaption></figcaption></figure>

### Bước 4: Tính số lượng sp sản xuất trong kỳ (giống BOM)

Luôn có một logic trong sản xuất như sau:&#x20;

Sản phẩm dở dang đầu kỳ+sản phẩm đưa vào sản xuất trong kỳ -🡪 tạo ra được🡪 thành phẩm +sản phẩm dở dang cuối kỳ

Do đó, phương trình trong quá trình sản xuất

Sản phẩm dở dang đầu kỳ+ sản phẩm sản xuất trong kỳ = Thành phẩm + dở dang cuối kỳ

Khi đó, biết được 3 yếu tố của phương trình này sẽ tính được yếu tố còn lại. Và ở đây, 3 giá trị luôn được xác định là:&#x20;

7. Số lượng dở dang đầu kỳ (từ kỳ trước chuyển sang),&#x20;
8. Thành phẩm sản xuất trong kỳ và&#x20;
9. Dở dang cuối kỳ (do kiểm kê của khách hàng cung cấp)

* Sản phẩm sản xuất trong kỳ = Thành phẩm+dở dang CK-Dở dang ĐK

Trên SB sẽ setup để tính ra được số lượng sản phẩm sản xuất này

<figure><img src="https://lh7-us.googleusercontent.com/-T5z1WS2evTIUzmht4NPMhVCv8ozCDO2o3sjTM5EW1tH0yEDoOgAuqV_l_LJ63dY9SPAbJqeHD1SBHErW4GHMqslrYZqeX3wUxQIP_nlJQf5eYqHDnOyjm_sG6ee_xLH78hdRVfp7plldNOO_APNHVTpPSRfaIby" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/ONyfwFHlkbd4BhbxOlVhzEOPrO3BzZiDeRFaJPJelm7o0v0arr8rEvGgqPc5D_V65XWvoWxVUvvbwvgixwkoO5ktHSJpQIwMoP-pj5WGdcAkYOWa1ppug5IlRNTpdznEPVAPg5PV6gBoJ2Mhvvd1irmLUjCPVlRc" alt=""><figcaption></figcaption></figure>

### Bước 5: Quy đổi sản phẩm sx trong kỳ ra sản phẩm tiêu chuẩn, theo hệ số đã được xác định ở bước 1

Sau khi xác định được số lượng sản phẩm sản xuất trong kỳ theo công thức phía trên, thì cần quy đổi những sản phẩm này ra sản phẩm tiêu chuẩn.

Sử dụng tỷ lệ sản phẩm chuẩn đã được thiết lập ở bước 1 nhân với số lượng sản phẩm sản xuất trong kỳ, để quy đổi ra sản phẩm tiêu chuẩn

<figure><img src="https://lh7-us.googleusercontent.com/LrWDID534eFQ4sWi95YNcZjEWmesl-XdhoAN8rsJUi_RnqunyN65DQBDpIE0uGQTd2LRzC8Pv3hJrUReK_ny0eHBl3UVMM_OJgbo9rKBRnjz0-EUudrd2vA-y_ErMEDdYndikSutXd2G3f2Qe11HGxlNH2dsglcP" alt=""><figcaption></figcaption></figure>

### Bước 6: Tính giá thành cho sản phẩm chuẩn

Khi tính giá thành cho sản phẩm chuẩn lưu ý trường hợp này sẽ cộng cả phần giá trị dở dang đầu kỳ cũng như số lượng dở dang đầu kỳ lại để tính đơn giá binh quân cho sản phẩm chuẩn.&#x20;

Bước này đơn giản chỉ lấy&#x20;

(giá trị dở dang đầu kỳ+ CP phát sinh trong kỳ)/(Số lượng sp trong kỳ+SL dở dang đầu kỳ)

### Bước 7: Tính lại giá thành cho từng loại sản phẩm

Sử dụng giá thành sản phẩm chuẩn đã tính được ở bước 6 và tỷ lệ sản phẩm chuẩn đã quy đổi ở bước 1

SB sẽ thiết lập một bảng tính lại giá thành cho từng loại sản phẩm, theo như bảng bên dưới

<figure><img src="https://lh7-us.googleusercontent.com/3T1Q5DSZDHEVMlKj8xCleh7203Gb-U3YBkHoXg-7x1ieqUNs2fDOQF2nVl0aCtn5BuUqn2s16NXsQe1dL4VQre8qReoHPaYIpBTNPGZwJ7PO6Sm0XF2VhrgjlrvBTfQwq4w2d-C1_S1rVJG-cX7TNl15VGcJMtGv" alt=""><figcaption></figcaption></figure>

### Bước 8: Tính toán giá trị sản phẩm dở dang cuối kỳ

Giá trị sản phẩm dở dang cuối kỳ được tính theo công thức

Sản phẩm hoàn thành tương đương \* unit cost

Sản phẩm hoàn thành tương đương được xác định tại bước 3, unit cost được xác định tại bước 6

<figure><img src="https://lh7-us.googleusercontent.com/Q31zpfKXjtB14uR-EMJi3lExpWuDjaCT4985RxkKIPiuKScZT3Ga4zo2Vsv6kaPbtCbTiBOmk0R5jEF0e7L9mXgfNd3JuwItBSEdVp4yJGkOcPgHqEgCHWyCy_pse5atIvYvpLAR8YChltJ_DEoTLyLD5NBDm0-E" alt=""><figcaption></figcaption></figure>

### Bước 9: Xác định giá trị thành phẩm nhập kho trong kỳ

Tại bước này, phương trình cân bằng của sản xuất được dùng để xác định giá trị thành phẩm nhập kho trong kỳ

Giá trị sản phẩm nhập kho trong kỳ = Giá trị dở dang đầu kỳ+chi phí sản xuất phát sinh trong kỳ- giá trị sản phẩm dở dang cuối kỳ

Sau khi tính được giá trị sản phẩm nhập kho 🡪 xác định giá thành đơn vị sản phẩm = tổng giá trị sp nhập kho/ tổng số lượng thành phẩm nhập kho (được xác định ở bước 2)

<figure><img src="https://lh7-us.googleusercontent.com/Tcxecs9E9pCffz4H_LJJ7lqRyfQnuIOZgNHScJC803AadvAL3_ZWN8puj0g5Gnd-laoTxSoz6DZTwGqJSey0JO5gQfv5HMpG4xsIp77Rrx00Z74a4WtSSZ5PqoRPIQd9dDRHVD-6z-N6QrvVv0Chn2a1rnWJYb7E" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/Gy9X6T-elufVs9ttn9XJcGy90tKXW906RibDovkmJFB8WBZ2ING9UYvzCYvvpIhGMOTRrrph4ip-a2UbB55XVj3THqxu5ZKGG2EpPzCJnczaTw-cfXTKr8pYd68xPq9AwJLrxLO6UREkgoYt266MWUoqZJBMulYi" alt=""><figcaption></figcaption></figure>

## **Phương pháp giá bán:**

Các bước tính giá thành theo giá bán/ Selling price

SMARTBOOKS

<figure><img src="https://lh7-us.googleusercontent.com/Yp4kfhEF3NlsVjA9eMeBN8OUR5rlSm4n-zvCyeCd7RipJMBpQTh1fpJxM8W7jKbgpcMXy3uuiqMpWCBl6t1lXw1NRprA00M-6Pw9I6DakVTeprrPYSV8u6WD51Khy90oOI2VChImbraV2a6UITJEflIh1rHWekUI" alt=""><figcaption></figcaption></figure>

### Bước 1: Tổng hợp giá bán cho từng sản phẩm

Tại bước này khai báo giá bán cho từng mã thành phẩm, giống như việc khai báo hệ số. SB nên có file excel để giúp người dùng import dễ hơn.&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/_YIpFB90og7bNFdIZUOAVgvd4VMIr8k02IkTjwgMFNOi_Mtvm9bHlZMlpjl587gx6h4J5KjwpGpxV1dlvOEkBNdyy-qdXVV_Z83qKJ54ky-oZjRD6kYJ5lzwS1F9i7XoHS3z5vNc6DE_7tmMio_pamx7tdAvErFz" alt=""><figcaption></figcaption></figure>

### Bước 2: Tổng hợp số lượng thành phẩm nhập kho trong kỳ (giống BOM)

Tại bước này, chỉ nhập liệu vào SB trên phiếu nhập kho thành phẩm

<figure><img src="https://lh7-us.googleusercontent.com/Q7-V2DIfvF1wEj_T9f4ZPa8h_wau4rJ50en7emDcmId4utjRNoKp1YCnwaKqjVocQH9sH7Ao14sSNLfuq4Zx41G5g-nslWAZnfJEg5K7cfhqYiVZDf39uqRs6T15-AwQ049rm0d08cSj7sK05VVh7fcBKAvm4E0f" alt=""><figcaption></figcaption></figure>

### Bước 3: Tổng hợp số lượng sản phẩm dở dang và quy đổi sp hoàn thành (giống BOM)

Trong phần mềm sẽ tạo một trường riêng liên quan đến nhập liệu sản phẩm dở dang và tỷ lệ hoàn thành. Đồng thời setup công thức quy đổi sản phẩm dở dang ra thành sản phẩm hoàn thành tương đương

Lưu ý: Một sản phẩm có thể có nhiều tỷ lệ dở dang vì nó có thể ở đầu quy trình sản xuất, giữa quy trình hoặc cuối quy trình sản xuất

Ví dụ:&#x20;

| Code     | Name                   | WIP qty a          | Ratio\_b | FG equivalent\_c=a\*b |
| -------- | ---------------------- | ------------------ | -------- | --------------------- |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |               250  | 65%      |               162.50  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |               150  | 80%      |               120.00  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |             6,816  | 50%      |             3,408.00  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |               538  | 70%      |               376.60  |
| DUOI DEN | Đuôi đèn nhựa (NLH100) |             9,346  | 35%      |             3,271.10  |

Sau khi tính ra được sản phẩm tương đương với tỷ lệ dở dang khác nhau, thì phần mềm sẽ tập hợp theo từng mã sản phẩm đã quy đổi về sản phẩm tương đương. Như trong ví dụ trên thì  sau  khi tính được sản phẩm dở dang với các tỷ lệ khác nhau thì tổng sản phẩm hoàn thành tương đương của mã này sẽ được tập hợp lại như sau:

| Code     | Name                   | WIP qty a  | Ratio       | FG equivalent                 |
| -------- | ---------------------- | ---------- | ----------- | ----------------------------- |
| DUOI DEN | Đuôi đèn nhựa (NLH100) | 17,100.00  | <p><br></p> |                     7,338.20  |



Mỗi mã sản phẩm dở dang cần được tập hợp lại thành từng dòng và thể hiện số tổng sản phẩm quy đổi tương đương sau cùng, vì phần kết quả phần này sẽ được sử dụng để tính giá trị sản phẩm dở dang ở bước sau.

<figure><img src="https://lh7-us.googleusercontent.com/HKl1U6zRtKeREzrJRsAfFZHUAZSVA-EALtGHNUuvD4T4O8a4igd8xUxkQ6_bZ5_nPTWJCp9MMp3SYe6nv8dJVxs7szsHpEORVq2xGdUBdMD-Omd3LABu4Lc5ofbV9jIKMns2P-QZPfRCMQGMVQkug2FsshL9M6N7" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/6AKnyJN3_Yl2LXBdNea3tkMe_YWE8IzzUc9QfcThZTJkDTqvuqYpdCWQHQ73NrN8rXQxaKnHqay5oq27gzm4CFzvrHBQI60zsnvQTA0OHnz4C70igcNPgBpZqZriC_wAb_x-_qj3G4bT4O9rpNTTkV175RndR3c-" alt=""><figcaption></figcaption></figure>

### Bước 4: Tính số lượng sp sản xuất trong kỳ&#x20;

Luôn có một logic trong sản xuất như sau:&#x20;

Sản phẩm dở dang đầu kỳ+sản phẩm đưa vào sản xuất trong kỳ -🡪 tạo ra được🡪 thành phẩm +sản phẩm dở dang cuối kỳ

Do đó, phương trình trong quá trình sản xuất

Sản phẩm dở dang đầu kỳ+ sản phẩm sản xuất trong kỳ = Thành phẩm + dở dang cuối kỳ

Khi đó, biết được 3 yếu tố của phương trình này sẽ tính được yếu tố còn lại. Và ở đây, 3 giá trị luôn được xác định là:&#x20;

10. Số lượng dở dang đầu kỳ (từ kỳ trước chuyển sang),&#x20;
11. Thành phẩm sản xuất trong kỳ và&#x20;
12. Dở dang cuối kỳ (do kiểm kê của khách hàng cung cấp)

* Sản phẩm sản xuất trong kỳ = Thành phẩm+dở dang CK-Dở dang ĐK

Trên SB sẽ setup để tính ra được số lượng sản phẩm sản xuất này

<figure><img src="https://lh7-us.googleusercontent.com/Jx777JgQtZuDXwNZpLgYusmqXSGS2T0vzoMt4vY_ihGQ_dTrTG8slv3v1c9suFpfYvSu7uk2GucEXcuzdp6z2jsDPhsBOYeSV1VRK1NwixEH_4ukb6O7wGd3sSsUFTL-cwwjSJ-0QDtKPjsi4pyR-73wjEg03KRT" alt=""><figcaption></figcaption></figure>

### Bước 5: Tính giá thành cho các sản phầm theo tỷ lệ giá bán

Bước này là bước phân bổ chi phí nvl trực tiếp, chi phí nhân công và sản xuất chung cho từng sản phẩm theo giá bán.&#x20;

<figure><img src="https://lh7-us.googleusercontent.com/LssxJna6ITH56W8_uQqZUE1JGBIvlJEXPzKN4f0_hp_Vb4_7sJ3aWgiJVxG3Q4I7pbcroeo3uppUwgmomqDNssFAPAw2PyGoGsUrrpj0H3tJIb-n1Urno4C1rUvW9P1vLBcPDid8ZOk6N46x5ESb1cofc7PDJMs5" alt=""><figcaption></figcaption></figure>

### Bước 6: Tính toán giá trị sản phẩm dở dang cuối kỳ

Giá trị sản phẩm dở dang cuối kỳ được tính theo công thức

Sản phẩm hoàn thành tương đương \* unit cost

Sản phẩm hoàn thành tương đương được xác định tại bước 3, unit cost được xác định tại bước 5

<figure><img src="https://lh7-us.googleusercontent.com/lt04-aH8et4_zrlWSu57w-MtEtibJqFDd02FGK6ufQTz38KtN_Ey2_7w3zMntXJh4Fz2uQzfTYll1ig7fVKAg_JCP6SOQmkGjg8My9CpCc7qErLXp_mKk2VRJv3q-kuCiaQdIxa8kO6RoSmD3aGxV0UmwyU5o14x" alt=""><figcaption></figcaption></figure>

### Bước 7: Xác định giá trị thành phẩm nhập kho trong kỳ

Tại bước này, phương trình cân bằng của sản xuất được dùng để xác định giá trị thành phẩm nhập kho trong kỳ

Giá trị sản phẩm nhập kho trong kỳ = Giá trị dở dang đầu kỳ+chi phí sản xuất phát sinh trong kỳ- giá trị sản phẩm dở dang cuối kỳ

Sau khi tính được giá trị sản phẩm nhập kho 🡪 xác định giá thành đơn vị sản phẩm = tổng giá trị sp nhập kho/ tổng số lượng thành phẩm nhập kho (được xác định ở bước 2)

<figure><img src="https://lh7-us.googleusercontent.com/r2hlD_mKn6rgMHNxHriw3_dPOrG4r6dZE4u7iQKjaV39bR3XYjYfgMuIBCPlIwlHy3oZJ5lPsWGV7nEIH-PRo78al27uaApKjz2Uu537JLiYtKtupcMg4spD-G4hfwX3Eh28l6slSm0X_pys1DO23eyD-ETmorvZ" alt=""><figcaption></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/Fn3zNGT3U32HSYzpl8LSI9YBmm6p8nfeIEfby3zIwBbRaFyD1waSC6O30n4gPz8ufYA1oCpyubM43M-lAYkdHINqH9fDQkc5VpqGxV5xCuUkwjcZs_UIbj0TbH7f8kQwwo7IrVp-fvYUkcdhn4wXnpKIyASX1XcM" alt=""><figcaption></figcaption></figure>

## **Giá thánh phân bước:**&#x20;

&#x20;         **Thiết lập tính giá thành theo CostCenter, theo giai đoạn, theo nhóm sản phẩm**

### Bước 1: Tạo Mã chi phí - Costcenter và thiết lập phân bổ chi phí cho nó

Main Menu => Thông tin chung => Mã chi phí:

<figure><img src="https://lh7-us.googleusercontent.com/KErrnq4wVLvCywbXCIZJMmQiZZAcjA2lC32RANWnpbk2SCNs9_WX5WOM-z2ZKKrSmvMGCiVD_s1gMR4tPwx9Uvc3-0UwCHetyM0cdnLE4evK8J05nFZVFZX4jOobfjIAOj5hjStJOiIMbzDhudSGA6sfk9aMkefr" alt=""><figcaption></figcaption></figure>

Mã chi phí – CostCenter : Mã chi phí

Tên chi phí: Tên loại chi phí

Nhóm chi phí: 621/622/627 tương ứng chi phí nguyên vật liệu / nhân công / sản xuất chung

Thiết lập phân bổ chi phí:&#x20;

* PharseID:  Thiết lập chi phí được dùng cho giai đoạn nào. Để số giai đoạn tương ứng 1, 2, 3, …. Nếu để All: chi phí dùng cho nhiều giai đoạn
* CostMethodID: Phương pháp phân bổ chi phí cho từng nhóm sản phẩm, sản phẩm

1 : chi phí được phân bổ đích danh sản phẩm&#x20;

2: chi phí được phân bổ theo tỷ lệ

3: chi phí được phân bổ đặc thù riêng cho mỗi khách hàng

* AllocationMethodID:  phương pháp phân bổ chi phí khi costMethodID sử dụng phương pháp phân bổ theo tỷ lệ&#x20;

1: phân bổ chi phí theo số lượng sản phẩm và hệ số phân bổ (giá bán, hệ số, giản đơn)

2: phân bổ chi phí 622, 627 theo tỷ lệ chi phí nguyên vật liệu 621

* AllocationPhaseID: phương pháp phân bổ chi phí cho từng giai đoạn sử dụng khi chi phí sử dụng cho nhiều giai đoạn (pharseID = All)

1: Phân bổ chi phí cho từng giai đoạn theo tỷ lệ chung

2: Phân bổ chi phí cho từng giai đoạn theo tỷ lệ riêng cho mỗi costcenter

### Bước 2: Thiết lập tỷ lệ phân bổ chi phí cho từng giai đoạn

Chi phí sau khi được tập hợp trong kì tính giá thành sẽ được phân bổ theo giai đoạn đầu tiên.

AllocationPhaseID: Loại phương pháp phân bổ mặc định 1

PhaseID: giai đoạn&#x20;

&#x20;     Rate: Tỷ lệ chi phí sử dụng cho giai đoạn đó

FromDate -ToDate: Kỳ áp dụng tính giá thành từ ngày nào đến ngày nào

<figure><img src="https://lh7-us.googleusercontent.com/QCdPro7goYwTM3yf2994zlVYN3pOjL58oxyYi2dKMmCoZrEyTJ-UXerJ-GBtTCwX8ENSFkqFLbqF7B7bGovP0GsqLzccp39KVBIiu_o1QhVpHhYmS5pAAebrUFPAX5QH1wCvqHxG6HTLe2x81upMOFKcPAC5gjHv" alt=""><figcaption></figcaption></figure>

### Bước 3: Thiết lập tỷ lệ phân bổ cho nhóm sản phẩm

Áp dụng khi phương thức phân bổ chi phí theo phương pháp tỷ lệ số lượng và hệ số: CostMethodID = 2  và AllocationMethodID = 1. Chi phí sau khi được tập hợp trong kì tính giá thành sẽ được phân bổ theo giai đoạn. Sau đó tới từng nhóm sản phẩm.

* Thiết lập

GroupID: Mã nhóm thành phẩm

Rate: hệ số phân bổ. (Nếu phân bổ đều theo số lượng thì hệ số bằng 1 cho tất cả các nhóm)

PhaseID: công đoạn tính giá thành

FromDate -ToDate: Kỳ áp dụng tính giá thành từ ngày nào đến ngày nào

<figure><img src="https://lh7-us.googleusercontent.com/Ie1lII4L5oY4jYChAyNKZtcCfJgU_R1SH1H-FofBbH-nMqzClV89KJMImPiL1zLhkmQngvVI63nnbBr241j7HqJ9OdLiZulzfGza-bj704URKTU3Enc-uFcYao5bJM4LMB2m9_wQZ987sk-a8_keRKPAcbxZ_i_s" alt=""><figcaption></figcaption></figure>

### **Bước 4: Thiết lập tỷ lệ phân bổ cho từng sản phẩm**

Áp dụng khi phương thức phân bổ chi phí theo phương pháp tỷ lệ số lượng và hệ số: CostMethodID = 2  và AllocationMethodID = 1. Chi phí sau khi được tập hợp trong kì tính giá thành sẽ được phân bổ theo giai đoạn. Sau đó tới từng nhóm sản phẩm. Sau đó tới từng sản phẩm trong nhóm.

* Thiết lập:

ProductID: Mã sản phẩm&#x20;

Rate: Hệ số phân bổ: hệ số theo sản phẩm chuẩn/ giá bán sản phẩm / 1 theo phương pháp giản đơn

PhaseID: Công đoạn tính giá thành

FromDate -ToDate: Kỳ áp dụng tính giá thành từ ngày nào đến ngày nào

<figure><img src="https://lh7-us.googleusercontent.com/otGCdu8vVcBB8PvxOwT73RAcmIL5OCkFL7pxQ1wR2Dqq8yLi6O-zlvBQvnQ5EplyaoN_Dwv7cXWqloDEgyUvrscjwwhf0KZrgKCsUSTnj6mGO3UUgfViVs5DFnz3OVlHx9H1bXqnP7PCULT4-wH9pyfd_qxy_Lkt" alt=""><figcaption></figcaption></figure>

## Tính giá thành:

&#x20;  **Nhập số lượng dở dang cuối kỳ và tỷ lệ hoàn thành tương đương nếu có**

Inventory config => Calculator qty 154 for each product

From date – To date: Kì tính giá thành

ProductID: Mã thành phẩm dở dang cuối kì

154Qty: Nhập số lượng sản phẩm dở dang cuối kì

621Rate, 622Rate, 627Rate: Nhập tỷ lệ hoàn thành tương đương tương ứng với từng nhóm chi phí 621, 622, 627

154EndAmt: Giá trị dở dang cuối kì được tự động cập nhật sau khi tính giá thành

621EndAmt, 622EndAmt, 627EndAmt: Giá trị dở dang cuối kì tương ứng từng nhóm chi phí 621, 622, 627 được tự động cập nhật sau khi tính giá thành

<figure><img src="https://lh7-us.googleusercontent.com/FuhHYVWCk8WKUzcpTrrXm-IzbdCODyBiVIEAezX_6ZEHcnDiKTq89HrcYrtWcOG5GziUadq8zD1jpGIpGThjZC4J-IU3o_vM2NBr0T-618vRZSWTOKwBUqehzuq72vBl8wmcujYKvMmhGgsH5o5M5bi_DkJbbkcX" alt=""><figcaption></figcaption></figure>

## **Costing**

Bước 1.1 : Tính số lượng thành phẩm nhập kho và số lượng thành phẩm dở dang quy đổi trong kỳ

ProductID: Mã sản phẩm&#x20;

FGQty: Số lượng thành phẩm nhập kho trong kỳ lấy ở phiếu nhập kho thành phẩm

154Qty: Số lượng dở dang cuối kì đã được nhập trước khi tính giá thành

621Qty, 622Qty, 627Qty: Số lượng dở dang quy đổi được tính bằng Số lượng dở dang 154Qty nhân với tỷ lệ hoàn thành tương đương 621Rate, 622Rate, 627Rate

FromDate – Todate: Kỳ tính giá thành

GroupID: nhóm sản phẩm – sản phẩm thuộc nhóm sản phẩm nào

PhaseID: Công đoạn tính giá thành cho sản phẩm



<figure><img src="https://lh7-us.googleusercontent.com/rrDH3koTGUPv17X-YBAgLHk6yHddfLcG_8_Z1aIK_4pGapP71OSHBo0FxmC7FB-1I32rE-POniSuV6aAFnxIsSj5t5cuvHv3epm3xZcffOtXYUNXNF70rqtDs_hcOc4hHrJn5vjj0JkJ3T9Ih3QeWmKO0HWFoYws" alt=""><figcaption></figcaption></figure>

### Bước 1.2: Tính tổng số lượng thành phẩm theo nhóm sản phẩm

Từ số lượng thành phẩm tính được ở bước 1.1 tính tổng thành phẩm sản xuất trong kì cho từng nhóm sản sản phẩm

GroupID: Nhóm sản phẩm

621TotGoodQty, 622TotGoodQty, 627TotGoodQty: Số lượng thành phẩm nhập kho FGQty cộng với số lượng dở dang quy đổi tương ứng 621Qty, 622Qty, 627Qty

Fromdate – Todate: Kỳ tính giá thành

PhaseID: Công đoạn tính giá thành

<figure><img src="https://lh7-us.googleusercontent.com/BW71FjXaVHG5WlQ4qiOXZ8c55Uqrjqdv3_mIiiatISsxdUxREA8g_7mGGkUEKTf5bsyuqWdYnhWqAWJDOLse-RTHu5DbvvtV8l_f-NxqSmfEuETywlwrZrBN5RzIt0bNyCorCCYTNuFxuvIrPWLlOONpiPoqLxjI" alt=""><figcaption></figcaption></figure>

### Bước 2: Tập hợp tổng chi phí phát sinh trong kỳ tính giá thành theo costcenter

Khi ghi nhận chi phí 621, 622, 627 người dùng cần chọn Mã chi phí

Chi phí 621, 622, 627 ở phân hệ kho là các chứng từ xuất kho sẽ được lấy ở nghiệp vụ kho. Chi phí 621, 622, 627 ở các phân hệ khác được lấy ở Chi tiết hạch toán trên Kế toán tổng hợp.

CostCenterID: Mã chi phí

CostMethodID, phaseID, AllocationMethoID: lấy theo thiết lập phân bổ chi phí của Mã chi phí. CostMethodID phương thức phân bổ chi phí, phaseID công đoạn sử dụng chi phí, AllocationMethoID phương thức phân bổ chi phí khi CostMethodID = 2.

Amt: Tổng chi phí phát sinh trong kỳ

ProductID: Mã sản phẩm ghi nhận chi phí đích danh khi CostMethodID = 1

<figure><img src="https://lh7-us.googleusercontent.com/n5E5Phy4bD6Pt2LKOx9oySVcXegn0F_Xpo5k3neul6QP0pOEnvpQrz0vUg23sV2cegu0gh_xB7k-NMBqJfYKYtrGwdiRlLu0lyRgb4z2lwoEN43U1YoLgBjgk4TnFp2wS3Sre6xcFnCbTZCgVLo7rT1dNDSeElNo" alt=""><figcaption></figcaption></figure>

PhaseID: Chọn công đoạn để tính giá thành cho bước kế tiếp

Bước 3 và bước 4 dùng để phân bổ chi phí cho các Mã chi phí thiết lập phương thức phân bổ theo phương pháp tỷ lệ số lượng và hệ số: CostMethodID = 2, AllocationMethodID = 1. Đối với các Mã chi phí đich danh CostMethodID = 1 và chi phí phân bổ theo chi phí nguyên vật liệu CostMethodID = 2, AllocationMethodID = 1 thì chi phí được tính ở bước 5

### Bước 3: Tính chi phí phân bổ cho nhóm sản phẩm ở giai đoạn được chọn.

Chi phí được phân bổ là chi phí tập hợp ở bước 2 có thiết lập CostMethodID = 2, AllocationMethodID = 1 với PhaseID là giai đoạn được chọn hoặc PhaseID là All. PhaseID là giai đoạn được chọn sẽ lấy toàn bộ chi phí. PhaseID là All thì chi phí sử dụng cho công đoạn đó được tính bằng tổng chi phí X tỷ lệ phân bổ theo giai đoạn (Thiết lập tỷ lệ phân bổ chi phí cho từng giai đoạn)

Chi phí được tập hợp theo Mã chi phí sẽ được phân bổ cho mỗi nhóm sản phẩm trong công đoạn theo số lượng và hệ số. Kết quả ở cột GroupAmt

CostGroupID: loại nhóm chi phí 621, 622, 627

CostCenterID: Mã chi phí

GroupID: Nhóm thành phẩm

IsCosting: chi phí có đươc tính cho nhóm sản phẩm đó hay không. 1 là có 0 là không

TotGoodQty: Số lượng sản phẩm hoàn thành trong kỳ theo nhóm sản phẩm ở bước 1.2. CostGroupID  = 621 lấy ở cột 621TotGoodQty, CostGroupID  = 622 lấy ở cột 622TotGoodQty,

CostGroupID  = 627 lấy ở cột 627TotGoodQty.

GroupRate: Tỷ lệ phân bổ chi phí của nhóm sản phẩm ( Thiết lập tỷ lệ phân bổ cho nhóm sản phẩm)

GroupQty: Tổng TotGoodQty x GroupRate theo từng CostcenterID

CostCenterAmt: Chi phí tập hợp được theo CostcenterID của giai đoạn tính

CostCenterRate: Tỷ lệ chi phí chia cho nhóm sản phẩm đó CostCenterRate = TotGoodQty x GroupRate / GroupQty

GroupAmt: là kết quả phân bổ chi phí cho mỗi nhóm sản phẩm với mỗi costcenter. GroupAmt  = CostCenterAmt x CostCenterRate. Dùng để sử dụng cho bước 4.

PhaseID: Công đoạn được chọn để tính giá thành

AllocationMethodID: Phương thức phân bổ lấy ở thiết lập luôn bằng 1

<figure><img src="https://lh7-us.googleusercontent.com/PegpnpGdgxjCPaVZNPx4u-mjEHlgTaV8SGKkDt5VfquH1FgdFRqoHfeHcTUtfgNk1fb6DOKsFTul9g5-fpiq46X00iKi9bdCr1fe4uLPqlk0B6_oULqVS7GmdQ3XamdwHJkiouWdZY42xuuIltTXJFBxaW_0T2TE" alt=""><figcaption></figcaption></figure>

### Bước 4: Phân bổ chi phí cho từng sản phẩm

Từ chi phí tính được cho mỗi nhóm sản phẩm ở bước 3. Phân bổ chi phí cho từng sản phẩm trong nhóm. Kết quả ở cột ProductAmt

CostCenterID: mã chi phí

GroupID: Nhóm sản phẩm

GroupAmt: Chi phí cho nhóm sản phẩm tính được ở bước 3

ProductID: Mã thành phẩm hoàn thành trong kỳ

TotGoodQty: Số lượng sản phẩm hoàn thành lấy ở bước 1.1: Số lượng thành phẩm nhập kho FGQty cộng với số lượng dở dang quy đổi tương ứng 621Qty, 622Qty, 627Qty

ProductRate: Thiết lập hệ số phân bổ cho sản phẩm

IsCosting: ghi nhận chi phí cho sản phẩm mặc định bằng 1

TotProductAmt: Tổng TotGoodQty X ProductRate theo từng nhóm sản phẩm

Rate: Tỷ lệ phân bổ chi phí cho sản phẩm Rate = TotGoodQty x ProductRate / TotProductAmt

ProductAmt: chi phí phân bổ cho sản phẩm ProductAmt = GroupAmt x Rate

<figure><img src="https://lh7-us.googleusercontent.com/XY-PU19SvPHOqJY0t4iWKtHvmlI9714CVI6FLy62UFc9MOs8KrES-HVVs4NyReoULc5cCuynCnne7Pto-LSdtU6Y_D6aK2BHILnjUFxvRqlWao0OoOAwkORo1gL3m0eVNsMb8WnuyDAMrJbmhqrmI1gA9UjsaC5V" alt=""><figcaption></figcaption></figure>

### Bước 5: Giá thành sản phẩm

Tổng chi phí cho từng sản phẩm là chi phí dở dang đầu kỳ và chi phí phát sinh trong kỳ. Chi phí phát sinh trong kỳ gồm chi phí phân bổ theo phương thức đích danh, chi phí phân bổ theo nguyên vật liệu, chi phí phân bổ cho sản phẩm tính được ở bước 4.

Giá thành sản phẩm bằng tổng chi phí chia cho số lượng thành phẩm hoàn thành trong kỳ.

ProductID: Mã thành phẩm

Qty: Số lượng sản phẩm hoàn thành lấy ở bước 1.1

BeginAmt: Dở dang đầu kỳ lấy từ chi phí dở dang kỳ trước

Amt621\_ide, Amt622\_ide, Amt627\_ide: Chi phí trong kỳ đích danh theo nhóm chi phí 621, 622, 627 được tổng hợp ở bước 2 với Costcenter có CostMethodID = 1

Amt621, Amt622, Amt627: chi phí trong kỳ tính được ở bước 4 cho từng nhóm 621, 622, 627 và chi phí phân bổ theo nguyên vật liệu.

TotAmt: Tổng chi phí dở dang đầu kỳ và chi phí phát sinh trong kỳ BeginAmt + Amt621\_ide + Amt622\_ide + Amt627\_ide + Amt621 + Amt622 + Amt627

UnitPrice: Giá thành sản phẩm  TotAmt / Qty

EndAmt: Dở dang cuối kỳ bằng UnitPrice X Số lượng dở dang

<figure><img src="https://lh7-us.googleusercontent.com/YwJlLCHYFMTEFryt0gBAUAncOYkHGq4GG3KxQmz3kGufHY9mPCD3LmeoHC5Rb7N6U9L0H6pfKpHAoWRLAFx6rL42HT4pCP4a0Knwplrvw8HiihebRjP4O6VqGNwIY3XZwV9IePwPKjiotPmdCvZRFBI9V0Twl6uS" alt=""><figcaption></figcaption></figure>

Sau khi lưu:

Giá thành sau khi tính UnitPrice sẽ được áp xuống cho phiếu nhập kho thành phẩm.

Dở dang cuối kỳ sẽ được cập nhật vào bảng dở dang

### Bước 6: Tính giá xuất kho theo phương pháp bình quân để tính giá vốn hoặc giá xuất kho cho công đoạn sau

ProductID: Mã sản phẩm

ItemName: Tên sản phẩm

BegbalanceQty: Số lượng tồn đầu kỳ

BegBalanceAmt: Giá trị tồn đầu kỳ

InputQty: Số lượng sản phẩm nhập kho trong kỳ

InputAmt: Giá trị sản phẩm nhập kho trong kỳ

PriceOut: Đơn giá xuất kho

<figure><img src="https://lh7-us.googleusercontent.com/wkgMK9TPpuVbz300tds3Wi15K09lBt-iiesQmvxWaOZ9xy-1LBEH1cYKQ35sd7rSai6-NXtOyslJitWGBaEToe8oBsqaHlzJdHE5RkLIfDJVFdP20CHAn3AoZLAAfJQf6x9ro-mNwV37c6BXDek6weBSg305d5Kj" alt=""><figcaption></figcaption></figure>

Cần cập nhật lại chi phí ở bước 2 trước khi tính giá thành cho công đoạn sau.

