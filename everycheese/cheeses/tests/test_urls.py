import pytest

from django.urls import reverse, resolve

from .factories import CheeseFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def cheese():
    return CheeseFactory()



def test_list_reverse():
    assert reverse('cheeses:list') == '/cheeses/'


def test_list_resolve():
    assert resolve('/cheeses/').view_name == 'cheeses:list'



def test_add_reverse():
    assert reverse('cheeses:add') == '/cheeses/~add/'


def test_add_resolve():
    assert resolve('/cheeses/~add/').view_name == 'cheeses:add'    


def test_detail_reverse(cheese):
    url = reverse('cheeses:detail', kwargs={'slug': cheese.slug})

    assert url == f'/cheeses/{cheese.slug}/'
    

def test_detail_resolve(cheese):
    url = f'/cheeses/{cheese.slug}/'
    assert resolve(url).view_name == 'cheeses:detail'