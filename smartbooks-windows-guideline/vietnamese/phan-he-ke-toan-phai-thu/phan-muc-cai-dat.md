# 3.1 Phân mục cài đặt

### Danh mục khách hàng

**Nghiệp vụ áp dụng:** Khi cần khai báo, quản lý thông tin các đối tượng (khách hàng, nhà cung cấp) giao dịch với doanh nghiệp. Đây là danh mục cốt lõi phục vụ theo dõi công nợ chi tiết (Phải thu TK 131, Phải trả TK 331), quản lý thông tin xuất hóa đơn và tự động liên kết dữ liệu khi hạch toán.

> **Ví dụ:** Khai báo KH "Công ty CP Thương mại XYZ" — MST 0301234567, TK phải thu mặc định 131, thuế suất đầu ra 10%, loại tiền VND.

![](../.gitbook/assets/image68.png)

Để khai báo thông tin khách hàng / nhà cung cấp, người dùng thực hiện như sau:

- **Thông tin cơ bản:**
  - Mã / Tên đối tượng (KH/NCC): Nhập mã định danh và tên đầy đủ theo giấy phép đăng ký kinh doanh.
  - Là NCC / Là KH: Tích chọn vai trò đối tượng; có thể chọn đồng thời cả hai nếu vừa mua vừa bán.
  - Mã số thuế / Địa chỉ / Điện thoại / Email: Nhập thông tin liên hệ và mã số thuế để đối chiếu bảng kê thuế GTGT.

- **Thông tin mặc định:**
  - Thời hạn thanh toán: Chọn điều khoản thanh toán (00 - Tiền mặt, 01 - 30 ngày...) để tự động tính ngày đến hạn.
  - Thuế suất: Chọn mức thuế GTGT mặc định — hệ thống tự gán mã thuế này cho đối tượng khi hạch toán.
  - Tài khoản phải thu / Phải trả / Doanh thu: Gán tài khoản công nợ và doanh thu mặc định cho đối tượng.
  - Loại tiền / Tỷ giá: Chọn đồng tiền giao dịch (mặc định VND).

- **Các nút chức năng:**
  - Xuất Excel / Nhập liệu: Xuất dữ liệu ra file Excel hoặc nhập dữ liệu từ file ngoài.
  - Lưu / Sao chép / Thêm mới / Xóa / Đóng: Các thao tác tiêu chuẩn.

> **Lưu ý:** Danh mục KH/NCC dùng chung cho cả phân hệ Phải thu (AR) và Phải trả (AP). Khi tích chọn đồng thời "Là KH" và "Là NCC", đối tượng sẽ xuất hiện ở cả hai phân hệ.
