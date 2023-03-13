maxCalories = 1500 

items= {
    "pizza":700,
    "hotdog": 450,
    "salad":400,
    "burger":650,
    "meatballs":1600,
    "sandwich":500
}


newItems ={}
for key in items.keys():
    if items[key] <= maxCalories:
        newItems[key]=items[key]


print(type(newItems))
