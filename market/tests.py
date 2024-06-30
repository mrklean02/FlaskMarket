class PracticeTest:
    def __init__(self, num):
        self.num = num

    def generator_function(self):
        for i in range(self.num):
            yield i


if __name__ == "__main__":
    pt = PracticeTest(10)

    for item in pt.generator_function():
        print(item)
