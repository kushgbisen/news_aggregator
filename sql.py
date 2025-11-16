#!/usr/bin/env python3

import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def execute_query(sql, params=None):
    """Execute SQL query and return results."""
    try:
        conn = sqlite3.connect('news_aggregator.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if params:
            rows = cursor.execute(sql, params).fetchall()
        else:
            rows = cursor.execute(sql).fetchall()
        
        # Get column names
        columns = [description[0] for description in cursor.description] if cursor.description else []
        
        conn.close()
        return True, rows, columns, None
    except Exception as e:
        return False, None, None, str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    columns = []
    rows = []
    error = None
    query = ""
    
    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        if query:
            success, rows, columns, error = execute_query(query)
            if success:
                result = rows
            else:
                error = error
    
    return render_template('sql.html', 
                         query=query, 
                         result=result, 
                         columns=columns,
                         error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
