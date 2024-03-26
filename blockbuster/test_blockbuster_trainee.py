# pylint: skip-file

from blockbuster_oop import Video, Customer, VideoStore, VendingMachine, DVD

import pytest


def test_customer_name():
    john = Customer('John', 'Smith', '24/01/1980')
    assert john.name == 'John Smith'


@pytest.fixture
def john_smith():
    return Customer('John', 'Smith', '24/01/1980')


def test_customer_name(john_smith):
    assert john_smith.name == 'John Smith'


def test_date_of_birth(john_smith):
    assert len(john_smith.date_of_birth) == 10


def test_age(john_smith):
    john_smith.age(34) == 34


def test_age_float(john_smith):
    john_smith.age(34.5) == ValueError
