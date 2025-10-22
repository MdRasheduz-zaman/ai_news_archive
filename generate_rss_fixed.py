#!/usr/bin/env python3

"""
RSS Feed Generator for AI Newsletter Archive
Automatically generates RSS feed from newsletter HTML files
"""

import os
import re
from datetime import datetime

# Configuration
BASE_URL = "https://mdrasheduz-zaman.github.io/ai_news_archive"
OUTPUT_DIR = "/Users/md.rasheduzzaman/Desktop/AI Newsletter/output"
FEED_FILE = os.path.join(OUTPUT_DIR, "feed.xml")

def extract_date_from_filename(filename):
    """Extract date from filename format: AI_Newsletter_YYYY_MM_DD.html or AI_Newsletter_YYYY-MM-DD.html"""
    # Try underscore format first
    match = re.match(r'AI_Newsletter_(\d{4})_(\d{2})_(\d{2})\.html', filename)
    if match:
        year, month, day = match.groups()
        return datetime(int(year), int(month), int(day))
    
    # Try hyphen format
    match = re.match(r'AI_Newsletter_(\d{4})-(\d{2})-(\d{2})\.html', filename)
    if match:
        year, month, day = match.groups()
        return datetime(int(year), int(month), int(day))
    
    return None

def format_rfc822_date(dt):
    """Format datetime to RFC-822 format for RSS"""
    return dt.strftime('%a, %d %b %Y %H:%M:%S GMT')

def get_newsletter_files():
    """Get all newsletter HTML files sorted by date (newest first)"""
    newsletter_files = []
    for file in os.listdir(OUTPUT_DIR):
        if file.startswith('AI_Newsletter_') and file.endswith('.html'):
            date = extract_date_from_filename(file)
            if date:
                newsletter_files.append((file, date))
    
    # Sort by date, newest first
    newsletter_files.sort(key=lambda x: x[1], reverse=True)
    return newsletter_files

def escape_xml(text):
    """Escape special XML characters"""
    return (text
        .replace('&', '&amp;')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
        .replace('"', '&quot;')
        .replace("'", '&apos;'))

def create_rss_feed():
    """Generate the RSS feed"""
    newsletters = get_newsletter_files()
    
    # Start building XML as string
    xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_lines.append('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">')
    xml_lines.append('    <channel>')
    xml_lines.append('        <title>PythRaSh\'s AI Newsletter</title>')
    xml_lines.append('        <description>Your Weekly Digest of AI Insights - Covering the latest developments, insights, and trends in artificial intelligence in Biology</description>')
    xml_lines.append(f'        <link>{BASE_URL}/</link>')
    xml_lines.append(f'        <atom:link href="{BASE_URL}/feed.xml" rel="self" type="application/rss+xml"/>')
    xml_lines.append('        <language>en-us</language>')
    
    if newsletters:
        most_recent_date = newsletters[0][1]
        xml_lines.append(f'        <lastBuildDate>{format_rfc822_date(most_recent_date)}</lastBuildDate>')
        xml_lines.append(f'        <pubDate>{format_rfc822_date(most_recent_date)}</pubDate>')
    
    xml_lines.append('        <ttl>1440</ttl>')
    xml_lines.append('        <generator>PythRaSh\'s AI Newsletter Archive</generator>')
    xml_lines.append('        <copyright>© 2025 PythRaSh\'s AI Newsletter. All rights reserved.</copyright>')
    xml_lines.append('        <managingEditor>md.rasheduzzaman.ugoe@gmail.com (AI Newsletter Team)</managingEditor>')
    xml_lines.append('        <webMaster>md.rasheduzzaman.ugoe@gmail.com (AI Newsletter Team)</webMaster>')
    xml_lines.append('        <category>Technology</category>')
    xml_lines.append('        <category>Artificial Intelligence</category>')
    xml_lines.append('        <category>Machine Learning</category>')
    xml_lines.append('')
    
    # Add newsletter items
    for index, (filename, date) in enumerate(newsletters, 1):
        issue_num = len(newsletters) - index + 1
        date_str = date.strftime('%B %d, %Y')
        
        xml_lines.append(f'        <!-- {date_str} Issue -->')
        xml_lines.append('        <item>')
        xml_lines.append(f'            <title>AI Newsletter - Issue #{issue_num}</title>')
        xml_lines.append('            <description><![CDATA[')
        xml_lines.append(f'                Newsletter from {date_str}.')
        xml_lines.append('                Latest updates in AI technology in Biology, breakthrough research, and industry insights.')
        xml_lines.append('                Read the full newsletter for detailed coverage of recent AI developments.')
        xml_lines.append('            ]]></description>')
        
        link = f'{BASE_URL}/{filename}'
        xml_lines.append(f'            <link>{link}</link>')
        xml_lines.append(f'            <guid isPermaLink="true">{link}</guid>')
        xml_lines.append(f'            <pubDate>{format_rfc822_date(date)}</pubDate>')
        xml_lines.append('            <dc:creator>AI Newsletter Team</dc:creator>')
        xml_lines.append('            <category>AI Technology</category>')
        xml_lines.append('            <category>Research</category>')
        xml_lines.append('        </item>')
        xml_lines.append('')
    
    xml_lines.append('    </channel>')
    xml_lines.append('</rss>')
    
    # Write to file
    with open(FEED_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml_lines))
    
    print(f"✅ RSS feed generated successfully!")
    print(f"📄 Feed saved to: {FEED_FILE}")
    print(f"📊 Total newsletters in feed: {len(newsletters)}")
    
    # List all newsletters found
    print("\n📰 Newsletters included:")
    for file, date in newsletters:
        print(f"   - {file} ({date.strftime('%B %d, %Y')})")
    
    print(f"\n🔗 RSS feed URL: {BASE_URL}/feed.xml")

if __name__ == '__main__':
    create_rss_feed()
