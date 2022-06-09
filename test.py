import pandas as pd

dataset = pd.read_csv("RAW_recipes.csv")
# print(dataset.head())

column = dataset["ingredients"]

#for loop for the column and for loop for every ingredient to find recipes

#split spring for ingredients by space and comma

# split = ingredients.split(', ') - uncomment this later and work it out into algorithm

ingredient_wanted = 'sugar'
wanted = dataset.loc[dataset['ingredients'] == ingredient_wanted]

for i,j in dataset[4:100].iterrows():
    a =j["ingredients"]
    a = a.split(", ")
    
    for ingredient in a:
        if ingredient == ingredient_wanted:
            # print(i) # index of the row that has recipe with available ingredient
            print(dataset['name'][i])