import streamlit as st
from openai import OpenAI

# 사이드바에서 API 키 입력 받기
st.sidebar.title("API 설정")
api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")

# OpenAI 클라이언트 초기화 (API 키가 있는 경우만)
client = None
if api_key:
    client = OpenAI(api_key=api_key)

# Streamlit 페이지 제목 설정
st.title("DALL-E 3 이미지 생성기")

# 사용자 입력 받기
prompt = st.text_input("단어를 입력하세요.", "a white siamese cat")

# 사용자 입력 단어가 '우주에 떠 있는' 형태로 자동으로 바뀌기
if prompt:
    prompt = f"{prompt} floating in space"

# 버튼을 클릭했을 때 이미지 생성
if st.button("이미지 생성"):
    if client:
        # OpenAI API를 사용하여 이미지 생성
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # 생성된 이미지 URL 가져오기
        image_url = response.data[0].url

        # 이미지 출력
        st.image(image_url, caption=f"Generated Image: {prompt}")
    else:
        st.warning("API 키를 사이드바에 입력하세요.")