# 🗂 CourseTracker Project Board

This is an **enhanced Kanban-style project board** for the CourseTracker project.  
It includes task types, priorities, and templates for new tasks.

---

## 📝 Backlog
Future ideas and tasks.

| Task | Type | Priority | Notes |
|------|------|----------|-------|
| Add support for **edX courses** | Feature | Medium | Include parser and GUI integration |
| Integrate **Skillshare API** | Feature | Medium | Use API or scraping if needed |
| Add **multi-language support** for GUI | Enhancement | Low | Start with English + Spanish |
| Telegram notifications for new courses | Feature | High | Optional, via bot |
| Auto-refresh courses daily | Enhancement | Medium | Cron or scheduler task |
| Add bookmarking/favorites for courses | Enhancement | Low | Allow marking important courses |

---

## 📌 To Do
Tasks planned for the next sprint.

| Task | Type | Priority | Notes |
|------|------|----------|-------|
| Implement **“Mark all courses completed”** button in GUI | Feature | High | Updates progress bar dynamically |
| Add **filters by topic, rating, duration** in GUI | Feature | Medium | Use dropdowns or search bar |
| Improve Coursera parser for **better accuracy** | Enhancement | High | Fix missing course titles or links |
| Add **CSV export option** alongside Excel | Feature | Medium | Use pandas DataFrame |

---

## ⚙️ In Progress
Tasks currently being worked on.

| Task | Type | Priority | Notes |
|------|------|----------|-------|
| Improve Udemy parser | Enhancement | High | Better course title detection |
| Add **progress bar in CLI output** | Feature | Medium | Optional CLI visual feedback |
| Refactor **database functions** | Enhancement | Medium | Add categories support |

---

## 🔍 Review / Testing
Tasks completed but requiring review or testing.

| Task | Type | Priority | Notes |
|------|------|----------|-------|
| CLI `complete` command validation | Feature | Medium | Ensure valid course IDs |
| GUI **export functionality test** | Testing | Medium | Check Excel file correctness |
| SQLite **database migration test** | Testing | Medium | Test schema upgrade scenarios |

---

## ✅ Done
Tasks that are fully completed.

| Task | Type | Priority | Notes |
|------|------|----------|-------|
| CLI search command (Coursera & Udemy) | Feature | High | Works for basic topics |
| Save courses in SQLite | Feature | High | Stored locally with progress |
| GUI course list with **progress bar** | Feature | High | Visual progress display |
| Export courses to Excel | Feature | High | Works with pandas |
| Mark course as completed (CLI & GUI) | Feature | High | Updates progress correctly |

---

## 🆕 New Task Template

When adding a new task, copy the template below:

````markdown
- [ ] **Task Title**
  - Type: Feature / Bug / Enhancement / Documentation
  - Priority: High / Medium / Low
  - Description: Add a short description of the task
  - Notes: Optional notes for contributors


