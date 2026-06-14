# Cài đặt hệ thống

### Thiết lập thông tin công ty

**Nghiệp vụ áp dụng:** Khai báo thông tin doanh nghiệp (tên công ty, địa chỉ, MST, logo, năm tài chính) — đây là bước bắt buộc khi bắt đầu sử dụng phần mềm hoặc khi cần thay đổi năm tài chính đang làm việc.

![](../.gitbook/assets/image6.png)

![](../.gitbook/assets/image7.png)

Để thiết lập thông tin công ty, người dùng thực hiện như sau:

1. Nhập **Tên công ty**, **Địa chỉ**, **Mã số thuế** và các thông tin cơ bản.
2. Chọn **Năm tài chính** đang làm việc.
3. Chọn **Phương thức tính giá thành phẩm nhập kho** phù hợp với đặc thù doanh nghiệp.
4. Nhấn **Lưu** để hoàn tất.

- **Các nút chức năng và tùy chọn:**
  - Lưu: Ghi nhận thông tin công ty và thiết lập năm tài chính/phương pháp tính giá.
  - Chọn logo/ảnh: Cập nhật logo dùng trên mẫu in, báo cáo hoặc chứng từ nếu màn hình có hiển thị.
  - Năm tài chính: Xác định năm dữ liệu đang làm việc, ảnh hưởng đến việc xem chứng từ và số dư đầu kỳ.
  - Phương thức tính giá thành phẩm nhập kho: Chọn phương pháp tính giá tồn kho/giá thành áp dụng cho doanh nghiệp.

> **Hệ thống tự kiểm tra khi Lưu:** Tên công ty, năm tài chính và các thông tin bắt buộc không được để trống. Không nên đổi năm tài chính khi người dùng khác đang nhập chứng từ.

- **Thiết lập năm tài chính:**

| Nghiệp vụ | Hướng dẫn |
|----|-----|
| **Năm kết chuyển số dư cuối kỳ** | Kết chuyển đầu kỳ năm 2025 => chỉnh lại năm tài chính là 2024 |
| **Tìm kiếm chứng từ năm tài chính** | Tìm kiếm chứng từ năm 2020 => chỉnh lại năm tài chính là năm 2020 – số chứng từ sẽ hiển thị từ năm tài chính tới năm hiện tại |

- **Phương thức tính giá thành phẩm nhập kho:**

| Mã | Phương thức | Mô tả |
|----|-------------|-------|
| **AVRG** | Bình quân gia quyền (Average Cost) | Giá xuất kho được tính theo đơn giá bình quân của hàng tồn trong kỳ. Đây là phương pháp phổ biến, phù hợp với doanh nghiệp có số lượng nhập xuất nhiều. |
| **SPEC** | Đích danh (Specific Identification) | Theo dõi và tính giá riêng cho từng lô hàng, serial hoặc mã hàng cụ thể. Phù hợp với hàng hóa có giá trị lớn hoặc cần quản lý riêng biệt. |
| **FIFO** | Nhập trước – Xuất trước (First In First Out) | Hàng nhập trước sẽ được xuất trước. Giá tồn kho cuối kỳ thường gần với giá thị trường hiện tại. |
| **SELLING PRICE** | Giá bán (Selling Price) | Tính giá dựa trên giá bán thiết lập của hàng hóa. Thường sử dụng cho mục đích quản trị hoặc ngành bán lẻ đặc thù. |
| **SIMPLE METHOD** | Phương pháp đơn giản | Phương pháp tính giá cơ bản theo cấu hình hệ thống, áp dụng cho mô hình quản lý đơn giản. |
| **COEFFICIENT** | Hệ số (Coefficient Method) | Phân bổ và tính giá thành theo hệ số quy đổi giữa các sản phẩm hoặc nhóm sản phẩm. Thường dùng trong sản xuất nhiều thành phẩm liên quan. |
| **BOM** | Định mức nguyên vật liệu (Bill of Materials) | Tính giá thành dựa trên định mức nguyên vật liệu, nhân công và chi phí cấu thành sản phẩm. Áp dụng cho doanh nghiệp sản xuất. |

