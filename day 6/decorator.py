def star(func):
    def wrapper():
        print('*' * 8)
        func()
        print('*' * 8)
    return wrapper

@star
def hello():
    print('hello')
@star
def bye():
    print('bye')
    
hello()