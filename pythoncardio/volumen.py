import math

def cylinder():
    r = float(input('Input radio: '))
    h = float(input('Input height: '))
    print(f'Surface is: {math.pi * r**2}')
    print(f'Volumen is: {math.pi * r**2 * h}')
 
def cube():
    a = float(input('Input side: '))
    print(f'Surface is: {6*a**2}')
    print(f'Volumen is: {a**3}')

def main():
    msg = """ Choose figure: 
                1 - Cylinder
                2 - Cube
          """
    option = int(input(f'{msg}'))
    if option == 1:
        cylinder()
    elif option == 2:
        cube()
    else:
        print("Select a correct option:")
        main() 
    
if __name__ == '__main__':
    main()