#!/usr/bin/env python3

"""
Add New Newsletter Helper Script
Automatically updates index.html when a new newsletter is added
"""

import os
import re
from datetime import datetime
import sys

OUTPUT_DIR = "/Users/md.rasheduzzaman/Desktop/AI Newsletter/output"
INDEX_FILE = os.path.join(OUTPUT_DIR, "index.html")

def get_existing_newsletters():
    """Get list of existing newsletter files"""
    newsletters = []
    for file in os.listdir(OUTPUT_DIR):
        if file.startswith('AI_Newsletter_') and file.endswith('.html'):
            match = re.match(r'AI_Newsletter_(\d{4})_(\d{2})_(\d{2})\.html', file)
            if match:
                year, month, day = match.groups()
                date = datetime(int(year), int(month), int(day))
                newsletters.append((file, date))
    
    # Sort by date, newest first
    newsletters.sort(key=lambda x: x[1], reverse=True)
    return newsletters

def update_index_html():
    """Update the index.html file with all newsletters"""
    newsletters = get_existing_newsletters()
    
    # Read the current index.html
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the newsletter grid section
    grid_start = content.find('<div class="newsletter-grid" id="newsletterGrid">')
    grid_end = content.find('</div>', grid_start) if grid_start != -1 else -1
    
    if grid_start == -1 or grid_end == -1:
        print("❌ Error: Could not find newsletter grid in index.html")
        return False
    
    # Generate new newsletter items HTML
    newsletter_items = []
    for index, (filename, date) in enumerate(newsletters, 1):
        issue_num = len(newsletters) - index + 1
        date_str = date.strftime('%B %d, %Y')
        date_attr = date.strftime('%Y-%m-%d')
        
        item_html = f'''                <!-- {date_str} Issue -->
                <div class="newsletter-item" data-date="{date_attr}">
                    <a href="{filename}" class="newsletter-link">
                        <div class="newsletter-date">{date_str}</div>
                        <h2 class="newsletter-title">AI Newsletter - Issue #{issue_num}</h2>
                        <p class="newsletter-description">
                            Latest updates in AI technology, breakthrough research, and industry insights.
                        </p>
                        <span class="view-btn">Read Issue →</span>
                    </a>
                </div>'''
        newsletter_items.append(item_html)
    
    # Construct new grid content
    new_grid = f'''<div class="newsletter-grid" id="newsletterGrid">
{chr(10).join(newsletter_items)}
            </div>'''
    
    # Replace the grid section
    new_content = content[:grid_start] + new_grid + content[grid_end + 6:]
    
    # Write back to index.html
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Updated index.html with {len(newsletters)} newsletters")
    return True

def main():
    """Main function"""
    print("🔄 Updating newsletter index...")
    
    # Check if we have new newsletters
    newsletters = get_existing_newsletters()
    if not newsletters:
        print("⚠️  No newsletters found in the output directory")
        return
    
    print(f"📊 Found {len(newsletters)} newsletters:")
    for file, date in newsletters[:5]:  # Show only first 5
        print(f"   - {file} ({date.strftime('%B %d, %Y')})")
    
    if len(newsletters) > 5:
        print(f"   ... and {len(newsletters) - 5} more")
    
    # Update index
    if update_index_html():
        print("\n✨ Index successfully updated!")
        print("📡 Don't forget to run ./update_archive.sh to push changes")
    else:
        print("\n❌ Failed to update index")
        sys.exit(1)

if __name__ == '__main__':
    main()
