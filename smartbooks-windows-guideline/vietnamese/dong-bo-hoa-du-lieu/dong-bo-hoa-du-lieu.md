# 15. ĐỒNG BỘ HÓA DỮ LIỆU

![](<../.gitbook/assets/0 (2).jpeg>)

Đồng bộ hóa dữ liệu là quá trình trao đổi và đồng bộ hóa thông tin giữa nhiều nguồn dữ liệu về 1 máy chủ trung tâm theo 2 chiều dữ liệu (Upload Data - Download Data) bằng thời gian thực.

Chúng tôi sử dụng công nghệ SQL Server Replication để thực hiện quá trình trao đổi và đồng bộ hóa thông tin

Công nghệ SQL Server Replication là một kỹ thuật copy mã hóa dữ liệu từ 1 database này phát tán dữ liệu đến 1 database khác, sau đó giữa các database tiến hành đồng bộ và thống nhất dữ liệu

Công nghệ này thường được sử dụng từ máy chủ đến máy chủ đòi hỏi giao dịch cao, bao gồm: cải thiện khả năng mở rộng và tính sẵn sàng, kho dữ liệu và báo cáo, tích hợp dữ liệu từ nhiều nơi, tích hợp dữ liệu không đồng bộ và giảm tải xử lý hàng loạt. Hợp nhất nhân rộng được thiết kế chủ yếu cho các ứng dụng điện thoại di động hoặc các ứng dụng máy chủ phân phối mà có thể xảy ra xung đột dữ liệu

Quá trình này được thực hiện tự động khi có kết nối Internet từ hệ thống Local và hệ thống Trung tâm.

Cài đặt bao gồm 2 phần:

Phần 1: Đặt 1 hệ thống Local tại công ty bạn cần quản lý\
Phần 2: Hệ thống trung tâm được cài đặt tại hệ thống trung tâm của SSAudit dữ liệu được quản lý 1 cách tập trung ại hệ thống máy chủ trung tâm

Thông tin tại Local, tại công ty của bạn sẽ được đồng bộ hóa và hợp nhất dữ liệu với hệ thống trung tâm thông qua mạng internet bằng giải pháp đồng bộ hóa dữ liệu.

Hệ thống trung tâm của chúng tôi có khả năng khôi phục dữ liệu hệ thống Local vì thế quá trình khôi phục và bảo trì diễn ra 1 cách nhanh chóng dễ dàng qua internet.

Ưu điểm:

kết hợp ưu điểm của cả giải pháp cổ điển Winform và Webform.

\- An toàn dữ liệu và tính sẵn sàng cao của dữ liệu là hết sức cần thiết.\
\- Khả năng sao lưu phục hồi dữ liệu, Bảo vệ hệ thống từ xa\
\- Thông tin được phản ánh kịp thời chính xác\
\- Đảm bảo an toàn và bảo mật dữ liệu khi thực hiện truyền thông.
