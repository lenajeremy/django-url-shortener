""" import math
class Patient:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = None

    def get_bmi(self):
        if not self.bmi:
            self.bmi = str(
                round(self.weight/math.pow(self.height, 2), 2)) + 'kg/m^2'
        return self.bmi

#get the patient's details
name = input('Enter your name')
height = float(input('Enter your height(m)'))
weight = float(input("Enter your weight(kg)"))

#create an instance of the Patient class with the details from the user
patient = Patient(name=name, height=height, weight=weight)

#get the bmi of the patient
bmi = patient.get_bmi()

print("\n###---------------###\n")

print(f"Your BMI is {bmi}")

#messages to print depending on the BMI of the patient
if float(bmi.split('kg/m^2')[0]) >= 25:
    print(f'Hey {patient.name.title()}! You are obese, you need to check your diet')
else:
    print(f"{patient.name.title()} is doing just great")
 """

import math

""" 
def hexToDecimal(hexString):
    def getDecEquiv(string):
        values = ['A', 'B', 'C', 'D', 'E', 'F']
        if string.upper() in values:
            return 10 + values.index(string.upper())
        return int(string)

    decimal = 0
    for i in range(0, len(hexString)):
        decimal += getDecEquiv(hexString[i]) * \
            math.pow(16, len(hexString) - i - 1)
    return int(decimal)


print(hexToDecimal(input('Enter a hex number:  ').strip())) """


# class Rational:
#     def __init__(self, numerator=1, denominator=0):
#         divisor = gcd(numerator, denominator)
#         self.__numerator = (1 if denominator > 0 else -1) * \
#             int(numerator / divisor)
#         self.__denominator = int(abs(denominator) / divisor)

#     def __add__(self, secondRational):
#         n = self.__numerator * \
#             secondRational[1] + self.__denominator * secondRational[0]
#         d = self.__denominator * secondRational[1]
#         return Rational(n, d)

#     def __sub__(self, secondRational):
#         n = self.__numerator * \
#             secondRational[1] - self.__denominator * secondRational[0]
#         d = self.__denominator * secondRational[1]
#         return Rational(n, d)

#     def __mul__(self, secondRational):
#         n = self.__numerator * secondRational[0]
#         d = self.__denominator * secondRational[1]
#         return Rational(n, d)

#     def __truediv__(self, secondRational):
#         n = self.__numerator * secondRational[1]
#         d = self.__denominator * secondRational[0]
#         return Rational(n, d)

#     def __float__(self):
#         return self.__numerator/self.__denominator

#     def __int__(self):
#         return int(self.__float__())

#     def __str__(self):
#         if self.__denominator == 1:
#             return str(self.__numerator)
#         else:
#             return str(self.__numerator) + "/" + str(self.__denominator)

#     def __lt__(self, secondRational):
#         return self.__cmp__(secondRational) < 0

#     def __le__(self, secondRational):
#         return self.__cmp__(secondRational) <= 0

#     def __gt__(self, secondRational):
#         return self.__cmp__(secondRational) > 0

#     def __ge__(self, secondRational):
#         return self.__cmp__(secondRartional) >= 0

#     def __cmp__(self, secondRational):
#         temp = self.__sub__(secondRational)
#         if(temp[0] > 0):
#             return 1
#         elif temp[0] < 0:
#             return -1
#         else:
#             return 0

#     def __getitem__(self, index):
#         if index == 0:
#             return self.__numerator
#         else:
#             return self.__denominator


# def gcd(n, d):
#     n1 = abs(n)
#     n2 = abs(d)
#     gcd = 1

#     k = 1
#     while k <= n1 and k <= n2:
#         if n1 % k == 0 and n2 % k == 0:
#             gcd = k
#         k += 1

#     return gcd


# rational1 = Rational(5, 9)
# rational2 = Rational(4, 9)
# print(rational1 + rational2)
def validate_password(password_string):

    def test1(password_string):
        return len(password_string) >= 8

    def test2(password_string):
        return password_string.isalnum()

    def test3(password_string):
        return len(list(filter(lambda x: ord(x) <= 57 and ord(
            x) >= 48, list(password_string)))) >= 2

    print(test1(password_string))
    print(test2(password_string))
    print(test3(password_string))
    if test1(password_string) and test2(password_string) and test3(password_string):
        return 'valid password'
    return 'invalid password'


for i in range(0, int(input('Count?'))):
    print(validate_password(input('Enter a password')))
