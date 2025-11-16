#!/usr/bin/env python3

import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db():
    return sqlite3.connect('news.db')

def build_query(search='', feed_type=''):
    conditions, params = [], []
    
    if search:
        conditions.append("(title LIKE ? OR description LIKE ?)")
        params.extend([f'%{search}%', f'%{search}%'])
    
    if feed_type:
        conditions.append("feed_type = ?")
        params.append(feed_type)
    
    where = f" WHERE {' AND '.join(conditions)}" if conditions else ""
    return f"SELECT * FROM news_articles{where}", params

@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    search = request.args.get('search', '')
    feed_type = request.args.get('feed_type', '')
    per_page = 20
    
    db = get_db()
    
    # Total count
    query, params = build_query(search, feed_type)
    total = db.execute(query.replace("SELECT *", "SELECT COUNT(*)"), params).fetchone()[0]
    
    # Paginated results
    query += " ORDER BY date DESC LIMIT ? OFFSET ?"
    params.extend([per_page, (page - 1) * per_page])
    
    db.row_factory = sqlite3.Row
    articles = db.execute(query, params).fetchall()
    db.close()
    
    return render_template('index.html',
        articles=articles,
        search=search,
        feed_type=feed_type,
        page=page,
        total_pages=(total + per_page - 1) // per_page,
        total=total
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
