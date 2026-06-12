# 1.1 Danh mục

Kế toán sổ cái tổng hợp (viết tắt là GL) là phân hệ chủ đạo trong bất kỳ một công tác ghi sổ kế toán nào. Tất cả các bút toán mà người dùng nhập vào hệ thống bao gồm tiền, phải thu, phải trả, tài sản cố định đều sẽ được ghi nhận vào sổ cái tổng hợp.

Để tiện sử dung và theo dõi, phân hệ kế toán tổng hợp sẽ bao gồm các chức năng:

·       Danh mục

·       Nhập liệu

·       Xử lý

·       Truy vấn

·       Báo cáo

<figure><img src=".gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>



#### 1.1.1 Danh mục tài khoản

Phần mềm Smartbook sẽ cung cấp sẵn danh mục hệ thống tài khoản kế toán chính theo quy định của Thông tư số 200/TT-BTC do Bộ Tài Chính ban hành ngày 22/12/2014.

Smartbook còn cho phép người sử dụng thiết lập thêm tài khoản cấp 2, cấp 3… (tối đa là cấp 5) dựa trên danh mục tài khoản chính.

<figure><img src=".gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Hướng dẫn tạo tài khoản

·       Mục Mã tài khoản: Nhập mã tài khoản thứ cấp. (\*)

Lưu ý: Smartbook mặc định mã tài khoản là 7 chữ số.

·       Tên tài khoản (VN): Nhập diễn giải tài khoản bằng tiếng Việt.

·       Tên tài khoản (EN): Nhập diễn giải tài khoản bằng tiếng Anh.

·       Tên tài khoản (KR): Nhập diễn giải tài khoản bằng tiếng Hàn Quốc hoặc các ngôn ngữ khác

·       Loại tài khoản: Chọn loại tài khoản theo tính năng: Tài sản (Asset), Nợ phải trả (Liability), Doanh thu (Income), Expense (Chi phí)

·       Nhóm TK: Chọn nhóm Tài khoản chính (3 chữ số đầu)

·       Trạng thái: thiết lập tình trạng Tài khoản: Đang hoạt động (Active), Không hoạt động (Inactive)

Chọn Save để lưu Tài khoản vừa thiết lập, New để tạo mới, Close để đóng cửa sổ nhập.

Xóa tài khoản đã thiết lập

·       Chọn dòng tài khoản cần xóa

·       Nhấn nút Delete

Lưu ý: Việc thiết lập danh mục tài khoản ảnh hưởng trực tiếp đến sổ tổng hợp, sổ chi tiết và Báo cáo tài chính nên người sử dụng cần xem xét kỹ trước khi xoá tài khoản. Nếu đã tạo các nghiệp vụ hạch toán liên quan đến tài khoản cần xóa sẻ ảnh hưởng đến tính chính xác của các báo cáo.

&#x20;

#### 1.1.2 Danh mục nhóm tài khoản

Smartbooks cung cấp sẵn danh mục nhóm tài khoản cấp 1 và cấp 2 theo thông tư số 200/2014/TT-BTC ngày 22/12/2014.

Người sử dụng có thể thiết lập thêm nhóm tài khoản cấp 1 và cấp 2 sau khi được Bộ Tài Chính chấp thuận.

<figure><img src=".gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

Hướng dẫn tạo nhóm tài khoản

·       Mã nhóm: Nhập mã Tài khoản cấp 1 cần tạo.

·       Tên nhóm (VN): Diễn giải tiếng Việt.

·       Tên nhóm (EN): Diễn giải tiếng Anh.

·       Tên nhóm (KR): Diễn giải tiếng Hàn Quốc.

Chọn Save để lưu Tài khoản vừa thiết lập, New để tạo Tài khoản mới, Close để đóng cửa sổ nhập.

&#x20;

#### 1.1.3 Thiết lập Bảng cân đối kế toán

Smartbook thiết lập sẵn những khoản mục sẽ thể hiện trên Bảng Cân Đối Kế Toán (BCĐKT) theo Thông tư 200/2014/TT-BTC ngày 22/12/2014.

Người sử dụng có thể lược bỏ những khoản mục không cần thiết trên BCĐKT bằng cách nhấp vào ô chọn.

<figure><img src=".gitbook/assets/image (102).png" alt=""><figcaption></figcaption></figure>

&#x20;·       Bước 1: Thiết lập các thông tin: Mã số, diễn giải (VN, EN, KR), Tổng cộng (sử dụng hàm tính tổng), Tình trạng (được hiện lên trên BCĐKT hay ẩn đi).

·       Bước 2: Chỉ định các số dư tài khoản theo những code trên BCĐKT

&#x20;        o   BalType: có 2 loại (D - Số dư bên Nợ; C - Số dư bên Có)

&#x20;        o   Tài khoản: nhấn F3 để chọn tài khoản

&#x20;        o   Chuyển tiếp: số dư được tính trên BCĐKT là số - hay +

&#x20;        o   Mã số: mã số sử dung trên BCĐKT

&#x20;        o   Đầu kỳ, Cuối kỳ: số dư đầu kì, cuối kì của lần mở BCĐKT cuối cùng (có thể dùng để kiểm tra dữ liệu).

<figure><img src=".gitbook/assets/image (103).png" alt=""><figcaption></figcaption></figure>

• Bước 3: Thiết lập các Code BCĐKT con lên các Code BCĐKT cao hơn

<figure><img src=".gitbook/assets/image (104).png" alt=""><figcaption></figcaption></figure>

• Bước 4: Thiết lập các Code BCĐKT tổng lên các Code BCĐKTTổng cao nhất (các Code này không có số dư từ tài khoản)

<figure><img src=".gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure>

#### 1.1.4   Khai báo bút toán kết chuyển số dư tài khoản:

Chức năng này giúp người sử dụng thiết lập phương thức kết chuyển tự động cuối kỳ.

<figure><img src=".gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

&#x20;Hướng dẫn thiết lập

·       Tài khoản/ Tới tài khoản: Nhập tài khoản nguồn (Nhấn F3 để chọn hoặc nhập trực tiếp)

·       AmtType: Phương thức kết chuyển số dư của tài khoản nguồn (C - ghi nhận Có (credit) của tài khoản nguồn  hoặc D - ghi nhận Nợ (debit) của tài khoản nguồn)

·       StepCode: Các bước kết chuyển (ví dụ từ tài khoản loại 5, 6, 7, 8 sang 911 là bước 1 và từ 911 kết chuyển sang 4212 sẽ là bước thứ 2).

·       Diễn giải.
