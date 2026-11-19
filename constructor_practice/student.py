class Student:
    """Простий клас для демонстрації роботи конструктора."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Мене звати {self.name}, мені {self.age} років."


student = Student("Віталій", 17)
print(student.introduce())
