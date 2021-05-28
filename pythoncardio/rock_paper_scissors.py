import random 

def play(): 
    posibilities = ['paper','rock','scissor']
    
    lifes = 3
    lifes_machine = 3 

    while(lifes > 0 and lifes_machine > 0):
        selection = input(f'Let\'s go! {posibilities} ?: ').lower() 
        n = random.randint(0,2) 
        if selection not in posibilities:
            print('Please, select a correct value (paper,rock or scissor) \n \n ')
            play()  
        else:
            print(f'\n You selected {selection} and the machine selected {posibilities[n]}, so: \n ')
            if posibilities[n] == selection: 
                print('It is a tie!')
            elif selection == 'paper':
                if posibilities[n] == posibilities[1]:
                    print('You win!')
                    lifes_machine -= 1
                else:
                    print('You lose!')
                    lifes -=1
            elif selection == 'rock':
                if posibilities[n] == posibilities[2]:
                    print('You win!')
                    lifes_machine -=1
                else:
                    print('You lose!')
                    lifes -=1
            elif selection == 'scissor':
                if posibilities[n] == posibilities[0]:
                    print('You win!')
                    lifes_machine -=1
                else:
                    print('You lose!')
                    lifes -=1
        print(f'\n Lifes: {lifes}')
        print(f'\n Machine lifes: {lifes_machine} \n ')

    if lifes == 0: 
            print('You lose the game!')
    else:
            print('You win the game!')


def main():
    print('Welcome to a new Game! \n')
    play()
        

if __name__ == '__main__':
    main()