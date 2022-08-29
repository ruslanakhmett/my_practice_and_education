


def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received:', message)

# g = subgen()
# g.send('fgfg') >
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't send non-None value to a just-started generator'''

#from inspect import getgeneratorstate
#getgeneratorstate(g) > 'GEN_CREATED'

#g.send(None)
#getgeneratorstate(g) > 'GEN_SUSPENDED'

#g.send('Ok') > 
# '''Subgen received: Ok Traceback (most recent call last): File "<stdin>", line 1, in <module> StopIteration'''

#g.send(None) > 'Ready to accept message'
#g.send('Ok') >
'''Subgen received: Ok
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration'''

class BlaBlaException(Exception):
    pass

def coroutine(func): #декоратор, что бы каждый раз не передавать None в генератор первым делом(инициализация генератора)
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g #возвращает проинициализированный объект генератора
    return inner


# генератор, возвращает среднее арифметическое
@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        except BlaBlaException:
            print('..........')
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2) #округляем до 2 знака
    return average

#g.throw (StopIteration) проброс в генератор исключения

