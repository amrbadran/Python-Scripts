from WebScrapper import *
from FileHandler import *


class Main:
    def __init__(self):
        print("This Script is Programmed for getting all news in specifed tag from aljazeera website")
        tag = input("Please Enter the Tag : ")
        path = input("Please Enter the Path To Result File : ")
        WebScrapper(tag, path).scrape()
        print_on_screen = input("The Result Was Written to a file Do You want to print it on the screen ? (Y/N) : ")
        if print_on_screen == 'Y':
            FileHandler(path).read()
        else:
            pass


if __name__ == "__main__":
    Main()
