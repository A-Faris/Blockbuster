"""Blockbuster"""

from datetime import datetime, date, timedelta


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
        self.outstanding_fine = 0
        self.age()

    @property
    def name(self) -> str:
        """Shows name"""
        return f"{self.first_name} {self.last_name}"

    def age(self, age=None) -> int:
        """Calculates age"""
        if age is None:
            day, month, year = map(int, self.date_of_birth.split("/"))
            today = date.today()
            age = today.year - year - ((today.month, today.day) < (month, day))

        if age < 13:
            raise ValueError("You are too young")

        if type(age) == int:
            return age
        raise ValueError("Must be an integer")


class Rental:
    """Rental"""

    def __init__(self):
        print("Rental Init")
        self.due_date = date.today() + timedelta(weeks=2)


class VideoStore:
    """Video Store"""

    def __init__(self, videos) -> None:
        print("VideoStore Init")
        if 0 < len(videos) < 10:
            self.videos = videos
        else:
            raise ValueError

        self.availability = {}
        for video in videos:
            if isinstance(video, Video):
                self.availability[video.title] = True
            else:
                raise TypeError("Only videos are accepted")

    def find_video_by_title(self, video_title: str) -> Video:
        """Show title"""
        for video in self.videos:
            if video_title in video.display_title():
                return video.display_title()
        raise ValueError("This video does not exist")

    def is_available(self, video_title: str) -> bool:
        if self.availability.get(video_title):
            return self.availability.get(video_title)
        raise ValueError

    def rent_video(self, title: str, customer: Customer) -> Rental:
        if self.find_video_by_title(title) and isinstance(customer, Customer):
            self.availability[title] = False
            return Rental()
        else:
            raise ValueError("Customer doesn't exist")

    def return_video(self, rental: Rental, return_date: str):
        ...


class DVD(Video):
    """DVD"""

    def __init__(self):
        print("DVD Init")


class VendingMachine(VideoStore):
    """Vending Machine"""

    def __init__(self):
        print("VendingMachine Init")


john_smith = Customer('John', 'Smith', '24/01/1980')
# print(john_smith.age(34))

matrix = Video('The Matrix', 1999, 150)
terminator = Video('The Terminator', 1985, 108)
video = VideoStore([matrix, terminator])


video.rent_video("The Matrix", john_smith)
print(video.availability)
