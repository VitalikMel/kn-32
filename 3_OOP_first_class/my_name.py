class MyName:
    """Клас для демонстрації основ об'єктно-орієнтованого програмування."""

    total_names = 0

    def __init__(self, name=None, domain="itcollege.lviv.ua") -> None:
        if name is None:
            name = "Anonymous"
        elif not isinstance(name, str):
            raise ValueError("Ім'я може містити лише літери!")
        elif not name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")

        self.name = name[0].upper() + name[1:]
        self.domain = domain
        MyName.total_names += 1
        self.my_id = MyName.total_names

    @property
    def whoami(self) -> str:
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        return self.create_email()

    def create_email(self, domain=None) -> str:
        """Створює email; домен можна змінити для окремого виклику."""
        email_domain = domain if domain is not None else self.domain
        return f"{self.name.lower()}@{email_domain}"

    @property
    def name_length(self) -> int:
        return len(self.name)

    @property
    def full_name(self) -> str:
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    @classmethod
    def anonymous_user(cls):
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        return f"You say: {message}"

    def save_to_file(self, filename="users.txt") -> None:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(self.full_name + "\n")


print("Розпочинаємо створювати об'єкти!")

names = ("Bohdan", "Marta", None, "Vitaliy")
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(
        f"""{">*<" * 20}
This is object: {me}
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello("Welcome to Python OOP!")}
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
Name length: {me.name_length}
Full name: {me.full_name}
{"<*>" * 20}"""
    )

print(f"We are done. We create {len(names)} names in the list.")
print(f"MyName.total_names = {MyName.total_names}")

first_user = next(iter(all_names.values()))
first_user.save_to_file()
