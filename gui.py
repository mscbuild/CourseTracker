import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QProgressBar, QMessageBox
from database import list_courses, mark_completed, export_courses

class CourseGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CourseTracker")
        self.layout = QVBoxLayout()

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.progress = QProgressBar()
        self.layout.addWidget(self.progress)

        self.refresh_btn = QPushButton("Load Courses")
        self.refresh_btn.clicked.connect(self.load_courses)
        self.layout.addWidget(self.refresh_btn)

        self.complete_btn = QPushButton("Mark Selected Completed")
        self.complete_btn.clicked.connect(self.complete_selected)
        self.layout.addWidget(self.complete_btn)

        self.export_btn = QPushButton("Export to Excel")
        self.export_btn.clicked.connect(self.export_courses)
        self.layout.addWidget(self.export_btn)

        self.setLayout(self.layout)
        self.load_courses()

    def load_courses(self):
        self.list_widget.clear()
        courses = list_courses()
        completed_count = 0
        for c in courses:
            status = "✅" if c[4] else "❌"
            if c[4]:
                completed_count += 1
            self.list_widget.addItem(f"{c[0]}. {c[1]} [{c[2]}] {status}")
        total = len(courses)
        self.progress.setValue(int((completed_count / total) * 100) if total else 0)

    def complete_selected(self):
        selected = self.list_widget.currentItem()
        if selected:
            course_id = int(selected.text().split(".")[0])
            mark_completed(course_id)
            self.load_courses()
        else:
            QMessageBox.information(self, "Info", "Select a course first!")

    def export_courses(self):
        export_courses()
        QMessageBox.information(self, "Export", "Courses exported to courses_export.xlsx")

app = QApplication(sys.argv)
window = CourseGUI()
window.show()
sys.exit(app.exec_())

