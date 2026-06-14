# 15. Đồng bộ hóa dữ liệu

Khi doanh nghiệp có nhiều chi nhánh hoặc văn phòng, cần đồng bộ dữ liệu kế toán giữa hệ thống Local (tại công ty) và hệ thống Trung tâm (máy chủ SSAudit) theo thời gian thực qua Internet.

### Mô hình hoạt động

SmartBooks sử dụng công nghệ **SQL Server Replication** để đồng bộ dữ liệu hai chiều:

- **Upload Data:** Gửi dữ liệu từ Local lên Trung tâm.
- **Download Data:** Nhận dữ liệu từ Trung tâm về Local.

### Cài đặt

- **Phần 1 — Hệ thống Local:** Cài đặt tại công ty cần quản lý.
- **Phần 2 — Hệ thống Trung tâm:** Cài đặt tại máy chủ SSAudit — dữ liệu được quản lý tập trung.

### Ưu điểm

- An toàn dữ liệu và tính sẵn sàng cao.
- Khả năng sao lưu, phục hồi và bảo vệ hệ thống từ xa.
- Thông tin phản ánh kịp thời, chính xác.
- Đảm bảo an toàn và bảo mật khi truyền thông.
- Kết hợp ưu điểm của cả giải pháp Winform (nhanh, ổn định) và Webform (truy cập mọi nơi).

> **Lưu ý:** Quá trình đồng bộ thực hiện tự động khi có kết nối Internet. Hệ thống Trung tâm có khả năng khôi phục dữ liệu Local nhanh chóng qua Internet.
