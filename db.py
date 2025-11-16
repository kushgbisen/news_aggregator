#!/usr/bin/env python3

import sqlite3
from flask import Flask, render_template
from app import get_db

app = Flask(__name__)

@app.route('/')
def database_info():
    """Display database info and basic SQL operations for viva."""
    db = get_db()
    cursor = db.cursor()
    
    # Table structure
    cursor.execute('PRAGMA table_info(news_articles)')
    columns = cursor.fetchall()
    
    # Sample data
    cursor.execute('SELECT * FROM news_articles LIMIT 5')
    sample = cursor.fetchall()
    
    # Sample queries for viva
    queries = [
        ('Total articles:', 'SELECT COUNT(*) FROM news_articles'),
        ('Articles with SBI stock:', 'SELECT COUNT(*) FROM news_articles WHERE stocks LIKE "%SBI%"'),
        ('Latest 3 articles:', 'SELECT title, date FROM news_articles ORDER BY date DESC LIMIT 3'),
        ('Articles by feed type:', 'SELECT feed_type, COUNT(*) FROM news_articles GROUP BY feed_type')
    ]
    
    query_results = []
    for desc, query in queries:
        if 'GROUP BY' in query:
            result = cursor.execute(query).fetchall()
        else:
            result = cursor.execute(query).fetchone()[0]
        query_results.append((desc, query, result))
    
    db.close()
    
    return render_template('db.html', 
                         columns=columns, 
                         sample=sample, 
                         queries=query_results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
