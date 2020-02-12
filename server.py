# импортируем необходимые сущности библиотеки bottle
from bottle import route
from bottle import run
from bottle import HTTPError # Импортируем класс HTTPError
from bottle import request

# регистрируем обработчик пути /hello/ с помощью декоратора route
@route('/hello')
def hello_word():
    return 'Hello Word' # Возвращаем приветственное сообщение

@route('/upper/<param>')
def upper(param):
    return param.upper()

@route('/fib/<n:int>')
def fib_handler(n):
    result = fib(n)
    return str(result)

def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a

@route('/modify/<param>/<method>')
def modify(param, method):
    # проверяем переданный модификатор и готовим соответствующий результат
    if method == 'upper':
        result = param.upper()
    elif method == 'lower':
        result = param.lower()
    elif method == 'title':
        result = param.title()
    else:
        result = HTTPError(400, "incorrect `method` value")
    return result

# Работаем с GET запросами
@route('/add')
def add():
    try:
        x = int(request.query.x)
        y = int(request.query.y)
        result = f'Сумма чисел {x} и {y} равна {x + y}'
    except ValueError:
        result = HTTPError(500, 'На вход ожидает int')
    return result

if __name__ == '__main__':
    # Запускаем веб-сервер с помощью функции run: указываем адрес узла и порт
    run(host='localhost', port=8080, debug=True)
    # Булев флаг debug=True запускает сервер в режиме отладки
