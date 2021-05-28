def calcArea(b,h):
    area = b * h / 2 
    return area

def triangleType(b,h,a):
    if b == a and h == a:
        return 'Equilateral'
    elif b == a or b == h:
        return 'Isoceles'
    else:
        return 'Scalene' 
 
def option1(): 
    base = float(input('Enter the base of the triangle: '))
    height = float(input('Enter the height of the triangle: '))
    area = calcArea(base,height) 
    print(f'The area is {area}')

def option2():
    sideA = float(input('Enter the the Side A: '))
    sideB = float(input('Enter the the Side B: '))
    sideC = float(input('Enter the the Side C: ')) 
    triangle_type = triangleType(sideA,sideB,sideC)
    print(f'The triangle is {triangle_type}')

def main():
    option = int(input('Select an option: \n 1 - Area  \n 2 - Type: \n'))
    if option == 1: 
        option1()
    elif option == 2: 
        option2()  
    else:
        print('Your option is incorrect, chose again.')
        main()

if __name__ == '__main__':
    main()
   