# Functions used like arguments for anothers functions
average = lambda *args: sum(args) / len(args) # Sum tuples elements and then divide for lenght
print(average(10, 10, 10, 10))


pass_exam = lambda q : q >= 7
print(pass_exam(7))
print(pass_exam(3))

def pass_course(a,p,*args): # a & p are callbacks. 
    av = a(*args)
    
    if p(av):
        print(f'Your Score is {av} :) . Congrats! ')
    else:
        print(f'''Your Score is {av} :( You don't pass''')

pass_course(average,pass_exam,1,5,7,10,10)
pass_course(average,pass_exam,10,8,5,7)


