class DataStrings:

    STRING_1 = f'Тестируем тестируем и никак не вытестируем'
    STRING_1R = STRING_1[::-1]

    STRING_2 = f'ТестируемБезПробелов'
    STRING_2R = STRING_2[::-1]

    STRING_3 = f''
    STRING_3R = STRING_3[::-1]

class StringsAndReversedStrings:
    strings_and_reversed_strings = [
        (DataStrings.STRING_1, DataStrings.STRING_1R),
        (DataStrings.STRING_2, DataStrings.STRING_2R),
        (DataStrings.STRING_3, DataStrings.STRING_3R)
    ]
