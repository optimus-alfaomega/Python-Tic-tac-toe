import os
import time
from random import random, randrange
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
board = [[1,2,3],[4,5,6],[7,8,9]]
lvacios =[]
salir ="exit"
victoria = False

def DisplayBoard(board):
    os.system('cls')

    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print("")
        
    return
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
def EnterMove(board):
    ok = False
    lleno =MakeListOfFreeFields(board)
    while ok == False:
        entrada=int(input("¿cual es su proximo movimiento? \n"))
        if len(lleno) < 1:
            print("no hay mas movimientos")
            ok = True
            quit()
            

        if (entrada > 0) and (entrada <= 9):
            for i in range(len(board)):
               for j in range(len(board)):
                  if board[i][j] == entrada:      
                     board[i][j]="O"
                     DisplayBoard(board)
                     ok = True
        else:
            print("entrada erronea digite los valores entre 1 y 9 ")
    else:
        print("fin Movimiento jugador O ")

#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#

def MakeListOfFreeFields(board):
    vacios=[]
    for i in range(len(board)):
       for j in range(len(board)):
           if type(board[i][j])== int:
               vacios.append(board[i][j])

    return vacios


#comprueba que los elementos sean iguales

#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#

def VictoryFor(board):
    N =len(board)
    diag=[]
    diagInv=[]
    lver_iz=[]
    lver_der=[]
    lver_centro=[]
    lhor_inf=[]
    lhor_centro=[]
    lhor_sup=[]
    global lGanador
    global victoria
    victoria= False
    lGanador =[]
    #llena la diagonal principal
    for i in range(len(board)):
       for j in range(len(board)):
           if i==j : 
               if type(board[i][j]) != int: 
                   diag.append(board[i][j])


    #llena la diagonal invertida            
    for i in range(len(board)):
       for j in range(len(board)):
           if i==j : 
               if type(board[i][j]) != int: 
                   diagInv.append(board[i][j])
    #llena las lineas verticales
    for i in range(N):
       for j in range(N):
           if   j == N - 3:
               if type(board[i][j]) != int:
                   lver_der.append(board[i][j])
           elif j == N - 2:
               if type(board[i][j]) != int:
                   lver_centro.append(board[i][j])
           elif j == N - 1:
               if type(board[i][j]) != int:
                   lver_iz.append(board[i][j])
    #llena las lineas Horizontales
    for i in range(N):
       for j in range(N):
           if i == N - 3:
               if type(board[i][j]) != int:
                   lhor_inf.append(board[i][j])
           elif i == N - 2:
               if type(board[i][j]) != int:
                   lhor_centro.append(board[i][j])
           elif i == N - 1:
               if type(board[i][j]) != int:
                   lhor_sup.append(board[i][j])

#comprueba el ganador si las lineas verticales u horizontales son iguales
    def ComprobarElm(arr,):
        if len(set(arr)) == 1:
           print ("gano alguien")
           return True         
        else:
           
           return False

    if len(diag) == N:
       if (ComprobarElm(diag)) == True:
           lGanador = diag
    elif len(diagInv)  == N:
       if (ComprobarElm(diagInv)) ==True:
           lGanador= diagInv      
    elif len(lver_iz)  == N:
       if (ComprobarElm(lver_iz)) ==True:
            lGanador =lver_iz
    elif len(lver_der) == N:
       if (ComprobarElm(lver_der)) ==True:
            lGanador=lver_der
    elif len(lver_centro) == N:
       if (ComprobarElm(lver_centro)) ==True:
            lGanador =lver_centro
    elif len(lhor_inf)  == N:
       if (ComprobarElm(lhor_inf)) ==True:
            lGanador = lhor_inf
    elif len(lhor_centro) == N:
       if(ComprobarElm(lhor_centro) ==True):
            lGanador = lhor_centro
    elif len(lhor_sup) == N:
       if(ComprobarElm(lhor_sup) ==True):
            lGanador =lhor_sup
    
    if len(lGanador) == N:
        victoria = True
    print(diag,diagInv,lver_iz,lver_der,lver_centro,lhor_inf,lhor_centro,lhor_sup)

#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
def DrawMove(board):
    print("movimiento de la maquina")
    time.sleep(2)
    vacios = MakeListOfFreeFields(board)
    N =len(vacios)
    if N > 0:
        randrange(1,N)
        for i in range(len(board)):
           for j in range(len(board)):
               if board[i][j] == N:
                  board[i][j] = "X"
                  DisplayBoard(board)
    else:
        print("No hay mas movimientos")



while victoria == False:
    DisplayBoard(board)
    EnterMove(board)
    DrawMove(board)
    VictoryFor(board)
    print(victoria,lGanador)
else:
    print("fin del juego")



