
# import pandas 

# data = pandas.read_csv("weather_data.csv")
# print(data)


# temp_list = data["temp"].to_list()
# print(len(temp_list))



# print(data["temp"].mean())
# print(data["temp"].max())

#Obtener datos de una fila
#print(data[data.day == "Monday"])

#obtener la data en columans
# print(data["condition"])
# print(data.condition)

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#crear un dataframe desde un diccionario
# # data_dict = {
# #     "students": ["Amy", "James", "Angela"],
# #     "scores": [76, 56, 65]
# # }
# # data = pandas.DataFrame(data_dict)
# # data.to_csv("new_data.csv")