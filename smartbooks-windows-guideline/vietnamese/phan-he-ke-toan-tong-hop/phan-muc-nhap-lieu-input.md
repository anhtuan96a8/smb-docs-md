# 1.2 Phân mục nhập liệu

### Bút toán tổng hợp

**Nghiệp vụ áp dụng:** Hạch toán các nghiệp vụ phát sinh không thuộc phân hệ chuyên trách: bút toán điều chỉnh, phân bổ chi phí trả trước (142→642), trích trước chi phí (642→335), kết chuyển lãi/lỗ cuối kỳ (911→421).

> **Ví dụ nghiệp vụ:** Chứng từ GL26/030116 ngày 31/03/2026 — Trích BHXH, BHYT, BHTN người VN T03/2026 phần Công ty trả: Nợ TK 62716 / Có TK 3383, số tiền 7.991.550đ. Tổng chứng từ trên ảnh là 264.980.405đ và có 5 dòng định khoản.

![](<../.gitbook/assets/image33.png>)

Để nhập chứng từ kế toán tổng hợp, người dùng thực hiện như sau:

1. Nhấn **Thêm mới** để tạo chứng từ mới; trường **Số tham chiếu** hiển thị `<NEW>` hoặc số tạm theo cấu hình.
2. Nhập **Ngày chứng từ** và kiểm tra **Tháng kế toán**. Hai thông tin này phải cùng kỳ để chứng từ được lưu đúng sổ.
3. Chọn **Cách xử lý**, **Loại tiền** và **Tỷ giá**. Với giao dịch VND, tỷ giá thường là 1.00; với ngoại tệ, kiểm tra tỷ giá trước khi nhập chi tiết.
4. Nhập ít nhất một nội dung **Diễn giải VN / EN / KR** để chứng từ có căn cứ tra cứu về sau.
5. Nhập từng dòng định khoản ở lưới chi tiết: **TK Nợ**, **TK Có**, **Tiền**, thông tin hóa đơn/công nợ và các mã phân bổ nếu nghiệp vụ yêu cầu.
6. Kiểm tra tổng tiền và các dòng phát sinh; nếu dùng chứng từ thuế hoặc công nợ, rà lại **Mã KH/NCC**, **Số hóa đơn**, **Số Seri**, **Ngày hóa đơn**.
7. Nhấn **Lưu**. Sau khi lưu ở trạng thái Chưa ghi sổ, vào **Phân mục xử lý → Ghi sổ nhiều chứng từ** để ghi sổ khi đã kiểm tra xong.

- **Thông tin chung:**
  - Số tham chiếu: Mặc định `<NEW>` khi thêm mới; nhấn **F3** để tìm chứng từ cũ.
  - Ngày chứng từ / Tháng kế toán / Số chứng từ: Hệ thống tự động hiển thị theo ngày hiện tại và quy tắc cấu hình.
  - Cách xử lý / Loại tiền / Tỷ giá: Chọn trạng thái chứng từ và loại tiền tệ (mặc định VND, tỷ giá 1.00).
  - Diễn giải VN / EN / KR: Nhập nội dung tóm tắt nghiệp vụ để tra cứu sau này.

- **Lưới chi tiết định khoản:**
  - TK Nợ / TK Có: Nhập trực tiếp hoặc nhấn **F3** để chọn tài khoản ghi Nợ/Có.
  - Thành tiền / Sau QĐ: Số tiền hạch toán theo nguyên tệ và sau quy đổi.
  - Mã KH / NCC, Số hóa đơn, Số Seri, Ngày hóa đơn: Nhập thông tin công nợ và hóa đơn GTGT nếu có.
  - Mã chi phí / Vụ việc / Lợi nhuận: Chọn khoản mục phân bổ tương ứng (dùng cho báo cáo chi phí theo trung tâm).

