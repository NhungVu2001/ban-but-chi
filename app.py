
import streamlit as st

# CẤU HÌNH WEBSITE
st.set_page_config(
    page_title="Bạn Bút Chì - Học phân số",
    page_icon="✏️",
    layout="centered"
)

# LỚP CHATBOT
class PhanSoBot:
    def __init__(self):
        self.name = "Bạn Bút Chì"

    def greet(self):
        return (
            f"Xin chào! Tớ là {self.name}, trợ lý học tập toán của cậu đây. "
            "Hôm nay chúng ta cùng khám phá về Phân số nhé! "
            "Cậu hãy tưởng tượng cậu có một chiếc bánh hình tròn, "
            "cậu chia nó thành 4 phần bằng nhau và lấy đi 1 phần. "
            "Đố cậu biết phần lấy đi được biểu diễn thế nào?"
        )

    def respond(self, student_input):
        text = student_input.lower()

        if "1/4" in text or "một phần tư" in text:
            return (
                "Giỏi quá! Cậu đã quan sát rất chính xác. "
                "Thế cậu có thể cho tớ biết số 4 ở dưới gạch ngang "
                "trong phân số 1/4 chỉ điều gì không?"
            )

        elif "4/1" in text:
            return (
                "Cậu đã đếm rất sát sao các con số rồi đấy! "
                "Nhưng hãy nhớ lại xem: phần được lấy ra nằm ở trên "
                "hay ở dưới gạch ngang nhỉ? Cậu thử suy nghĩ lại nhé!"
            )

        elif "không đều" in text or "to nhỏ" in text:
            return (
                "Ý tưởng của cậu rất thú vị! Tuy nhiên, hãy nhớ rằng "
                "phân số chỉ xuất hiện khi các phần của đơn vị phải "
                "như thế nào với nhau nhỉ? Cậu thử chia lại cho thật đều nhé!"
            )

        elif "chia" in text and (
            "phần" in text or "bằng nhau" in text
        ):
            return (
                "Chính xác tuyệt vời! Cậu nắm rất chắc bài rồi đấy. "
                "Số 4 chính là số phần bằng nhau mà cái bánh được chia ra."
            )

        else:
            return (
                "Tớ hiểu ý cậu, nhưng cậu hãy thử quan sát kỹ lại "
                "hình vẽ hoặc đề bài xem: Các phần được chia đã bằng nhau "
                "chưa nhỉ? Cậu thử mô tả lại cho tớ nghe nhé!"
            )


# THIẾT KẾ GIAO DIỆN
st.markdown("""
<style>
.stApp {
    background-color: #FFF9ED;
}

h1 {
    color: #79552C;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #98794F;
    font-size: 17px;
}

div[data-testid="stChatMessage"] {
    background-color: white;
    border-radius: 15px;
    padding: 12px;
}
</style>
""", unsafe_allow_html=True)


# TIÊU ĐỀ
st.title("✏️ BẠN BÚT CHÌ")

st.markdown(
    '<p class="subtitle">Cùng học toán vui vẻ mỗi ngày!</p>',
    unsafe_allow_html=True
)

st.divider()


# KHỞI TẠO CHATBOT
if "bot" not in st.session_state:
    st.session_state.bot = PhanSoBot()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": st.session_state.bot.greet()
        }
    ]


# HIỂN THỊ TIN NHẮN
for message in st.session_state.messages:
    if message["role"] == "assistant":
        with st.chat_message("assistant", avatar="✏️"):
            st.write(message["content"])
    else:
        with st.chat_message("user", avatar="🧑‍🎓"):
            st.write(message["content"])


# Ô NHẬP CÂU TRẢ LỜI
student_input = st.chat_input("Nhập câu trả lời của cậu...")

if student_input:
    st.session_state.messages.append({
        "role": "user",
        "content": student_input
    })

    reply = st.session_state.bot.respond(student_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    st.rerun()


# NÚT HỌC LẠI
st.divider()

if st.button("🔄 Học lại từ đầu", use_container_width=True):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": st.session_state.bot.greet()
        }
    ]
    st.rerun()

st.caption("© Bạn Bút Chì | Trợ lý học tập toán")
