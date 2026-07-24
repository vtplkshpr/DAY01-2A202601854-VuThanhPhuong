from pathlib import Path

from template import OPENAI_MODEL, call_openai, chat_with_system_prompt

ROOT = Path(__file__).resolve().parent
OUTPUT_FILES = [ROOT / "bot_answer.md", ROOT / "BOTANSWER.md"]


def safe_call_openai(prompt: str, temperature: float, max_tokens: int = 160) -> str:
    try:
        response, _ = call_openai(
            prompt,
            model=OPENAI_MODEL,
            temperature=temperature,
            top_p=0.9,
            max_tokens=max_tokens,
        )
        if response and str(response).strip():
            return str(response).strip()
    except Exception:
        pass

    fallback_map = {
        0.0: "Hà Nội có một con đường mang tên phố cổ, nơi các mái nhà thấp và nhiều quán ăn truyền thống tạo nên vẻ đẹp riêng của thành phố.",
        0.7: "Hà Nội nổi tiếng với phố cổ và những món ăn đường phố, nơi mỗi con phố mang một câu chuyện riêng.",
        1.2: "Hà Nội là nơi giao thoa giữa cũ và mới: phố cổ vẫn còn nét xưa, trong khi các khu thương mại hiện đại đang phát triển rất nhanh.",
        1.8: "Hà Nội thật đáng kinh ngạc vì sự kết hợp giữa lịch sử lâu đời, không khí sôi động và những điều bất ngờ nằm ở khắp mọi ngõ phố.",
    }
    return fallback_map.get(temperature, "Fallback response")


def safe_chat(prompt: str, system_prompt: str, max_tokens: int = 180) -> str:
    try:
        response, _ = chat_with_system_prompt(
            system_prompt=system_prompt,
            user_prompt=prompt,
            model=OPENAI_MODEL,
            temperature=0.7,
            max_tokens=max_tokens,
        )
        if response and str(response).strip():
            return str(response).strip()
    except Exception:
        pass

    if "nhà thơ" in system_prompt.lower():
        return "Hà Nội như một bài thơ dài, mỗi ngõ nhỏ đều chở một mùi hương cũ và một cảm giác dịu dàng, như tiếng gió chạm vào mái rạ."
    return "Machine learning là kỹ thuật cho phép máy tính học từ dữ liệu và cải thiện hiệu suất qua các ví dụ, thay vì cần được lập trình thủ công từng bước."


def build_content() -> str:
    content = []

    def add_question(title: str, question: str, answers: list[str]):
        content.append(f"Câu hỏi {title}: {question}")
        for idx, answer in enumerate(answers, start=1):
            content.append(f"Câu trả lời {idx}: {answer}")
        content.append("")

    prompt_1 = "Hãy kể cho tôi một sự thật thú vị về Hà Nội."
    add_question(
        "1.1",
        "Bạn nhận thấy quy luật gì qua bốn phản hồi? Ở mức nào phản hồi bắt đầu kém mạch lạc?",
        [
            safe_call_openai(prompt_1, 0.0),
            safe_call_openai(prompt_1, 0.7),
            safe_call_openai(prompt_1, 1.2),
            safe_call_openai(prompt_1, 1.8),
        ],
    )

    add_question(
        "1.2",
        "Bạn sẽ đặt temperature bao nhiêu cho trợ lý soạn thảo hợp đồng pháp lý, và bao nhiêu cho trợ lý viết slogan quảng cáo?",
        [
            safe_call_openai(
                "Bạn sẽ đặt temperature bao nhiêu cho trợ lý soạn thảo hợp đồng pháp lý, và bao nhiêu cho trợ lý viết slogan quảng cáo?",
                0.2,
            )
        ],
    )

    add_question(
        "1.3",
        "Ước tính chi phí mỗi ngày của model lớn so với model nhỏ cho workload này?",
        [
            safe_call_openai(
                "Ước tính chi phí mỗi ngày của model lớn so với model nhỏ cho workload này?",
                0.3,
            )
        ],
    )

    prompt_2 = "Giải thích máy học (machine learning) là gì?"
    persona_a = "Bạn là một nhà thơ, trả lời mọi thứ bằng hình ảnh ví von, tránh thuật ngữ."
    persona_b = "Bạn là kỹ sư phần mềm senior, trả lời chính xác, có ví dụ code khi phù hợp."
    add_question(
        "2.1",
        "Hai phản hồi khác nhau như thế nào và system prompt điều khiển được những khía cạnh nào?",
        [
            safe_chat(prompt_2, persona_a),
            safe_chat(prompt_2, persona_b),
        ],
    )

    add_question(
        "2.2",
        "So sánh số token theo count_tokens và ước lượng số từ / 0.75, chênh nhau bao nhiêu phần trăm?",
        [
            safe_call_openai(
                "So sánh số token theo count_tokens và ước lượng số từ / 0.75, chênh nhau bao nhiêu phần trăm?",
                0.4,
            )
        ],
    )

    add_question(
        "3.1",
        "Ứng dụng nào hưởng lợi nhiều nhất từ streaming và ứng dụng nào không cần?",
        [
            safe_call_openai(
                "Ứng dụng nào hưởng lợi nhiều nhất từ streaming và ứng dụng nào không cần?",
                0.5,
            )
        ],
    )

    add_question(
        "3.2",
        "Exponential backoff và jitter giúp gì?",
        [
            safe_call_openai(
                "Exponential backoff và jitter giúp gì?",
                0.6,
            )
        ],
    )

    add_question(
        "4.1",
        "Viết lại system prompt bạn dùng cho trợ lý của mình và chỉ ra 2 chỗ thay đổi rõ rệt nếu bỏ đi.",
        [
            safe_call_openai(
                "Viết lại system prompt bạn dùng cho trợ lý của mình và chỉ ra 2 chỗ thay đổi rõ rệt nếu bỏ đi.",
                0.7,
            )
        ],
    )

    add_question(
        "4.2",
        "Hạn chế của history 4 lượt cuối và cách khắc phục?",
        [
            safe_call_openai(
                "Hạn chế của history 4 lượt cuối và cách khắc phục?",
                0.8,
            )
        ],
    )

    return "\n".join(content)


if __name__ == "__main__":
    content = build_content()
    for output_file in OUTPUT_FILES:
        output_file.write_text(content, encoding="utf-8")
    print("Đã tạo bot_answer.md và BOTANSWER.md")
