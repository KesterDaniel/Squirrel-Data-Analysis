import pandas

data = pandas.read_csv("Squirrel Census Data.csv")

Black_Squirrels = data[data["Primary Fur Color"] == "Black"]
Gray_Squirrels = data[data["Primary Fur Color"] == "Gray"]
Cinnamon_Squirrels = data[data["Primary Fur Color"] == "Cinnamon"]

Num_Black_Squirrels = sum(Black_Squirrels["Hectare Squirrel Number"])
Num_Gray_Squirrels = sum(Gray_Squirrels["Hectare Squirrel Number"])
Num_Cinnamon_Squirrels = sum(Cinnamon_Squirrels["Hectare Squirrel Number"])

squirrel_count_data = {
    "Fur_Color": ["Black", "Gray", "Cinnamon"],
    "Count": [Num_Black_Squirrels, Num_Gray_Squirrels, Num_Cinnamon_Squirrels]
}


