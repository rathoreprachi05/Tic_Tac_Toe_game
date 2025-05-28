def print_board(list):
    print(list[0][0], "|", list[0][1], "|", list[0][2])
    print("- + - + -")
    print(list[1][0], "|", list[1][1], "|", list[1][2])
    print("- + - + -")
    print(list[2][0], "|", list[2][1], "|", list[2][2])

quit = False
while(quit == False):

    
    list = [[" "," "," "], [" "," "," "], [" "," "," "]]

    accept = False
    while(accept == False):

        p_symbol = input("Choose your symbol('x', 'o'): ").lower()

        if(symbol == 'x' or symbol =='o'):
            accept = True
        else:
            print("Please enter either 'x' or 'o'")

        if(p_symbol == 'x'):
            c_symbol = 'o'
        else:
            c_symbol = 'x'


    
    for i in range(1,5,1):
        user_moves()
        computer_moves()
        print_board(list)

        if(list[0][0] == list[0][1] == list[0][2] == p_symbol or \
           list[1][0] == list[1][1] == list[1][2] == p_symbol or \
           list[2][0] == list[2][1] == list[2][2] == p_symbol or \
           list[0][0] == list[1][0] == list[2][0] == p_symbol or \
           list[0][1] == list[1][1] == list[2][1] == p_symbol or \
           list[0][2] == list[1][2] == list[2][2] == p_symbol or \
           list[0][0] == list[1][1] == list[2][2] == p_symbol or \
           list[2][0] == list[1][1] == list[0][2] == p_symbol) :
            print("Yay! You won!")
            ask = input("Do you want to play the game again or do you want to exit?")

#------------------------------------------------------------------
