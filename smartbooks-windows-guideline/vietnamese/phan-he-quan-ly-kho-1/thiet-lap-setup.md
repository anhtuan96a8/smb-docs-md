# 7.1 BOM

Chọn phương pháp tính giá thành từ Thông tin công ty

<figure><img src="../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

### 7.1  BOM: <a href="#toc199251991" id="toc199251991"></a>

Các Bước tính giá thành theo BOM

<figure><img src="../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

**Step 1: Xây dựng bảng định mức cho mỗi sản phẩm**

Sản phẩm A được làm từ những NVL nào, khối lượng mỗi NVL cần thiết để làm ra 1 sản phẩm là bao nhiêu).

Mỗi sp có thể dùng từ 1-->100 nvl (lớn hơn customize riêng). NVL có thể xây dựng theo kg, chiếc, m, chai (tùy theo từng loại hình)

Phần này khi thiết lập trên smart book sẽ tạo trường khai báo phần định mức cho từng sản phẩm và tạo file excel để import trong trường hợp công ty có nhiều mã sản phẩm.

Chi tiết xem hình bên dưới

Ví dụ ở đây: 1 sản phẩm cần sử dụng 4 nguyên vật liệu chính và định mức từng loại nguyên vật liệu được chi tiết theo kg

&#x20;

&#x20;

| <p> </p><p>FGCode</p><p> </p>     | <p> </p><p>Material code</p><p> </p>           | <p> </p><p>Norms kg</p><p> </p> |
| --------------------------------- | ---------------------------------------------- | ------------------------------- |
| <p> </p><p>NIBA-07-CT</p><p> </p> | <p> </p><p>7W LED PCB</p><p> </p>              | <p> </p><p>0.570</p><p> </p>    |
| <p> </p><p>NIBA-07-CT</p><p> </p> | <p> </p><p>LED E27 CAP</p><p> </p>             | <p> </p><p>0.758</p><p> </p>    |
| <p> </p><p>NIBA-07-CT</p><p> </p> | <p> </p><p>LED BULB A60 HOUSING 7W</p><p> </p> | <p> </p><p>0.852</p><p> </p>    |
| <p> </p><p>NIBA-07-CT</p><p> </p> | <p> </p><p>LED DRIVER 7W</p><p> </p>           | <p> </p><p>0.570</p><p> </p>    |
|                                   |                                                |                                 |

<figure><img src="../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

**Step 2: Tổng hợp số lượng thành phẩm nhập kho trong kỳ**

Tại bước này, chỉ nhập liệu vào SB trên phiếu nhập kho thành phẩm

<figure><img src="../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

**Step 3: Tổng hợp số lượng sản phẩm dở dang và quy đổi sp hoàn thành**

Trong phần mềm sẽ tạo một trường riêng liên quan đến nhập liệu sản phẩm dở dang và tỷ lệ hoàn thành. Đồng thời setup công thức quy đổi sản phẩm dở dang ra thành sản phẩm hoàn thành tương đương

Lưu ý: Một sản phẩm có thể có nhiều tỷ lệ dở dang vì nó có thể ở đầu quy trình sản xuất, giữa quy trình hoặc cuối quy trình sản xuất

Ví dụ:

