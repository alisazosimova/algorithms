
class Solutions:
    def divides(self, dividend: int, divisor: int) -> int:
        minus = dividend - divisor   # 2 = 4 - 2
        print(minus)
        if minus >= divisor:  # if 2 => 2
            dividend = minus
            print(dividend)
            list.append(dividend)
            print(list)
            self.divide(dividend, divisor)



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        list = []
        for i in range(dividend): # 10
            result = dividend - divisor
            print(result)
            dividend = result
            print(dividend)
            list.append(0)
            print(list)
            if dividend < divisor:
                return len(list)