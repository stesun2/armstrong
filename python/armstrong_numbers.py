# How can you make this more scalable and reusable later?
# Testing

# ------ PSEUDOCODE ------
# Write function/method that takes in an argument that is a RANGE OF NUMBERS
# Create an ANSWER var that is an array
# ITERATE/LOOP through the range of number
# Convert each num into a string
# Create var called EXPONENT == length of string number
# Create var called SUM and have its initial value = 0
# Create a TEMP var that stores a number to extract each individual integer from the number
# Create a WHILE LOOP where TEMP is GREATER THAN 0
# Find the remainder of the TEMP by using MOD 10 to last int and store it into a var called DIGIT
# Take the DIGIT var and take the power of the EXPONENT variable and ADD to the SUM
# reassign the TEMP var to the floor of the TEMP / 10
# Write an IF STATEMENT that checks if NUM is equal to SUM and if it's true, add it to the ANSWER var

# Tom's Solution Work along
def find_armstrong_numbers(numbers):
    answer = []
    for num in numbers:
        exponent = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** exponent
            temp //= 10  # Taking the floor
        if num == sum:
            answer.append(num)
    return answer

print(find_armstrong_numbers(list(range(0,999))))