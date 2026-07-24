# Tổng hợp thay đổi đã thực hiện

Tài liệu này ghi lại các thay đổi chính đã được thực hiện trong dự án để giải quyết lỗi và hoàn thành bài lab.

## 1. File đã chỉnh sửa

### [template.py](template.py)
Đây là file chính được sửa để triển khai đầy đủ các hàm còn thiếu trong bài lab.

#### Các hàm đã được triển khai
- `call_openai`
  - Tạo client OpenAI bên trong hàm
  - Gọi `chat.completions.create()`
  - Đo thời gian phản hồi và trả về `(response_text, latency)`

- `call_openai_mini`
  - Gọi lại `call_openai` với model `OPENAI_MINI_MODEL`

- `compare_models`
  - Gọi cả `call_openai` và `call_openai_mini`
  - Trả về dict chứa câu trả lời, thời gian và ước tính chi phí

- `chat_with_system_prompt`
  - Gửi cả `system prompt` và `user prompt` trong `messages`
  - Trả về kết quả tương tự hàm gọi API cơ bản

- `count_tokens`
  - Dùng thư viện `tiktoken` để đếm token
  - Có fallback khi `tiktoken` lỗi hoặc model không được hỗ trợ

- `estimate_cost`
  - Đếm token cho prompt và response
  - Tính chi phí input/output dựa trên bảng giá
  - Trả về dict gồm các giá trị chi phí

- `streaming_chatbot`
  - Xây dựng chatbot tương tác trên dòng lệnh
  - Hỗ trợ streaming token theo từng chunk
  - Giữ lịch sử hội thoại và cắt lịch sử về 4 lượt gần nhất
  - Thoát khi nhập `quit`, `exit`, hoặc `bye`

- `retry_with_backoff`
  - Thử lại khi gặp lỗi tạm thời
  - Dùng exponential backoff
  - Raise exception cuối cùng sau khi hết số lần thử

- `run_assistant`
  - Xây dựng trợ lý CLI hoàn chỉnh
  - Dùng `persona` làm system prompt
  - Gửi history và user message cho API
  - Streaming phản hồi từng chunk
  - Cập nhật thống kê token và chi phí
  - Dừng đúng khi đạt `max_turns` hoặc người dùng nhập lệnh thoát

- `batch_compare` (bonus)
  - Chạy `compare_models` cho từng prompt trong danh sách

- `format_comparison_table` (bonus)
  - Định dạng kết quả thành bảng text dễ đọc

## 2. Vấn đề ban đầu

Ban đầu các hàm trong [template.py](template.py) vẫn còn là placeholder và raise `NotImplementedError`, nên khi chạy tests sẽ thất bại.

## 3. Cách kiểm tra

Đã chạy kiểm thử thành công bằng lệnh:

```bash
cd /home/ad/vinuni/lesson1/DAY01-2A202601854-VuThanhPhuong
. .venv/bin/activate
pytest tests/ -v
```

Kết quả:
- 36 tests passed
- 0 failed

## 4. Kết quả cuối cùng

Dự án đã được hoàn thiện đúng theo yêu cầu của bài lab và các kiểm thử đều pass.
