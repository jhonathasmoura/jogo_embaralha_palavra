import random, os
os.system('cls' if os.name == 'nt' else 'clear')

def embaralha_palavra(palavra):
    palavra = palavra_desembaralhada = palavra[random.randint(0, len(palavra) - 1)]
    palavra = list(palavra)
    random.shuffle(palavra)
    palavra_embaralhada = ''.join(palavra)
    return palavra_embaralhada, palavra_desembaralhada

def jogo(palavra_embaralhada, palavra_desembaralhada, frase_motivacao):
    print('-' * 40)
    print ('JOGO - ACERTE A PALAVRA')
    print(f'Palavra embaralhada: \033[33m{palavra_embaralhada}\033[m')
    print('-' * 40)
    print('Você tem no máximo 5 tentativas!')

    num_tentativas = 0
    i = 1
    while i <= 5:
        num_tentativas += 1
        tentativa = input(f'Digite a palavra desembaralhada (Tentativa {num_tentativas}): ')
        if tentativa == palavra_desembaralhada:
            print('\n\033[32mParabéns, você acertou!\033[m')
            print(f'\033[32mPalavra correta: \033[33m{palavra_desembaralhada}\033[m\033[m')
            print(f'\033[32mNúmero de tentativas usadas: {num_tentativas}\033[m')
            break
        else:
            print(f'\n\033[31mVocê errou! Restam {abs(num_tentativas - 5)} tentativas\033[m')
            if abs(num_tentativas - 5) != 0:
                print(f'\033[31m{frase_motivacao[random.randint(0, len(frase_motivacao) - 1)]}\033[m')
            else:
                print(f'\033[31mPalavra correta: {palavra_desembaralhada}\033[m')
                print(f'\033[31mNúmero de tentativas usadas: {num_tentativas}\033[m')
        i += 1


def main():
    palavras = ['python', 'linux', 'windows', 'universidade', 'tecnologia', 'computador', 'programacao']
    frases_motivacao = ['Vamos, você consegue!', 'Não desista!', 'Mantenha a calma e tente novamente!', 'Eu acredito em você!']

    palavra_embaralhada, palavra_desembaralhada = embaralha_palavra(palavras)
    jogo(palavra_embaralhada, palavra_desembaralhada, frases_motivacao)


if __name__ == '__main__':
    main()
