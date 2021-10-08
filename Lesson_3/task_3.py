def first_func(var_1, var_2=10):
    sub = var_1 - var_2
    #print(f'Sub: {sub}')
    return sub, 56, False

print(first_func(20, 5)[2])
#first_func(int(input('var_1: ')))
#print(first_func(156)*156)

def my_f(v1, *args, v2=10, **kwargs):
    print(args[0])
    return args, kwargs

print(my_f(1, 2, 3, 4, v3=17, v4=19))