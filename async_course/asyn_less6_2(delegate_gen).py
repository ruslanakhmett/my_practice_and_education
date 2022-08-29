#делегирующий генератор - это тот, который вызывает другой генератор
#подгенератор - тот, который вызывают


from email import message


class BlaBlaException(Exception):
    pass

def coroutine(func): #декоратор, что бы каждый раз не передавать None в генератор первым делом(инициализация генератора)
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g #возвращает проинициализированный объект генератора
    return inner


def subgen(): #читающий генератор, например из сокета
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print('........', message)
    return 'returned from subgen()'

@coroutine
def delegator(g): #генератор транслятор, принимает генератор g
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e) #пробрасываем исключение в подгенератор
    result = yield from g
    print(result) #сразу сам инициализирует, не надо декоратор
#в result попадет то что ушло в return из подгенератора