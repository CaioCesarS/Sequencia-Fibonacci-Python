'''
Fibonacci em Python
'''
__author__ = 'Caio César'
__license__ = 'MIT'
__version__ = '1.0'
__status__ = 'Development'

from fibonacci import Fibonacci

num = int(input('Digite o termo da sequencia fibonacci:'))

print('~'*40)
fib = Fibonacci(num)
fib.getResult()
print('~'*40)