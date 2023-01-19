from blockbuster_oop import Video, Customer, VideoStore, VendingMachine, DVD
import pytest


def test_video_release_after_1900():
    with pytest.raises(Exception):
        Video('The Dreyfus Affair', 1899, 13)


def test_video_title():
    video = Video('The Matrix', 1999, 150)
    assert video.displayTitle() == 'The Matrix (1999)'


def test_video_price_regular():
    video = Video('Mission Impossible 8', 2023, 90)
    assert video.rentalPrice() == 1000


def test_video_price_previous_years():
    video = Video('The Mummy', 1999, 124)
    assert video.rentalPrice() == 500


def test_video_price_extra_long():
    video = Video("Zack Snyder's Justice League",  2023, 242)
    assert video.rentalPrice() == 2000


def test_video_extra_long_previous_year():
    video = Video('Fellowship of the Ring: Extended Edition', 2001, 250)
    assert video.rentalPrice() == 1000


def test_video_display_price():
    video = Video('The Matrix', 1999, 150)
    assert video.displayPrice() == '£5.00'


def test_video_has_title():
    with pytest.raises(Exception):
        Video(None, 2010, 90)
