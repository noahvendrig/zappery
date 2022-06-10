#import required modules
import pandas as pd

# self.dataset = pd.read_csv("RAW_recipes.csv")

class RecipeFinder:
    def __init__(self, query):
        self.query = query
        self.user_time = query[1]
        self.found_recipe_indexes = [] # list of the indexes of the matching recipes we will find later
        self.ingredients = ""
        self.Recipes = None
        self.dataset = pd.read_csv("RAW_recipes.csv")
    
    def ProcessInput(self):
        self.ingredients = self.query[0].split(", ") # make a list so we can add multiple ingredients that we have


    
    def Search(self):
        self.ProcessInput()
        for i,j in self.dataset[:10000].iterrows(): # iterate through self.dataset
            ingred_list = j["ingredients"] # line e.g. the cell with the ingredients
            ingred_list = ingred_list.split(", ") # split by comma to get individual ingredients in list
            if len(ingred_list) >= j['n_ingredients']:
                if set(ingred_list).issubset(self.ingredients): # convert to set so and see if recipe is a subset of our ingredients list (returns recipes in which we either have just enough or more than enough ingreds for)
#                     if j['minutes'] <= self.user_time:
                    self.found_recipe_indexes.append(i) # add to list of indexes of recipes we found with the desired ingredient
        self.Recipes = self.FoundRecipes(self.found_recipe_indexes)
        
    class FoundRecipes(): #subclass for found recipes
        def __init__(self, indexes):
#             print(indexes)
            self.all = self.dataset.iloc[indexes] # new dataframe with the recipes that match user's query
            self.ids = [j['id'] for i,j in self.all.iterrows()]
            self.names = [j['name'] for i,j in self.all.iterrows()] # list comprehension to return the names of the recipes we found (similar to the one we used earlier)
            self.minutes = [j['minutes'] for i,j in self.all.iterrows()]
            self.steps = [j['steps'] for i,j in self.all.iterrows()]
            self.n_steps = [j['n_steps'] for i,j in self.all.iterrows()]
        
        def AccessRecipe(self, index):
            id_num = self.ids[index]
            name = self.names[index]
            steps = self.steps[index]
            return id_num, name, steps
        
        def FormatRecipe(self, index):
            id_num = self.ids[index]
            name = self.names[index].title() # capitalise the letters
            name = name.replace("  ", " ")
            minutes = self.minutes[index]
            steps = self.steps[index].split("', '")
            
            print(name, "\n")
            print(f"This recipe takes {minutes} minutes to cook\n")
            
            for step in range(len(steps)): # iterate through amount of steps we have, we do this instead of iterating through the list so we can get the step number
                line = steps[step].capitalize() # capitalise first letter
                line = line.replace("'","").replace(" ,", ",") + "."#replace any leftover quotation marks that might be left (there are some)
                print(f"{step+1}. {line}") # step num = step+1 since index starts at 0, and we dont want step 0
            
            
            
# user_ingreds = 'all-purpose flour, icing sugar, shortening, vanilla, baking powder, sugar, eggs, salt, milk, butter, butter, sugar, vanilla, eggs, all-purpose flour, baking cocoa, baking powder, salt, miniature peppermint patties'
#matches recipe at index 47 jeaness bday cake
user_ingreds = 'butter, lemon, juice of, salt, white pepper, egg yolks, bananas, zappery, all-purpose flour, icing sugar, shortening, vanilla, baking powder, sugar, eggs, salt, milk, butter, butter, sugar, vanilla, eggs, all-purpose flour, baking cocoa, baking powder, salt, miniature peppermint patties' # test cases
minutes = 100
instance = RecipeFinder([user_ingreds, minutes]) #pass it all in one list as one query - ideally receive user input from GUI in a list
instance.Search()
res = instance.Recipes.FormatRecipe(0)
print(res)
            
        
        
        


