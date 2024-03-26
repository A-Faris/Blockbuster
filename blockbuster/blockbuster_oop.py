"""Blockbuster"""

import datetime


class Video:
    """Video class"""

    def __init__(self, title: str, year: int, runtime: int) -> None:
        print("Video Init")
        if year < 1900:
            raise ValueError("Videos can't be released before 1900")
        if title is None:
            raise ValueError("Title must be provided")
        self.title = title
        self.year = year
        self.runtime = runtime

    def display_title(self) -> str:
        """Displays title"""
        return f"{self.title} ({self.year})"

    def rental_price(self) -> int:
        """Calculates rental price"""
        price = 0
        if self.year == datetime.now().year:
            price = 1000
        else:
            price = 500
        if self.runtime > 240:
            return price * 2
        return price

    def display_price(self) -> str:
        """Displays the price"""
        price = str(self.rental_price())
        return f"£{price[:-2]}.{price[-2:]}"


class Customer:
    """Customer"""

    def __init__(self, first_name: str, last_name: str, date_of_birth: str) -> None:
        print("Customer Init")
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.age()

    @property
    def name(self) -> str:
        """Shows name"""
        return f"{self.first_name} {self.last_name}"

    def age(self, age=None) -> int:
        """Calculates age"""
        if age is None:
            day, month, year = map(int, self.date_of_birth.split("/"))
            today = datetime.date.today()
            age = today.year - year - ((today.month, today.day) < (month, day))

        if age < 13:
            raise ValueError

        try:
            return age
        except Exception as exc:
            raise ValueError("Must be an integer") from exc


class VideoStore:
    """Video Store"""

    def __init__(self, videos) -> None:
        print("VideoStore Init")
        if 0 < len(videos) < 10:
            self.videos = videos
        else:
            raise ValueError

    def find_video_by_title(self, title: str) -> Video:
        """Show title"""
        for video in self.videos:
            if title in video.display_title():
                return video.display_title()
        raise ValueError("This video does not exist")


class Rental:
    """Rental"""

    def __init__(self):
        print("Rental Init")


class DVD(Video):
    """DVD"""

    def __init__(self):
        print("DVD Init")


class VendingMachine(VideoStore):
    """Vending Machine"""

    def __init__(self):
        print("VendingMachine Init")
