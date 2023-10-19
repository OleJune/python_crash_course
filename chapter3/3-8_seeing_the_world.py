places = ['iceland', 'australia', 'canada', 'spain', 'japan']
print(places)    #original order

print(sorted(places))  #sorting in alphabetical order TEMPORARILY
print(places)    #original order

print(sorted(places,reverse=True))  #sorting in reverse alphabetical order TEMPORARILY
print(places)   #original order

places.reverse()   #sorting in reverse order PERMANENTLY 
print(places)    #reverse order

places.reverse()	#sorting in reverse order PERMANENTLY 
print(places)	#back to original order

places.sort()	#sorting in alphabetical order PERMANENTLY 
print(places)	#alphabetical order

places.sort(reverse=True)	#sorting in reverse alphabetical order PERMANENTLY
print(places)	#reverse alphabetical order
