from main import possitive_assert, negative_assert_code_400, negative_assert_no_first_name

# 1-й тест: Допустимое количество символов (1)
def test_create_kit_1_letter_in_name_get_successful_response():
    possitive_assert("А")

# 2-й тест: Допустимое количество символов (511)
def test_create_kit_511_letter_in_name_get_successful_response():
    possitive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
                      "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" 
                      "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
                      "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" 
                      "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
                      "cdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcd" 
                      "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
                      "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" 
                      "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
                      "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" 
                      "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
                      "cdabC")

# 3-й тест: Недопустимое количество символов (меньше допустимого) - 0
def test_create_kit_zero_letter_in_name_get_unsuccessful_response():
    negative_assert_code_400("")

# 4-й тест: Недопустимое количество символов (512)
def test_create_kit_512_letter_in_name_get_unsuccessful_response():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" 
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" 
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
                    "cdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcd" 
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" 
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" 
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
                    "cdabcD")

# 5-й тест: Разрешены английские буквы
def test_create_kit_english_letter_in_name_get_successful_response():
    possitive_assert("QWErty")

# 6-й тест: Разрешены русские буквы
def test_create_kit_russian_letter_in_name_get_successful_response():
    possitive_assert("Мария")

# 7-й тест: Разрешены спецсимволы
def test_create_kit_special_symbol_in_name_get_successful_response():
    possitive_assert("№%@")

# 8-й тест: Разрешены пробелы
def test_create_kit_white_space_in_name_get_successful_response():
    possitive_assert("Человек и КО")

# 9-й тест: Разрешены цифры
def test_create_kit_number_in_name_get_successful_response():
    possitive_assert("123")

# 10-й тест: Параметр не передан в запросе
def test_create_kit_no_name_get_unsuccessful_response():
    negative_assert_no_first_name()

# 11-й тест: Передан другой тип параметра (число)
def test_create_kit_number_different_type_of_name_parameter_get_unsuccessful_response():
    negative_assert_code_400(123)