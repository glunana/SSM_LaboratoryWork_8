import random

def generate_string(n):
    if n == 0:
        return "Λ"
    else:
        return "2" * (2 * n) + "1" * (2 * n)

def generate_random_string():
    n = random.randint(0, 5)  # Для прикладу, обмежимо n від 0 до 5
    return generate_string(n)

def main():
    terminal_symbols = {'1', '2'}
    nonterminal_symbols = {'S', 'A', 'B'}

    print("L(G)={2^(2n) 1^(2n), n=0,1,2...}")
    print("G={V, T, S, P}")
    print("V={1, 2, A, B, S}")
    print("T={1, 2}")
    print('S0 – початковий елемент')
    print("P={S→AASBB, S→Λ, A→1, B→2}")

    for n in range(3):  # Змінив на range(3), щоб вивести для n=0, 1, 2
        print("n =", n)
        generated_string = generate_string(n)
        print("S =", generated_string)

if __name__ == "__main__":
    main()