<table data-header-hidden><thead><tr><th valign="bottom"></th><th valign="bottom"></th><th valign="bottom"></th><th valign="bottom"></th><th valign="bottom"></th></tr></thead><tbody><tr><td valign="bottom"><p> </p><p>Code</p><p> </p></td><td valign="bottom"><p> </p><p>Name</p><p> </p></td><td valign="bottom"><p> </p><p> WIP qty a</p><p> </p></td><td valign="bottom"><p> </p><p> Ratio_b</p><p> </p></td><td valign="bottom"><p> </p><p> FG equivalent_c=a*b</p><p> </p></td></tr><tr><td valign="bottom"><p> </p><p>DUOI DEN</p><p> </p></td><td valign="bottom"><p> </p><p>Đuôi đèn nhựa (NLH100)</p><p> </p></td><td valign="bottom"><p> </p><p>               250 </p><p> </p></td><td valign="bottom"><p> </p><p>65%</p><p> </p></td><td valign="bottom"><p> </p><p>               162.50 </p><p> </p></td></tr><tr><td valign="bottom"><p> </p><p>DUOI DEN</p><p> </p></td><td valign="bottom"><p> </p><p>Đuôi đèn nhựa (NLH100)</p><p> </p></td><td valign="bottom"><p> </p><p>               150 </p><p> </p></td><td valign="bottom"><p> </p><p>80%</p><p> </p></td><td valign="bottom"><p> </p><p>               120.00 </p><p> </p></td></tr><tr><td valign="bottom"><p> </p><p>DUOI DEN</p><p> </p></td><td valign="bottom"><p> </p><p>Đuôi đèn nhựa (NLH100)</p><p> </p></td><td valign="bottom"><p> </p><p>            6,816 </p><p> </p></td><td valign="bottom"><p> </p><p>50%</p><p> </p></td><td valign="bottom"><p> </p><p>            3,408.00 </p><p> </p></td></tr><tr><td valign="bottom"><p> </p><p>DUOI DEN</p><p> </p></td><td valign="bottom"><p> </p><p>Đuôi đèn nhựa (NLH100)</p><p> </p></td><td valign="bottom"><p> </p><p>               538 </p><p> </p></td><td valign="bottom"><p> </p><p>70%</p><p> </p></td><td valign="bottom"><p> </p><p>               376.60 </p><p> </p></td></tr><tr><td valign="bottom"><p> </p><p>DUOI DEN</p><p> </p></td><td valign="bottom"><p> </p><p>Đuôi đèn nhựa (NLH100)</p><p> </p></td><td valign="bottom"><p> </p><p>            9,346 </p><p> </p></td><td valign="bottom"><p> </p><p>35%</p><p> </p></td><td valign="bottom"><p> </p><p>            3,271.10 </p><p> </p></td></tr></tbody></table>

Sau khi tính ra được sản phẩm tương đương với tỷ lệ dở dang khác nhau, thì phần mềm sẽ tập hợp theo từng mã sản phẩm đã quy đổi về sản phẩm tương đương. Như trong ví dụ trên thì sau  khi tính được sản phẩm dở dang với các tỷ lệ khác nhau thì tổng sản phẩm hoàn thành tương đương của mã này sẽ được tập hợp lại như sau:

| <p> </p><p>Code</p><p> </p>     | <p> </p><p>Name</p><p> </p>                   | <p> </p><p> WIP qty a</p><p> </p>  | <p> </p><p> Ratio</p><p> </p> | <p> </p><p> FG equivalent</p><p> </p>                |
| ------------------------------- | --------------------------------------------- | ---------------------------------- | ----------------------------- | ---------------------------------------------------- |
| <p> </p><p>DUOI DEN</p><p> </p> | <p> </p><p>Đuôi đèn nhựa (NLH100)</p><p> </p> | <p> </p><p> 17,100.00 </p><p> </p> |                               | <p> </p><p>                    7,338.20 </p><p> </p> |

&#x20;

Mỗi mã sản phẩm dở dang cần được tập hợp lại thành từng dòng và thể hiện số tổng sản phẩm quy đổi tương đương sau cùng, vì phần kết quả phần này sẽ được sử dụng để tính giá trị sản phẩm dở dang ở bước 9

<figure><img src="../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

**Step 4: Tính số lượng sp sản xuất trong kỳ**

**Luôn có một logic trong sản xuất như sau:**

Sản phẩm dở dang đầu kỳ+sản phẩm đưa vào sản xuất trong kỳ -à tạo ra đượcà thành phẩm +sản phẩm dở dang cuối kỳ

**Do đó, phương trình trong quá trình sản xuất**

**Sản phẩm dở dang đầu kỳ+ sản phẩm sản xuất trong kỳ = Thành phẩm + dở dang cuối kỳ**

Khi đó, biết được 3 yếu tố của phương trình này sẽ tính được yếu tố còn lại. Và ở đây, 3 giá trị luôn được xác định là:

1\.     Số lượng dở dang đầu kỳ (từ kỳ trước chuyển sang),

2\.     Thành phẩm sản xuất trong kỳ và

3\.     Dở dang cuối kỳ (do kiểm kê của khách hàng cung cấp)

-> Sản phẩm sản xuất trong kỳ = Thành phẩm+dở dang CK-Dở dang ĐK

&#x20;

Trên SB sẽ setup để tính ra được số lượng sản phẩm sản xuất này

<figure><img src="../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

**Step 5: Tính toán lượng nguyên vật liệu theo BOM cho số lượng sản phẩm sản xuất**