> **Lưu ý:** Đây là thiết lập **năm tài chính** đang làm việc trên thông tin công ty (để lấy số dư đầu kỳ / tìm chứng từ theo năm), **không phải** chức năng *Kết chuyển cuối kỳ*. Việc kết chuyển/đóng kỳ thực hiện ở **GL → Xử lý → Kết chuyển cuối kỳ**.

---

### Đổi mật khẩu

**Nghiệp vụ áp dụng:** Khi người dùng cần thay đổi mật khẩu đăng nhập hệ thống để đảm bảo bảo mật tài khoản.

![](../.gitbook/assets/image8.png)

Để đổi mật khẩu, người dùng thực hiện như sau:

1. Nhập **Mật khẩu hiện tại**.
2. Nhập **Mật khẩu mới**.
3. Nhập lại **Xác nhận mật khẩu** mới.
4. Nhấn **OK** để hoàn tất.

![](../.gitbook/assets/image9.png)

- **Các nút chức năng:**
  - OK: Xác nhận đổi mật khẩu.
  - Cancel/Đóng: Hủy thao tác và giữ nguyên mật khẩu cũ.

> **Hệ thống tự kiểm tra khi đổi mật khẩu:** Mật khẩu hiện tại phải đúng; mật khẩu mới và xác nhận mật khẩu phải trùng nhau.

> **Lưu ý:** Mật khẩu mới và xác nhận mật khẩu phải trùng khớp. Nên đổi mật khẩu định kỳ để đảm bảo an toàn dữ liệu kế toán.

---

### Phân quyền truy cập

**Nghiệp vụ áp dụng:** Quản trị viên thiết lập quyền truy cập hệ thống cho từng người dùng — phân quyền theo từng màn hình và từng phân hệ/chức năng. Mỗi người dùng thuộc một nhóm; khi lưu quyền, hệ thống hỏi có đồng bộ quyền cho cả nhóm hay không.

#### Tạo mới "Người sử dụng"

Cho phép Quản trị viên khởi tạo và quản lý các tài khoản đăng nhập độc lập cho từng nhân sự.

![](../.gitbook/assets/image10.png)

Để thêm người dùng, người dùng thực hiện như sau:

1. Nhập **Mã người dùng** (hoặc nhấn **F3** để tìm kiếm người dùng hiện có).
2. Điền các thông tin cơ bản: **Tên người dùng**, **Số điện thoại**, **Địa điểm**, **Email**.
3. Thiết lập **Mật khẩu** cho tài khoản mới.
4. Nhấn **Lưu** để lưu.

![](../.gitbook/assets/image11.png)

- **Các nút chức năng:**
  - F3 tại Mã người dùng: Tìm người dùng đã có để xem hoặc chỉnh sửa.
  - Lưu: Lưu tài khoản người dùng.
  - Thêm mới: Tạo tài khoản mới.
  - Xóa: Xóa tài khoản chưa còn sử dụng theo quyền quản trị.
  - Đóng: Thoát khỏi màn hình.

> **Hệ thống tự kiểm tra khi Lưu:** Mã người dùng không được trùng và các thông tin bắt buộc như tên người dùng/mật khẩu cần nhập đầy đủ.

#### Phân quyền truy cập phân hệ

Xác định người dùng được phép truy cập những phân hệ nào (GL, AP, AR, CA, IN…).

![](../.gitbook/assets/image12.png)

![](../.gitbook/assets/image13.png)

Để phân quyền phân hệ, người dùng thực hiện như sau:

1. Nhập tên người dùng hoặc nhấn **F3** để chọn người dùng cần phân quyền — hệ thống tải toàn bộ danh sách phân hệ.
2. Tại lưới dữ liệu, tích chọn các phân hệ muốn cấp quyền truy cập (VD: GL, AP, CA…) và bỏ tích những phân hệ không muốn hiển thị.
3. Nhấn **Lưu** để hoàn tất.

- **Ô chọn và nút chức năng:**
  - Ô chọn từng phân hệ: Cấp hoặc bỏ quyền truy cập phân hệ đó cho người dùng.
  - Chọn tất cả/Bỏ chọn tất cả nếu có trên màn hình: Cấp hoặc bỏ nhanh toàn bộ quyền phân hệ đang hiển thị.
  - Lưu: Lưu quyền phân hệ.
  - Đóng: Thoát khỏi màn hình.

