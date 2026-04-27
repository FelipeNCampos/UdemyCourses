def logging_decorator(f):
    def wraper(*args , **kargs):
        print(f"You called {f.__name__}{args}")
        resul = f(*args)
        print(f"It returnde: {resul}")
        return resul        
    return wraper

@logging_decorator
def a_function(*args):
    return sum(args)
    
teste:int = a_function(1,2,3)
print(teste)