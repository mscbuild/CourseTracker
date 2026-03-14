### 📚 CourseTracker

**CourseTracker — CLI/GUI application for managing and tracking your online courses. It parses courses from Coursera and Udemy, tracks progress, and allows exporting course data for easy offline review.**

Perfect for learners who want a centralized system to manage their learning journey. 

### 🚀 Features

- 🔍 Search courses on Coursera and Udemy by topic

- 💾 Save courses locally in SQLite database

- ✅ Track completion with CLI and GUI

- 📊 Progress bar shows completion percentage in GUI

- 📈 Export courses to Excel/CSV for offline tracking

- 🖥 Cross-platform GUI with PyQt5

### 🎬 Demo

**GUI Preview:**

- List of courses

- Progress bar showing completion percentage

- Mark selected courses as completed

- Export to Excel

### 🛠 Installation

1.Clone the repository
~~~bash
git clone https://github.com/mscbuild/CourseTracker.git
cd CourseTracker
~~~
2.Install dependencies
~~~bash
pip install -r requirements.txt
~~~
3.Initialize the database (optional, happens automatically):
~~~bash
python cli.py list
~~~

### 💻 CLI Usage

- Search for courses
~~~bash
python cli.py search --platform coursera --query "python"
python cli.py search --platform udemy --query "data science"
~~~
- List all saved courses
~~~bash
python cli.py list
~~~
- Mark a course as completed
~~~bash
python cli.py complete 1
~~~
- Export courses to Excel
~~~bash
python cli.py export --filename my_courses.xlsx
~~~~

### 🖥 GUI Usage
~~~bash
python gui.py
~~~

**GUI Features:**

- 📋 Course list with platform and completion status

- ✅ Mark courses as completed

- 📊 Dynamic progress bar showing percentage completed

💾 Export courses to courses_export.xlsx

### 📁 Project Structure
~~~bash
CourseTracker/
│
├── cli.py            # Command-line interface
├── gui.py            # Graphical interface (PyQt5)
├── parsers/          # Course parsers
│   ├── __init__.py
│   ├── coursera.py
│   └── udemy.py
├── database.py       # SQLite database handling
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
~~~

### 🔧 Technologies

- Python 3.10+

- CLI: Click

- GUI: PyQt5

- Web parsing: Requests + BeautifulSoup

- Database: SQLite

- Data export: pandas

 ### 📌 How it works

 1.CLI allows searching courses by topic on Coursera or Udemy.

2.Courses are saved in a local SQLite database.

3.CLI and GUI can list courses and mark them as completed.

4.GUI shows progress bar and dynamic completion percentage.

5.Export feature generates Excel/CSV files for offline tracking.

### 📈 Future Improvements

- Support for additional platforms: edX, Skillshare, LinkedIn Learning

- Notifications via Telegram or Email for new courses

- Automated daily updates of course lists

- Advanced GUI filters: topic, platform, rating, duration

- Add bookmarks for important courses

###🤝 Contributing

**We welcome contributions!**

1.Fork the repository

2.Create a feature branch: git checkout -b feature/awesome-feature

3.Commit your changes: git commit -m "Add awesome feature"

4.Push to branch: git push origin feature/awesome-feature

5.Open a Pull Request

### 📄 License

This project is licensed under the MIT License.
