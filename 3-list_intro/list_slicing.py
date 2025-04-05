
players = ['charles,' 'martina','michael','florence','eli','john','mark','marie']
print(players[1])
print(players[0:4]) #partial list,from 0 to 3rd index
first3_players = players[0:4]
print(players[3:6])

#['john','mark',marie']
print(players[5:8])

print(players[:]) #whole list,usually to copy the list
copy_players = players[:]
players2 = players #this is not a copy ,second reference to the list
print(copy_players)
print(players2)

print("------------looping ---------")