# Forrest Siminoe
# UWYO COSC 1010
# 9/29/24
# Lab 03 
# Lab Section: 13

print("Part One ------------------------------------------------------------------")
states = ["Wyoming", "Colorado","Montana"]
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
#print the entire list
print(states)

#now print the first element in the list
print(states[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(states[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
message = f"{states[1]} is south of {states[0]}"
print(message)
print(states[1],"is south of",states[0])

print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
states.append("Washington")
states.append("Oregon")
states.append("California")
print(states)
#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
states[-2] = "Maine"
print(states)
#Insert the state Texas to be the third element in the list, again printing your list
states.insert(2,"Texas")
print(states)

#Using the `del` statement remove the fourth item from the list, print your list 
del states[3]
print(states)
#Remove Texas using its value, print the list
states.remove("Texas")
print(states)
print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print(states)
print(sorted(states))

#Permanently sort your list in reverse order, printing it out
states.sort()
print(states)
#Using the reverse method reverse the list and print it
states.sort(reverse=True)
print(states)