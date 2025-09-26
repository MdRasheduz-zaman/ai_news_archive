#!/usr/bin/env python3

"""
RSS Feed Generator for AI Newsletter Archive
Automatically generates RSS feed from newsletter HTML files
"""

import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from xml.dom import minidom
import html

# Configuration
BASE_URL = "https://mdrasheduz-zaman.github.io/ai_news_archive"
OUTPUT_DIR = "/Users/md.rasheduzzaman/Desktop/AI Newsletter/output"
FEED_FILE = os.path.join(OUTPUT_DIR, "feed.xml")

def extract_date_from_filename(filename):
    """Extract date from filename format: AI_Newsletter_YYYY_MM_DD.html"""
    match = re.match(r'AI_Newsletter_(\d{4})_(\d{2})_(\d{2})\.html', filename)
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

def create_rss_feed():
    """Generate the RSS feed"""
    # Create RSS root element
    rss = ET.Element('rss', {
        'version': '2.0',
        'xmlns:atom': 'http://www.w3.org/2005/Atom',
        'xmlns:dc': 'http://purl.org/dc/elements/1.1/'
    })
    
    channel = ET.SubElement(rss, 'channel')
    
    # Add channel metadata
    ET.SubElement(channel, 'title').text = 'AI Newsletter'
    ET.SubElement(channel, 'description').text = 'Your Weekly Digest of AI Insights - Covering the latest developments, insights, and trends in artificial intelligence'
    ET.SubElement(channel, 'link').text = f'{BASE_URL}/'
    
    atom_link = ET.SubElement(channel, '{http://www.w3.org/2005/Atom}link', {
        'href': f'{BASE_URL}/feed.xml',
        'rel': 'self',
        'type': 'application/rss+xml'
    })
    
    ET.SubElement(channel, 'language').text = 'en-us'
    
    # Get newsletter files
    newsletters = get_newsletter_files()
    
    if newsletters:
        # Use the most recent newsletter date for lastBuildDate
        most_recent_date = newsletters[0][1]
        ET.SubElement(channel, 'lastBuildDate').text = format_rfc822_date(most_recent_date)
        ET.SubElement(channel, 'pubDate').text = format_rfc822_date(most_recent_date)
    
    ET.SubElement(channel, 'ttl').text = '1440'
    ET.SubElement(channel, 'generator').text = 'AI Newsletter Archive'
    ET.SubElement(channel, 'copyright').text = '© 2025 AI Newsletter. All rights reserved.'
    ET.SubElement(channel, 'managingEditor').text = 'your-email@example.com (AI Newsletter Team)'
    ET.SubElement(channel, 'webMaster').text = 'your-email@example.com (AI Newsletter Team)'
    
    # Add categories
    categories = ['Technology', 'Artificial Intelligence', 'Machine Learning']
    for cat in categories:
        ET.SubElement(channel, 'category').text = cat
    
    # Add newsletter items
    for index, (filename, date) in enumerate(newsletters, 1):
        item = ET.SubElement(channel, 'item')
        
        # Calculate issue number (counting backwards from total)
        issue_num = len(newsletters) - index + 1
        
        ET.SubElement(item, 'title').text = f'AI Newsletter - Issue #{issue_num}'
        
        # Create description
        description_text = f"""
            Newsletter from {date.strftime('%B %d, %Y')}.
            Latest updates in AI technology, breakthrough research, and industry insights.
            Read the full newsletter for detailed coverage of recent AI developments.
        """
        ET.SubElement(item, 'description').text = description_text.strip()
        
        # Add link
        link = f'{BASE_URL}/{filename}'
        ET.SubElement(item, 'link').text = link
        ET.SubElement(item, 'guid', {'isPermaLink': 'true'}).text = link
        
        # Add publication date
        ET.SubElement(item, 'pubDate').text = format_rfc822_date(date)
        
        # Add creator
        ET.SubElement(item, '{http://purl.org/dc/elements/1.1/}creator').text = 'AI Newsletter Team'
        
        # Add categories
        ET.SubElement(item, 'category').text = 'AI Technology'
        ET.SubElement(item, 'category').text = 'Research'
    
    # Convert to string with pretty printing
    xml_str = minidom.parseString(ET.tostring(rss, encoding='unicode')).toprettyxml(indent='    ')
    
    # Write to file
    with open(FEED_FILE, 'w', encoding='utf-8') as f:
        f.write(xml_str)
    
    print(f"✅ RSS feed generated successfully!")
    print(f"📄 Feed saved to: {FEED_FILE}")
    print(f"📊 Total newsletters in feed: {len(newsletters)}")
    print(f"🔗 RSS feed URL: {BASE_URL}/feed.xml")

if __name__ == '__main__':
    create_rss_feed()
