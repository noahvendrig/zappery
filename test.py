import pandas as pd

dataset = pd.read_csv("RAW_recipes.csv")
# print(dataset.head())

column = dataset["ingredients"]

#for loop for the column and for loop for every ingredient to find recipes

#split spring for ingredients by space and comma

# split = ingredients.split(', ') - uncomment this later and work it out into algorithm
ingredient_wanted = 'sugar'
wanted = dataset.loc[dataset['ingredients'] == ingredient_wanted]

for i,j in dataset[4:8].iterrows():
    a =j["ingredients"]
    a = a.split(", ")

    for n in a:
        # if "'" in n:
        # n.replace("'", "")
        # print(a)
        print(n.split()[0])

    # for ingredient in a:
    #     print(ingredient)
    #     if ingredient == ingredient_wanted:
    #         print(i)
