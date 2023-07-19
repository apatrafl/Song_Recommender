import sys
import random as random
import pandas as pd

data = pd.read_csv("songs.csv")

#intiializing all the lists below
index = data.head(1994)
Index_List = list(index["Index"])
#print(Index_List)

title = data.head(1994)
Title_List = list(title["Title"])
#print(Title_List)

artist = data.head(1994)
Artist_List = list(artist["Artist"])
#print(Artist_List)

genre = data.head(1994)
Genre_List = list(genre["Top Genre"])
#print(Genre_List)

year = data.head(1994)
Year_List = list(year["Year"])
#print(Year_List)

energy = data.head(1994)
Energy_List = list(energy["Energy"])
#print(Energy_List)

danceability = data.head(1994)
Danceability_List = list(danceability["Danceability"])
#print(Danceability_List)

valence = data.head(1994)
Valence_List = list(valence["Valence"])
#print(Valence_List)

duration = data.head(1994)
Duration_List = list(duration["Length (Duration)"])
#print(Duration_List)

popularity = data.head(1994)
Popularity_List = list(popularity["Popularity"])
#print(Popularity_List)

bpm = data.head(1994)
Bpm_List = list(bpm["Beats Per Minute (BPM)"])
#print(Bpm_List)

def quiz():
    reclist1 = []
    print("Question #1")
    print("Would you prefer a happier or sadder song? ")
    Q1 = "sadder" #input("Would you prefer a happier or sadder song? ")
    if Q1 == "happier":
        for i in range(len(Valence_List)):
            if Valence_List[i]>55:
                reclist1.append(Title_List[i])
    elif Q1 == "sadder":
        for i in range(len(Valence_List)):
            if Valence_List[i] <= 55:
                reclist1.append(Title_List[i])
    else:
        print("Invalid Input")
        sys.exit()
    reclist2 = []
    print("\nQuestion #2")
    print("Would you want a low or high energy song?")
    Q2 = "low" #input("Would you want a low or high energy song?")
    if Q2 == "high":
        for i in range(len(Energy_List)):
            if Energy_List[i]>45:
                reclist2.append(Title_List[i])
               
    elif Q2 == "low":
        for i in range(len(Energy_List)):
            if Energy_List[i] <= 45:
                reclist2.append(Title_List[i])
    else:
        print("Invalid Input")
        sys.exit()
        
    reclist3 = []
    print("\nQuestion #3")
    print("Are you up to dance? ")
    Q3 = "no" #input("Are you up to dance? ")
    if Q3 == "yes":
        for i in range (len(Danceability_List)):
            if Danceability_List[i] >= 69:
                reclist3.append(Title_List[i])
    elif Q3 == "no":
        for i in range (len(Danceability_List)):
            if Danceability_List[i]<69:
                reclist3.append(Title_List[i])
    else:
        print("Invalid Input")
        sys.exit()
        
    reclist4 = []
    print("\nQuestion #4")
    print("Would you like a slow or fast song? ")
    Q4 = "slow" #input("Would you like a slow or fast song? ")
    if Q4 == "fast":
        for i in range (len(Bpm_List)):
            if Bpm_List[i] >= 101:
                reclist4.append(Title_List[i])
    elif Q4 == "slow":
        for i in range (len(Bpm_List)):
            if Bpm_List[i]<101:
                reclist4.append(Title_List[i])
    else:
        print("Invalid Input")
        sys.exit()
    reclist5 = []
    print("\nQuestion #5")
    print("Would you like a short, medium, or long song? ")
    Q5 = "medium" #input("Would you like a short, medium, or long song? ")
    if Q5 == "short":
        for i in range (len(Duration_List)):
            if 93 <= Duration_List[i] < 224:
                reclist5.append(Title_List[i])
    elif Q5 == "medium":
        for i in range (len(Duration_List)):
            if 224 <= Duration_List[i]<356:
                reclist5.append(Title_List[i])
    elif Q5 == "long":
        for i in range (len(Duration_List)):
            if Duration_List[i]>=356:
                reclist5.append(Title_List[i])
    else:
        print("Invalid Input")
        sys.exit()
                
    reclist6 = []
    print("\nQuestion #6")
    print("Do you want popular or underground music? ")
    Q6 = "popular" #input("Do you want popular or underground music? ")
    if Q6 == "popular":
        for i in range (len(Popularity_List)):
            if Popularity_List[i] > 64:
                reclist6.append(Title_List[i])
    elif Q6 == "underground":
        for i in range (len(Popularity_List)):
            if Popularity_List[i] <= 64:
                reclist6.append(Title_List[i])
    else:
        print("Invalid Input")
        sys.exit()
    request = 1 #input("How many songs do you want? ")
    potentials = []
    for j in range(1994):
        if (Title_List[j] in reclist1) and (Title_List[j] in reclist2) and (Title_List[j] in reclist3) and (Title_List[j] in reclist4) and (Title_List[j] in reclist5) and (Title_List[j] in reclist6):
            potentials.append(Title_List[j])
            potentials = list(dict.fromkeys(potentials))
            
    if request > len(potentials):
        print("We don't have that many songs for you! This is what we can do! ")
        while request > len(potentials):
            request -= request
    if len(potentials) == 0:
        print("Hmm, you're picky! Try to expand your music taste and try something different?")
        sys.exit()
        
    finalsong = random.sample(potentials, request)

    print((finalsong[0]), sep = ", ")
    asha = Title_List.index(finalsong[0])
    print(Artist_List[asha])
    print(Year_List[asha])
    
    
    satisfy = "yes" #input("\nAre these songs okay?")
    if satisfy == "yes":
        print("Great! Have a good listening experience!")
        sys.exit()
    elif satisfy == "no":
        again = "no" #input("I'm sorry to hear that. Would you like another list? ")
        if again == 'no':
            print("Sorry!")
            sys.exit()
        elif again == "yes":
            print((random.sample(potentials, request)), sep = ", ")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
            
#actual printing below

print("Hi there! Welcome to my music recommender!")
print("If you'd like a random playlist, please type 1. If you'd like a curated playlist, type 2 to answer some questions! ")
choice = 2 #input("What's your choice? ")

if choice == 1:
    playlist = []
    print("Gotcha! Let's do this!")
    number = 10 #input(int("How many songs? "))
    if (number > 1994):
        print("invalid song number, do you really need that many?")
    else:
        for x in range(number):
            p = random.randint(0,1993)
            randtitle = Title_List[p]
            randartist = Artist_List[p]
            randyear = Year_List[p]
            randgenre = Genre_List[p]
            print((randtitle, randartist, randyear, randgenre), sep = ", ")
            print("\n")
           
elif choice == 2:
    print("Great! Let's get this quiz started!")
    print("\n")
    quiz()

else:
    print("Invalid Choice") 
