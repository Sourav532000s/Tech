def generator_func():
    yield "Yeild"
    yield "Keyword"
    yield "in"
    yield "Python"

generator_object = generator_func()
#print( type(generator_object))
for i in generator_object:
    print(i)