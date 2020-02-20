class divition:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def divfunction(self):
        try:
            result = self.num1 / self.num2
            print("Divition is:", result)
        except:
            print("Divide by zero is not possible!")