> **Hệ thống tự kiểm tra khi Lưu:** Phải chọn đúng người dùng trước khi lưu quyền. Nếu người dùng thuộc nhóm, hệ thống có thể hỏi có áp dụng thay đổi cho cả nhóm hay không.

#### Phân quyền truy cập chi tiết

Phân quyền chi tiết theo chức năng trong từng phân hệ đã được cấp — kiểm soát quyền thêm, xóa, sửa, sao chép, in chứng từ, nhập liệu, xuất Excel, ghi sổ, bỏ ghi sổ.

> **Ví dụ:** Phân quyền truy cập phân hệ "Quản lý kho" nhưng chỉ được phép xem báo cáo nhập xuất tồn, tình hình tồn kho — không được phép thêm/xóa/sửa chứng từ kho.

![](../.gitbook/assets/image14.png)

Để phân quyền chi tiết, người dùng thực hiện như sau:

1. Nhấn **F3** để chọn người dùng — hệ thống tải danh sách chức năng.
2. Nếu muốn kế thừa nhanh bộ quyền đã có, chọn người dùng tại ô **Sao chép quyền từ**, sau đó nhấn nút sao chép để hệ thống lấy quyền chi tiết của người dùng đó sang người dùng đang phân quyền.
3. Tại lưới dữ liệu, tích chọn hoặc bỏ tích các chức năng cần phân quyền (xem, thêm, xóa, sửa, sao chép, in chứng từ, nhập liệu, xuất Excel, ghi sổ, bỏ ghi sổ).
4. Nhấn **Lưu** để hoàn tất.

![](../.gitbook/assets/image15.png)

- **Ô chọn quyền chi tiết:**
  - Xem: Cho phép mở màn hình và xem dữ liệu.
  - Thêm: Cho phép tạo chứng từ/danh mục mới.
  - Sửa: Cho phép chỉnh dữ liệu chưa bị khóa.
  - Xóa: Cho phép xóa chứng từ/danh mục theo điều kiện hệ thống.
  - Sao chép: Cho phép nhân bản chứng từ.
  - In: Cho phép in chứng từ/báo cáo.
  - Nhập liệu: Cho phép nhập dữ liệu từ Excel hoặc nhập dữ liệu hàng loạt nếu màn hình hỗ trợ.
  - Xuất Excel: Cho phép xuất lưới/báo cáo ra Excel.
  - Ghi sổ/Bỏ ghi sổ: Cho phép chuyển trạng thái chứng từ giữa Chưa ghi sổ và Đã ghi sổ.

- **Nút và trường chức năng:**
  - Sao chép quyền từ: Chọn một người dùng nguồn để sao chép nhanh toàn bộ quyền chi tiết sang người dùng đang phân quyền. Chức năng này chỉ sao chép quyền thao tác trên màn hình, không sao chép mật khẩu, thông tin cá nhân hoặc trạng thái đăng nhập của người dùng nguồn.
  - F3 tại ô người dùng: Mở danh sách người dùng để chọn đúng tài khoản cần phân quyền.
  - Lưu: Lưu bộ quyền chi tiết sau khi chỉnh sửa hoặc sau khi sao chép quyền.
  - Đóng: Thoát khỏi màn hình; các thay đổi chưa lưu sẽ không được áp dụng.

- **Lưu ý khi thao tác:**
  - Sau khi dùng **Sao chép quyền từ**, cần rà lại các ô chọn quan trọng trước khi lưu, nhất là quyền xóa, ghi sổ, bỏ ghi sổ, nhập liệu và xuất Excel.
  - Mỗi người dùng thuộc một nhóm — khi lưu quyền, hệ thống hỏi có đồng bộ quyền cho cả nhóm hay không.
  - Sau khi đổi quyền, người dùng cần **đăng xuất và đăng nhập lại** để quyền mới có hiệu lực.
  - Nên phân quyền theo nguyên tắc "quyền tối thiểu" — chỉ cấp những quyền cần thiết cho công việc.

> **Hệ thống tự kiểm tra khi Lưu:** Người dùng cần được cấp quyền phân hệ trước khi cấp quyền chi tiết trong phân hệ đó. Nếu sao chép quyền từ người dùng khác nhưng người dùng hiện tại chưa có quyền truy cập phân hệ tương ứng, quyền chi tiết của phân hệ đó có thể không có hiệu lực cho đến khi quyền phân hệ được cấp bổ sung.

