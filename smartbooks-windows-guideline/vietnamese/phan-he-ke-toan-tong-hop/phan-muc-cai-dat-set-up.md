# 1.1 Phân mục cài đặt (Set up)

Gồm 4 khoản mục:

### PHÂN HỆ KẾ TOÁN TỔNG HỢP

Kế toán tổng hợp (viết tắt là GL) là phân hệ chủ đạo trong bất kỳ một công tác ghi sổ kế toán tài khoản trong Phần mềm này. Tất cả các giao dịch mà người sử dụng nhập vào hệ thống tài khoản tiền phải thu, tài khoản tiền phải trả, tài sản cố định, hàng tồn kho đều sẽ được kết chuyển vào sổ cái (sẽ được ghi hình thức sổ theo dõi). Từ chương trình này, người sử dụng có thể thiết lập, nhập liệu thông tin tài khoản, bút toán kết chuyển và kết xuất báo cáo tài chính.

Phân hệ GL bao gồm 4 phân mục: Phân mục cài đặt, Phân mục nhập liệu, Phân xử lý dữ liệu, Phân mục kết xuất báo cáo.

#### a) Danh mục tài khoản:

Phần mêm Smartbook sẽ cung cấp sẵn danh mục hệ thống tài khoản kế toán chính theo quy định của Thông tư số 200/TT-BTC do Bộ Tài Chính ban hành ngày 22/12/201&#x34;**.**

Smartbook còn cho phép người sử dụng thiết lập thêm tài khoản cấp 2, cấp 3… (tối đa là cấp 5) dựa trên danh mục tài khoản chính.

![](<../.gitbook/assets/0 (114).png>)

Hướng dẫn tạo tài khoản:

* Mục Mã tài khoản: Nhập mã tài khoản thứ cấp. (\*)

**Lưu ý**: Smartbook mặc định mã tài khoản là 7 chữ số.

* Tên tài khoản (VN): Nhập diễn giải tài khoản bằng tiếng Việt.
* Tên tài khoản (EN): Nhập diễn giải tài khoản bằng tiếng Anh.
* Tên tài khoản (KR): Nhập diễn giải tài khoản bằng tiếng Hàn Quốc hoặc các ngôn ngữ khác
* Loại tài khoản: Chọn loại tài khoản theo tính năng: Tài sản (Asset), Nợ phải trả (Liability), Doanh thu (Income), Expense (Chi phí)
* Nhóm TK: Chọn nhóm Tài khoản chính (3 chữ số đầu)
* Trạng thái: thiết lập tình trạng Tài khoản: Đang hoạt động (Active), Không hoạt động (Inactive)
* Chọn Save để lưu Tài khoản vừa thiết lập.
* Chọn New để tạo Tài khoản mới.
* Chọn Close để đóng cửa sổ nhập.
* Muốn xóa tài khoản đã thiết lập:

&#x20;\+ Nhấp vào Tài khoản cần xóa

&#x20;\+ Nhấn nút Delete.

**Lưu ý:** Việc thiết lập danh mục tài khoản ảnh hưởng trực tiếp đến sổ tổng hợp, chi tiết và Báo cáo tài chính nên người sử dụng cần xem xét kỹ trước khi xoá tài khoản. Nếu đã tạo các nghiệp vụ hạch toán liên quan đến tài khoản cần xóa sẻ ảnh hưởng đến tính chính xác của các báo cáo.

#### b) Danh mục nhóm tài khoản:

Smartbook cung cấp sẵn danh mục nhóm tài khoản cấp 1 và cấp 2 theo thông tư số 200/2014/TT-BTC ngày 22/12/2014.

Người sử dụng có thể thiết lập thêm nhóm tài khoản cấp 1 và cấp 2 sau khi được Bộ Tài Chính chấp thuận.

![](<../.gitbook/assets/1 (58).png>)

Hướng dẫn tạo nhóm tài khoản:

* Mã nhóm: Nhập mã Tài khoản cấp 1 cần tạo.
* Tên nhóm (VN): Diễn giải tiếng Việt.
* Tên nhóm (EN): Diễn giải tiếng Anh.
* Tên nhóm (KR): Diễn giải tiếng Hàn Quốc.
* Chọn Save để lưu Tài khoản vừa thiết lập.
* Chọn New để tạo Tài khoản mới.
* Chọn Close để đóng cửa sổ nhập.

#### c) Thiết lập Bảng cân đối kế toán:

Smartbook thiết lập sẵn những khoản mục sẽ thể hiện trên Bảng Cân Đối Kế Toán (BCĐKT) theo Thông tư 200/2014/TT-BTC ngày 22/12/2014.

Người sử dụng có thể lược bỏ những khoản mục không cần thiết trên BCĐKT bằng cách nhấp vào ô chọn.

**Bước 1**: thiết lập các thông tin: code, diễn giải (VN, EN, KR), IsTotal(là code tổng), InActive (có được hiện lên trên BCĐKT hay không).

![](<../.gitbook/assets/2 (50).png>)

**Bước 2**: Chỉ định các số dư tài khoản theo những code trên BCĐKT

* BalType: có 2 loại

\+ D: Số dư bên Nợ

\+ C: Số dư bên Có

* Acct: nhấn F3 để chọn tài khoản
* AmtType: số dư được tính trên BCĐKTlà số - hay +
* Code: Code của BCĐKT
* BegAmt, EndAmt: số dư đầu kì, cuối kì của lần mở BCĐKT cuối cùng (có thể dùng để kiểm tra dữ liệu).

![](<../.gitbook/assets/3 (32).png>)

**Bước 3**: Thiết lập các Code BCĐKT con lên các Code BCĐKT cao hơn

![](<../.gitbook/assets/4 (30).png>)

**Bước 4**: Thiết lập các Code BCĐKT tổng lên các Code BCĐKTTổng cao nhất (các Code này không có số dư từ tài khoản)

![](<../.gitbook/assets/5 (18).png>)

#### d) Khai báo bút toán kết chuyển số dư tài khoản:

Chức năng này giúp người sử dụng thiết lập phương thức kết chuyển tự động cuối kỳ.

![](<../.gitbook/assets/6 (17).png>)

Hướng dẫn thiết lập:

\- Acct: Nhập TK nguồn (Nhấn F3 chọn TK hoặc nhập trực tiếp)

\- AmtType: Phương thức kết chuyển số dư của TK nguồn

\+ C: ghi nhận Có (credit) của TK nguồn

\+ D: ghi nhận Nợ (debit) của TK nguồn

\- StepCode: Các bước kết chuyển (ví dụ từ TK loại 5, 6, 7, 8 sang 911 là bước 1 và từ 911 kết chuyển sang 4212 sẽ là bước thứ 2).
