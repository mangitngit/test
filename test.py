class Test:
    def __init__(self, test):
        self.test = test

    def print_test(self):
        if self.test == "test":
            print(self.test)
        else:
            print("non " + self.test)
