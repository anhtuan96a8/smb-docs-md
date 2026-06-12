# 4.2 Phân mục nhập liệu

#### a) **Hạch toán thu, chi tiền:**

Quản lý tiền mặt được thực hiện thông qua module Kế toán tiền mặt. Tất cả các nghiệp vụ liện quan đến tiền mặt trong phạm vi doanh nghiệp đều được module CA tạo lập, lưu trữ và xử lý. Việc tạo lập, lưu trữ và xử lý này có thể được thực hiện bằng cách:



![](<../.gitbook/assets/0 (94).png>)

![](<../.gitbook/assets/1 (46).png>)

**Phần Tổng hợp:**

**+ Số lô.:** Để trống, chương trình tự phát sinh

**+ Kỳ kế toán:**(ví dụ hóa đơn của tháng 8 năm 2014: 08-2014) Số tháng phát sinh

**+ Số phiếu chi:** Nhập số phiếu ch&#x69;**.**

**+ Ngày lập phiếu:** Nhập ngày phát sinh

**+ Tài khoản tiền:** Nhấn F3 để chọn tài khoản tiền

**+ Loại tiền, Tỷ giá quy đổi:** Tùy theo loại tiền sẽ có tỷ giá đối với VND

**+ Tạm ứng trước:** Nếu khoản tiền chi ra này liên quan đến khoản tạm ứng cho nhà cung cấp có gốc ngoại tệ thì click chọn vào đây. Nếu không có thì để trống. Mục đích là có thể link qua phần kế toán phải trả để khi hạch toán kế toán phải trả cho các đơn hàng có ứng trước phần mềm giúp lấy tỷ giá đúng với phiếu tạm ứng này.

**+ Lý do chi(VN-EN):** Nhập lý do chi

**+ Người nhận tiền:** Nhập tên người nhận

**+ Địa chỉ:** Nhập địa chỉ người nhận

**Phần chi tiết:**

**+ Tài khoản:** Nhấn F3 để chọn tài khoản tương ứng hoặc nhập tài khoản

**+ Diễn giải(VN-EN):** Sẽ được link từ diễn giải của phần tổng hợp ở trên

**+ Số tiền** Nhập số tiền cần chi

Nhập các thông tin của hóa đơn như:

* **Serial No.**: Số Sêri của hóa đơn phát hành
* **Số hóa đơn.**: Số hóa đơn
* **Ngày hóa đơn**: Ngày hóa đơn
* **Nhà cung cấp**: Nhấn F3 để chọn

Nhấn nút **Save** để ghi nhận thông tin chi tiền

* **Có**: TK tiền
* **Nợ**: TK tương ứng (TK định khoản ở vùng lưới)

Nhấn nút **in chứng từ** để in phiếu chi

![](<../.gitbook/assets/2 (52).png>)

Đối với thanh toán cho hóa đơn nhà cung cấp

Bước 1: Tại ô Hóa đơn (AP Voucher) ấn F3 để tìm và chọn những hóa đơn cần thanh toán

Bước 2: Có thể chọn 1 hay nhiều phiếu hóa đơn phải trả khi tích vào cột lựa chọn.

Bước 3: Khi chọn các hóa đơn dữ liệu sẽ được tự động nhập vào lưới dữ liệu

Các thông tin được tự động ghi nhận :

![](<../.gitbook/assets/4 (32).png>)



\+ Số tiền

\+ Tài khoản đối ứng ( 331 công nợ )

\+ Diễn giải ( VN + EN )

\+ Loại tiền

\+ Tỷ Giá

\+ Thông tin hóa đơn ( Số hóa đơn , ngày hóa đơn , số serial )

\+ Mã nhà cung cấp

\+ Số phiếu hóa đơn phải trả

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

Các nút khác:

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

\-        P trước: Previous Voucher

\-        P sau: Next Voucher

\-        Điều chỉnh : thay đổi trạng thái của phiếu để sửa trực tiếp ( trong trường hợp người dùng được phân quyền )

#### b) Nghiệp vụ thu tiền mặt, thu tiền gửi

