import streamlit as st
from google import genai

try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except KeyError:
    st.error("Streamlit Cloud 설정에서 GOOGLE_API_KEY를 설정해주세요!")
    st.stop()

client = genai.Client(api_key=GOOGLE_API_KEY)

st.title("🤖 나만의 간단한 Gemini 챗봇")
st.write("질문을 입력하면 구글 Gemini 모델이 답변해 드립니다.")

user_question = st.text_input("Gemini에게 무엇이든 물어보세요:", placeholder="예: 하늘은 왜 파랗지?")

if st.button("답변 받기"):
    if user_question:
        with st.spinner("Gemini가 생각하는 중..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=user_question,
                )
                st.success("답변 완료!")
                st.write(response.text)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("질문을 먼저 입력해주세요.")
