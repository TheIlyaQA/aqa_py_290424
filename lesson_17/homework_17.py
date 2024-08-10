"""
Ромбовидне наслідування

### Опис

Створіть клас **`Employee`**, який має атрибути **`name`** та **`salary`**.
Далі створіть два класи, **`Manager`** та **`Developer`**, які успадковуються від **`Employee`**.
Клас **`Manager`** повинен мати додатковий атрибут **`department`**, а клас **`Developer`** -
атрибут **`programming_language`**.

Тепер створіть клас **`TeamLead`**, який успадковується як від **`Manager`**, так і від **`Developer`**.
Цей клас представляє керівника з команди розробників. Клас **`TeamLead`** повинен мати всі атрибути як
**`Manager`** (ім'я, зарплата, відділ), а також атрибут **`team_size`**, який вказує на кількість розробників
у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрібутів з `Manager` та `Developer` у класі `TeamLead`

### Складність

Висока

# Як робити домашне завдання у Git

1. **ОБОВ’ЯЗКОВО с**творіть нову гілку, яка буде використовуватись для змін, за 
    допомогою команди `git checkout -b homework##`
2. **Виконайте ДЗ у окремому файлі homework_<#lesson>.py**
3. Зробіть коміт з змінами, додавши опис виконаних змін
4. Відправте свої зміни до вашого репозиторію 
5. Створіть pull request у  власну гілку `main` на головний репозиторію 
    [https://github.com](https://github.com/), натиснувши кнопку "New pull request" на
    відповідному розділі репозиторію.
6. Назначте ревьювером викладача
7. **Посилання на PR вставте у форму відповіді для ДЗ в навчальній системі**
"""

class Employee:
    def __init__(self, name: str, salary: float):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str):
            raise ValueError('Name must be a string')
        self.__name = new_name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary: float):
        if not isinstance(new_salary, float):
            raise ValueError('Salary should be a float value')
        self.__salary = new_salary


class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        Employee.__init__(self, name, salary)
        self._department = department

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, new_department: str):
        if not isinstance(new_department, str):
            raise ValueError('Department must be a string')
        self._department = new_department


class Developer(Employee):

    def __init__(self, name: str, salary: float, programming_language: str):
        Employee.__init__(self, name, salary)
        self._programming_language = programming_language

    @property
    def programming_language(self):
        return self._programming_language

    @programming_language.setter
    def programming_language(self, new_programming_language: str):
        if not isinstance(new_programming_language, str):
            raise ValueError('Programming language must be a string')
        self._programming_language = new_programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name: str, salary: float, department: str, programming_language: str, team_size: int):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self._team_size = team_size

    @property
    def team_size(self):
        return self._team_size

    @team_size.setter
    def team_size(self, new_team_size: int):
        if not isinstance(new_team_size, int):
            raise ValueError('Team size should be int')
        self._team_size = new_team_size


if __name__ == '__main__':
    t1 = TeamLead('Johnny', 25000.00, 'IT', 'Python', 12)
    print(t1.name)
    print(t1.salary)
    print(t1.department)
    print(t1.programming_language)
    print(t1.team_size)