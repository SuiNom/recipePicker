from flask import Flask
import random

app = Flask(__name__)
#Define Recipes as a dictionary nested in a list

##Variable - Python List of recipes
###Dictionary
####Key = Dish Name
#####Value = Python List of ingredients
recipes = [
	{"Meatballs and Pasta":
		["Meatballs", "Pasta", "Pasta Sauce"]},
	{"Fried Chicken":
		["Chicken Breast", "Buttermilk", "Seasoning"]},
	{"Dish 3":
		["Ingredient 1", "Ingredient 2", "Ingredient 3"]},
	{"Jacket Potato":
		["Potato", "Fillings"]}
	]

#Uses random.sameple() and a passed interger to present a selection
def pickDish(sampleSize):
	return(random.sample(recipes, sampleSize))

#Format the text nicely and print - calls pickDish
@app.route("/")
def displayDish():
    tmp = ""
    for i in pickDish(3): #Call pickDish(), convert output into a string, then remove brackets, etc then print.
        tmp += str(i).translate(None, "([{'}])") + "<br>"
    return("<h1>" + tmp + "</h1>")


if __name__ == "__main__":
	app.run(debug=True)
#===Default Flask Test App===#
#@app.route("/")
#def hello():
#    return "Hello World!"
