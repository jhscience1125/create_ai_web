import streamlit as st

# # 제목 추가
st.title("안녕, Streamlit!")

# # 부제목 추가
st.subheader("Streamlit를 사용해보세요")

# # 텍스트 표시
st.write("이것은 간단한 예제입니다. 아래에서 다양한 Streamlit 기능을 확인해보세요!")

# # 버튼 추가
if st.button("버튼 클릭"):
    st.write("버튼이 클릭되었습니다!")

# # 슬라이더 추가
number = st.slider("숫자를 선택하세요", 0, 100, 50)
st.write(f"선택된 숫자는: {number}")

# # 텍스트 입력 추가
name = st.text_input("이름을 입력하세요")
st.write(f"입력된 이름: {name}")

# # 체크박스 추가
if st.checkbox("체크박스"):
    st.write("체크박스가 선택되었습니다!")

# # 라디오 버튼 추가
# option = st.radio("옵션을 선택하세요", ("옵션 1", "옵션 2", "옵션 3"))
# st.write(f"선택된 옵션: {option}")

# # 셀렉트 박스 추가
# select_option = st.selectbox("옵션을 선택하세요", ["옵션 A", "옵션 B", "옵션 C"])
# st.write(f"선택된 셀렉트 박스 옵션: {select_option}")

# # 멀티 셀렉트 추가
# multi_select = st.multiselect("하나 이상의 옵션을 선택하세요", ["옵션 1", "옵션 2", "옵션 3"])
# st.write(f"선택된 멀티 셀렉트 옵션: {', '.join(multi_select)}")

# # 이미지 표시
# st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1DNsfskjJtWhewcdCt8_4spNsZf7lmL3wKQ&s", caption="샘플 이미지")

# # 차트 추가 (예: 라인 차트)
# import pandas as pd
# import numpy as np

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# st.line_chart(chart_data)

# # 파일 업로드 기능 추가
# uploaded_file = st.file_uploader("파일을 업로드하세요")
# if uploaded_file is not None:
#     st.write("파일이 업로드되었습니다!")
