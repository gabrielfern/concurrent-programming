#!/usr/bin/python
# Gabriel Fernandes


from time import sleep
from random import randint
from threading import Thread


# Subrotina que representa uma tarefa de tempo nao deterministico
def tarefa(id):
    pausa = randint(5, 10)
    print('tarefa %d, executando por %d segs' %(id, pausa))
    sleep(pausa)
    print('tarefa %d, encerrando' %id)


# Principal subrotina do nosso programa
def main():
    # A tarefa 2 so comecara a executar apos a 1 terminar por completo
    print('EXECUCAO SINCRONA:')
    tarefa(1)
    tarefa(2)
    sleep(1)

    # Criando duas threads para dar as tarefas que podem demorar a elas
    print('\nEXECUCAO ASSINCRONA:')
    thread = Thread(target=tarefa, args=(3,))
    thread2 = Thread(target=tarefa, args=(4,))

    # Aqui uma nao vai esperar a outra terminar para comecar
    thread.start()
    thread2.start()


if __name__ == '__main__':
    main()
