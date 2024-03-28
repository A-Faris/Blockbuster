# pylint: skip-file

from blockbuster_oop import Video, Customer, VideoStore, VendingMachine, DVD, Rental, VideoError

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
    john_smith.calculate_age() == 34


def test_age_float(john_smith):
    with pytest.raises(Exception):
        john_smith.calculate_age(34.5)


def test_age_young():
    with pytest.raises(VideoError):
        Customer("Jimmy", "Jimmy", '24/01/2020')


def test_age_young_second(john_smith):
    with pytest.raises(VideoError):
        john_smith.calculate_age(12)


@pytest.fixture
def matrix():
    return Video('The Matrix', 1999, 150)


@pytest.fixture
def terminator():
    return Video('The Terminator', 1985, 108)


@pytest.fixture
def videostore(matrix, terminator):
    return VideoStore([matrix, terminator])


def test_VideoStore_no_videos():
    with pytest.raises(VideoError):
        VideoStore([])


def test_display_title(videostore):
    assert isinstance(videostore.find_video_by_title('The Matrix'), Video)


def test_display_title_not_real(videostore):
    with pytest.raises(VideoError):
        videostore.find_video_by_title('Not here')


def test_is_available_true(videostore, matrix):
    assert videostore.is_available(matrix) == True


def test_is_available_not_real(videostore):
    with pytest.raises(VideoError):
        videostore.is_available('not here')


def test_rent_video(videostore, john_smith, matrix):
    assert isinstance(videostore.rent_video(matrix, john_smith), Rental)


@pytest.fixture
def rental(matrix, john_smith):
    return Rental(matrix, john_smith)


def test_return_video(rental, videostore):
    videostore.return_video(rental, '27/03/2024')
    assert rental.customer.outstanding_fine == 0


def test_return_video_late(rental, videostore):
    videostore.return_video(rental, '27/03/2025')
    assert rental.customer.outstanding_fine == 500


def test_watch(matrix):
    matrix.watch()
    assert matrix.is_rewound == False
    matrix.rewind()


def test_rewind(matrix):
    matrix.watch()
    matrix.rewind()
    assert matrix.is_rewound == True


def test_rewind_before_returning(matrix, videostore, rental):
    matrix.watch()
    with pytest.raises(VideoError):
        videostore.return_video(rental, '27/03/2024')


def test_pay_fine_before_renting(matrix, john_smith, videostore):
    john_smith.outstanding_fine = 50001
    with pytest.raises(VideoError):
        videostore.rent_video(matrix, john_smith)


def test_fine_paid_before_renting(matrix, john_smith, videostore):
    john_smith.outstanding_fine = 5001
    john_smith.pay_off_fine()
    assert isinstance(videostore.rent_video(matrix, john_smith), Rental)


@pytest.fixture
def dvd():
    return DVD('The Matrix', 1999, 150)


@pytest.fixture
def dvd_rental(dvd, john_smith):
    return Rental(dvd, john_smith)


def test_dvd_rent(dvd):
    assert dvd.rental_price() == 1200


def test_return_video_late(dvd_rental, videostore):
    videostore.return_video(dvd_rental, '27/03/2025')
    assert dvd_rental.customer.outstanding_fine == 1200


def test_dvd_rewind_before_returning(dvd, videostore, dvd_rental):
    dvd.watch()
    assert videostore.return_video(dvd_rental, '27/03/2024') == None
