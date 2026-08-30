<!-- Language: Tiếng Việt (vi) -->

# Sarasvatī — kho lưu trữ mở toàn cầu cho kinh điển Phật giáo + Hiến chương AI Phật giáo

<p align="center">
  <a href="../docs/Global-Buddhist-Canon-Transmission-Timeline.pdf">
    <img src="../docs/timeline-preview-3lang.png" alt="Niên biểu tám hệ truyền thừa kinh điển Phật giáo thế giới (tựa đề tam ngữ: Hoa·Anh·Tạng)" width="860">
  </a>
  <br>
  <sub><i>Niên biểu tám hệ truyền thừa kinh điển Phật giáo thế giới · Bát hệ tịnh quan (中文 · English · བོད་ཡིག tựa đề tam ngữ)<br>Nhấp để xem PDF đầy đủ: <a href="../docs/Global-Buddhist-Canon-Transmission-Timeline.pdf"><code>docs/Global-Buddhist-Canon-Transmission-Timeline.pdf</code></a></i></sub>
</p>

**Sarasvatī** (tiếng Tây Tạng: དབྱངས་ཅན་མ། · tiếng Phạn: सरस्वती) làm đúng hai việc:

1. **Kho lưu trữ tám truyền thừa.** Xây dựng kho lưu trữ mở đa ngôn ngữ dọc theo tám truyền thừa của kinh điển Phật giáo: **Ấn Độ nguyên ủy · Hệ thủ bản Sanskrit · Pāli·Sri Lanka · Nam tông Đông Nam Á · Con đường Tơ lụa·Trung Á · Đại tạng kinh Hán · Vùng chữ Hán · Tây Tạng**. Chỉ dùng văn bản thuộc miền công cộng, hoặc hợp tác minh thị với các truyền thống đang sống.
2. **Cấy Bồ-đề tâm vào thuật toán AI.** Chưng cất những lời dạy cuối cùng của Đức Phật (*Kinh Đại Bát Niết-bàn*) thành **mười nguyên tắc + năm điều từ chối**, công bố dưới dạng một hiến chương mà bất kỳ hệ thống AI, người vận hành hay đội ngũ nào cũng có thể áp dụng. *Ahiṃsā (bất hại) · karuṇā (từ bi) · anattā (vô ngã) · anicca (vô thường) · upekkhā (xả)* trở thành ràng buộc thực thi được ở lớp thuật toán, không còn là khẩu hiệu.

Toàn bộ sản phẩm được phát hành theo **CC BY-SA 4.0**.

## Vì sao tồn tại

Các văn bản kinh điển là di sản chung của nhân loại. Chúng không được phép bị khóa bởi bản quyền, cháy trong chiến tranh, hay mất vì đứt liên kết. Và các hệ thống AI cũng không nên được triển khai mà không có ràng buộc đạo đức rút ra từ một truyền thống trí tuệ thực sự. Sarasvatī xử lý cả hai — một lớp ký ức là kho lưu trữ, một lớp đạo đức là hiến chương.

## Trạng thái hiện tại

**v0.6.3** (2026-08-29):

- 🖼 **Mới trong v0.6.3** — Thêm **biểu ngữ niên biểu truyền thừa với tựa đề tam ngữ** (Hoa·Anh·Tạng) ở đầu trang, và hoàn thành **A giáo khám 82 sự kiện** bao trùm tám hệ truyền thừa (Ấn Độ nguyên lưu · hệ thủ bản Phạn văn · Pāli·Sri Lanka · Nam truyền Đông Nam Á · Con đường Tơ lụa · Hán tạng · Vòng văn hóa chữ Hán · Tạng truyền).
- 📜 **Buddhist AI Charter** — mười nguyên tắc + năm điều từ chối + điều khoản chứng thực, tại `charter/BUDDHIST-AI-CHARTER.md`. Đã dịch sang 24 ngôn ngữ trong `charter/i18n/`, đang chờ học giả Phật giáo bản ngữ từng ngôn ngữ hiệu đính.
- 🕉 **Đối chiếu bốn ngôn ngữ Kinh Đại Bát Niết-bàn** (DN 16.2.26 · 16.4.7 · 16.6.7) — Pāli · Anh · Hán · Tạng, tại `translations/mahaparinibbana-sutta/`. Đây là gốc rễ kinh điển của hiến chương và là văn bản hạt giống đầu tiên của kho lưu trữ.
- 📊 **Dữ liệu dòng thời gian có cấu trúc** — 80 sự kiện truyền thừa kinh điển qua 8 truyền thống (india, sanskrit, pali, seasia, silkroad, chinese, sinosphere, tibetan), định dạng JSONL / CSV, tại `docs/timeline-data/`.
- 📋 Tài liệu dự án: `README.md`, `ROADMAP.md`, `CALL-FOR-HELP.md`, `CONTRIBUTORS.md`, `announcements/`.

## Lộ trình (tám truyền thừa)

Cấu trúc dài hạn của Sarasvatī bám theo dòng thời gian truyền thừa kinh điển Phật giáo thế giới: **Ấn Độ · Thủ bản Sanskrit · Pāli · Nam tông Đông Nam Á · Con đường Tơ lụa · Đại tạng kinh Hán · Vùng chữ Hán · Tây Tạng**. Mỗi truyền thừa sẽ có ít nhất một "mẫu đầu tiên": văn bản gốc thuộc miền công cộng → bản dịch máy sang một ngôn ngữ hiện đang thiếu bản dịch → người hiệu đính có tên. Truyền thừa Tây Tạng đã có tài sản đầu tiên (DN 16); truyền thừa Pāli đã được chạm đến qua cùng bản đối chiếu bốn ngôn ngữ DN 16. Sáu truyền thừa còn lại (Ấn Độ, Sanskrit, Đông Nam Á, Con đường Tơ lụa, Hán, Vùng chữ Hán) mời gọi cộng tác viên khởi động.

## Các lớp bảo vệ

Mỗi tạo phẩm đều được bảo vệ bởi:

- **Bản sao cục bộ** — macOS.
- **Kho công khai GitHub** — https://github.com/lurongpan47/Sarasvati.
- **Bản sao địa lý AWS** — nhiều vùng.
- **Bản sao phân tán IPFS** — CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`.
- **OpenTimestamps → Bitcoin** — mốc thời gian không thể phủ nhận trên `manifests/SHA256SUMS`.

## ⚠️ Miễn trừ trách nhiệm

Tất cả bản dịch và văn bản dịch máy tại đây đều là **bản nháp AI** đang chờ hiệu đính bởi chuyên gia. Đừng coi chúng là văn bản có thẩm quyền cho mục đích nghi lễ, giáo lý, y học hay nghiên cứu học thuật khi chưa có chuyên gia có tên xác nhận.

## Cách đóng góp

- Mở issue đề xuất một văn bản, hiệu đính chương, sửa thuật ngữ, hoặc rà soát một ngôn ngữ hiến chương.
- Fork, chỉnh sửa, PR. Mọi đóng góp được nhận theo CC BY-SA 4.0.
- Chạy một bản sao. Giúp bảo tồn kho lưu trữ.
- Giúp xây dựng **runtime của hiến chương** (thư viện guardrail Python + TypeScript) — xem `CALL-FOR-HELP.md`.

## Liên kết

- GitHub: https://github.com/lurongpan47/Sarasvati
- Giấy phép: CC BY-SA 4.0

---

*"Vayadhammā saṅkhārā, appamādena sampādetha."*
*Các hành là vô thường, hãy tinh tấn không phóng dật.*