Tại bước này, SB sẽ setup công thức để tính toán số lượng nguyên vật liệu  theo định mức (đã được setup ở bước 1) cho những sản phẩm sản xuất trong kỳ ( đã được tính ở bước 4)

&#x20;

| <p> </p><p>FGCode</p><p> </p>     | <p> </p><p>RMCode</p><p> </p>                  | <p> </p><p>Norms kg (a)</p><p> </p> | <p> </p><p> Qty products (b) </p><p> </p>  | Material used by BOM (c)=(a)\*(b)         |
| --------------------------------- | ---------------------------------------------- | ----------------------------------- | ------------------------------------------ | ----------------------------------------- |
| <p> </p><p>NIBA-07-CT</p><p> </p> | <p> </p><p>7W LED PCB</p><p> </p>              | <p> </p><p>0.570</p><p> </p>        | <p> </p><p>            58,315 </p><p> </p> | <p> </p><p>           33,230 </p><p> </p> |
| <p> </p><p>NIBA-07-CT</p><p> </p> | <p> </p><p>LED E27 CAP</p><p> </p>             | <p> </p><p>0.758</p><p> </p>        | <p> </p><p>            58,315 </p><p> </p> | <p> </p><p>           44,225 </p><p> </p> |
| <p> </p><p>NIBA-07-CT</p><p> </p> | <p> </p><p>LED BULB A60 HOUSING 7W</p><p> </p> | <p> </p><p>0.852</p><p> </p>        | <p> </p><p>            58,315 </p><p> </p> | <p> </p><p>           49,697 </p><p> </p> |
| <p> </p><p>NIBA-07-CT</p><p> </p> | <p> </p><p>LED DRIVER 7W</p><p> </p>           | <p> </p><p>0.570</p><p> </p>        | <p> </p><p>            58,315 </p><p> </p> | <p> </p><p>           33,230 </p><p> </p> |
| <p> </p><p>NIBA-07-WT</p><p> </p> | <p> </p><p>7W LED PCB</p><p> </p>              | <p> </p><p>1.000</p><p> </p>        | <p> </p><p>            26,366 </p><p> </p> | <p> </p><p>           26,366 </p><p> </p> |
| <p> </p><p>NIBA-07-WT</p><p> </p> | <p> </p><p>LED E27 CAP</p><p> </p>             | <p> </p><p>1.000</p><p> </p>        | <p> </p><p>            26,366 </p><p> </p> | <p> </p><p>           26,366 </p><p> </p> |
| <p> </p><p>NIBA-07-WT</p><p> </p> | <p> </p><p>LED BULB A60 HOUSING 7W</p><p> </p> | <p> </p><p>1.000</p><p> </p>        | <p> </p><p>            26,366 </p><p> </p> | <p> </p><p>           26,366 </p><p> </p> |
| <p> </p><p>NIBA-07-WT</p><p> </p> | <p> </p><p>LED DRIVER 7W</p><p> </p>           | <p> </p><p>1.000</p><p> </p>        | <p> </p><p>            26,366 </p><p> </p> | <p> </p><p>           26,366 </p><p> </p> |

&#x20;

Lưu ý: Một sản phẩm sẽ sử dụng nhiều nguyên vật liệu để sản xuất do vậy, công thức sẽ setup để tính toán đầy đủ tất cả các mã nvl được sử dụng để sản xuất một mã thành phẩm.



**Step 6: Tổng hợp nguyên vật liệu xuất kho thực tế theo từng mã sản phẩm**

Tại bước này, khá giống với bước thiết lập nguyên vật liệu đích danh cho từng mã sản phẩm, vì số liệu ở đây là số liệu thực tế xuất kho của khách hàng.

SB nên có form để input vì với nhiều mã thành phẩm sẽ không thể nhập tay được

| <p> </p><p><strong>RMCode</strong></p><p> </p> | **NVL xuất kho thực tế/ output material in practice**            |
| ---------------------------------------------- | ---------------------------------------------------------------- |
| <p> </p><p>7W LED PCB</p><p> </p>              | <p> </p><p>                               34,918.19 </p><p> </p> |
| <p> </p><p>LED E27 CAP</p><p> </p>             | <p> </p><p>                               45,909.50 </p><p> </p> |
| <p> </p><p>LED BULB A60 HOUSING 7W</p><p> </p> | <p> </p><p>                               51,385.13 </p><p> </p> |

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