- **Các nút chức năng:**
  - P. trước / P. Sau: Duyệt chứng từ liền kề.
  - Xuất lưới: Xuất dữ liệu định khoản ra Excel.
  - In chứng từ: In hoặc xuất PDF theo mẫu.
  - Nhập liệu: Bật/tắt chế độ nhập định khoản từ file Excel.
  - Tệp mẫu: Xuất mẫu Excel đúng cấu trúc để kế toán điền dữ liệu trước khi nhập vào hệ thống.
  - Lưu / Sao chép / Thêm mới / Xóa / Đóng: Các thao tác tiêu chuẩn.

- **Lưu ý khi thao tác:**
  - Chứng từ ở trạng thái Đã ghi sổ không nên sửa trực tiếp; cần thực hiện bỏ ghi sổ/điều chỉnh theo quyền được phân công.
  - Khi nhập dữ liệu từ Excel, **Loại tiền** và **Tỷ giá** lấy theo phần thông tin chung trên màn hình, không lấy từ file Excel. Hãy chọn đúng trước khi nhấn **Nhập liệu**.
  - Nếu tài khoản yêu cầu mã chi phí, mã vụ việc hoặc mã lợi nhuận, cần nhập đủ các mã này để báo cáo quản trị lên đúng số liệu.
  - Với tài khoản công nợ hoặc nghiệp vụ có hóa đơn, nhập đủ mã đối tượng và thông tin hóa đơn để đối chiếu công nợ, VAT và truy vấn chứng từ sau này.

> **Hệ thống tự kiểm tra khi Lưu:**
> - Ngày chứng từ phải thuộc đúng tháng kế toán và kỳ kế toán chưa đóng.
> - Số chứng từ không được trùng trong cùng kỳ và phải đúng quy tắc đánh số.
> - Phải có ít nhất một dòng định khoản và mỗi dòng phải có đủ TK Nợ, TK Có, số tiền hợp lệ.
> - Tài khoản phải thuộc phạm vi được phép hạch toán trong phân hệ kế toán tổng hợp.
> - Nếu tài khoản yêu cầu theo dõi công nợ, chi phí, vụ việc hoặc lợi nhuận, hệ thống sẽ yêu cầu nhập các mã tương ứng.
> - Với tài khoản thuế 133/333 có thông tin thuế, cần nhập số tiền trước thuế khi hệ thống yêu cầu.

> **Lưu ý:** Sau khi Lưu, chứng từ ở trạng thái Chưa ghi sổ. Vào **Phân mục xử lý → Ghi sổ nhiều chứng từ** để ghi sổ hàng loạt.

---

### Bù trừ công nợ

**Nghiệp vụ áp dụng:** Thực hiện bù trừ công nợ giữa Phải thu và Phải trả của cùng một đối tượng (khách hàng đồng thời là nhà cung cấp), bù trừ giữa các đối tượng khác nhau, hoặc cấn trừ khoản trả trước với hóa đơn phát sinh.

> **Ví dụ nghiệp vụ:** Chứng từ OF26/010001 ngày 05/01/2026 — Trích trước 5% bảo hành hệ thống xử lý nước thải (HTC): Nợ TK 3311 số tiền 5.744.310đ cho đối tượng HTC 1 / Có TK 3311 số tiền 5.744.310đ cho đối tượng MOITRUONGH... Chênh lệch trên màn hình là 0.00.

![](<../.gitbook/assets/image34.png>)

Để nhập chứng từ bù trừ công nợ, người dùng thực hiện như sau:

1. Nhấn **Thêm mới** để tạo chứng từ bù trừ; trường **Số tham chiếu** hiển thị `<NEW>` hoặc số tạm.
2. Nhập **Ngày chứng từ**, kiểm tra **Tháng kế toán** và **Số chứng từ** theo kỳ bù trừ.
3. Chọn **Cách xử lý**. Khi đang nhập và cần kiểm tra thêm, giữ chứng từ ở trạng thái Chưa ghi sổ.
4. Chọn **Loại tiền** và **Tỷ giá**. Với giao dịch VND, tỷ giá thường là 1.00.
5. Nhập diễn giải nghiệp vụ bù trừ, ví dụ lý do cấn trừ công nợ hoặc khoản bảo hành/trả trước cần xử lý.
6. Nhập lưới chi tiết theo nguyên tắc 1 dòng Nợ đối ứng với một hoặc nhiều dòng Có, hoặc ngược lại.
7. Kiểm tra tổng **Nợ**, tổng **Có** và **Chênh lệch**. Chỉ lưu khi chênh lệch bằng 0.00.
8. Nhấn **Lưu**, sau đó ghi sổ theo quy trình xử lý chứng từ khi nghiệp vụ đã được kiểm tra.

