# AI Newsletter Archive

This repository contains the archive of AI Newsletter issues.

## 🌐 View the Newsletter Archive

Visit the live archive at: https://mdrasheduz-zaman.github.io/ai_news_archive/

Subscribe via RSS: https://mdrasheduz-zaman.github.io/ai_news_archive/feed.xml

## 📚 Current Issues

- [September 23, 2025](AI_Newsletter_2025_09_23.html) - AI Newsletter Issue #2
- [September 15, 2025](AI_Newsletter_2025_09_15.html) - AI Newsletter Issue #1

## 🚀 Features

- **Beautiful Archive Page**: Responsive design with search functionality
- **RSS Feed**: Automatically generated RSS feed for subscribers
- **Search**: Real-time search across all newsletters
- **GitHub Pages**: Automatically deployed via GitHub Pages

## 📝 Adding New Newsletters

### Method 1: Automatic (Recommended)

1. Save your new newsletter HTML file to this folder with the naming format:
   ```
   AI_Newsletter_YYYY_MM_DD.html
   ```

2. Run the update script:
   ```bash
   python3 add_newsletter.py  # Updates index.html
   python3 generate_rss.py    # Generates RSS feed
   ./update_archive.sh        # Commits and pushes to GitHub
   ```

### Method 2: Manual

1. Save your newsletter HTML file with proper naming
2. Update `index.html` manually to add the new issue
3. Run:
   ```bash
   python3 generate_rss.py
   git add .
   git commit -m "Add new newsletter"
   git push origin main
   ```

## 🛠️ Scripts

- **`update_archive.sh`**: Main update script - generates RSS, commits, and pushes
- **`generate_rss.py`**: Generates RSS feed from existing newsletters
- **`add_newsletter.py`**: Updates index.html when new newsletters are added

## 📁 File Structure

```
output/
├── .git/                    # Git repository
├── .gitignore              # Ignore system files
├── .nojekyll               # Disable Jekyll processing
├── index.html              # Main archive page with search
├── feed.xml                # RSS feed (auto-generated)
├── AI_Newsletter_*.html    # Individual newsletter files
├── README.md               # This file
├── update_archive.sh       # Update script
├── generate_rss.py         # RSS generator
└── add_newsletter.py       # Index updater
```

## 🔧 Setup Requirements

- Git
- Python 3 (for RSS generation and index updates)
- GitHub account with GitHub Pages enabled

## 📊 Workflow

1. Create new newsletter HTML → Save to output folder
2. Run `python3 add_newsletter.py` → Updates index
3. Run `python3 generate_rss.py` → Updates RSS feed  
4. Run `./update_archive.sh` → Pushes to GitHub
5. GitHub Pages automatically deploys → Live in 2-5 minutes

## 🔗 Important URLs

- **Live Archive**: https://mdrasheduz-zaman.github.io/ai_news_archive/
- **RSS Feed**: https://mdrasheduz-zaman.github.io/ai_news_archive/feed.xml
- **GitHub Repo**: https://github.com/MdRasheduz-zaman/ai_news_archive

## 📧 Customization

To customize the email addresses in RSS feed, edit `generate_rss.py` and update:
```python
ET.SubElement(channel, 'managingEditor').text = 'your-email@example.com (AI Newsletter Team)'
ET.SubElement(channel, 'webMaster').text = 'your-email@example.com (AI Newsletter Team)'
```

## License

© 2025 All rights reserved.