**Note: Khi nhấn update sẽ tự động lấy dữ liệu từ phiếu xuất kho qua. Cần nhập thông tin bên phiếu xuất kho NVL (S1) và áp giá xuất kho NVL trước khi thực hiện bước này.**

&#x20;

**Step 7: So sánh chênh lệch giữa thực tế NVL xuất kho và định mức NVL**

Sau khi có được số lượng nvl xuất kho theo thực tế và số lượng xuất kho theo định mức. Tại bước này, cần xác định số lượng nguyên vật liệu chênh lệch giữa số lượng thực tế và định mức.

Trong thực tế, luôn có sự chênh lệch giữa lượng xuất kho nvl thực tế và NVL xây dựng trên định mức.

_TH 1: nvl xuất kho theo thực tế> NVL theo định mức_

Về mặt quy định kế toán: trường hợp nvl xuất kho thực tế > NVL xuất kho theo BOM. Thì phần chênh lệch sẽ được ghi nhận vào giá vốn bán hàng

Ví dụ: NVL xuất kho thực tế là 100, nvl theo định mức là 75. Chênh lệch là 25 thì sẽ được ghi nhận trực tiếp vào giá vốn 632

Các bút toán trên SB khi xuất nvl cho trường hợp này sẽ như sau

1/ NVL xuất kho theo định mức:

Nợ 621/Có 152: 100

2/ Nguyên vật liệu mà SB tính toán theo BOM: 75

3/ Kết chuyển nvl để tính giá thành

Nợ 154: 75

Nợ 632: 25

Có 621: 100

TH2: Nguyên vật liệu xuất kho thực tế< định mức

Ngoài ra, trường hợp số nvl thực tế xuất kho mà nhỏ hơn số nvl theo định mức, thì đối với trường hợp này kế toán có thể quay lại bước 1 để điều chỉnh lại định mức nvl cho từng sản phẩm.

Vì vậy, SB cần setup 2 công thức để xử lý cho 2 trường hợp này. Vì sẽ có những mã nvl xuất ra > Định mức và có những mã NVL xuất ra< định mức.

-> Chi tiết xem file excel

<figure><img src="../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

**Step 8: Xác định số nvl để tính giá thành**

Sau khi đã xử lý xong bước 7, thì giá trị nvl chạy vào tính giá thành sẽ là nvl thực tế hoặc định mức tùy theo từng mã nvl.

**Step 9: Tính giá thành cho từng sản phẩm**

Bước này là bước phân bổ chi phí nhân công và sản xuất chung cho từng sản phẩm theo chi phí nguyên vật liệu. Phần chi phí nhân công và sản xuất chung được tập hợp và tải lên trong phần tính giá thành như bảng bên dưới:

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

Lưu ý: công thức khi tính giá thành đơn vị cho từng mã sản phẩm (cột cuối cùng\_unit cost)

Thì ở đây, khi tính đơn giá cho 1 đơn vị sản phẩm sẽ binh quân lai cho cả phần dở dang đầu kỳ.

Lý do: vì sp dở dang đầu kỳ vẫn tiếp tục sản xuất trong kỳ này, và khi binh quân lại như vậy, thì phần giá thành đơn vị sản phẩm sẽ ít bị biến động.

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

**Step 10: Tính toán giá trị sản phẩm dở dang cuối kỳ**

<figure><img src="../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

Giá trị sản phẩm dở dang cuối kỳ được tính theo công thức

Sản phẩm hoàn thành tương đương \* unit cost

Sản phẩm hoàn thành tương đương được xác định tại bước 3, unit cost được xác định tại bước 9

**Step 11: Xác định giá trị thành phẩm nhập kho trong kỳ**

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

Tại bước này, phương trình cân bằng của sản xuất được dùng để xác định giá trị thành phẩm nhập kho trong kỳ

**Giá trị sản phẩm nhập kho trong kỳ = Giá trị dở dang đầu kỳ+chi phí sản xuất phát sinh trong kỳ- giá trị sản phẩm dở dang cuối kỳ**

Sau khi tính được giá trị sản phẩm nhập kho à xác định giá thành đơn vị sản phẩm = tổng giá trị sp nhập kho/ tổng số lượng thành phẩm nhập kho (được xác định ở bước 2)

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>
