'''temp = float(input('What is the current temperature ? '))'''

def temp_comment(temp):
    if 60 < temp < 90:
        print("It is a Warm day")
    elif temp >= 90:
        print("It is a Hot day")
    else:
        print("It is a Cold day")

var = " "
while var != "End" :  # This constructs an infinite loop
    temp_comment(float(input('What is the current temperature ? ')))

print "Good bye!"


