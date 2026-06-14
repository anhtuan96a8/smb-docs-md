# 7.1 BOM

Phương pháp BOM (Bill of Materials — Định mức nguyên vật liệu) áp dụng cho doanh nghiệp sản xuất có xây dựng bảng định mức NVL chi tiết cho từng sản phẩm. Đây là phương pháp tính giá thành chính xác nhất, cho phép so sánh chênh lệch giữa NVL thực tế và định mức.

> Để chọn phương pháp tính giá thành, vào **Thông tin công ty** trong phần **Bảo mật**.

Quy trình gồm 11 bước:

**Bước 1 — Xây dựng bảng định mức cho mỗi sản phẩm**

Khai báo danh sách NVL và khối lượng cần thiết để sản xuất 1 đơn vị sản phẩm.

> **Ví dụ:** SP NIBA-07-CT cần 4 NVL: 7W LED PCB (0.570kg), LED E27 CAP (0.758kg), LED BULB A60 HOUSING 7W (0.852kg), LED DRIVER 7W (0.570kg).

**Bước 2 — Tổng hợp số lượng thành phẩm nhập kho trong kỳ**

Hệ thống tổng hợp từ phiếu nhập kho thành phẩm đã nhập liệu.

**Bước 3 — Tổng hợp sản phẩm dở dang và quy đổi SP hoàn thành tương đương**

Nhập số lượng SP dở dang cuối kỳ và tỷ lệ hoàn thành. Một mã SP có thể có nhiều tỷ lệ dở dang (đầu, giữa, cuối quy trình). Hệ thống tự tập hợp thành tổng SP hoàn thành tương đương.

**Bước 4 — Tính số lượng SP sản xuất trong kỳ**

> SP sản xuất trong kỳ = Thành phẩm nhập kho + Dở dang cuối kỳ − Dở dang đầu kỳ

**Bước 5 — Tính toán NVL theo BOM cho SP sản xuất**

Nhân định mức NVL (bước 1) × Số lượng SP sản xuất (bước 4).

**Bước 6 — Tổng hợp NVL xuất kho thực tế**

Nhấn **Cập nhật** để tự động lấy dữ liệu từ phiếu xuất kho NVL. Cần hoàn thành áp giá xuất kho NVL trước.

**Bước 7 — So sánh chênh lệch thực tế và định mức**

- NVL thực tế > Định mức: Chênh lệch ghi nhận vào giá vốn (Nợ TK 632 / Có TK 621).
- NVL thực tế < Định mức: Kế toán điều chỉnh lại định mức ở bước 1.

**Bước 8 — Xác định NVL để tính giá thành**

Giá trị NVL đưa vào tính giá thành là NVL thực tế hoặc định mức tùy từng mã.

**Bước 9 — Tính giá thành cho từng sản phẩm**

Phân bổ chi phí nhân công (TK 622) và SXC (TK 627) theo tỷ lệ chi phí NVL. Giá thành đơn vị tính bình quân bao gồm dở dang đầu kỳ.

**Bước 10 — Tính giá trị SP dở dang cuối kỳ**

> Giá trị dở dang cuối kỳ = SP hoàn thành tương đương × Giá thành đơn vị

**Bước 11 — Xác định giá trị thành phẩm nhập kho**

> Giá trị TP nhập kho = Dở dang đầu kỳ + CP SX phát sinh − Dở dang cuối kỳ

> **Lưu ý:** Chi tiết các phương pháp tính giá thành khác, xem tại trang [Tính giá thành](../phan-he-quan-ly-kho/tinh-gia-thanh.md).
