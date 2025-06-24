class FunctionForTest:

    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def count_vowels(string):
        vowels = set(
            'aeiouAEIOU' +
            'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
        )
        return sum(1 for ch in string if ch in vowels)

    @staticmethod
    def is_palindrome(string):
        return string == FunctionForTest.reverse_string(string)
