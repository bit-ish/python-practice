# with open('./weather_data.csv')as weather:
#     aa=weather.readlines()
# print(aa)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data=csv.reader(weather_data)
#     temperature=[]
# #     for row in data:
# #         print(row
# #               )
# #         if row[1]!="temp":
# #             temperature.append(int (row[1]))
# # print(temperature)
#
#
import pandas
# data=pandas.read_csv("weather_data.csv")
# # print(data)
# data_temp=(data['temp'].to_list())
# # sum=0
# # for a in data_temp:
# #     sum+=a
# # print(f"average temperature for the past week is {round(sum/(len(data_temp)),1)} degrees.")
# # print(round(sum(data_temp)/len(data_temp),2))
# # print(data['temp'].mean())
# # print(data['temp'].max())
#
# # data_dict=data.to_dict()
# #
# # print(data[data.day=="Friday"])
# #
# # print(data[data.temp==data.temp.max()])
#
# monday=data[data.day == "Monday"]
# monday_tempt= (monday.temp * 1.8) + 32
# print(monday_tempt)
grey=0
red=0
black=0
squirrel_data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250609.csv")
fur=squirrel_data["Primary Fur Color"]
# for color in fur:
#     if color=="Gray":
#         grey+=1
#         dict[f"{color}"]=grey
#     if color=="Cinnamon":
#         red+=1
#         dict[f"{color}"] = red
#     if color=="Black":
#         black+=1
#         dict[f"{color}"] = black

squirrel_grey=squirrel_data[fur=="Gray"]
grey_count=len(squirrel_grey)
red_count=len(squirrel_data[squirrel_data["Primary Fur Color"]=="Cinnamon"])
black_count=len(squirrel_data[squirrel_data["Primary Fur Color"]=="Black"])

dict={
    "Fur Color":['Red','Black','Gray'],
    "Count":[red_count,black_count,grey_count]
}

# df=pandas.DataFrame(dict)
# final_csv=df.to_csv('output.csv',index=False)
# # print(final_csv)
print(dict)
dc=pandas.DataFrame(dict)
dict_csv=dc.to_csv("squirrel.csv")

aaa=pandas.read_csv("squirrel.csv")

ab=aaa[aaa["Fur Color"]=="Black"]

print(ab)