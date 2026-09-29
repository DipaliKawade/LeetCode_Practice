class Solution:
    def plusOne(self, digits):
        number = 0

        for digit in digits:
            number = number * 10 + digit

        number = number + 1

        result = []

        for digit in str(number):
            result.append(int(digit))

        return result