a = 10
def wrapper(times):
    print(a)
    return lambda lambda_input: lambda_input * times

time_func = wrapper(200)
print(time_func(3))