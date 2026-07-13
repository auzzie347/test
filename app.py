import streamlit as st
import google.generativeai as genai

# 1. Streamlit Secrets에서 API 키를 안전하게 불러옵니다.
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except KeyError:
    st.error("Streamlit Cloud 설정에서 GOOGLE_API_KEY를 설정해주세요!")
    st.stop()

# 2. Gemini API 설정
genai.configure(api_key=GOOGLE_API_KEY)

# 웹 앱 UI 구성
st.title("? 나만의 간단한 Gemini 챗봇")
st.write("질문을 입력하면 구글 Gemini 모델이 답변해 드립니다.")

# 사용자 입력 받기
user_question = st.text_input("Gemini에게 무엇이든 물어보세요:", placeholder="예: 하늘은 왜 파랗지?")

if st.button("답변 받기"):
    if user_question:
        with st.spinner("Gemini가 생각하는 중..."):
            try:
                # 3. Gemini 모델 로드 및 답변 생성 (가장 기본적이고 안정적인 gemini-2.5-flash 모델 사용)
                model = genai.GenerativeModel("gemini-2.5-flash")
                response = model.generate_content(user_question)
                
                # 4. 결과 출력
                st.success("답변 완료!")
                st.write(response.text)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("질문을 먼저 입력해주세요.")