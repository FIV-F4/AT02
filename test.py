from count_vowels import count_vowels
def test_count_vowels():
    # Тест: строка содержит только гласные
    assert count_vowels("aeiouAEIOU") == 10, "Failed test: only vowels"

    # Тест: строка не содержит гласных
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0, "Failed test: no vowels"

    # Тест: смешанная строка (гласные и согласные, разные регистры)
    assert count_vowels("Hello World!") == 3, "Failed test: mixed string"
    assert count_vowels("Python Programming") == 4, "Failed test: mixed string with different cases"

    # Дополнительный тест: пустая строка
    assert count_vowels("") == 0, "Failed test: empty string"

    # Дополнительный тест: строка с цифрами и символами
    assert count_vowels("123456!@#") == 0, "Failed test: string with numbers and symbols"

    print("All tests passed!")

# Запуск тестов
test_count_vowels()
