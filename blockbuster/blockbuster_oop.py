class Video:
    def __init__(self):
        print("Video Init")


class Customer:
    def __init__(self):
        print("Customer Init")


class VideoStore:
    def __init__(self):
        print("VideoStore Init")


class Rental:
    def __init__(self):
        print("Rental Init")


class DVD(Video):
    def __init__(self):
        print("DVD Init")


class VendingMachine(VideoStore):
    def __init__(self):
        print("VendingMachine Init")
