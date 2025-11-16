# News Aggregator

Fast news search with SQLite backend.

## Start

```bash
pip install flask pandas fastparquet
python3 ingest.py  # Load parquet -> db
python3 app.py
# http://localhost:5000
```

## Database

`news.db` (213,457 articles)

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

- Full-text search
- Feed type filtering
- Pagination (20/page)
- Dark theme
- Mobile responsive

---

*kushagra | 2025*
