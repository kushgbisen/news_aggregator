#!/usr/bin/env python3

import sqlite3
import pandas as pd
import os

def ingest_data(parquet_file='news.parquet', db_file='news.db'):
    """Ingest parquet data into SQLite database."""
    
    print(f"Reading {parquet_file}...")
    df = pd.read_parquet(parquet_file)
    print(f"Loaded {len(df):,} rows from parquet")
    
    # Clean data
    df = df.rename(columns={'_id': 'article_id'})
    df = df.drop_duplicates(subset=['link'])
    df = df.fillna('')
    
    print(f"After cleaning: {len(df):,} unique rows")
    
    # Remove existing database
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Removed existing {db_file}")
    
    # Create database and table
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE news_articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            feed_type TEXT,
            link TEXT UNIQUE,
            description TEXT,
            date TEXT,
            image TEXT,
            publisher TEXT,
            stocks TEXT,
            article_id TEXT UNIQUE
        )
    ''')
    
    # Insert data
    df.to_sql('news_articles', conn, if_exists='append', index=False)
    
    conn.commit()
    conn.close()
    print(f"Successfully ingested {len(df):,} articles into {db_file}")

if __name__ == '__main__':
    ingest_data()