- **Thông tin chung:**
  - Số tham chiếu: Mặc định `<NEW>` khi thêm mới; nhấn **F3** để tìm chứng từ cũ.
  - Ngày chứng từ / Tháng kế toán / Số chứng từ: Hệ thống tự động hiển thị theo ngày hiện tại.
  - Cách xử lý / Loại tiền / Tỷ giá: Chọn trạng thái chứng từ và loại tiền tệ (mặc định VND).
  - Diễn giải VN / EN / KR: Nhập nội dung tóm tắt nghiệp vụ.

- **Lưới chi tiết định khoản:**
  - Tài khoản + Nợ/Có: Nhập theo cặp bù trừ — 1 dòng Nợ và nhiều dòng Có hoặc ngược lại.
  - Tiền / Sau QĐ: Số tiền hạch toán theo nguyên tệ và sau quy đổi.
  - Mã KH / NCC, Số hóa đơn, Số Seri, Ngày hóa đơn: Bắt buộc nhập để theo dõi công nợ chi tiết theo từng hóa đơn.
  - Mã chi phí / Vụ việc / Lợi nhuận: Chọn khoản mục phân bổ nếu cần.

- **Các nút chức năng:**
  - P. trước / P. Sau: Duyệt chứng từ liền kề.
  - Xuất lưới: Xuất dữ liệu định khoản ra Excel.
  - In chứng từ: In hoặc xuất PDF theo mẫu.
  - Nhập liệu: Bật/tắt chế độ nhập từ file Excel.
  - Lưu / Sao chép / Thêm mới / Xóa / Đóng: Các thao tác tiêu chuẩn.

- **Lưu ý khi thao tác:**
  - Tổng Nợ và tổng Có phải bằng nhau; nếu còn chênh lệch, chứng từ chưa đủ điều kiện lưu/ghi sổ.
  - Bù trừ công nợ cần nhập đúng đối tượng trên từng dòng để sổ chi tiết công nợ của khách hàng/nhà cung cấp không bị lệch.
  - Tài khoản dùng cho bù trừ phải là tài khoản công nợ phù hợp; tránh nhập tài khoản doanh thu, chi phí hoặc tiền nếu nghiệp vụ chỉ là cấn trừ công nợ.
  - Khi nhập dữ liệu từ Excel, loại tiền và tỷ giá lấy theo phần thông tin chung trên màn hình; dữ liệu trong file chỉ dùng cho tài khoản, số tiền, đối tượng và thông tin hóa đơn.

> **Hệ thống tự kiểm tra khi Lưu:**
> - Ngày chứng từ phải khớp với tháng kế toán và kỳ kế toán còn mở.
> - Phải có diễn giải ở ít nhất một ngôn ngữ VN/EN/KR.
> - Mỗi dòng phải có tài khoản, loại tiền, số tiền Nợ/Có hợp lệ và không âm.
> - Tất cả dòng chi tiết phải dùng cùng loại tiền với phần thông tin chung.
> - Với tài khoản công nợ, hệ thống yêu cầu mã khách hàng/nhà cung cấp hoặc mã nhân viên khi tài khoản cần theo dõi đối tượng.
> - Kết cấu bù trừ phải là 1 Nợ - nhiều Có hoặc 1 Có - nhiều Nợ, và tổng Nợ phải bằng tổng Có.

> **Lưu ý:** Tổng Nợ phải bằng tổng Có trước khi Lưu. Chứng từ sau khi Lưu ở trạng thái Chưa ghi sổ — cần ghi sổ để phản ánh lên sổ cái.
