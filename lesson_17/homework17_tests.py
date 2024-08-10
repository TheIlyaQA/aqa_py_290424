import pytest
from homework_17 import TeamLead, Manager, Developer

def test_team_lead_attributes():
    # Creating a TeamLead instance
    team_lead = TeamLead('Johnny', 25000.00, 'IT', 'Python', 12)

    # Testing inherited attributes from Employee class
    assert team_lead.name == 'Johnny'
    assert team_lead.salary == 25000.00

    # Testing inherited attribute from Manager class
    assert team_lead.department == 'IT'

    # Testing inherited attribute from Developer class
    assert team_lead.programming_language == 'Python'

    # Testing TeamLead-specific attribute
    assert team_lead.team_size == 12


def test_team_lead_setters():
    team_lead = TeamLead('Johnny', 25000.00, 'IT', 'Python', 12)

    # Testing setters for Employee class attributes
    team_lead.name = 'John Doe'
    assert team_lead.name == 'John Doe'

    team_lead.salary = 30000.00
    assert team_lead.salary == 30000.00

    # Testing setters for Manager class attribute
    team_lead.department = 'HR'
    assert team_lead.department == 'HR'

    # Testing setters for Developer class attribute
    team_lead.programming_language = 'JavaScript'
    assert team_lead.programming_language == 'JavaScript'

    # Testing setter for TeamLead-specific attribute
    team_lead.team_size = 10
    assert team_lead.team_size == 10


def test_team_lead_invalid_setters():
    team_lead = TeamLead('Johnny', 25000.00, 'IT', 'Python', 12)

    # Testing invalid name setter
    with pytest.raises(ValueError):
        team_lead.name = 123  # Not a string

    # Testing invalid salary setter
    with pytest.raises(ValueError):
        team_lead.salary = '30000'  # Not a float

    # Testing invalid department setter
    with pytest.raises(ValueError):
        team_lead.department = 456  # Not a string

    # Testing invalid programming language setter
    with pytest.raises(ValueError):
        team_lead.programming_language = 789  # Not a string

    # Testing invalid team size setter
    with pytest.raises(ValueError):
        team_lead.team_size = '15'  # Not an int

    if __name__ == '__main__':
        pytest.main()