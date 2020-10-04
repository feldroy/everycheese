import pytest
from .factories import CheeseFactory

pytestmark = pytest.mark.django_db

from ..models import Cheese


def test__str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name