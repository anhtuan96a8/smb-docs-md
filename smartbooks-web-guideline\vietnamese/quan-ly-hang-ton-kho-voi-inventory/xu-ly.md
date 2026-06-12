# 6.2 Xử lý

#### 6.2.1    Quy trình kho: Nhập kỳ xử lý – Tính giá

Chọn từ ngày … tới ngày

Bao gồm 5 bước

·       Bước 1: Xử lý chứng từ

·       Bước 2: Áp giá xuất kho nguyên vật liệu cho sản xuất

·       Bước 3: Áp giá nhập kho thành phẩm/ Tính đơn giá thành phẩm

·       Bước 4: Áp giá vốn hàng bán

·       Bước 5: Kết chuyển lên sổ

<figure><img src="../.gitbook/assets/image (219).png" alt=""><figcaption></figcaption></figure>

**Xử lý chứng từ**

Xử các chứng từ đã nhập trong kỳ ở phân nhập chứng từ.

Lưu ý: Các chứng từ cân phải được xử lý hết để tính giá thành và giá vốn chính xác.

&#x20;

**Áp giá xuất nguyên vật liệu cho sản xuất**

Tính giá xuất kho nguyên vật liệu theo:

·       Theo bình quân theo công đoạn,

·       Theo từng lần nhập xuất

Chọn Tải để lấy hết những bút toán xuất kho đã Release hoặc Chọn tệp để import các bút toán trực tiếp

<figure><img src="../.gitbook/assets/image (220).png" alt=""><figcaption></figcaption></figure>

Áp giá nhập kho thành phẩm/ Tính đơn giá thành phẩm

_Áp giá thành phẩm_: Dùng trong trường hợp công ty không tính giá thành bằng phần mềm, nhưng muốn theo dõi nhập xuất tồn và tính giá vốn bằng phần mềm.

&#x20;

_Tính đơn giá thành phẩm_: là công cụ dung để tính giá thành sản xuất trong kỳ. Smartbook có tích hợp 5 phương pháp tính giá thành, bao gồm:

·       Tính giá thành phân bước

·       Phương pháp giá bán

·       Phương pháp hệ số

·       Phương pháp giản đơn

·       Phương pháp định mức BOM

&#x20;

a. Tính giá thành theo đinh mức nguyên vật liêu, nhân công, và chi phí sản xuất chung (BOM).

Điều kiên áp dụng: Có xây dựng được đinh mức tiêu hao nguyên vật liệu trực tiếp, tiêu hao chi phí nhân công, tiêu hao chi phí sản xuất chung.

Cách sử dụng:

Bước 1: Khai báo thông tin BOM

·       Thiết lập quy trình sản xuất

·       Thiết lập đinh mức tiêu hao 621, 622, 627 tương ứng với từng quy trình,

Nhập chi phí 622, 627 phát sinh trong kỳ, chi phí 621 đã được tính ở bước áp giá xuất nguyên vật liệu cho sản xuất.

<figure><img src="../.gitbook/assets/image (221).png" alt=""><figcaption></figcaption></figure>

Bước 2: Tập hợp dở dang đầu kỳ và dở dang cuối kỳ

<figure><img src="../.gitbook/assets/image (222).png" alt=""><figcaption></figcaption></figure>

Bước 3: Cập nhật thành phẩm

<figure><img src="../.gitbook/assets/image (223).png" alt=""><figcaption></figcaption></figure>

Bước 4: Tính giá thành sản phẩm

Căn cứ vào BOM thiết lập và lương thành phẩm sản xuất trong kỳ cộng với tồn kho dở dang cuối kỳ, phần mềm sẽ tính chi phí 621,622,627 cần.              &#x20;

So sánh chi phí thực tế với chi phí theo BOM.

Trường hợp chi phí theo BOM > chi phí thực tế (621, 622, 627), phần mềm sẽ phân bổ chi phí thực tế theo tiêu thức tùy chọn.

Trường hợp chi phí theo BOM < chi phí thực tế (621, 622, 627), giá thành sẽ tính theo BOM, phân chênh lệch sẽ tùy chọn (ghi nhân trên 154 hoặc kết chuyển vào giá vốn trong kỳ).

<figure><img src="../.gitbook/assets/image (224).png" alt=""><figcaption></figcaption></figure>

Áp giá vốn hàng bán

Tính đơn giá vốn hàng bán trong kỳ theo 2 phương pháp

·       Bình quân theo giai đoạn

·       Bình quân theo từng lần nhập xuất.

<figure><img src="../.gitbook/assets/image (226).png" alt=""><figcaption></figcaption></figure>

Kết chuyển lên sổ

Tất cả các giao dịch trong phân hệ kho với kỳ được chọn, có giá trị đã được tính toán, sẽ được nhập vào sổ cái.

<figure><img src="../.gitbook/assets/image (227).png" alt=""><figcaption></figcaption></figure>

#### 6.2.2    Xử lý chứng từ kho

Bước đầu tiên trước khi thực hiện việc tính giá thành hoặc giá vốn hàng bán.

Màn này được tách riêng trong trường hợp người dùng không cần sử dụng chức năng tính giá thành, chỉ cần chuyển đổi trạng thái các bút toán kho lên GL

<figure><img src="../.gitbook/assets/image (228).png" alt=""><figcaption></figcaption></figure>
