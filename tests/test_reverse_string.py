import pytest
import allure
import functions
from data.data_for_reversed_function import *

class TestReverseString:

    @allure.title('Проверяем кооректность работы переворачивания строки')
    @pytest.mark.parametrize(('string', 'string_r'), StringsAndReversedStrings.strings_and_reversed_strings)
    def test_reverse_string(self, string, string_r):
        function = functions.FunctionForTest()
        result = function.reverse_string(string)
        assert result == string_r
