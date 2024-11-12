import pytest


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

    def __str__(self):
        return f"TeamLead:\n{self.name} {self.salary} {self.department} {self.programming_language} {self.team_size}"


tl_1 = TeamLead("Andrew", 1500, "finance", "python", 5)
print(tl_1)
@pytest.mark.parametrize("actual, expected", [
    (tl_1.name, "Andrew"),
    (tl_1.salary, 1500),
    (tl_1.department, "finance"),
    (tl_1.programming_language, "python"),
    (tl_1.team_size, 5)
])
def test_team_lead_variables_present(actual, expected):
    assert expected == actual
