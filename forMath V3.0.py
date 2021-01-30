import math
print("Hello, the application you entered finds the square , cube or square root of the number you want, and also checks whether it is a double . I Certainly Didn't Do This App To Use It On My Math Exam. ")

def main():


    print("")

    print("Enter a Number for Calculate ")

    number = int(input())
    print("")
    def cube(number):
        return number*number*number

    def square(number):
        return number*number

    sq = math.sqrt(number)
    print('Square Root of Your Number : '+str(sq))
    print('Cube of Your Number : ' + str(cube(number)))
    print('Square of Your Number : ' + str(square(number)))
    print("")
    if number % 2 == 0:
        print("This is a Double Number")
    else:
        print("That's Not Double Number")
    print("")
    res = input("Do You Want Return to Start ? Type Yes or No ")

    if res == "Yes":
        main()
    else:
        print("See You Later")
        exit()

main()


