#자주 바뀌는 설정 값 모아두기
# ── Steam API ──
APP_ID = 1868140                        # Dave the Diver의 Steam App ID
API_BASE_URL = "https://store.steampowered.com/appreviews"

# ── 파일 경로 ──
RAW_DATA_DIR = "data/raw/"
PROCESSED_DATA_DIR = "data/processed/"
SAMPLE_DATA_DIR = "data/sample/"
DB_PATH = "data/dave_diver.db"

# ── 분석 설정 ──
PLAYTIME_SEGMENTS = {
    "casual":   (0, 120),       # 2시간 미만
    "regular":  (120, 600),     # 2~10시간
    "engaged":  (600, 3000),    # 10~50시간
    "hardcore": (3000, 999999), # 50시간 이상
}
N_TOPICS = 8

# ── 주요 이벤트 타임라인 (EDA 시각화에서 세로선으로 표시) ──
EVENTS = {
    # ── 출시 ──────────────────────────────────────────
    "2022-10-28": "얼리액세스 출시 (PC)",
    "2023-06-28": "정식 출시 (PC/Mac)",

    # ── 주요 업데이트 ──────────────────────────────────
    "2023-08":    "접근성 개선 업데이트 (QTE 스킵 등)",
    "2023-10-12": "10/11 콘텐츠 업데이트",

    # ── 플랫폼 확장 ────────────────────────────────────
    "2023-10-26": "Nintendo Switch 출시",
    "2024-04-16": "PlayStation 4 / 5 출시",
    "2025-11-20": "Xbox One / Series X|S 출시",
    "2025-11-06": "Nintendo Switch 2 Edition 출시",

    # ── DLC / 콜라보 ───────────────────────────────────
    "2023-12-15": "DREDGE 크로스오버 DLC 출시 (무료, 상시)",
    "2024-05-23": "고질라 콘텐츠 팩 출시 (무료, 기간한정 ~2024-11-23)",
    "2024-06-28": "Guilty Gear Strive 콘텐츠 팩 (Switch 물리판 Anniversary Edition)",
    "2025-04-10": "고질라 콘텐츠 팩 복귀 (유료, ~2026-12-31)",
    "2025-06-27": "DREDGE DLC 복귀 (~2026-12-31)",

    # ── 기타 ──────────────────────────────────────────
    "2024-09":    "Nexon, Mintrocket 완전 자회사 편입",
    "2024-11":    "누적 판매량 500만 장 돌파",
}

# ── Chroma 설정 ──
CHROMA_COLLECTION_EN = "reviews_en"
CHROMA_COLLECTION_KO = "reviews_ko"