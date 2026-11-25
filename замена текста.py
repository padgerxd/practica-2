def replace_cyrillic_to_latin(text):
    mapping = {
        'А': 'A', 'В': 'B', 'С': 'C', 'Е': 'E', 'Н': 'H',
        'К': 'K', 'М': 'M', 'О': 'O', 'Р': 'P', 'Т': 'T',
        'Х': 'X', 'У': 'Y',
        'а': 'a', 'в': 'b', 'с': 'c', 'е': 'e', 'н': 'h',
        'к': 'k', 'м': 'm', 'о': 'o', 'р': 'p', 'т': 't',
        'х': 'x', 'у': 'y'
    }
    return text.translate(str.maketrans(mapping))

# --- Интерактивный режим ---
print("Введите текст")
user_input = input("> ")

result = replace_cyrillic_to_latin(user_input)

print("\nРезультат замены:")
print(result)