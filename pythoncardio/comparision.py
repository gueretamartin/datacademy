def main():
    l = float(input('Input your low boundary: '))
    h = float(input('Input your high boundary: '))
    is_between = False
    while(is_between == False):  
        c = float(input('Input your comparision value: ')) 
        if l <= c <= h:
             print(f'Your comparision value: {c} is between boundaries: [{l};{h}]')
             is_between = True
        else:
            print(f'Your comparision value: {c} is not between boundaries: [{l};{h}]')
            
if __name__ == '__main__':
    main()