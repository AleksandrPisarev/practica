from student_repository import*

if __name__ == '__main__':
    repository = Student_repository("user.csv")
    students = repository.get_all()
    for i in students:
        print(i)
    repository.get_by_id(3)
    st = Student(5, "Alex", 46)
    repository.add(st)