#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.

#First I added newline characters to each prompt so that the user input should be on a new line. While not necessarily a syntax error, it makes the program look nicer.
#Next, I added an input prompt for the third test score and named it test3.
#Finally, I changed the input function to int so that the user input would be converted to an integer. This is necessary because the average is calculated using the test scores, which are integers.

test1 = int(input('Enter the score for test 1:\n'))
test2 = int(input('Enter the score for test 2:\n'))
test3 = int(input('Enter the score for test 3:\n'))
# Calculate the average test score.

#I enclosed the test scores in parentheses so that they would be added together before being divided by 3.

average = (test1 + test2 + test3) / 3
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.

#I changed the if statement so that it would compare the average to the high score variable. I did this by writing the variable name in all caps to match the stored variable.
#I removed the print statement that printed 'That is a great average' regardless of score and added that message to the if statement so that it would only print if the average was greater than or equal to the high score.
if average >= HIGH_SCORE:
    print('Congratulations! That is a great average!')

# Wait for user input to proceed to the next section
input('Press Enter to continue...')


#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

#The following is my first quick code. I followed that with a more safe code to control for user errors and to be able to easily adjust the programs for more rectangles.

#len_rect_1 = int(input('Please enter the length of the first rectangle:\n'))
#wid_rect_1 = int(input('Please enter the width of the first rectangle:\n'))
#len_rect_2 = int(input('Please enter the length of the second rectangle:\n'))
#wid_rect_2 = int(input('Please enter the width of the second rectangle:\n'))

#area_rect_1 = len_rect_1 * wid_rect_1
#area_rect_2 = len_rect_2 * wid_rect_2
#combined_area = area_rect_1 + area_rect_2

#print('The area of the first rectangle is', area_rect_1)
#print('The area of the second rectangle is', area_rect_2)
#print('The combined area of both rectangles is', combined_area)

rectangles = []
for i in range(2):
    while True:
        try:
            length = int(input(f'Please enter the length of rectangle {i+1}:\n'))
            width = int(input(f'Please enter the width of rectangle {i+1}:\n'))
            break
        except ValueError:
            print('Please enter integers only.')
    rectangles.append((length, width))

# Calculate and print the area of both rectangles
for i, (length, width) in enumerate(rectangles):
    area = length * width
    print('The area of rectangle {i+1} is {area}')

# Wait for user input to proceed to the next section
input('Press Enter to continue...')

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

#Here, I again allowed for user error by using a while loop to prompt the user to enter an integer for their age.

name = input('Please enter your first name:\n')

for _ in range(3):
    try:
        age = int(input('Please enter your age using numbers:\n'))
        break
    except ValueError:
        print('Invalid input. Please enter an integer.')
else:
    print('Invalid input three times. Goodbye.')

print('Happy birthday,', name + '! You are', age, 'years old today!')


