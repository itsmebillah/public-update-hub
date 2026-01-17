"""
বাংলাদেশ আপডেট API - এক ফাইলের সার্ভার
রান করতে: python api.py
"""

from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)  # সব জায়গা থেকে অ্যাক্সেস দিবে

# ডাটাবেস তৈরি
def init_db():
    conn = sqlite3.connect('data.db', check_same_thread=False)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS updates
                 (id INTEGER PRIMARY KEY, 
                  title TEXT, 
                  summary TEXT, 
                  url TEXT,
                  source TEXT,
                  category TEXT,
                  date TEXT)''')
    
    # ডেমো ডাটা যোগ
    demo_data = [
        ("বিসিএস ৪৫তম পরীক্ষার বিজ্ঞপ্তি", "বাংলাদেশ সিভিল সার্ভিস ৪৫তম বার্ষিক পরীক্ষার বিজ্ঞপ্তি প্রকাশিত হয়েছে", "https://www.bpsc.gov.bd", "বিসিএস কমিশন", "job", "২০২৪-০১-১৫"),
        ("সোনালী ব্যাংকে নিয়োগ", "সোনালী ব্যাংক লিমিটেডে সহকারী অফিসার পদে নিয়োগ", "https://www.sonalibank.com.bd", "সোনালী ব্যাংক", "job", "২০২৪-০১-১৪"),
        ("এইচএসসি পরীক্ষার রুটিন", "২০২৪ সালের এইচএসসি পরীক্ষার রুটিন প্রকাশ", "http://www.educationboardresults.gov.bd", "শিক্ষা বোর্ড", "education", "২০২৪-০১-১৩"),
        ("জাতীয় বিশ্ববিদ্যালয় পরীক্ষা স্থগিত", "অনার্স চতুর্থ বর্ষের পরীক্ষা এক সপ্তাহ পিছানো হয়েছে", "https://www.nu.ac.bd", "জাতীয় বিশ্ববিদ্যালয়", "education", "২০২৪-০১-১২"),
        ("২০২৪ সালের ছুটির তালিকা", "সরকারি ছুটির তালিকা প্রকাশিত হয়েছে", "https://cabinet.gov.bd", "মন্ত্রিপরিষদ বিভাগ", "government", "২০২৪-০১-১১"),
        ("ইন্টারনেট ডাটা দাম কমানো", "মোবাইল ইন্টারনেট ডাটা প্যাকের দাম কমানোর সিদ্ধান্ত", "https://www.btrc.gov.bd", "বিটিআরসি", "hot", "২০২৪-০১-১০"),
    ]
    
    c.executemany("INSERT OR IGNORE INTO updates (title, summary, url, source, category, date) VALUES (?, ?, ?, ?, ?, ?)", demo_data)
    conn.commit()
    conn.close()
    
    print("✅ ডাটাবেস তৈরি হয়েছে")

# API এন্ডপয়েন্টস
@app.route('/')
def home():
    return jsonify({
        "message": "বাংলাদেশ আপডেট API সার্ভার চলছে",
        "author": "Bangladesh Public Updates",
        "endpoints": ["/api/all", "/api/jobs", "/api/education", "/api/government", "/api/hot"]
    })

@app.route('/api/all')
def get_all():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM updates ORDER BY date DESC")
    data = c.fetchall()
    conn.close()
    
    updates = []
    for row in data:
        updates.append({
            "id": row[0],
            "title": row[1],
            "summary": row[2],
            "url": row[3],
            "source": row[4],
            "category": row[5],
            "date": row[6]
        })
    
    return jsonify({
        "success": True,
        "count": len(updates),
        "updates": updates
    })

@app.route('/api/jobs')
def get_jobs():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM updates WHERE category='job' ORDER BY date DESC")
    data = c.fetchall()
    conn.close()
    
    updates = []
    for row in data:
        updates.append({
            "id": row[0],
            "title": row[1],
            "summary": row[2],
            "url": row[3],
            "source": row[4],
            "date": row[6]
        })
    
    return jsonify({
        "success": True,
        "category": "চাকরি",
        "count": len(updates),
        "updates": updates
    })

@app.route('/api/education')
def get_education():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM updates WHERE category='education' ORDER BY date DESC")
    data = c.fetchall()
    conn.close()
    
    updates = []
    for row in data:
        updates.append({
            "id": row[0],
            "title": row[1],
            "summary": row[2],
            "url": row[3],
            "source": row[4],
            "date": row[6]
        })
    
    return jsonify({
        "success": True,
        "category": "শিক্ষা",
        "count": len(updates),
        "updates": updates
    })

@app.route('/api/government')
def get_government():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM updates WHERE category='government' ORDER BY date DESC")
    data = c.fetchall()
    conn.close()
    
    updates = []
    for row in data:
        updates.append({
            "id": row[0],
            "title": row[1],
            "summary": row[2],
            "url": row[3],
            "source": row[4],
            "date": row[6]
        })
    
    return jsonify({
        "success": True,
        "category": "সরকারি নোটিশ",
        "count": len(updates),
        "updates": updates
    })

@app.route('/api/hot')
def get_hot():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM updates WHERE category='hot' ORDER BY date DESC")
    data = c.fetchall()
    conn.close()
    
    updates = []
    for row in data:
        updates.append({
            "id": row[0],
            "title": row[1],
            "summary": row[2],
            "url": row[3],
            "source": row[4],
            "date": row[6]
        })
    
    return jsonify({
        "success": True,
        "category": "হট আপডেট",
        "count": len(updates),
        "updates": updates
    })

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    init_db()
    print("🚀 সার্ভার শুরু হচ্ছে...")
    print("👉 ব্রাউজারে যান: http://localhost:5000")
    print("👉 API টেস্ট: http://localhost:5000/api/jobs")
    app.run(host='0.0.0.0', port=5000, debug=True)
