from fastapi import FastAPI, HTTPException, status
from typing import List
from app.models import Student
from app.database import load_students, save_students

app = FastAPI(title="Student API")


# ---------- Helpers ----------

def find_student_index(students: List[dict], student_id: int):
    for i, s in enumerate(students):
        if s["id"] == student_id:
            return i
    return None


def is_duplicate_id(students: List[dict], student_id: int):
    return any(s["id"] == student_id for s in students)


# ---------- Routes ----------

@app.get("/")
def home():
    return {"message": "Student API running"}


# CREATE
@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    students = load_students()

    if is_duplicate_id(students, student.id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student with this ID already exists"
        )

    students.append(student.dict())
    save_students(students)

    return {"message": "Student created successfully"}


# READ ALL
@app.get("/students", response_model=List[Student])
def get_students():
    return load_students()


# READ ONE
@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    students = load_students()

    for s in students:
        if s["id"] == student_id:
            return s

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )


# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, updated: Student):
    students = load_students()

    index = find_student_index(students, student_id)

    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    if updated.id != student_id and is_duplicate_id(students, updated.id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New ID already exists"
        )

    students[index] = updated.dict()
    save_students(students)

    return {"message": "Student updated successfully"}


# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    students = load_students()

    index = find_student_index(students, student_id)

    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    students.pop(index)
    save_students(students)

    return {"message": "Student deleted successfully"}