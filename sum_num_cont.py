#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Created: Nov 8, 2022
# Program that takes the users amount and numbers before adding to a sum


def main():

    # Initializing sum variables
    sum_string = ""
    sum_int = 0

    # Gets the total amount of numbers to be added
    tot_num_str = input("Enter the amount of numbers to add: ")

    # Tries casting the total amount of numbers to an integer
    try:
        tot_num_int = int(tot_num_str)

    # Exception thrown if the total number is not an integer
    except:
        print("Inputs must be a positive integer only!")
        input("Please retry input: ")

    if tot_num_int > 0:
        # Loop executed if the total number is greater than 0
        while tot_num_int > 0:
            # Gets the user's number
            user_num_str = input("Input a value to add to the sum: ")

            # Casts user's number to an integer
            try:
                user_num_int = int(user_num_str)
            except:
                print("Invalid input!")
                continue
            else:

                # If there is only one number left
                if tot_num_int == 1:

                    # Tells the user the number added to the sum
                    print(f"Added {user_num_int} to the sum!")

                    # Adds the user's number to the string
                    sum_string += user_num_str

                    # Prints equation
                    print(f"{sum_string}")

                    # Adds the integer form of the number to the sum
                    sum_int += user_num_int

                    # Decrements the amount of remaining numbers
                    tot_num_int -= 1

                    continue

                elif user_num_int == 0:
                    # Tells the user the number added to the sum
                    print(f" 0 was added to sum")
                    continue

                elif user_num_int < 0:
                    # Tells the user the number added to the sum
                    print("Input must be a positive number")
                    continue

                # For numbers greater than 0 and 1
                else:

                    # Tells the user the number added to the sum
                    print(f"{user_num_int} was added to the sum")

                    # Adds the user's number to the string
                    sum_string += user_num_str + " + "

                    # Prints equation
                    print(f"{sum_string}")

                    # Adds the integer form of the number to the sum
                    sum_int += user_num_int

                    # Decrements the amount of remaining numbers
                    tot_num_int -= 1
                    continue
    else:
        print("Input must be greater then 0 to start")
        input("Please retry: ")

    print("")
    print(f"{sum_string} = {sum_int}")
    print(f"Sum = {sum_int}")


if __name__ == "__main__":
    main()