---

### Danh sách các bút toán đã xóa

**Nghiệp vụ áp dụng:** Quản trị viên cần theo dõi, kiểm tra lại toàn bộ các chứng từ hoặc bút toán kế toán đã bị xóa trên hệ thống trong một khoảng thời gian nhất định — đảm bảo tính minh bạch và kiểm soát dữ liệu.

Để xem danh sách bút toán đã xóa, người dùng thực hiện như sau:

1. Nhập khoảng thời gian vào ô **Từ ngày / Đến ngày**.
2. Nhấn **View / Xem lưới** để truy xuất danh sách chứng từ đã xóa.

![](../.gitbook/assets/image16.png)

- **Các nút chức năng:**
  - View/Xem lưới: Tải danh sách chứng từ đã xóa theo khoảng ngày.
  - Xuất Excel: Xuất danh sách phục vụ kiểm tra hoặc kiểm toán nội bộ nếu màn hình hỗ trợ.
  - Đóng: Thoát khỏi màn hình.

> **Hệ thống tự kiểm tra khi xem lưới:** Khoảng ngày phải hợp lệ. Nếu không có dữ liệu, kiểm tra lại khoảng thời gian hoặc quyền truy cập của người dùng.

> **Lưu ý:** Chức năng này chỉ dành cho Quản trị viên. Danh sách lưu vết ai đã xóa, thời điểm xóa — phục vụ kiểm toán nội bộ.

---

### Nhập liệu từ Excel

**Nghiệp vụ áp dụng:** Nhập dữ liệu chứng từ hàng loạt từ file Excel vào từng phân hệ kế toán tương ứng — giúp tối ưu hóa thời gian nhập liệu, giảm thiểu sai sót thủ công và nâng cao hiệu suất xử lý dữ liệu.

![](../.gitbook/assets/image17.png)

Để nhập dữ liệu từ Excel, người dùng thực hiện như sau:

1. Vào menu **Nhập liệu → Nhập liệu từ Excel**.
2. Chọn **Phân hệ** cần nhập dữ liệu, ví dụ **GL - Tổng Hợp**, **OF - Bù Trừ Công Nợ**, **AP - Phải Trả**, **AR - Phải Thu**, **CAR - Thu Tiền**, **CAP - Chi Tiền**, **INIn - Nhập Kho**, **INOut - Xuất Kho**.
3. Nhấn **File mẫu** để tải file Excel mẫu đúng phân hệ. Luôn dùng mẫu mới nhất vì mỗi phân hệ có bộ cột riêng.
4. Nếu nhập dữ liệu thuế GTGT đầu vào, tích **Thuế GTGT đầu vào** trước khi đọc file; nếu chỉ nhập chứng từ thông thường thì để trống.
5. Nhấn nút chọn file tại ô **File**, chọn file Excel đã chuẩn bị.
6. Nhấn **Đọc file Excel** để hệ thống đọc file và hiển thị dữ liệu lên lưới kiểm tra.
7. Kiểm tra cột **Thông tin lỗi/cảnh báo** và các ô được tô màu trên lưới.
8. Sửa dữ liệu trực tiếp trên lưới hoặc quay lại file Excel để sửa, sau đó đọc lại file nếu cần.
9. Khi không còn lỗi chặn nhập dữ liệu, nhấn **Nhập dữ liệu** để ghi dữ liệu vào SmartBooks.

![](../.gitbook/assets/image18.png)

