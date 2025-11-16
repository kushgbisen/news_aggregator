# Economic Intelligence Platform

Financial news search and analytics with SQLite backend.

## Start

```bash
pip install flask pandas fastparquet
python3 ingest.py  # Load parquet -> db
python3 app.py
# http://localhost:5000
```

## Database

`news.db` (283,520+ financial articles)

```sql
SELECT COUNT(*) FROM news_articles;
-- Latest articles
SELECT title, date FROM news_articles 
ORDER BY date DESC LIMIT 5;
-- Search by stock
SELECT title FROM news_articles 
WHERE stocks LIKE '%SBI%' LIMIT 10;
```

## Features

- Financial news aggregation
- Stock market intelligence
- Full-text search in titles/descriptions
- Feed type filtering
- Pagination (20/page)
- Dark theme with professional aesthetic
- Mobile responsive

---

*Economic Intelligence Platform | 2025*
