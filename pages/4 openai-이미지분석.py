import streamlit as st
from openai import OpenAI
import tempfile
import base64

# 사이드바에서 API 키 입력 받기
st.sidebar.title("API 설정")
api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if api_key:
    # OpenAI 클라이언트 초기화
    client = OpenAI(api_key=api_key)

    # Streamlit 페이지 제목 설정
    st.title("인공지능 이미지 분석기")

    # 이미지 업로드 기능 추가
    uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

    def encode_image(image_file):
        """이미지를 Base64로 인코딩하는 함수"""
        return base64.b64encode(image_file).decode('utf-8')

    if uploaded_file is not None:
        # 업로드된 이미지를 임시 파일로 저장
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_file_path = temp_file.name

        # 이미지를 Base64로 인코딩
        with open(temp_file_path, "rb") as image_file:
            base64_image = encode_image(image_file.read())

        # OpenAI API를 사용하여 이미지 분석
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "아래 사진은 세포 분열을 그림으로 표현한 작품입니다. 학생의 작품을 보고, 평가를 해주고, 어떻게 표현하면 더 잘할수 있는지 조언해주세요."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
        )

        # 결과 출력
        st.subheader("이미지 분석 결과")
        st.write(response.choices[0].message.content)  # 수정된 부분
else:
    st.warning("API 키를 사이드바에 입력하세요.")