- **Các trường và nút chức năng:**
  - Phân hệ: Chọn phân hệ/chứng từ cần nhập dữ liệu. Mẫu file, danh sách cột và quy tắc kiểm tra sẽ thay đổi theo phân hệ đã chọn.
  - File mẫu: Tải file Excel mẫu theo phân hệ. File mẫu giúp đảm bảo đúng tên sheet, đúng tên cột và đúng thứ tự dữ liệu.
  - Thuế GTGT đầu vào: Dùng khi nhập dữ liệu hóa đơn GTGT đầu vào. Chỉ tích khi file nhập là dữ liệu thuế GTGT đầu vào.
  - File: Đường dẫn file Excel cần đọc. Sau khi chọn file, kiểm tra lại tên file để tránh nhập nhầm phiên bản.
  - Đọc file Excel: Đọc dữ liệu từ file Excel, đưa lên lưới kiểm tra và tự động kiểm tra lỗi/cảnh báo.
  - Nhập dữ liệu: Ghi dữ liệu đã kiểm tra vào hệ thống. Chỉ thực hiện khi lưới không còn lỗi chặn nhập.
  - Lưới dữ liệu: Hiển thị từng dòng Excel sau khi đọc file; cho phép sửa trực tiếp một số ô và tự kiểm tra lại sau khi sửa.
  - Cột **Thông tin lỗi/cảnh báo**: Hiển thị lý do vì sao dòng đang bị chặn hoặc cần người dùng chú ý trước khi nhập dữ liệu.

- **Quy ước màu lỗi trên lưới:**
  - **Đỏ:** Lỗi chặn nhập dữ liệu. Nếu còn bất kỳ dòng đỏ nào, hệ thống không nhập dữ liệu.
  - **Vàng:** Cảnh báo. Hệ thống vẫn có thể cho nhập dữ liệu nhưng người dùng cần kiểm tra kỹ trước khi tiếp tục.
  - Dòng không có màu cảnh báo/lỗi: Dữ liệu đã vượt qua bước kiểm tra cơ bản.

- **Các lỗi đỏ thường gặp:**
  - Số chứng từ đã ở trạng thái **Đã ghi sổ**; cần bỏ ghi sổ/mở khóa chứng từ trước khi nhập lại.
  - Chứng từ đã có bút toán sổ cái liên quan; cần xử lý chứng từ liên quan trước khi ghi đè.
  - Chứng từ kho đã có dữ liệu phải thu/phải trả liên quan; cần xử lý liên kết AR/AP trước khi nhập lại.
  - Tài khoản kế toán không tồn tại, không thuộc phân hệ được phép, hoặc không phải tài khoản chi tiết.
  - Tài khoản công nợ thiếu mã khách hàng/nhà cung cấp, hoặc mã khách hàng/nhà cung cấp không khớp với tên trong danh mục.
  - Tài khoản tiền không phù hợp với phân hệ tiền mặt/ngân hàng, ví dụ chứng từ tiền yêu cầu tài khoản 111/112 nhưng file dùng tài khoản khác.
  - Loại chứng từ không hợp lệ với phân hệ đang chọn.
  - Dữ liệu ngày tháng, số tiền, tỷ giá hoặc mã danh mục sai định dạng khiến hệ thống không thể chuyển thành chứng từ.

- **Các cảnh báo vàng thường gặp:**
  - Số chứng từ trong file đang tồn tại ở trạng thái **Chưa ghi sổ**. Nếu tiếp tục nhập dữ liệu, dữ liệu cũ có thể bị ghi đè.
  - Số chứng từ không khớp kỳ/ngày chứng từ, ví dụ số chứng từ thể hiện tháng 03 nhưng ngày chứng từ thuộc tháng 04.
  - Đơn vị tính trong file Excel chưa khớp danh mục vật tư. Người dùng cần kiểm tra lại trước khi nhập dữ liệu.
  - Một dòng có nhiều cảnh báo/lỗi sẽ được tổng hợp đầy đủ trong cột **Thông tin lỗi/cảnh báo**.

- **Lưu ý khi thao tác:**
  - Hệ thống kiểm tra toàn bộ file trước khi nhập dữ liệu. Nếu có lỗi đỏ ở bất kỳ dòng nào, toàn bộ file sẽ dừng nhập; không chỉ riêng dòng lỗi.
  - Không nên nhập trực tiếp vào dữ liệu chính nếu chưa kiểm tra trên dữ liệu thử hoặc chưa sao lưu.
  - Khi nhập lại cùng số chứng từ, cần xác định rõ chứng từ cũ đang Chưa ghi sổ hay Đã ghi sổ để tránh ghi đè sai dữ liệu.
  - Nếu sửa dữ liệu trực tiếp trên lưới, chờ hệ thống tự kiểm tra lại cột lỗi/cảnh báo trước khi nhấn **Nhập dữ liệu**.
  - Với các file nhiều dòng, nên xử lý lần lượt từ lỗi đỏ đến cảnh báo vàng; chỉ nhập dữ liệu khi người phụ trách kế toán đã xác nhận số liệu.

