# Tính giá thành

**Nghiệp vụ áp dụng:** Khi doanh nghiệp sản xuất cần tính giá thành sản phẩm cuối kỳ. SmartBooks hỗ trợ nhiều phương pháp tính giá thành: theo BOM (định mức nguyên vật liệu), giản đơn, hệ số, giá bán và phân bước. Mỗi phương pháp phù hợp với từng loại hình sản xuất cụ thể.

> **Ví dụ:** Cuối tháng, kế toán tính giá thành sản phẩm đèn LED — tập hợp chi phí NVL trực tiếp (TK 621), nhân công trực tiếp (TK 622), sản xuất chung (TK 627) vào TK 154, sau đó phân bổ cho từng sản phẩm hoàn thành nhập kho (TK 155).

---

### Các phương pháp tính giá thành

SmartBooks hỗ trợ các phương pháp sau:

| Phương pháp | Áp dụng cho | Đặc điểm |
|-------------|-------------|----------|
| **Theo BOM** | DN có định mức NVL cho từng SP | Tính chính xác NVL theo định mức, so sánh chênh lệch thực tế |
| **Giản đơn** | DN sản xuất đơn giản, ít sản phẩm | Lấy tổng CP chia đều cho SP sản xuất |
| **Hệ số** | DN sản xuất SP cùng loại khác kích cỡ | Quy đổi SP về SP chuẩn bằng hệ số |
| **Giá bán** | DN phân bổ CP theo tỷ lệ giá bán | Phân bổ CP cho SP theo giá bán |
| **Phân bước** | DN SX nhiều giai đoạn (phân xưởng) | Tính giá thành theo từng công đoạn |

---

### Phương pháp theo BOM (Định mức NVL)

Áp dụng cho doanh nghiệp có xây dựng bảng định mức nguyên vật liệu (BOM — Bill of Materials) cho từng sản phẩm. Phương pháp này tính chính xác lượng NVL tiêu hao cho mỗi SP dựa trên định mức, đồng thời xác định chênh lệch giữa thực tế và định mức.

Quy trình gồm 11 bước:

**Bước 1 — Xây dựng bảng định mức cho mỗi sản phẩm**

Khai báo danh sách NVL và khối lượng cần thiết để sản xuất 1 đơn vị sản phẩm. Mỗi SP có thể sử dụng từ 1 đến 100 loại NVL.

> **Ví dụ:** SP đèn LED NIBA-07-CT cần 4 loại NVL: 7W LED PCB (0.570 kg), LED E27 CAP (0.758 kg), LED BULB A60 HOUSING 7W (0.852 kg), LED DRIVER 7W (0.570 kg).

**Bước 2 — Tổng hợp số lượng thành phẩm nhập kho trong kỳ**

Hệ thống tổng hợp từ phiếu nhập kho thành phẩm đã nhập liệu trong kỳ.

**Bước 3 — Tổng hợp sản phẩm dở dang và quy đổi SP hoàn thành tương đương**

Nhập số lượng sản phẩm dở dang cuối kỳ và tỷ lệ hoàn thành. Hệ thống tự động quy đổi ra sản phẩm hoàn thành tương đương.

> **Lưu ý:** Một mã sản phẩm có thể có nhiều tỷ lệ dở dang (đầu, giữa, cuối quy trình sản xuất). Hệ thống sẽ tập hợp thành tổng SP hoàn thành tương đương cho mỗi mã.

**Bước 4 — Tính số lượng SP sản xuất trong kỳ**

Theo phương trình cân bằng sản xuất:

> SP sản xuất trong kỳ = Thành phẩm nhập kho + Dở dang cuối kỳ − Dở dang đầu kỳ

**Bước 5 — Tính toán NVL theo BOM cho SP sản xuất**

Nhân định mức NVL (bước 1) với số lượng SP sản xuất (bước 4) để tính tổng NVL tiêu hao theo BOM.

**Bước 6 — Tổng hợp NVL xuất kho thực tế**

Hệ thống tự động lấy dữ liệu từ phiếu xuất kho NVL. Cần hoàn thành áp giá xuất kho NVL trước khi thực hiện bước này.

**Bước 7 — So sánh chênh lệch thực tế và định mức**

Xác định chênh lệch NVL giữa thực tế và định mức:

- NVL thực tế > Định mức: Phần chênh lệch ghi nhận trực tiếp vào giá vốn (Nợ TK 632 / Có TK 621).
- NVL thực tế < Định mức: Kế toán có thể điều chỉnh lại định mức ở bước 1.

**Bước 8 — Xác định NVL để tính giá thành**

Sau khi xử lý chênh lệch, giá trị NVL đưa vào tính giá thành là giá trị NVL thực tế hoặc định mức (tùy từng mã NVL).

**Bước 9 — Tính giá thành cho từng sản phẩm**

Phân bổ chi phí nhân công (TK 622) và sản xuất chung (TK 627) cho từng SP theo tỷ lệ chi phí NVL. Giá thành đơn vị được tính bình quân bao gồm cả dở dang đầu kỳ.

**Bước 10 — Tính giá trị SP dở dang cuối kỳ**

> Giá trị dở dang cuối kỳ = SP hoàn thành tương đương (bước 3) × Giá thành đơn vị (bước 9)

**Bước 11 — Xác định giá trị thành phẩm nhập kho**

> Giá trị TP nhập kho = Dở dang đầu kỳ + CP SX phát sinh trong kỳ − Dở dang cuối kỳ
>
> Giá thành đơn vị = Tổng giá trị TP nhập kho ÷ Tổng SL thành phẩm nhập kho (bước 2)

