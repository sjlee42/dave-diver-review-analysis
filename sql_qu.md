### 생성된 DB 테이블
| 테이블 | 내용 | 복합키 |
|--------|------|--------|
| `neg_reviews_classified` | 영어+한국어 부정 리뷰 × 최대 3 methods | (review_id, classify_method) |

### 테이블 구조
```
neg_reviews_classified
├── 식별: review_id (PK1), classify_method (PK2), language_group
├── 분류: category, sub_category, tone, actual_sentiment, confidence, reason
├── 유저: play_segment, playtime_hours, num_games_owned, num_reviews
├── 구매: steam_purchase, received_for_free
├── 영향력: votes_up, votes_funny, weighted_vote_score
├── 개발자: has_dev_response
├── 시기: review_month, written_during_early_access
└── 텍스트: review_text, cleaned_text
```

### SQL 쿼리 예시
```sql
-- 건설적 비판만 (기획자용)
SELECT * FROM neg_reviews_classified
WHERE tone = 'constructive' AND classify_method = 'gemini';

-- 긍정인데 비추천 유저
SELECT * FROM neg_reviews_classified
WHERE actual_sentiment = 'positive_but_negative_vote';

-- 20시간 전후 감성 분기
SELECT
    CASE WHEN playtime_hours < 20 THEN '0-20h'
         WHEN playtime_hours < 30 THEN '20-30h'
         ELSE '30h+' END as band,
    category, COUNT(*) as n
FROM neg_reviews_classified
WHERE classify_method = 'gemini'
GROUP BY band, category ORDER BY band, n DESC;

-- 개발자가 어떤 불만에 응답했는가?
SELECT category,
       SUM(has_dev_response) as with_resp,
       COUNT(*) as total,
       ROUND(SUM(has_dev_response)*100.0/COUNT(*),1) as resp_rate
FROM neg_reviews_classified
WHERE classify_method = 'gemini'
GROUP BY category ORDER BY resp_rate DESC;

-- 영향력 큰데 개발자 응답 없는 리뷰
SELECT category, votes_up, weighted_vote_score,
       SUBSTR(review_text,1,100) as preview
FROM neg_reviews_classified
WHERE has_dev_response = 0 AND weighted_vote_score > 0.5
  AND classify_method = 'gemini'
ORDER BY weighted_vote_score DESC LIMIT 20;

-- 3모델 비교: 같은 리뷰의 카테고리 차이
SELECT r.review_id,
       r.category as rules_cat,
       g.category as gemini_cat,
       a.category as anthropic_cat
FROM neg_reviews_classified r
JOIN neg_reviews_classified g ON r.review_id = g.review_id
JOIN neg_reviews_classified a ON r.review_id = a.review_id
WHERE r.classify_method = 'rules'
  AND g.classify_method = 'gemini'
  AND a.classify_method = 'anthropic'
  AND NOT (r.category = g.category AND g.category = a.category)
LIMIT 20;
```