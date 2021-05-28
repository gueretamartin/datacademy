def do(o,q):
    mile = 1.609344
    if o == 1:  
        print(f'{round(q * mile,2)} Kilometers')
    else:  
        print(f'{round(q / mile,2)} Miles')

def main():
    msg= '''Please, select an option: 
              1 - Miles to Kilometers 
              2 - Kilometers to Miles
         '''
    option = int(input(f'{msg}'))
    if option in [1,2]:
        quantity = float(input('Input Quantity: '))
        do(option,quantity)
    else:
        print('Select a correct option. \n')
        main()

if __name__ == '__main__':
    main()