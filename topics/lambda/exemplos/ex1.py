num_dobrado = lambda x : x * 2

func_quadratica = lambda x, func : x * x + func(x+2)
print(func_quadratica(2,lambda x : x / 2))