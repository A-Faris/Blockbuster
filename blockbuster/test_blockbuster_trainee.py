# pylint: skip-file

from blockbuster_oop import Video, Customer, VideoStore, VendingMachine, DVD


def test_customer_name():
    john = Customer('John', 'Smith', '24/01/1980')
    assert john.name == 'John Smith'
