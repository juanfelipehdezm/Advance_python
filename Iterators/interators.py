from collections import namedtuple

def cast_datatypes(data_type:str, value: str):

    if data_type == "DOUBLE":
        return float(value)
    elif data_type == "INT":
        return int(value)
    else:
        return value

def cast_row(data_types, data_row):
    return [cast_datatypes(data_type, value)
            for data_type, value in zip(data_types, data_row)]

cars = []

with open("G:\My Drive\Big Data\Advance Python\Iterators\cars.csv") as file:

    file_iterator = iter(file)
    #instead of using a for loop to extract the first and the second row, we use the iterator which allow us
    #to go one by one, and after that, we can iterate over the rest
    headers = next(file_iterator).strip("\n").split(";")
    Car_tuple = namedtuple("Car_item", headers)
    
    data_types = next(file_iterator).strip("\n").split(";")

    for line in file_iterator: #we iter over the remaining row
        data_row = line.strip("\n").split(";")
        data_casted = cast_row(data_types, data_row)

        car = Car_tuple(*data_casted)

        cars.append(car)


print(cars[:11])

