#List: 
squares = [x**2 for x in range(5)]
#Dictionary: 
square_dict = {x: x**2 for x in range(5)}
#Generator: 
square_gen = (x**2 for x in range(5)) #(generates values one at a time, saving memory).

print("List of squares:", squares)
print("Dictionary of squares:", square_dict)
print("Generator of squares:", list(square_gen))
print(square_dict.keys())