import random
from unidecode import unidecode
from termcolor import colored
import os


def read_random_word(fileName):
    with open(fileName, 'r', encoding='utf-8') as _file:

        # Conta o número total de linhas no arquivo
        n_lines = sum(1 for _ in _file)

        # Volta para o início do arquivo
        _file.seek(0)

        # Gera um índice aleatório para a linha
        random_index = random.randint(1, n_lines - 1)  
        
        # volta a percorrer o arquivo do início até ler a palavra no index aleatório
        for current_index, current_word in enumerate(_file, start=1):
            if current_index == random_index:
                return current_word.strip()


def valid_word(word):
    if len(word) != 5:
        return False
    for char in word:
        if not char.isalpha():
            return False
    return True


def match_word(guess, password):
    decoded_chars = []
    match = False

    if guess == password:
        match = True
        for char_g in guess:
            decoded_chars.append(colored(char_g, 'green'))
        
        decoded_guess = f"{decoded_chars[0]} {decoded_chars[1]} {decoded_chars[2]} {decoded_chars[3]} {decoded_chars[4]}"
        return match, decoded_guess

    for c in range(len(password)):
        if guess[c] == password[c]:
            decoded_chars.append(colored(guess[c], 'green'))
        elif guess[c] in password:
            decoded_chars.append(colored(guess[c], 'yellow'))
        else:
            decoded_chars.append(colored(guess[c], 'red'))


    decoded_guess = f"{decoded_chars[0]} {decoded_chars[1]} {decoded_chars[2]} {decoded_chars[3]} {decoded_chars[4]}"
    return match, decoded_guess


def print_table(table):
    for row in table:
        print("\t" + row)
    print()
        

def fill_table(table, decoded, c):
    table[c] = decoded     

def main_loop(password, table):
    match = False

    for c in range(7):
        os.system('cls' if os.name == 'nt' else 'clear') # limpa o terminal
        
        #print(f"\n\n{password}\n\n")

        # imprimi o estado atual do jogo
        print(f"======= {c + 1}ª Rodada =======")
        print_table(table)

        # encerra o jogo caso precise
        if c == 6 or match:
            break

        # coleta o chute do jogador
        guess = str(input("Chute uma palavra: "))
        while not valid_word(guess):
            print("Palavra inválida!")
            guess = str(input("Chute uma palavra: "))

        # verifica se jogador acertou
        match, decoded = match_word(guess, password)
        fill_table(table, decoded, c)

    return match
            
def main():
    
    table = ["_ _ _ _ _",
    "_ _ _ _ _",
    "_ _ _ _ _",
    "_ _ _ _ _",
    "_ _ _ _ _",
    "_ _ _ _ _"]

    password = str(read_random_word("palavras.txt"))
    match = main_loop(password, table)

    if match:
        print("Parabéns, você ganhou!")
    else:
        print(f"Você perdeu :(. A palavra secreta era: {password}")

main()