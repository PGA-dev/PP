from django.test import TestCase
from django.urls import reverse
from grocery.models import Grocery as grocery_tester
import pytest

# def test_homepage_access():
#     url = reverse('home')
#     assert url == "/"
# Create your tests here.
test1 = "produce"

def test_get_name(test1):
    test1= grocery_tester.groc_item_title
    assert type(test1) in grocery_tester.groc_item_title

test2 = 7
def test_get_name_notint(test2):
    test2= grocery_tester.groc_item_title
    assert type(test2) in grocery_tester.groc_item_title