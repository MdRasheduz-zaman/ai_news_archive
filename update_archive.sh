#!/bin/bash

# Update Newsletter Archive Script with RSS Feed Generation
# Usage: ./update_archive.sh

echo "📧 Updating AI Newsletter Archive..."

# Navigate to the output directory
cd "/Users/md.rasheduzzaman/Desktop/AI Newsletter/output"

# Check if we're in a git repository
if [ ! -d .git ]; then
    echo "❌ Error: Not a git repository. Please initialize git first."
    exit 1
fi

# Generate RSS feed
echo "📡 Generating RSS feed..."
if command -v python3 &> /dev/null; then
    python3 generate_rss.py
else
    echo "⚠️  Python3 not found. RSS feed not updated."
    echo "   Please run: python3 generate_rss.py manually"
fi

# Add only HTML files and essential files
git add *.html .nojekyll .gitignore README.md feed.xml

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "✅ No new changes to commit"
else
    # Get the current date for commit message
    DATE=$(date +"%Y-%m-%d")
    
    # Commit changes
    echo "📝 Committing changes..."
    git commit -m "Update newsletter archive - $DATE"
    
    # Push to GitHub
    echo "🚀 Pushing to GitHub..."
    git push origin main
    
    echo "✅ Newsletter archive updated successfully!"
    echo "🌐 Your archive will be updated at:"
    echo "   https://mdrasheduz-zaman.github.io/ai_news_archive/"
    echo "   (Updates may take 2-5 minutes to appear)"
fi

echo ""
echo "📊 Current newsletters in archive:"
ls -la *.html | grep -v index.html | grep AI_Newsletter
echo ""
echo "📍 Archive URL: https://mdrasheduz-zaman.github.io/ai_news_archive/"
echo "📡 RSS Feed URL: https://mdrasheduz-zaman.github.io/ai_news_archive/feed.xml"
