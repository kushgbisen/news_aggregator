# News Aggregator

A clean, minimal news aggregation web application built with Flask and SQLite. Features search, filtering, and database management tools.

## 🚀 Quick Start

```bash
# Start main news app
python3 app.py
# Visit: http://localhost:5000

# Start database schema viewer (for viva prep)  
python3 db.py
# Visit: http://localhost:5001

# Start SQL executor interface
python3 sql.py
# Visit: http://localhost:5002
```

## 📁 Project Structure

```
sql_mini_project/
├── app.py              # Main news aggregator (port 5000)
├── db.py               # Database schema display (port 5001)
├── sql.py              # SQL executor interface (port 5002)
├── news_aggregator.db  # SQLite database (10k articles)
├── SBIN.parquet       # Original data source
└── templates/         # HTML templates
    ├── index.html     # News UI
    ├── db.html        # Schema viewer
    └── sql.html       # SQL interface
```

## 🎯 Features

### Main News App (`/`)
- Browse 10,000 news articles
- Full-text search in titles/descriptions
- Filter by article type
- Pagination (20 items/page)
- Minimal dark theme design
- Mobile responsive

### Database Schema (`/db` - Port 5001)
- Complete table schema display
- Sample data preview
- Common SQL queries with results
- Viva preparation materials
- SQLite command reference

### SQL Executor (`/sql` - Port 5002)
- Execute custom SQL queries
- Real-time result display
- Quick example queries
- Error handling
- Clean table formatting

## 📊 Database

**Table**: `news_articles` (10,000 records)

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| title | TEXT | Article headline |
| feed_type | TEXT | Content type |
| link | TEXT | Article URL |
| description | TEXT | Article summary |
| date | TEXT | Publication date |
| image | TEXT | Thumbnail URL |
| publisher | TEXT | Source publisher |
| stocks | TEXT | Related stock tickers |
| article_id | TEXT | External ID |

## 🔍 Example Queries

```sql
-- Total articles
SELECT COUNT(*) FROM news_articles;

-- Articles with SBI stocks  
SELECT title FROM news_articles 
WHERE stocks LIKE '%SBI%' LIMIT 10;

-- Latest articles
SELECT title, date FROM news_articles 
ORDER BY date DESC LIMIT 5;

-- Group by content type
SELECT feed_type, COUNT(*) 
FROM news_articles GROUP BY feed_type;
```

## 🛠️ Tech Stack

- **Backend**: Python 3.13, Flask
- **Database**: SQLite 
- **Data**: Pandas, FastParquet
- **Frontend**: HTML, CSS, Space Grotesk font
- **Design**: Minimal dark theme, mobile-first

## 📱 Design

- **Theme**: Pure black (#000) with white text
- **Typography**: Space Grotesk (400/500 weights)
- **Layout**: Single column, 680px max-width
- **Responsive**: Mobile-optimized
- **Philosophy**: Content-first, minimal visual noise

## 📝 Installation

```bash
# Install dependencies
pip install flask pandas fastparquet

# Run any of the three apps
python3 app.py  # or db.py or sql.py
```

---

**Author**: Kushagra  
**Date**: November 2025  
**Purpose**: SQL Mini Project - Web-based News Aggregator
