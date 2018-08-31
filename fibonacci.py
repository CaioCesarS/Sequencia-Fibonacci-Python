'''
Fibonacci em Python
'''
__author__ = 'Caio César'
__license__ = 'MIT'
__version__ = '1.0'
__status__ = 'Development'

class Fibonacci():
  def __init__(self, sequencia):
    self.__sequencia = sequencia

  def getResult(self):
    t1 = 1 #Primeiro termo da Sequência Fibonnacci
    t2 = 1 #Segundo termo termo da Sequência Fibonnacci
    t3 = t1 + t2
    cont = 3 #Conta à partir do Terceiro termo

    print('{} | {} | '.format(t1, t2), end='')

    while cont <= self.__sequencia:
      print('{} | '.format(t3), end='')
      t1 = t2
      t2 = t3
      t3 = t1 + t2
      cont += 1

    print('FIM')