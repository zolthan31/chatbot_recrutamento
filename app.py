import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, Bem hoje sou Pj, tenho 4 anos de experiencia na area de desenvolvimento Fullstack, migrei da area de infra onde pasei 13 anos{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, Sou pro-ativo, gosto de resolver problemas, adoro trabalhar em equipe pois acredito que trabalhar em conjunto agrega muito mais valor! {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, Sou denvolvedor fullstack com experiencia nas linguagens Python, JavaScript, Typescript, Golang, NodeJS e tambem com conhecimentos nas abstrações ReactJs, Angular e Django, experiencia com banco de dados relacionais MySQL e não relacionais Mongo DB, e tambem microserviços, Docker, AWS e Google Cloud Platform e certo conhecimento em metodologias ageis Scrum{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, Em torno de R$ 5.000,00{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}{nome}, Como já frisei estou há procura de um squad de sucesso pois tenho muito a ensinar e a aprender{os.linesep}')
    else:
        print('Digite apenas 1,2,3,4 e 5')
def start():
    # Apresentação do Chat
    print('Ola! Bem vindo ao chat de respostas de processos de recrutamento.')
    # Nome
    nome = input('Digite seu nome: ')
    # E-mail
    email = input('Digite seu e-mail: ')
    while True:
        # Menu de opções
        resposta = input(
            f'O que você gostaria de saber?{os.linesep}[1] - Fale do seu momento atual.{os.linesep}[2] - Fale de suas habilidades.{os.linesep}[3] - Fale de seus conhecimentos.{os.linesep}[4] - Sua pretensão salarial{os.linesep}[5] - Porque se candidatou a esta vaga?')

        # Processar resposta
        processar_resposta(resposta, nome)
if __name__ == '__main__':
    start()
