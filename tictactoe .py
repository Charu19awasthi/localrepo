row1 =["😃","😃","😃"]
row2 =["😃","😃","😃"]
row3 =["😃","😃","😃"]
print("lets play cross a tic tac toe game")
print(f"{row1}\n {row2}\n{row3}")
final_matrix= [row1,row2,row3]
print("1st player = x \n 2nd player = 0")
y= "notdone"
player1=input("enter 1st player name")
player2=input("enter 2nd player name")
while (y!="done"):
   print(f"{player1} chance")
   position= input("enter position where you want to add x")
   rowselected= final_matrix [int(position[0])-1]
   rowselected[int(position[1])-1]= 'x'   
   print(f"{final_matrix[0]}\n {final_matrix[1]}\n {final_matrix[2]}")
   #player2
   print(f"{player2}chance")
   position_2= input("enter position where you want to add 0")
   rowselected= final_matrix[int(position_2[0])-1]
   rowselected[int(position_2[1])-1]= '0'   
   print(f"{final_matrix[0]}\n {final_matrix[1]}\n {final_matrix[2]}")
l=['x','x','x']
l1=['0','0','0']
condition_1 = [final_matrix[0][1],final_matrix[1][1],final_matrix[2][1]]
condition_2 = [final_matrix[0][0],final_matrix[1][1],final_matrix[2][2]]
condition_3 = [final_matrix[0][2],final_matrix[1][1],final_matrix[2][0]]
if (final_matrix[1]==l or condition_1==l or condition_2==l or condition_3==l):
        y="done"
        print(f"{player1} wins")
elif (final_matrix[1] ==l1 or condition_1==l1 or condition_2==l1 or condition_3==l1):
        y="done"
        print(f"{player2} wins")

       