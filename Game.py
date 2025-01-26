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
    symbol = input("Choose your symbol('x', 'o'): ").lower()
    if(symbol == 'x' or symbol =='o'):
      accept = True
    else:
      print("Please enter either 'x' or 'o'")
  

  


