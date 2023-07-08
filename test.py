class Test:
    def __init__(self):
        self.was_run = False

    def run(self):
        self.was_run = True


if __name__ == "__main__":
    test = Test()
    print(f"{test.was_run = }")
    test.run()
    print(f"{test.was_run = }")
