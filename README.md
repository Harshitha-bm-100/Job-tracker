# Job Tracker

Save job applications in a SQLite database and manage them in the browser.

## Description

Job Tracker is a small Django web app for job applications. The home page lists every saved job, newest applied date first. Each row shows the company, role, applied date, and status. Add job opens a form for a new application. Edit opens that same form filled in for one job. Delete removes that row. A missing id shows a 404 page.

Company, role, and applied date are required. Status defaults to Applied. The other choices are Pending, Shortlisted, Interview Scheduled, Accepted, and Rejected.

## Getting Started

### Dependencies

- Python 3
- pip
- Git

Django 6.1.2 is installed from `requirements.txt`. SQLite comes with Python, so you do not install a separate database. The app runs on macOS, Linux, and Windows.

### Installing

Clone the repository and install its dependencies inside a virtual environment.

macOS and Linux:

```bash
git clone https://github.com/Harshitha-bm-100/Job-tracker.git
cd Job-tracker
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

Windows:

```bash
git clone https://github.com/Harshitha-bm-100/Job-tracker.git
cd Job-tracker
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

`migrate` creates `db.sqlite3` in the project folder. That file is local. No project files need to be edited before the first run.

### Executing program

1. Activate the virtual environment if the terminal does not already show `(.venv)`.
2. Start the server:

```bash
python manage.py runserver
```

3. Open http://127.0.0.1:8000/.
4. Press Add job, fill in the form, and press Save.
5. Use Edit on a row to change it, or Delete to remove it.

Stop the server with Ctrl+C.

## Authors

- [Harshitha-bm-100](https://github.com/Harshitha-bm-100)

## Version History

- 0.1
  - Initial release
