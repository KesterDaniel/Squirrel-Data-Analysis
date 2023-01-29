import pandas

data = pandas.read_csv("Squirrel Census Data.csv")

Black_Squirrels = data[data["Primary Fur Color"] == "Black"]
Gray_Squirrels = data[data["Primary Fur Color"] == "Gray"]
Cinnamon_Squirrels = data[data["Primary Fur Color"] == "Cinnamon"]


