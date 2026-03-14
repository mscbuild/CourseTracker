import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget
from database import list_courses

class CourseGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CourseTracker")
        self.layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)
        self.refresh_btn = QPushButton("Load Courses")
        self.refresh_btn.clicked.connect(self.load_courses)
        self.layout.addWidget(self.refresh_btn)
        self.setLayout(self.layout)

    def load_courses(self):
        self.list_widget.clear()
        courses = list_courses()
        for c in courses:
            status = "✅" if c[4] else "❌"
            self.list_widget.addItem(f"{c[1]} [{c[2]}] {status}")

app = QApplication(sys.argv)
window = CourseGUI()
window.show()
sys.exit(app.exec_())
