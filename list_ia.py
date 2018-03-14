name = "Isa"
subjects = ["Math","French","English","Science"]

print("My name is " + name)

#print(subjects)

for i in subjects:
    print("One of my classes is " + i)

tvshows = ["Gilmore Girls", "Friends", "How I met your mother"]

for i in tvshows:
    if i == "Gilmore Girls":
        print(i + " is the best show ever!")
    elif i == "Friends":
        print(i + " is so funny!")
    elif i == "How I met your mother":
        print("So mad its not on Netflix anymore!")


teams = []

while True:
    print("Who are your facvorite teams? Type 'end to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        teams.append(answer)

for i in teams:
    print("One of your favorite teams is " + i)
    
        
        

    
   
    
