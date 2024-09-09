# class Bank_calculator:
#
#     __interest_rate = 8.6
#     __interest_rate_seiner_citizen = 8.4
#
#     def __init__(self, p_amount, duration, senior_citizen):
#         self.p_amount = p_amount
#         self.duration = duration
#         self.seiner_citizen_flag = senior_citizen
#
#     def simple_interest_calculator(self):
#         interest = self.__interest_rate_seiner_citizen if self.seiner_citizen_flag else self.__interest_rate
#         return self.duration * self.p_amount * interest / 100
#
#     def emi_calculator(self):
#         r = (self.__interest_rate_seiner_citizen if self.seiner_citizen_flag else self.__interest_rate) / 100
#         r /= 12
#         p = self.p_amount
#         n = self.duration * 12
#         emi = (p * r * ((1 + r) ** n)) / (((1 + r) ** n) -1)
#         return emi
#
#
# if __name__ == '__main__':
#     person1 = Bank_calculator(10000, 12, False)
#     person2 = Bank_calculator(10000, 12, True)
#
#     print(f'Interest: {person1.simple_interest_calculator()} EMI: {person1.emi_calculator()}')
#
#     print(f'Interest: {person2.simple_interest_calculator()} EMI: {person2.emi_calculator()}')
#
#

#----------------------------------------------------------------------------------------------------

class bank_interest_calculator:

    __interest_rate = 8.6
    __interest_rate_senior_citizen = 8.4
    senior_citizen = False

    def __init__(self,):
        pass
