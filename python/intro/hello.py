
# celsius = input()

# fahrenheit = (int(celsius)*(9/5)) + 32

# print (f"The result is: {fahrenheit}.")

# celsius = input()

# fahrenheit = (celsius*9/5) + 32

# print (f"The result is: {fahrenheit}.")
# # =================================================

# arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]

# i = 0

# while (i<arr.len() -1) and (arr[i] < arr[i+1]):
#      i += 1
# print(i)
#     arr[i] = arr[i+1]
#     arr[i+1] = arr[i]

arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]

i = 0

while i < len(arr) -1:

     if arr[i] > arr[i+1]:
          arr[i], arr[i+1] = arr[i+1], arr[i]
          
     i += 1

print(arr)


# arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]

# i = 0

# while (i<len(arr) -1) and (arr[i] < arr[i+1]):
#      arr[i] = arr[i+1]
#      arr[i+1] = arr[i]
#      i += 1
# print(arr)
