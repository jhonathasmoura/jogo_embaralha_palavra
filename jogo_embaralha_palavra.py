import random, os
os.system('cls' if os.name == 'nt' else 'clear')

def embaralha_palavra(palavra, num_tema, nivel):
    palavras = define_tema(palavra, num_tema)
    palavras = define_nivel_dificuldade(palavras, nivel)

    palavra = palavra_desembaralhada = random.choice(palavras)
    palavra = list(palavra)
    random.shuffle(palavra)
    palavra_embaralhada = ''.join(palavra)
    return palavra_embaralhada, palavra_desembaralhada


def define_tema(palavra, num_tema):
    tema_palavras = palavra[num_tema - 1]
    return tema_palavras


def define_nivel_dificuldade(palavra, nivel):
    nivel_palavras = []
    if nivel == 1:
        nivel_palavras.append([p for p in palavra if len(p) <= 4])
    elif nivel == 2:
        nivel_palavras.append([p for p in palavra if len(p) > 4 and len(p) <= 8])
    else:
        nivel_palavras.append([p for p in palavra if len(p) > 8])
    return nivel_palavras.pop()


def jogo(palavras, frases_motivacao):
    print('-' * 55)
    print ('JOGO - ACERTE A PALAVRA')
    print('-' * 55)

    num_tema = int(input('Escolha o tema: \n[1] Animais \n[2] Objetos \n[3] Países \n[4] Times de Futebol\n> '))
    while num_tema not in [1, 2, 3, 4]:
        num_tema = int(input('Tema inválido! Tente novamente.\n> '))
    nivel = int(input('\nEscolha o nível de dificuldade: \n[1] Fácil \n[2] Médio \n[3] Difícil\n> '))
    while nivel not in [1, 2, 3]:
        nivel = int(input('Nível de dificuldade inválido! Tente novamente.\n> '))

    palavra_embaralhada, palavra_desembaralhada = embaralha_palavra(palavras, num_tema, nivel)
    print(f'\nPalavra embaralhada: \033[33m{palavra_embaralhada}\033[m')
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
                print(f'\033[31m{random.choice(frases_motivacao)}\033[m')
            else:
                print(f'\033[31mPalavra correta: {palavra_desembaralhada}\033[m')
                print(f'\033[31mNúmero de tentativas usadas: {num_tentativas}\033[m')
        i += 1


def main():
    arquivo_palavras = open('palavras.txt', 'r', encoding='utf-8')
    palavras = arquivo_palavras.readlines()
    palavras = [palavra.strip().split(' ')[1:] for palavra in palavras]
    arquivo_palavras.close()

    arquivo_frases_motivacao = open('frases_motivacao.txt', 'r', encoding='utf-8')
    frases_motivacao = arquivo_frases_motivacao.readlines()
    frases_motivacao = [frase.strip() for frase in frases_motivacao]
    arquivo_frases_motivacao.close()

    jogo(palavras, frases_motivacao)


if __name__ == '__main__':
    main()
 