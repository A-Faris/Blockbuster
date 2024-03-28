"""Blockbuster"""

from datetime import datetime, timedelta

OLDEST_MOVIE_YEAR = 1900
MAX_RUNTIME = 1440
MIN_RUNTIME = 10
THIS_YEAR_VIDEO_RENT = 1000
STANDARD_VIDEO_RENT = 500
YOUTH_AGE = 13
MAX_CUSTOMER_RENT = 50000
STANDARD_DVD_RENT = 1200


class VideoError(Exception):
    """Video Error"""
    pass


class Video:
    """Video class"""

    def __init__(self, video_title: str, year: int, runtime: int) -> None:
        print("Video Init")
        if year < OLDEST_MOVIE_YEAR:
            raise VideoError("Videos can't be released before 1900")
        if not video_title:
            raise VideoError("Title must be provided")
        if not MIN_RUNTIME < runtime < MAX_RUNTIME:
            raise VideoError("runtime is wrong length")
        self.video_title = video_title
        self.year = year
        self.runtime = runtime
        self.is_rewound = True

    def display_title(self) -> str:
        """Displays title"""
        return f"{self.video_title} ({self.year})"

    def rental_price(self) -> int:
        """Calculates rental price"""
        if self.year == datetime.now().year:
            price = THIS_YEAR_VIDEO_RENT
        else:
            price = STANDARD_VIDEO_RENT
        if self.runtime > 240:
            return price * 2
        return price

    def display_price(self) -> str:
        """Displays the price"""
        price = str(self.rental_price())
        return f"£{price[:-2]}.{price[-2:]}"

    def watch(self) -> None:
        """Watching"""
        if self.is_rewound == False:
            raise VideoError("Video isn't rewinded")
        self.is_rewound = False

    def rewind(self) -> None:
        """Rewinding"""
        if self.is_rewound == True:
            raise VideoError("Video has already been rewinded")
        self.is_rewound = True


class Customer:
    """Customer"""

    def __init__(self, first_name: str, last_name: str, date_of_birth: str) -> None:
        print("Customer Init")
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.outstanding_fine = 0
        self.calculate_age()

    @property
    def name(self) -> str:
        """Shows name"""
        return f"{self.first_name} {self.last_name}"

    def calculate_age(self, age=None) -> int:
        """Calculates age"""
        if age is None:
            day, month, year = map(int, self.date_of_birth.split("/"))
            today = datetime.today()
            age = today.year - year - ((today.month, today.day) < (month, day))

        if age < YOUTH_AGE:
            raise VideoError("You are too young")

        if isinstance(age, int):
            return age
        raise VideoError("Must be an integer")

    def pay_off_fine(self):
        self.outstanding_fine = 0


class Rental:
    """Rental"""

    def __init__(self, video: Video, customer: Customer) -> None:
        print("Rental Init")
        self.video = video
        self.customer = customer
        self.due_date = datetime.today() + timedelta(weeks=2)


class VideoStore:
    """Video Store"""

    def __init__(self, videos: list[Video], max_videos: int = 10) -> None:
        print("VideoStore Init")
        if 0 < len(videos) <= max_videos:
            self.videos_in_stock = videos
        else:
            raise VideoError(f"Can only hold a maximum of {max_videos} Videos")

        self.availability = {}
        for video in videos:
            if isinstance(video, Video):
                self.availability[video] = True
            else:
                raise TypeError("Only videos are accepted")

    def find_video_by_title(self, video_title: str) -> Video:
        """Show title"""
        for video_in_stock in self.videos_in_stock:
            if video_title == video_in_stock.video_title:
                return video_in_stock
        raise VideoError("This video does not exist")

    def is_available(self, video: Video) -> bool:
        """Check availability of video"""
        print(self.availability, video)
        if self.availability.get(video):
            return self.availability.get(video)
        raise VideoError("Video is not available")

    def rent_video(self, video: Video, customer: Customer) -> Rental:
        """Rent video"""
        if customer.outstanding_fine > MAX_CUSTOMER_RENT:
            raise VideoError("Pay off your fines first")

        if isinstance(video, Video) and isinstance(customer, Customer):
            self.availability[video] = False
            return Rental(video, customer)
        raise VideoError("Customer doesn't exist")

    def fine(self, rental: Rental) -> int:
        return rental.video.rental_price()

    def return_video(self, rental: Rental, return_date: str) -> None:
        """Return video before due date or get fined"""
        if not rental or not return_date:
            raise VideoError("Give rental details and return date")
        if not isinstance(rental, Rental) or not isinstance(return_date, str):
            raise TypeError("Give inputs in valid type")
        if not rental.video.is_rewound:
            raise VideoError("Video needs to be rewound first")

        return_date = datetime.strptime(return_date, '%d/%m/%Y')
        if return_date > rental.due_date:
            rental.customer.outstanding_fine += self.fine(rental)

        self.availability[rental.video] = True


class DVD(Video):
    """DVD"""

    def rental_price(self) -> int:
        return STANDARD_DVD_RENT

    def watch(self):
        self.is_rewound = True


class VendingMachine(VideoStore):
    """Vending Machine"""

    def __init__(self, videos: list[Video]) -> None:
        print("VendingMachine Init")
        super().__init__(videos, 5)

    def fine(self, rental: Rental) -> int:
        return 0


# john_smith = Customer('John', 'Smith', '24/01/1980')
# print(john_smith.calculate_age(34))

# matrix = Video('The Matrix', 1999, 150)
# terminator = Video('The Terminator', 1985, 108)
# video_example = VideoStore([matrix, terminator])


# video_example.rent_video(matrix, john_smith)
# print(video_example.availability)

# video_example.return_video(Rental(matrix, john_smith), "27/03/2024")
