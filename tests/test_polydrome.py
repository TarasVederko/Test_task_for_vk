import pytest
import allure
import functions
from data.data_for_polydromes import *

class TestPalindroms:

    @allure.title('Проверяем что функция корректно определяет полиндромы')
    @pytest.mark.parametrize(('string', 'logic_type_data'), StringsAndLogicData.strings_and_logic_data)
    def test_palindromes(self, string, logic_type_data):
        function = functions.FunctionForTest()
        assert function.is_palindrome(string) == logic_type_data
