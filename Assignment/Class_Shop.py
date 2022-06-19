
class shop:
    def __init__(self):
        self.is_open = False

    def open(self):
        self.is_open = True
        print("The shop is open")

    def close(self):
        self.is_open = False
        print("The shop is closed")


def main():
    dairy = shop()
    print(type(dairy))
    print(dairy.is_open)
    shop.open(dairy)
    print(dairy.is_open)


main()
