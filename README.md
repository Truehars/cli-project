# 🎓 Student Management CLI + FastAPI

A Python-based project that combines a Command Line Interface (CLI) with a FastAPI backend to perform CRUD operations on student data, with persistent storage using a JSON file.

---

## 🚀 Features

* ✅ Create, Read, Update, Delete (CRUD) operations
* 🖥️ CLI-based interaction
* ⚡ FastAPI backend
* 💾 Persistent storage using JSON file
* 🔒 Input validation with Pydantic
* ❌ Duplicate ID prevention

----

## 🛠️ Tech Stack

* Python
* FastAPI
* Requests (for CLI)
* Pydantic

---

## 📁 Project Structure

```
CLI/
│── app/
│   ├── main.py        # FastAPI app (routes)
│   ├── models.py      # Pydantic models
│   ├── database.py    # File-based storage logic
│
│── students.json      # Persistent data storage
│── cli.py             # CLI tool
│── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/Truehars/cli-project.git
cd cli-project
```

---

### 2. Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

### Start FastAPI server

```
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

### Run CLI

```
python cli.py
```

---

## 📌 API Endpoints

| Method | Endpoint       | Description        |
| ------ | -------------- | ------------------ |
| POST   | /students      | Create student     |
| GET    | /students      | Get all students   |
| GET    | /students/{id} | Get single student |
| PUT    | /students/{id} | Update student     |
| DELETE | /students/{id} | Delete student     |

---

## 💾 Data Storage

* Data is stored in `students.json`
* Persistent across server restarts

---

## ⚠️ Notes

* Duplicate student IDs are not allowed
* Data is stored locally (not for multi-user production use)

---

## 👨‍💻 Author

**Harshit Verma**

---

## ⭐ Future Improvements

* SQLite / PostgreSQL integration
* Authentication system
* Advanced CLI using Typer
* Docker support
