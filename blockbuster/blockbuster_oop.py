"""Blockbuster"""

from datetime import datetime


class Video:
    """Video class"""

    def __init__(self, title: str, year: int, runtime: int) -> None:
        print("Video Init")
        if year < 1900:
            raise Exception("Videos can't be released before 1900")
        if title is None:
            raise Exception("Title most be provided")
        self.title = title
        self.year = year
        self.runtime = runtime

    def display_title(self):
        """Displays title"""
        return f"{self.title} ({self.year})"

    def rental_price(self):
        """Calculates rental price"""
        if self.year == datetime.now().year and self.runtime > 240:
            return 2000
        if self.year == datetime.now().year and self.runtime <= 240:
            return 1000
        if self.runtime > 240:
            return 1000
        return 500

    def display_price(self):
        """Displays the price"""
        price = str(self.rental_price())
        return f"£{price[:-2]}.{price[-2:]}"


class Customer:
    """Customer"""

    def __init__(self):
        print("Customer Init")


class VideoStore:
    """Video Store"""

    def __init__(self):
        print("VideoStore Init")


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