![](<../.gitbook/assets/5 (21).png>)

![](<../.gitbook/assets/6 (15).png>)

**Phần Tổng hợp:**

**+ Số lô.:** Để trống, chương trình chạy tự động

**+ Kỳ kế toán:**(ví dụ hóa đơn của tháng 7 năm 2015: 07-2015) Tháng phát sinh

**+ Số phiếu thu:** Nhập số phiếu thu

**+ Ngày lập phiếu:** Nhập ngày phát sinh

**+ Tài khoản tiền:** Nhấn F3 để chọn tài khoản tiền

**+ Loại tiền, Tỷ giá quy đổi:** tùy theo loại tiền sẽ có tỷ giá đối với VND

**+ Tạm ứng trước:** Nếu khoản tiền nhận về này liên quan đến khoản đã tạm ứng trước từ khách hàng có gốc ngoại tệ thì click chọn vào đây. Nếu không có thì để trống. Mục đích là có thể link qua phần kế toán phải thu để khi hạch toán kế toán phải thu cho các đơn hàng có ứng trước phần mềm giúp lấy tỷ giá đúng với phiếu tạm ứng này.

**+ Lý do thu (VN-EN):** Nhập lý do thu

**+ Người nhận tiền:** Nhập tên người trả tiền

**+ Địa chỉ:** Nhập địa chỉ người trả tiền

\+ Số phiếu hóa đơn phải thu

\+ Các nút

&#x20;\_ HĐ Trước: Phiếu kế tiếp

&#x20;\_ HĐ Sau: Phiếu trước

&#x20;\_ ĐC Phiếu: điều chỉnh chứng từ trực tiếp (chỉ hiện khi được phân quyền)

**Phần chi tiết:**

**+ Tài khoản:** nhấn F3 để chọn tài khoản tương ứng.

**+ Diễn giải(VN-EN):** Nhập diễn giải cho nghiệp vụ

**+Số tiền:** Nhập số tiền thu về

Nhập các thông tin của hóa đơn như:

* **Serial No.**: Số Sêri của hóa đơn phát hành
* **Số hóa đơn.**: Số hóa đơn
* **Ngày hóa đơn**: Ngày hóa đơn
* **Nhập mã khách hàng**: Nhấn F3 để chọn

Nhấn nút **Save** để ghi nhận thông tin thu tiền

* **Nợ**: TK tiền
* **Có**: TK tương ứng (TK định khoản ở vùng lưới)

Nhấn nút **in chứng từ** để in phiếu thu

![](<../.gitbook/assets/7 (18).png>)

**Ghi chú:**

Trường hợp nhập chi phí kèm thuế VAT đầu vào hay nhập doanh thu tiền mặt kèm thuế VAT đầu ra, trong phần chi tiết nhập 2 dòng:

\+ Dòng 1: Nhập nghiệp vụ tương ứng với số tiền chưa thuế

\+ Dòng 2: Nhập thuế đầu vào (133) hoặc đầu ra (333), việc nhập giá trị thuế VAT đầu vào hay đấu ra là do người dùng tự tính toán và nhập.

&#x20;

Tương tự với chi tiền mặt và chi ngân hàng , khi thu tiền từ hóa đơn phải thu

![](<../.gitbook/assets/8 (13).png>)

Bước 1: Nhấn F3 để tìm phiếu AR

Bước 2: Tại ô Số Phiếu Hóa đơn phải thu ấn F3 để chọn 1 hoặc nhiều phiếu

Bước 3: Ấn nút Xử lý (Execute) để dữ liệu ghi nhận vào lưới dữ liệu

Các thông tin được tự động ghi nhận :

\+ Số tiền

\+ Tài khoản đối ứng ( 131 công nợ )

\+ Diễn giải ( VN + EN )

\+ Loại tiền

\+ Tỷ Giá

\+ Thông tin hóa đơn ( Số hóa đơn , ngày hóa đơn , số serial )

\+ Mã khách hàng

\+ Số phiếu hóa đơn phải thu

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>
