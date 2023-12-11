def generate_strings(grammar, current_symbol):
    if current_symbol not in grammar['P']:
        # Якщо поточний символ - термінал, повертаємо його
        return [current_symbol]

    result = []
    # Для кожного правила, що починається з поточного символу
    for rule in grammar['P'][current_symbol]:
        # Генеруємо рядок для кожного символу правила
        current_string = ''
        for symbol in rule:
            current_string += ''.join(generate_strings(grammar, symbol))
        result.append(current_string)

    return result
def determine_grammar_type(grammar):
    start_symbol = grammar['S']

    # Перевірка на контекстно-вільність
    if all(all(len(production) >= 1 and production[0] in grammar['V'] for production in productions) for
           productions in grammar['P'].values()):
        return "Тип 2 (Контекстно-вільна граматика)"

    # Перевірка на контекстно-залежність
    if any(len(production) > 2 and start_symbol in production for productions in grammar['P'].values() for production in
           productions):
        return "Тип 1 (Контекстно-залежна граматика)"

    # Перевірка на регулярність
    if all(
            (len(production) == 2 and production[0] in grammar['V'] and production[1] in grammar['V'].union(
                grammar['T'])) or
            (len(production) == 1 and production[0] in grammar['T'] and production[0] != '𝜆') or
            (len(production) == 2 and production[0] == start_symbol and production[1] == '𝜆') or
            (len(production) == 1 and production[0] == start_symbol and production[0] == '𝜆') for
            productions in grammar['P'].values() for production in productions):
        return "Тип 3 (Регулярна граматика)"

    return "Невідомий тип граматики"
def main():
    # Вхідні дані
    grammar = {
        'V': {'0', '1', 'S', 'A', 'B'},
        'T': {'0', '1'},
        'S': 'S',
        'P': {
            'S': ['AB', '1A'],
            'A': ['1'],
            'B': ['0', '1']
        }
    }

    # Початковий символ
    start_symbol = grammar['S']

    # Генеруємо рядки, породжені граматикою
    generated_strings = generate_strings(grammar, start_symbol)

    # Виводимо результат
    print("L(G) =", set(generated_strings))

    grammar_type = determine_grammar_type(grammar)
    print("Тип граматики:", grammar_type)

if __name__ == "__main__":
    main()