> **Hệ thống tự kiểm tra trước khi nhập dữ liệu:**
> - Đúng phân hệ, đúng file mẫu và đúng cấu trúc cột bắt buộc.
> - Tài khoản, mã khách hàng, mã nhà cung cấp, mã nhân viên, mã vật tư, mã kho, đơn vị tính và mã thuế tồn tại trong danh mục.
> - Số chứng từ, ngày chứng từ và kỳ kế toán hợp lệ.
> - Trạng thái chứng từ hiện có không bị khóa ghi sổ.
> - Các chứng từ liên quan GL/AR/AP/Kho không chặn việc ghi đè dữ liệu.
> - Dòng dữ liệu không còn lỗi đỏ trước khi thực hiện nhập dữ liệu hàng loạt.

---

### Điều chỉnh chứng từ

**Nghiệp vụ áp dụng:** Mở khóa các chứng từ đã ghi sổ thuộc một phân hệ bất kỳ, đưa chứng từ quay về trạng thái **Chưa ghi sổ** để có thể thực hiện hiệu chỉnh hoặc sửa đổi thông tin sai sót.

![](../.gitbook/assets/image19.png)

Để điều chỉnh chứng từ đã ghi sổ, người dùng thực hiện như sau:

1. Chọn **Phân hệ** cần điều chỉnh từ danh sách thả xuống tại ô Phân hệ.
2. Chọn điều kiện lọc chứng từ: theo **Kỳ kế toán** và nhập kỳ kế toán cụ thể, hoặc theo **Năm kế toán** để lấy toàn bộ chứng từ trong năm kế toán.
3. Tại lưới dữ liệu, tích chọn vào ô vuông ở cột đầu tiên tương ứng với các chứng từ cần mở khóa.
4. Nhấn **Xử lý** để thực thi — các chứng từ được chọn sẽ tự động chuyển về trạng thái Chưa ghi sổ, cho phép chỉnh sửa hoặc xóa.

![](../.gitbook/assets/image20.png)

- **Ô chọn và nút chức năng:**
  - Kỳ kế toán: Lọc chứng từ theo một kỳ kế toán cụ thể.
  - Năm kế toán: Lọc chứng từ theo toàn bộ năm kế toán.
  - Ô chọn từng dòng: Chọn chứng từ cần điều chỉnh.
  - Ô chọn đầu cột: Chọn nhanh toàn bộ chứng từ đang hiển thị.
  - Xử lý: Thực hiện mở khóa/bỏ ghi sổ các chứng từ đã chọn.
  - Đóng: Thoát khỏi màn hình.

> **Hệ thống tự kiểm tra khi xử lý:** Chỉ chứng từ thuộc phân hệ được chọn và người dùng có quyền mới được xử lý. Chứng từ liên quan nhiều phân hệ cần kiểm tra trước khi mở khóa để tránh lệch sổ.

> **Lưu ý:** Chỉ những người dùng có quyền mới được phép điều chỉnh chứng từ đã ghi sổ. Cần kiểm tra kỹ trước khi mở khóa vì có thể ảnh hưởng đến số liệu trên Sổ cái.

---

### Xóa chứng từ

**Nghiệp vụ áp dụng:** Quản trị viên hoặc nhân sự được phân quyền thực hiện xóa hàng loạt các chứng từ/bút toán theo danh sách thuộc từng phân hệ — giúp xử lý nhanh dữ liệu lỗi hoặc dữ liệu nhập thử nghiệm.

![](../.gitbook/assets/image21.png)

Để xóa chứng từ hàng loạt, người dùng thực hiện như sau:

1. Chọn **Phân hệ** cần xóa từ danh sách thả xuống tại ô Phân hệ.
2. Chọn điều kiện lọc chứng từ: theo **Kỳ kế toán** và nhập kỳ kế toán cụ thể, hoặc theo **Năm kế toán** để lấy toàn bộ chứng từ trong năm kế toán.
3. Tại lưới dữ liệu, tích chọn các chứng từ cần xóa.
4. Nhấn **Thực hiện / Xử lý** để thực hiện xóa.