---

### Phương pháp giản đơn

Áp dụng cho doanh nghiệp sản xuất đơn giản, ít loại sản phẩm. Đây là phương pháp đơn giản nhất — lấy tổng chi phí chia đều cho tổng sản phẩm sản xuất.

Quy trình gồm 6 bước:

1. Tổng hợp thành phẩm sản xuất trong kỳ.
2. Tổng hợp sản phẩm dở dang và quy đổi SP hoàn thành tương đương.
3. Tính số lượng SP sản xuất trong kỳ.
4. Tính giá thành: Lấy tổng chi phí chia cho tổng SP sản xuất, nhân với số lượng từng loại.
5. Tính giá trị SP dở dang cuối kỳ.
6. Xác định giá trị thành phẩm nhập kho.

---

### Phương pháp hệ số

Áp dụng cho doanh nghiệp sản xuất các sản phẩm có tính chất giống nhau, chỉ khác kích thước (VD: chai thủy tinh 1L, 0.5L, 250ml). Chọn một sản phẩm làm chuẩn, quy đổi các SP khác theo hệ số.

Quy trình gồm 9 bước:

1. Chọn SP chuẩn và khai báo hệ số cho từng SP.
2. Tổng hợp thành phẩm sản xuất trong kỳ.
3. Tổng hợp SP dở dang và quy đổi SP hoàn thành tương đương.
4. Tính số lượng SP sản xuất trong kỳ.
5. Quy đổi SP sản xuất ra SP tiêu chuẩn (nhân hệ số).
6. Tính giá thành cho SP chuẩn (bình quân bao gồm dở dang đầu kỳ).
7. Tính lại giá thành cho từng loại SP (nhân hệ số ngược lại).
8. Tính giá trị SP dở dang cuối kỳ.
9. Xác định giá trị thành phẩm nhập kho.

---

### Phương pháp giá bán

Áp dụng khi doanh nghiệp muốn phân bổ chi phí sản xuất cho từng sản phẩm theo tỷ lệ giá bán. SP có giá bán cao sẽ được phân bổ nhiều chi phí hơn.

Quy trình gồm 7 bước:

1. Khai báo giá bán cho từng mã thành phẩm.
2. Tổng hợp thành phẩm sản xuất trong kỳ.
3. Tổng hợp SP dở dang và quy đổi SP hoàn thành tương đương.
4. Tính số lượng SP sản xuất trong kỳ.
5. Tính giá thành cho các SP theo tỷ lệ giá bán.
6. Tính giá trị SP dở dang cuối kỳ.
7. Xác định giá trị thành phẩm nhập kho.

---

### Phương pháp phân bước

Áp dụng cho doanh nghiệp sản xuất qua nhiều giai đoạn (công đoạn/phân xưởng). Chi phí được tập hợp và phân bổ theo từng giai đoạn, sau đó tính giá thành cho từng nhóm SP trong mỗi giai đoạn.

**Thiết lập ban đầu:**

1. **Tạo Mã chi phí:** Khai báo mã chi phí cho từng nhóm (621/622/627) và gắn với giai đoạn, phương pháp phân bổ.
   - Nhóm chi phí: 621 (NVL trực tiếp), 622 (Nhân công trực tiếp), 627 (SXC).
   - Giai đoạn: Gắn chi phí với giai đoạn cụ thể hoặc "All" nếu dùng cho nhiều giai đoạn.
   - Phương pháp phân bổ: Đích danh SP, theo tỷ lệ, hoặc đặc thù riêng.

2. **Thiết lập tỷ lệ phân bổ theo giai đoạn:** Khai báo tỷ lệ chi phí phân bổ cho từng giai đoạn và kỳ áp dụng.

3. **Thiết lập tỷ lệ phân bổ theo nhóm SP:** Khai báo hệ số phân bổ cho từng nhóm thành phẩm trong mỗi giai đoạn.

4. **Thiết lập tỷ lệ phân bổ theo từng SP:** Khai báo hệ số phân bổ chi tiết đến từng mã sản phẩm.

---

### Thực hiện tính giá thành

Sau khi hoàn thành thiết lập, thực hiện tính giá thành như sau:

1. Nhập **kỳ tính giá thành** (Từ ngày — Đến ngày).
2. Nhập **số lượng SP dở dang cuối kỳ** và **tỷ lệ hoàn thành tương đương** cho từng nhóm chi phí (621, 622, 627).
3. Nhấn **Tính giá thành** — hệ thống tự động:
   - Tập hợp chi phí NVL, nhân công, SXC theo từng giai đoạn.
   - Phân bổ chi phí cho nhóm SP và từng SP.
   - Tính giá trị dở dang cuối kỳ.
   - Xác định giá thành đơn vị cho từng SP.
4. Kiểm tra kết quả trên lưới và nhấn **Lưu** để xác nhận.

- **Lưu ý khi thao tác:**
  - Phải hoàn thành xuất kho NVL và áp giá xuất kho trước khi tính giá thành.
  - Số lượng dở dang cuối kỳ phải được xác nhận qua kiểm kê thực tế.
  - Có thể xuất kết quả ra Excel để đối chiếu và lưu trữ.

> **Lưu ý:** Giá thành đơn vị sản phẩm sau khi tính xong sẽ được sử dụng tại bước **Áp giá nhập kho TP** (bước 3 trong quy trình 5 bước xử lý kho). Đảm bảo chạy tính giá thành trước khi chạy quy trình xử lý cuối kỳ.
