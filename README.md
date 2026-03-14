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
2️⃣ Run the project

1.Install dependencies:
~~~bash
pip install -r requirements.txt
~~~
2.CLI:
~~~bash
python cli.py search --platform coursera --query "python"
python cli.py list
~~~
3.GUI:
~~~bash
python gui.py
~~~
