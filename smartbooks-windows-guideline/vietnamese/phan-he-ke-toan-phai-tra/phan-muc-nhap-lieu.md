# 2.2 Phân mục nhập liệu

## Hóa đơn nhà cung cấp

**-** Những hóa đơn có theo dõi nhập xuất tồn thì nhập ở phân hệ quản lý kho. Khi xử lý thì sẽ link qua phân hệ phải trả.

\- Hóa đơn cho các khoản nguyên liệu, vật tư và chi phí dịch vụ khác (như chi phí điện, nước, điện thoại, thuê nhà, …) mà treo công nợ thì: Các hóa đơn này sẽ được nhập trong phân hệ kế toán phải trả.

![](<../.gitbook/assets/0 (108).png>)

Chi tiết quy trình xử lý hóa đơn từ nhà cung cấp

Trong Form nhập dữ liệu thường gồm 2 phần:

**Phần Tổng hợp**: Những thông tin chung của hóa đơn và thường nằm phía trên.

* **Số Lô:** Để trống, chương trình sẽ tự sinh ra số nà.
* **Kỳ kế toán:**(ví dụ hóa đơn của tháng 7 năm 2015: 07-2015) Số tháng, phát sinh
* **Số Chứng từ**: Nhập số chứng t&#x1EEB;**.**
* **Ngày Chứng từ**: phải nằm trong kỳ kế toán.
* **Loại Chứng từ:** chọn Voucher.
* **Nhà Cung Cấp:** Nhấn F3 để chọn nhà cung cấp hoặc nhập tên mã nhà cung cấp (Phần mềm sẽ tự động kiểm tra nhập đúng mã hay không)
* **Tài khoản ngân hàng:** Lựa chọn tài khoản ngân hàng để phần mềm lấy tự động tỷ giá bán ra nếu đồng tiền là ngoại tệ do đã khai báo ở phân hệ quản trị hệ thống.
* **Diễn giải (VN - EN):** Nhập diễn giải
* **Số đơn đặt hàng:** (nhập số đơn đặt hàng nếu có)
* **Ngày thanh toán:** Chọn ngày thanh toán.
* **Thời hạn thanh toán:** Nhấn F3 để chọn.
* **Tài khoản công nợ:** Nhấn F3 để chọn.

**Phần Chi tiết:** những thông tin chi tiết của hóa đơn, mỗi chi tiết là 1 dòng trong lưới



* **Account:** Nhấn F3 để chọn tài khoản chi phí hoặc nhập tài khoản (Phần mềm sẽ tự động kiểm tra tài khoản đúng hay không, trong trường hợp nhập sai tài khoản phần mềm sẽ không cho phép chuyển sang thông tin khác)
* **Tạm ứng trước đây**: Nếu có tạm ứng trước tiền cho đơn hàng này bằng ngoại tệ thì chọn đến phiếu đã tạm ứng để lấy tỷ giá và số tiền đã ứng trước của phiếu này. Phần chênh lệch còn lại thì hạch toán theo tỷ giá bán ra tại ngày nhận khoản công nợ.
* **Loại tiền**: Chọn loại tiền thanh toán
* **Tỷ giá Quy đổi:** Nhập tỷ giá Loại Tiền thanh toán so với VND
* Ví dụ: Loại tiền USD, tỉ giá thời điểm hóa đơn là 21500: nhập 21500
* Nếu Loại tiền là VND: Tỉ giá là 1
* **Thành tiền**: Gõ số tiền trước thuế hoặc tiền ngoại tệ
* **Thành tiền sau quy đổi**: Là số tiền sau khi nhân với tỷ giá
* **Thuế suất**: Nhần F3 để chọn loại thuế suất tương ứng.
* **Tiền thuế là tiền thuế thực tế phát sinh**. Tiền thuế sau quy đổi là tiền thuế sau khi nhân với (tỷ giá nếu có).
* **Diễn giải (VN - EN):** Sẽ tự động lấy diễn giải đã nhập ở phần tổng hợp ở trên
* **Nhập số hóa đơn**
* **Nhập ngày hóa đơn**

**Các Lựa chọn khác**

![](<../.gitbook/assets/1 (69).png>)

*
  * Nút HĐ Trước : Phiếu hạch toán tiếp theo
  * Nút HĐ Sau : Phiếu hạch toán trước
  * Nút ĐC Phiếu : Điều chỉnh chứng từ trực tiếp trên form nhập nếu người dùng được phân quyền.
  * Nút Tạo NCC : Tạo Thông tin nhà cung cấp trực tiếp mà không cần quay lại Menu chính và vào lại phần thông tin nhà cung cấp

![](<../.gitbook/assets/2 (43).png>)
