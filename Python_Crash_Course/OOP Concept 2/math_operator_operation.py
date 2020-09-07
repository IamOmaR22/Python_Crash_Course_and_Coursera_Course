
class operation():

    lis=[]

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def alloperation(self):
        resulta = self.num1 + self.num2
        results = self.num1 - self.num2
        resultm = self.num1 * self.num2

        try:
            resultd = self.num1 / self.num2
            print("Divition is:", resultd)
        except:
            print("Divide by zero is not possible!")


        self.lis.append(resulta)
        self.lis.append(results)
        self.lis.append(resultm)

        return self.lis
