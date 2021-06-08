# Special function that returns and iterable object

def p():  # Lazy iterator
    for n in range(0, 10, 2):
        yield n  # Suspend the execution
       # print('Continue')


generator = p()

while True:
    try:
        par=next(generator)
        print(par)
    except StopIteration:
        print('End')
        break