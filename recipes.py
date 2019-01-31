import random
import pprint 
#Define Recipes as a dictionary nested in a list.
recipes = [
	{"Meatballs and Pasta:": 
	 	["Meatballs", "Pasta", "Pasta Sauce"]},
	{"Fried Chicken:": 
	 	["Chicken Breast", "Buttermilk", "Seasoning"]},
	{"Dish 3:": 
	 	["Ingredient 1", "Ingredient 2", "Ingredient 3"]}	
	]

#Prints all dishes from the "recipes" variable
def printDishes():
	print("===All Dishes===")
	#Outer loop for items in the list
	for i in recipes:
		#Inner loop for dictionary key==dish and values==ingredient
		for dish in i.items(): 
			print("{}".format(dish))

#Uses random.sameple() and a passed interger to present a selection
def pickDish(sampleSize):
	return(random.sample(recipes, sampleSize))	

#Takes a param "output" to format the text nicely to return for a print
#def formatOutput(output):
#	return()	

if __name__ == "__main__":
	#print(pickDish(2))
	pprint.pprint(pickDish(2), width=1)
	#printDishes()
	#print("===Dish Picks===")
	#print(pickDish(1))
	#print("===Dish Picks===")
	#print(pickDish(2))
	#print("===Dish Picks===")
	#print(pickDish(3))
