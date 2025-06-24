import pytest
import allure
import functions
from data.data_for_count_function import *

class TestCountVowels:

    @allure.title('Проверяем корректность подсчета гласных в строке')
    @pytest.mark.parametrize(('string', 'count_vowels'), DataStringAndCounts.string_and_count)
    def test_count_vowels(self, string, count_vowels):
        function = functions.FunctionForTest()
        result = function.count_vowels(string)
        assert result == count_vowels