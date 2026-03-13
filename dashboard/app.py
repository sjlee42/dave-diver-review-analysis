"""
Dave the Diver — Steam Review Analysis Dashboard
Streamlit app using pre-generated analysis images
"""

import streamlit as st
from pathlib import Path
from PIL import Image

# ── 경로 설정 ──
BASE_DIR = Path(__file__).parent.parent
FIGURES_DIR = BASE_DIR / "reports" / "figures"

# ── 페이지 설정 ──
st.set_page_config(
    page_title="Dave the Diver — Steam Review Analysis",
    page_icon="🤿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── 커스텀 CSS ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Noto+Sans+KR:wght@400;600&display=swap');

:root {
    --ocean-deep:  #0a1628;
    --ocean-mid:   #0d2444;
    --ocean-teal:  #00b4d8;
    --ocean-light: #90e0ef;
    --sand:        #f4a261;
    --coral:       #e76f51;
    --text-main:   #caf0f8;
    --text-dim:    #8ecae6;
    --border:      rgba(0,180,216,0.25);
}

html, body, [data-testid="stApp"] {
    background-color: var(--ocean-deep) !important;
    color: var(--text-main) !important;
}
[data-testid="stSidebar"] {
    background-color: var(--ocean-mid) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-main) !important; }

.dash-title {
    font-family: 'Space Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    color: var(--ocean-teal);
    letter-spacing: -1px;
    margin-bottom: 0;
    line-height: 1.1;
}
.dash-subtitle {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.95rem;
    color: var(--text-dim);
    margin-top: 4px;
    margin-bottom: 24px;
}
.kpi-card {
    background: linear-gradient(135deg, rgba(0,180,216,0.12), rgba(0,180,216,0.04));
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 24px;
    text-align: center;
}
.kpi-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 8px;
}
.kpi-value {
    font-family: 'Space Mono', monospace;
    font-size: 2rem;
    font-weight: 700;
    color: var(--ocean-teal);
    line-height: 1;
}
.kpi-sub {
    font-size: 0.75rem;
    color: var(--text-dim);
    margin-top: 4px;
}
.section-header {
    font-family: 'Space Mono', monospace;
    font-size: 0.88rem;
    color: var(--ocean-teal);
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
    margin-top: 32px;
    margin-bottom: 16px;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.insight-box {
    background: rgba(0,180,216,0.07);
    border-left: 3px solid var(--ocean-teal);
    border-radius: 0 8px 8px 0;
    padding: 16px 20px;
    margin-bottom: 16px;
}
.insight-box h4 {
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    color: var(--ocean-teal);
    margin: 0 0 8px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.insight-box p {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.88rem;
    color: var(--text-main);
    margin: 0;
    line-height: 1.7;
}
.warn-box {
    background: rgba(231,111,81,0.08);
    border-left: 3px solid var(--coral);
    border-radius: 0 8px 8px 0;
    padding: 16px 20px;
    margin-bottom: 16px;
}
.warn-box h4 {
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    color: var(--coral);
    margin: 0 0 8px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.warn-box p {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.88rem;
    color: var(--text-main);
    margin: 0;
    line-height: 1.7;
}
.img-caption {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 0.76rem;
    color: var(--text-dim);
    text-align: center;
    margin-top: 6px;
}
h1, h2, h3, h4, h5 { color: var(--text-main) !important; }
p, li, span { color: var(--text-main) !important; }
[data-testid="stExpander"] {
    background: rgba(0,180,216,0.04) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Space Mono', monospace;
    font-size: 0.82rem;
    color: var(--text-dim) !important;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    color: var(--ocean-teal) !important;
}
.stTabs [data-baseweb="tab-border"] {
    background-color: var(--ocean-teal) !important;
}
hr { border-color: var(--border) !important; }
img { border-radius: 8px; }
</style>
""", unsafe_allow_html=True)


# ── 헬퍼 함수 ──
def show_image(filename: str, caption: str = ""):
    path = FIGURES_DIR / filename
    if path.exists():
        img = Image.open(path)
        st.image(img, use_container_width=True)
        if caption:
            st.markdown(f'<p class="img-caption">{caption}</p>', unsafe_allow_html=True)
    else:
        st.warning(f"이미지 없음: {filename}")


def insight(title: str, body: str):
    st.markdown(f"""<div class="insight-box"><h4>{title}</h4><p>{body}</p></div>""",
                unsafe_allow_html=True)


def warn(title: str, body: str):
    st.markdown(f"""<div class="warn-box"><h4>{title}</h4><p>{body}</p></div>""",
                unsafe_allow_html=True)


def section(title: str):
    st.markdown(f'<p class="section-header">{title}</p>', unsafe_allow_html=True)


# ── 사이드바 ──
with st.sidebar:
    st.markdown("### 🤿 Dave the Diver")
    st.markdown('<p style="font-size:0.78rem;color:#8ecae6;">Steam Review Analysis</p>',
                unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio(
        "페이지",
        ["📊 Overview", "🎮 유저 세그먼트", "🗂 토픽 & 키워드", "📋 인사이트 리포트"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("""
    <div style="font-size:0.72rem;color:#8ecae6;line-height:1.9;">
        <b style="color:#00b4d8;">데이터</b><br>총 145,877건<br>2022-10 ~ 2026-02<br><br>
        <b style="color:#00b4d8;">LLM 분류 샘플</b><br>긍정 4,000건 · 부정 2,032건<br><br>
        <b style="color:#00b4d8;">분석 언어</b><br>영어 · 한국어 · 일본어
    </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════
# PAGE 1 — Overview
# ════════════════════════════════════════
if page == "📊 Overview":

    st.markdown('<p class="dash-title">🤿 Dave the Diver</p>', unsafe_allow_html=True)
    st.markdown('<p class="dash-subtitle">Steam Review NLP Analysis · 145,877 reviews · 2022–2026</p>',
                unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    cards = [
        ("총 리뷰", "145,877", "2022.10 ~ 2026.02"),
        ("긍정률", "96.7%", "압도적으로 긍정적"),
        ("분석 언어", "EN · KO", "+ 일본어 994건"),
        ("LLM 분류", "6,032건", "긍정 4,000 · 부정 2,032"),
    ]
    for col, (label, value, sub) in zip([col1, col2, col3, col4], cards):
        with col:
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-sub">{sub}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    section("월별 긍정률 추이 · 이벤트 타임라인")
    show_image("monthly_trend.png", "주요 업데이트/DLC 출시 전후 긍정률 변화")

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        section("언어별 분포")
        show_image("language_dist.png")
    with col_b:
        section("플레이타임 구간별 긍정률")
        show_image("playtime_segment.png")

    st.markdown("<br>", unsafe_allow_html=True)
    section("언어별 플레이타임 세그먼트 비교")
    show_image("playtime_segment_by_language.png", "영어·한국어·일본어 유저의 플레이타임 분포 비교")

    st.markdown("<br>", unsafe_allow_html=True)
    section("기술 이슈 리뷰 월별 추이")
    show_image("step1_tech_monthly_trend.png", "버그/충돌/성능 관련 부정 리뷰 비율 변화")


# ════════════════════════════════════════
# PAGE 2 — 유저 세그먼트
# ════════════════════════════════════════
elif page == "🎮 유저 세그먼트":

    st.markdown('<p class="dash-title">유저 세그먼트 분석</p>', unsafe_allow_html=True)
    st.markdown('<p class="dash-subtitle">플레이타임 구간별 행동 패턴 · 이탈 인사이트</p>',
                unsafe_allow_html=True)

    insight(
        "가설 2 — 라이트 유저의 높은 긍정률",
        "2~14h 유저는 긍정률이 높지만, 칭찬하는 요소의 구성이 플레이타임에 따라 질적으로 변한다. "
        "이탈 유저는 'chill/relaxing', 완주 유저는 'addictive/love/amazing' 사용. "
        "캐주얼 즐거움 ↔ 감정적 몰입 사이의 갭이 핵심 리텐션 문제. "
        "Tasting 세그먼트(2~6h) 엔딩 도달률: 45.8%."
    )

    section("플레이타임 빈별 긍정률 · 리뷰 수")
    show_image("step1_positive_rate_by_bin.png", "전 구간 93~97% flat → 내용(aspect) 변화 분석 필요")

    st.markdown("<br>", unsafe_allow_html=True)
    section("플레이타임별 LDA 토픽 구성비 변화")
    col1, col2 = st.columns(2)
    with col1:
        show_image("step2a_lda_topic_en_pos.png", "영어 긍정 리뷰")
    with col2:
        show_image("step2b_lda_topic_en_neg.png", "영어 부정 리뷰")

    st.markdown("<br>", unsafe_allow_html=True)
    section("LLM 분류 — aspect / category 구성비 변화")
    col3, col4 = st.columns(2)
    with col3:
        show_image("step4a_aspect_en.png", "영어 긍정 — aspect 구성비")
    with col4:
        show_image("step4b_category_en.png", "영어 부정 — category 구성비")

    col5, col6 = st.columns(2)
    with col5:
        show_image("step5a_aspect_ko.png", "한국어 긍정 — aspect 구성비")
    with col6:
        show_image("step5b_category_ko.png", "한국어 부정 — category 구성비")

    st.markdown("<br>", unsafe_allow_html=True)
    section("구간 변곡점 종합")
    show_image("step6_inflection_overview.png", "aspect 구성비 코사인 유사도 기반 변곡점 식별")

    st.markdown("<br>", unsafe_allow_html=True)
    section("영어 vs 한국어 버터플라이 비교")
    col7, col8 = st.columns(2)
    with col7:
        show_image("step7a_butterfly_pos_aspect.png", "긍정 aspect")
    with col8:
        show_image("step7b_butterfly_neg_category.png", "부정 category")

    st.markdown("<br>", unsafe_allow_html=True)
    section("이탈 인사이트 — 리뷰 후 추가 플레이타임")
    show_image("step8a_churn_analysis.png", "리뷰 작성 후 추가 플레이 분포 · 구간별 클리어 도달률")

    col9, col10 = st.columns(2)
    with col9:
        show_image("step8b_churned_vs_cleared_keywords.png", "이탈 vs 클리어 유저 특징 키워드")
    with col10:
        show_image("step8c_tone_change.png", "부정 리뷰 tone 변화")

    st.markdown("<br>", unsafe_allow_html=True)
    section("긍정 리뷰 속 숨겨진 비판 + 환불 분석")
    col11, col12 = st.columns(2)
    with col11:
        show_image("step8e_subcategory_heatmap.png", "부정 subcategory 히트맵")
    with col12:
        show_image("step6_refund_vs_nonrefund_category.png", "환불 vs 비환불 부정 category")

    warn(
        "강제 콘텐츠 통합의 양면성",
        "환불 유저 불만 1위 = forced_neg. "
        "그러나 비환불 유저에게는 같은 요소가 '비빔밥' 다양성으로 긍정 인식 → 환불률 0%. "
        "제거가 아닌 전환 시점의 완충 설계가 필요."
    )


# ════════════════════════════════════════
# PAGE 3 — 토픽 & 키워드
# ════════════════════════════════════════
elif page == "🗂 토픽 & 키워드":

    st.markdown('<p class="dash-title">토픽 & 키워드 분석</p>', unsafe_allow_html=True)
    st.markdown('<p class="dash-subtitle">LDA 토픽 모델링 · TF-IDF 키워드 · 공기어 네트워크</p>',
                unsafe_allow_html=True)

    section("LDA 토픽 분포")
    col1, col2 = st.columns(2)
    with col1:
        show_image("topic_dist_en.png", "영어 리뷰 — 토픽 분포")
    with col2:
        show_image("topic_dist_ko.png", "한국어 리뷰 — 토픽 분포")

    st.markdown("<br>", unsafe_allow_html=True)
    section("토픽 히트맵 — 플레이타임 구간 × 토픽")
    show_image("topic_heatmap.png")

    st.markdown("<br>", unsafe_allow_html=True)
    section("TF-IDF 감성 키워드")
    col3, col4 = st.columns(2)
    with col3:
        show_image("keywords_en.png", "영어 — 긍정/부정 상위 키워드")
    with col4:
        show_image("keywords_ko.png", "한국어 — 긍정/부정 상위 키워드")

    st.markdown("<br>", unsafe_allow_html=True)
    section("구간별 특징 키워드 히트맵 (영어)")
    show_image("step3_tfidf_heatmap_en.png")
    show_image("step3_keyword_trend_en.png", "주요 키워드 플레이타임 트렌드")

    st.markdown("<br>", unsafe_allow_html=True)
    section("공기어 네트워크 — 부정 리뷰")
    col5, col6 = st.columns(2)
    with col5:
        show_image("cooccurrence_network_en.png", "영어 부정 리뷰")
    with col6:
        show_image("cooccurrence_network_ko.png", "한국어 부정 리뷰")

    show_image("cooccurrence_bars.png", "영어 부정 리뷰 — 상위 공기어 쌍")

    insight(
        "언어권 차이",
        "영어: 경험 묘사 중심 / 한국어: 판단 선언 중심. "
        "한국어 상위 토큰 3위 = '넥슨' → 퍼블리셔 평판 효과가 한국 시장에 특유하게 작용."
    )

    st.markdown("<br>", unsafe_allow_html=True)
    section("장기 플레이 유저 (20h+) 분석")
    with st.expander("상세 차트 펼치기"):
        col7, col8 = st.columns(2)
        with col7:
            show_image("long_player_step1_posrate.png", "긍정률 패턴")
            show_image("long_player_step3_keyword_heatmap.png", "키워드 히트맵")
            show_image("long_player_step5_category.png", "부정 category")
        with col8:
            show_image("long_player_step2_lda_topic.png", "LDA 토픽")
            show_image("long_player_step4_tone.png", "부정 tone 변화")
            show_image("long_player_step7_aspect.png", "긍정 aspect")
        show_image("long_player_step7_churn_vs_stay.png", "이탈 vs 잔류")
        show_image("long_player_step8_butterfly.png", "버터플라이")


# ════════════════════════════════════════
# PAGE 4 — 인사이트 리포트
# ════════════════════════════════════════
elif page == "📋 인사이트 리포트":

    st.markdown('<p class="dash-title">인사이트 리포트</p>', unsafe_allow_html=True)
    st.markdown('<p class="dash-subtitle">기획자용 · 사업팀용 분리 — 데이터 기반 액션 아이템</p>',
                unsafe_allow_html=True)

    tab1, tab2 = st.tabs(
        ["🎯 기획자용 — 무엇을 고쳐야 하는가", "📈 사업팀용 — 숫자가 어떻게 움직이는가"]
    )

    with tab1:
        st.markdown("<br>", unsafe_allow_html=True)
        insight(
            "H1 — 첫인상 (sub-2h 유저)",
            "2시간 미만 이탈 유저의 부정률이 상대적으로 높음. "
            "주요 불만: 초반 튜토리얼 과부하 + QTE 강제성. "
            "2023-08 접근성 개선 업데이트 이후 이 구간 긍정률 유의미하게 회복."
        )
        insight(
            "H2 — 라이트 유저 이탈 (2~14h)",
            "긍정률 flat하지만 내용이 바뀐다. "
            "이탈 유저: 'chill / relaxing' / 완주 유저: 'addictive / love / amazing'. "
            "Tasting 세그먼트(2~6h) 엔딩 도달률 45.8% — 절반 가까이 이 구간에서 이탈."
        )
        warn(
            "이탈의 핵심 분기점",
            "5~10h 구간(Core Loop)에서 반복성 불만 첫 등장. "
            "이 지점에 새 게임플레이 메커닉 언락 또는 스토리 후킹 포인트 필요."
        )
        warn(
            "강제 콘텐츠 통합의 양면성",
            "환불 유저 불만 1위 = forced_neg. 비환불 유저에게는 다양성으로 긍정 인식. "
            "제거가 아닌 전환 시점 완충 설계 권장."
        )
        section("액션 아이템")
        st.markdown("""
        <ol style="font-family:'Noto Sans KR',sans-serif;font-size:0.9rem;line-height:2.2;color:#caf0f8;padding-left:1.2rem;">
            <li><b style="color:#00b4d8;">5~8h 지점 메커닉 언락</b> — 반복 피로가 시작되는 Core Loop에 새 요소 도입</li>
            <li><b style="color:#00b4d8;">진행도 시각화 강화</b> — "엔딩까지 XX% 남았다" 명시적 동기 부여</li>
            <li><b style="color:#00b4d8;">초반 온보딩 단순화</b> — 첫 30분 핵심 루프만, 복잡한 시스템은 단계적 언락</li>
            <li><b style="color:#00b4d8;">강제 전환 시점 완충</b> — 다이빙 ↔ 레스토랑 전환을 자연스러운 스토리 흐름으로 포장</li>
        </ol>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("<br>", unsafe_allow_html=True)
        insight(
            "긍정률 곡선의 한계",
            "DtD는 압도적 긍정 게임 → 긍정률 변화 추적 자체가 무의미. "
            "LLM 분류 기반 aspect/category 구성 변화가 더 유효한 세그멘테이션 지표."
        )
        insight(
            "업데이트/DLC 효과",
            "DREDGE DLC(2023-12), 고질라 DLC(2024-05) 출시 후 리뷰 볼륨 급증 + 긍정률 소폭 상승. "
            "무료 DLC 전략이 커뮤니티 재활성화에 효과적임을 데이터로 확인."
        )
        insight(
            "글로벌 vs 한국 시장",
            "영어: 게임플레이 경험 묘사 중심 / 한국: 판단 선언 + 퍼블리셔 인식(넥슨) 영향. "
            "한국 마케팅은 민트로켓 브랜드를 전면에 내세우는 전략이 유효."
        )
        section("마케팅 키워드 제언")
        st.markdown("""
        <ul style="font-family:'Noto Sans KR',sans-serif;font-size:0.9rem;line-height:2.2;color:#caf0f8;padding-left:1.2rem;">
            <li><b style="color:#00b4d8;">글로벌 Steam</b> — 완주 유저 최다 키워드: <b>addictive · charming · unique</b></li>
            <li><b style="color:#00b4d8;">한국 마케팅</b> — '민트로켓' 브랜드 강조 + 수상 실적</li>
            <li><b style="color:#00b4d8;">리텐션 캠페인</b> — "5시간까지 했다면 엔딩이 궁금해질 겁니다"</li>
            <li><b style="color:#00b4d8;">DLC 전략</b> — 무료 콜라보가 볼륨 + 긍정률 동시 기여, 지속 권장</li>
        </ul>
        """, unsafe_allow_html=True)
        section("후속 과제")
        st.markdown("""
        <ul style="font-family:'Noto Sans KR',sans-serif;font-size:0.83rem;line-height:2;color:#8ecae6;padding-left:1.2rem;">
            <li>일본어 유저 낮은 긍정률 원인 (로컬라이제이션 vs 퍼블리셔 인식)</li>
            <li>Steam Deck 유저 행동 — 샘플 사이즈 검증 필요</li>
            <li>얼리액세스 코호트 복귀율</li>
            <li>리뷰 후 이탈 유저 정밀 분석 (playtime_forever - playtime_at_review &lt; 1h)</li>
        </ul>
        """, unsafe_allow_html=True)
