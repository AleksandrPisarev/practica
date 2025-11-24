import csv

path = "user.csv"
class Student:
    def __init__(self, id, name, age):
        self.name = name
        self.age = age
        self.id = id

    def __dict__(self):
        return {"id": self.id,
                "name": self.name,
                "age": self.age}

    def __str__(self):
        return f"{self.id}: {self.name} - {self.age}"
class Student_repository:
    def __init__(self, path):
        self.__path = path

    def get_all(self):
        students = list()
        with open(path, 'r', encoding="UTF-8") as file:
            reader = csv.reader(file)
            for row in reader:
                student = Student(row[0], row[1], int(row[2]))
                students.append(student)
        return students

    def get_by_id(self, id):
        with open(path, 'r', encoding="UTF-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if int(row[0]) == int(id):
                    student = Student(row[0], row[1], int(row[2]))
                    return print(student)
            return print(f"id: {id} в базе не значится")

    def add(self, student):
        with open(self.__path, 'a', newline="") as file:
            writer = csv.DictWriter(file, ["id", "name", "age"])
            writer.writerow(student.__dict__())

    def update(self, student):
        students = self.get_all()
        for i in students:
            if int(i.id) == int(student.id):
                i = student
