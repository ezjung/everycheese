import pytest

from ..models import Cheese
from .factories import CheeseFactory


# cheese = Cheese.objects.create(
#     name='Stracchino',
#     description='Semi-Sweet Cheese that goes well with starches',
#     firmness=Cheese.Firmness.SOFT,
# )
# cheese = CheeseFactory(name='Stracchino')

def test__str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name