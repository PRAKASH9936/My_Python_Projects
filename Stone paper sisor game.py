player_1=(input("Enter the name of the first player"))
player_2=(input("Enter the name of the second player"))

turn_player_1=(input("First Player:- Enter 'Stone', 'Paper' or 'Sisor'"))
turn_player_2=(input("Second Player:- Enter 'Stone', 'Paper' or 'Sisor'"))

if(turn_player_1=='Stone')and(turn_player_2=='Stone'):
    print("Tie")
    
elif(turn_player_1=='Stone')and(turn_player_2=='Paper'):
    print(player_2,"Win!!!")
    
elif(turn_player_1=='Stone')and(turn_player_2=='Sisor'):
    print(player_1,"Win!!!")
    
    
elif(turn_player_1=='Paper')and(turn_player_2=='Stone'):
    print(player_1,"win!!!")
    
elif(turn_player_1=='Paper')and(turn_player_2=='Paper'):
    print("Tie")
    
elif(turn_player_1=='Paper')and(turn_player_2=='Sisor'):
    print(player_2,"Win!!!")
    
    
elif(turn_player_1=='Sisor')and(turn_player_2=='Stone'):
    print(player_2,"Win!!!")
    
elif(turn_player_1=='Sisor')and(turn_player_2=='Paper'):
    print(player_1,"Win!!!") 
    
elif(turn_player_1=='Sisor')and(turn_player_2=='Sisor'):
    print("Tie")  
          