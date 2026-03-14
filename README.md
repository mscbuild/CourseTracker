1️⃣ Basic Idea

Name: CourseTracker

Features:

Course parsing

Supported platforms: Coursera, Udemy, edX, Skillshare (via their API or scraping).

Retrieving metadata: title, author, rating, language, duration, URL.

Filters and sorting

By topic (e.g., Python, Data Science).

By rating, language, duration.

Download/save

Local storage of course list in JSON/SQLite.

Export to CSV/Excel.

Progress tracking

The user marks completed lessons.

The CLI/GUI displays progress as a percentage.

1️⃣ Project structure

~~~bash
CourseTracker/
│
├── cli.py           # Command line
├── gui.py           # Graphical interface
├── parsers/
│   ├── __init__.py
│   ├── coursera.py
│   └── udemy.py
├── database.py      # Working with SQLite
└── requirements.txt # Dependencies
~~~
