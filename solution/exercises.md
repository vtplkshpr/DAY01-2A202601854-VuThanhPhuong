# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 14h00–18h00
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.7, 1.2 và 1.8 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Hà Nội."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi? Ở mức nào phản hồi bắt đầu
kém mạch lạc?** (2–3 câu)
** Khi temperature tăng, phản hồi trở nên đa dạng hơn nhưng cũng dễ mất độ ổn định và mạch lạc. Ở mức 1.2 trở lên, nhất là 1.8, câu trả lời bắt đầu có xu hướng lạc khỏi ý chính và ít kiểm soát hơn. Với temperature thấp như 0.0–0.7, phản hồi thường nhất quán và dễ dự đoán hơn.

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho trợ lý soạn thảo hợp đồng pháp lý,
và bao nhiêu cho trợ lý viết slogan quảng cáo? Giải thích khác biệt.**
**
Tôi chọn temperature thấp, khoảng 0.0–0.3, cho trợ lý soạn thảo hợp đồng pháp lý vì cần sự nhất quán, an toàn và ít sai lệch. 
Với trợ lý viết slogan quảng cáo, tôi sẽ dùng temperature cao hơn, khoảng 0.7–1.2, để tạo nhiều biến thể sáng tạo và hấp dẫn hơn.
**

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 20.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 2 lần,
mỗi lần trung bình ~500 token đầu ra.

**Ước tính chi phí mỗi ngày của model lớn so với model nhỏ cho workload này
(dựa trên bảng giá trong template). Nêu một trường hợp model lớn xứng đáng
với chi phí và một trường hợp model nhỏ là lựa chọn đúng:**
** Với 20.000 người dùng, mỗi người 2 lần/ngày và mỗi lần 500 token đầu ra, tổng là 20.000.000 token đầu ra mỗi ngày. 
Nếu dùng gpt-4o, chi phí khoảng 20.000.000 / 1.000 × 0.010 = 200 USD/ngày; nếu dùng gpt-4o-mini, chi phí khoảng 20.000.000 / 1.000 × 0.0006 = 12 USD/ngày. Model lớn làm trợ lý hỗ trợ pháp lý hoặc trả lời phức tạp, còn model nhỏ phù hợp cho tóm tắt tin nhắn, sinh tiêu đề hoặc chatbot đơn giản.
**

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích máy học (machine learning) là gì?"** nhưng hai system prompt
khác nhau:
- "Bạn là một nhà thơ, trả lời mọi thứ bằng hình ảnh ví von, tránh thuật ngữ."
- "Bạn là kỹ sư phần mềm senior, trả lời chính xác, có ví dụ code khi phù hợp."

**Hai phản hồi khác nhau như thế nào (giọng văn, độ dài, mức kỹ thuật)?
Từ đó rút ra system prompt điều khiển được những khía cạnh nào của phản hồi?**
(3–4 câu)
** Phản hồi của persona thơ mang giọng văn hình ảnh, ví von và ít dùng thuật ngữ kỹ thuật, còn phản hồi của persona kỹ sư thì ngắn gọn, rõ ràng và có ví dụ code. Persona thơ thường dài và ấn tượng hơn, trong khi persona kỹ sư tập trung vào độ chính xác và cấu trúc. Từ đó có thể thấy system prompt điều khiển được phong cách trả lời, mức độ kỹ thuật, độ dài và cách trình bày thông tin. **

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~150 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Nếu dùng ước lượng thô để dự
toán ngân sách API cho ứng dụng tiếng Việt, bạn sẽ dự toán thiếu hay thừa —
và vì sao?**
** Với đoạn văn tiếng Việt, số token theo tiktoken thường chênh khá đáng kể so với ước lượng số từ / 0.75, có thể chênh khoảng 20–40% tùy đoạn văn. Nếu dùng ước lượng thô, dễ bị dự toán thiếu hoặc thừa tùy ngữ liệu, vì tiếng Việt không luôn tuân theo tỷ lệ token/word như tiếng Anh. Vì vậy, khi cần kiểm soát ngân sách API, nên dùng count_tokens thật thay vì chỉ dựa vào ước lượng.
**
---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Xét ba ứng dụng: (a) chatbot văn bản, (b) trợ lý giọng nói đọc to phản hồi,
(c) pipeline dịch tài liệu chạy ngầm ban đêm. Ứng dụng nào hưởng lợi nhiều
nhất từ streaming, ứng dụng nào không cần — và tại sao?** (1 đoạn văn)
** 
Chatbot văn bản và trợ lý giọng nói hưởng lợi nhiều nhất từ streaming vì người dùng thấy phản hồi hiện ra ngay khi model tạo từng phần, tạo cảm giác nhanh và tự nhiên hơn. Pipeline dịch tài liệu chạy ngầm ban đêm không cần streaming vì người dùng không cần thấy phản hồi tức thì, nên hiệu quả tập trung vào xử lý toàn bộ thay vì phản hồi từng chunk.
***

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**Khi API quá tải và hàng nghìn client cùng retry, exponential backoff giúp
gì so với delay cố định? Tra cứu thêm: kỹ thuật "jitter" (thêm độ trễ ngẫu
nhiên) giải quyết vấn đề gì còn sót lại?**
**
Exponential backoff giúp giảm tải cho hệ thống bằng cách tăng thời gian chờ sau mỗi lần retry, thay vì để tất cả client retry cùng lúc với cùng một khoảng delay cố định. Jitter thêm yếu tố ngẫu nhiên vào khoảng chờ để tránh tình trạng hàng nghìn client retry đồng loạt và gây tắc nghẽn thêm.
**
---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Viết lại system prompt bạn dùng cho trợ lý của mình. Chỉ ra 2 chỗ trong
prompt mà nếu xóa đi, hành vi trợ lý sẽ thay đổi rõ rệt — và mô tả thay đổi
đó:**
**
Tôi sẽ dùng system prompt: “Bạn là trợ lý học tập thân thiện, trả lời ngắn gọn bằng tiếng Việt, ưu tiên ví dụ thực tế và không đưa ra câu trả lời quá kỹ thuật khi người dùng mới bắt đầu.” Nếu bỏ đi câu “trả lời ngắn gọn” thì trợ lý sẽ dài dòng hơn; nếu bỏ đi câu “không đưa ra câu trả lời quá kỹ thuật” thì trợ lý sẽ trở nên khó hiểu với người mới.
**

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn giữ history 4 lượt cuối. Hãy mô tả một tình huống hội thoại
cụ thể mà giới hạn này khiến trợ lý trả lời sai/mất ngữ cảnh, và đề xuất một
cách khắc phục (ví dụ: tóm tắt các lượt cũ, tăng giới hạn có chọn lọc...):**
**
Ví dụ, người dùng hỏi lần đầu: “Tôi cần viết email xin nghỉ làm”, sau đó vài lượt sau lại hỏi: “Viết lại theo giọng thân thiện hơn”. Nếu trợ lý chỉ nhớ 4 lượt cuối, có thể quên bối cảnh đầu tiên và viết lại email không đúng phong cách. Cách khắc phục là lưu một bản tóm tắt ngữ cảnh ngắn hoặc tăng giới hạn history cho các cuộc hội thoại dài hơn.
**

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/`, push lên GitHub cá nhân và nộp link repo vào vlearn (theo hướng dẫn README)
