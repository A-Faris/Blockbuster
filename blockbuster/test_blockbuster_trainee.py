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
    john_smith.age() == 34


def test_age_float(john_smith):
    with pytest.raises(Exception):
        john_smith.age(34.5)


def test_age_young():
    with pytest.raises(ValueError):
        Customer("Jimmy", "Jimmy", '24/01/2020')


def test_age_young_second(john_smith):
    with pytest.raises(ValueError):
        john_smith.age(12)


@pytest.fixture
def video():
    matrix = Video('The Matrix', 1999, 150)
    terminator = Video('The Terminator', 1985, 108)
    return VideoStore([matrix, terminator])


def test_VideoStore_no_videos():
    with pytest.raises(ValueError):
        VideoStore([])


def test_display_title(video):
    assert video.find_video_by_title('The Matrix') == 'The Matrix (1999)'


def test_display_title_not_real(video):
    with pytest.raises(ValueError):
        video.find_video_by_title('Not here')


def test_is_available_true(video):
    assert video.is_available('The Matrix') == True


def test_is_available_not_real(video):
    with pytest.raises(ValueError):
        video.is_available('not here')


def test_rent_video(video, john_smith):
    assert video.rent_video('The Matrix', john_smith) == "HI"
