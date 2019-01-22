import numpy as np

# print(str(sum([x * x for x in range(1000000)])))
# print(str(np.sum([np.square(x) for x in range(1000000)])))
# print(f"{sum([x * x for x in range(1000000)])}")
#
# def varfun(a, b, *c):
#    print(a)
#    print(b)
#    print(c)
#    print('---')
#
# print (varfun(1, 2))
# print (varfun(1, 2, 3))
# print (varfun(1, 2, 3, 4, 5, 42))
# print (varfun(1))

# def mysum(*a):
#     return sum(a)
#
# print(mysum())
# print(mysum(1))
# print(mysum(1, 2, 3, 4, 5))

# import operator
#
# def mostFrequentChar(mystring):
#     mydict = {}
#     for _, s in enumerate(mystring):
#         if s in mydict:
#           mydict[s] = mydict[s] + 1
#         else:
#           mydict[s] = 1
#     print(mydict)
#     print(f'Most frequent char is {max(mydict.items(), key=operator.itemgetter(1))[0]}')
#
# mostFrequentChar("datascienceretreatrocks ")
#
# def mostFrequentWord(myword):
#     mydict = {}
#     myword = myword.replace('.', ' ')
#     for word in myword.split():
#         if word in mydict:
#           mydict[word] = mydict[word] + 1
#         else:
#           mydict[word] = 1
#     print(mydict)
#     print(f'Most frequent word is {max(mydict.items(), key=operator.itemgetter(1))[0]}')
#
# mostFrequentWord("the fox jumps over the red squirrel on the red tree.")

# import time
# from functools import lru_cache
#
# @lru_cache() # memorization of intermediate values, severe speedup
# def fibu(n):
#     if n < 2:
#         return n
#     else:
#         return fibu(n - 1) + fibu(n - 2)
#
# tic = time.time()
# print(str(fibu(40)))
# toc = time.time()
# print(f'It took {toc-tic:.10f} seconds')

# Closures
# def adder(f):
#     def  myfun(n):
#         return n + f
#     return myfun
#
# my_adder = adder(5)
# print(str(my_adder(100)))

# Decorators
# def mydecorator(original_fun):
#     def logged_function(arg):
#         result = -1
#         if arg > 0:
#             result = original_fun(arg)
#         else:
#             print(f'Error: Negative argument')
#         return result
#     return logged_function
#
# @mydecorator
# def mylogic(n):
#     return n + 1
# print(mylogic(-1))