![](../.gitbook/assets/image22.png)

- **Ô chọn và nút chức năng:**
  - Kỳ kế toán: Lọc chứng từ theo một kỳ kế toán cụ thể.
  - Năm kế toán: Lọc chứng từ theo toàn bộ năm kế toán.
  - Ô chọn từng dòng: Chọn chứng từ cần xóa.
  - Thực hiện/Xử lý: Xóa các chứng từ đã chọn.
  - Đóng: Thoát khỏi màn hình.

> **Hệ thống tự kiểm tra khi xóa:** Chứng từ đã ghi sổ, chứng từ thuộc kỳ khóa sổ hoặc chứng từ có dữ liệu liên quan có thể bị chặn xóa. Cần mở khóa/bỏ ghi sổ và xử lý chứng từ liên quan trước khi xóa.

> **Lưu ý:** Chứng từ đã xóa không thể khôi phục. Nên backup dữ liệu trước khi thực hiện xóa hàng loạt. Danh sách chứng từ đã xóa có thể xem lại tại **Danh sách các bút toán đã xóa**.

---

### Cấu hình (Số chữ số thập phân)

**Nghiệp vụ áp dụng:** Quản trị viên thiết lập quy tắc đánh số chứng từ tự động và cấu hình số chữ số sau dấu thập phân (số lẻ) cho các chỉ tiêu số lượng, đơn giá, thành tiền theo từng màn hình nhập liệu cụ thể.

![](../.gitbook/assets/image23.png)

![](../.gitbook/assets/image24.png)

- **Các trường và nút chức năng:**
  - Loại chứng từ/màn hình: Chọn phạm vi áp dụng quy tắc đánh số hoặc số chữ số thập phân.
  - Số chứng từ tự động: Thiết lập tiền tố, số chạy và quy tắc tăng số chứng từ nếu màn hình hỗ trợ.
  - Số chữ số thập phân: Quy định cách làm tròn số lượng, đơn giá, thành tiền hoặc tỷ giá.
  - Lưu: Lưu cấu hình.
  - Đóng: Thoát khỏi màn hình.

> **Hệ thống tự kiểm tra khi Lưu:** Không nên để trống cấu hình bắt buộc. Thay đổi số chữ số thập phân có thể làm số tiền hiển thị khác trước do quy tắc làm tròn mới.

> **Lưu ý:** Cấu hình số thập phân ảnh hưởng đến toàn bộ chứng từ — nên thiết lập trước khi bắt đầu nhập liệu. Thay đổi sau khi đã có dữ liệu có thể gây chênh lệch làm tròn.

---

### Ngôn ngữ

**Nghiệp vụ áp dụng:** Chuyển đổi giao diện làm việc sang ngôn ngữ phù hợp với nhu cầu sử dụng — hệ thống hỗ trợ đa ngôn ngữ: Tiếng Việt, Tiếng Anh, Hàn Quốc, Trung Quốc, Nhật Bản, Campuchia.

![](../.gitbook/assets/image25.png)

- **Cách thực hiện:**
  1. Mở chức năng **Ngôn ngữ**.
  2. Chọn ngôn ngữ cần sử dụng.
  3. Xác nhận thay đổi nếu hệ thống hiển thị thông báo.
  4. Đăng xuất và đăng nhập lại để giao diện tải đầy đủ ngôn ngữ mới.

- **Các nút chức năng:**
  - Chọn ngôn ngữ: Chọn tiếng Việt, tiếng Anh, tiếng Hàn hoặc ngôn ngữ khác đang được triển khai.
  - OK/Apply: Áp dụng ngôn ngữ đã chọn.
  - Đóng: Thoát khỏi màn hình.

> **Hệ thống tự kiểm tra khi đổi ngôn ngữ:** Người dùng cần có quyền truy cập hệ thống bình thường; thay đổi ngôn ngữ không sửa dữ liệu kế toán, chỉ thay đổi nhãn giao diện.

> **Lưu ý:** Thay đổi ngôn ngữ chỉ ảnh hưởng đến giao diện hiển thị, không ảnh hưởng đến dữ liệu kế toán. Người dùng cần đăng xuất và đăng nhập lại để ngôn ngữ mới có hiệu lực.
