import streamlit as st

# 브라우저 탭에 보이는 제목과 아이콘
st.set_page_config(page_title="곱셈 그림 놀이", page_icon="🍎", layout="centered")

# -----------------------------------------------------------------------------
# 기본 설정

# 선택할 수 있는 그림 (이모지라서 따로 이미지 파일이 필요 없어요)
PICTURES = {
    "사과": "🍎",
    "별": "⭐",
    "꽃": "🌸",
}

# 처음 상태 (초기화 버튼을 누르면 이 값으로 돌아가요)
DEFAULTS = {
    "multiplicand": 2,  # 피승수: 한 줄에 놓을 그림 수
    "multiplier": 3,    # 승수: 줄 수
    "picture": "사과",
}

# 처음 실행할 때 기본값을 저장해 둬요
for key, value in DEFAULTS.items():
    st.session_state.setdefault(key, value)


def reset():
    """숫자와 그림 선택을 처음 상태로 되돌려요."""
    for key, value in DEFAULTS.items():
        st.session_state[key] = value


# 글자와 그림을 크게 보여주기 위한 스타일
st.markdown(
    """
    <style>
    /* 입력창 이름표와 입력값 글자 크기 */
    div[data-testid="stWidgetLabel"] p { font-size: 1.4rem; font-weight: 700; }
    div[data-testid="stNumberInput"] input { font-size: 1.6rem; }
    div[role="radiogroup"] label p { font-size: 1.6rem; }
    div[data-testid="stButton"] button p { font-size: 1.3rem; font-weight: 700; }

    /* 그림 배열: 칸과 줄의 간격을 똑같이 맞춰요 */
    .picture-grid {
        display: grid;
        gap: 14px;
        justify-content: center;
        padding: 24px;
        margin: 8px auto;
        background: #fff8e7;
        border: 3px dashed #f0b44c;
        border-radius: 20px;
        width: fit-content;
    }
    .picture-cell {
        width: 64px;
        height: 64px;
        font-size: 52px;
        line-height: 64px;
        text-align: center;
    }

    /* 계산 결과 */
    .equation {
        text-align: center;
        font-size: 4rem;
        font-weight: 800;
        color: #d9480f;
        margin: 16px 0 4px;
    }
    .explain {
        text-align: center;
        font-size: 1.4rem;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 화면 그리기

st.title("🍎 곱셈 그림 놀이")
st.markdown(
    "<p style='font-size:1.3rem'>같은 개수의 그림이 여러 줄 반복되면 곱셈으로 셀 수 있어요!</p>",
    unsafe_allow_html=True,
)

# 1. 숫자 두 개 입력
col1, col2 = st.columns(2)
with col1:
    st.number_input(
        "한 줄에 놓을 그림 수(피승수)",
        min_value=1,
        max_value=9,
        step=1,
        key="multiplicand",
    )
with col2:
    st.number_input(
        "줄 수(승수)",
        min_value=1,
        max_value=9,
        step=1,
        key="multiplier",
    )

# 2. 그림 선택
st.radio(
    "어떤 그림을 쓸까요?",
    options=list(PICTURES.keys()),
    format_func=lambda name: f"{PICTURES[name]} {name}",
    horizontal=True,
    key="picture",
)

# 5. 초기화 버튼
st.button("🔄 초기화", on_click=reset)

multiplicand = int(st.session_state["multiplicand"])
multiplier = int(st.session_state["multiplier"])
emoji = PICTURES[st.session_state["picture"]]
total = multiplicand * multiplier

st.divider()

# 3. 2차원 배열 시각화: 한 줄에 피승수만큼, 승수만큼 줄을 만들어요
cells = "".join(
    f'<div class="picture-cell">{emoji}</div>' for _ in range(total)
)
st.markdown(
    f'<div class="picture-grid" '
    f'style="grid-template-columns: repeat({multiplicand}, 64px);">{cells}</div>',
    unsafe_allow_html=True,
)

# 4. 계산 결과 표시
st.markdown(
    f'<div class="equation">{multiplicand} × {multiplier} = {total}</div>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<div class="explain">{emoji} {multiplicand}개씩 {multiplier}줄이면 '
    f"모두 {total}개예요.</div>",
    unsafe_allow_html=True,
)
