"""Task 14: Compulsory Task 1:"""

# In this program, we are giving the user a choice of holiday destinations, rental and hotel
# We are giving the user the choice to choose and giving an overall cost for the holiday as well as breaking it down
destinations = ["Barcelona", "Madrid", "London", "Dubai", "Tokyo", "Paris"]

print("Welcome to HyperFlights, one stop app to book your flight, hotel and rentals.")
print("Please choose a city from the following list:", ", ".join(destinations))

# I have used defensive programming here to ensure that the program does not crash
# I used 3 different 'while True' loops, if there is a wrong input then only one will reset than all of them
# They get the inputs from the user for destination, number of nights and rental days
# I have made sure that even if zero is input, the program will not crash
while True:
    city_flight = input("Please enter one of the cities from the list that you will be flying to: ").capitalize()
    if city_flight in destinations:
        break
    else:
        print("Invalid input! Please enter a city from the list.")

while True:
    try:
        num_nights = int(input("Please enter the number of nights you will be staying: "))
        try:
            if num_nights == 0:
                raise ValueError("You can not stay zero (0) nights")
        except ValueError as zero:
            print(zero)
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

while True:
    try:
        rental_days = int(input("Please enter the number of days you will be hiring a car for: "))
        try:
            if rental_days == 0:
                raise ValueError("You can not rent for zero (0) days")
        except ValueError as zero:
            print(zero)
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")


# We have 3 functions below for hotel cost, rental cost and flight cost
# I have set a price for all of them myself randomly
def hotel_cost(nights):
    return 85.50 * nights

def rental_cost(days):
    return 200 * days

def flight_cost(destination):
    if destination == 'Barcelona':
        return 499.89
    elif destination == 'Madrid':
        return 350.99
    elif destination == 'London':
        return 100.50
    elif destination == 'Dubai':
        return 750.50
    elif destination == 'Tokyo':
        return 990
    elif destination == 'Paris':
        return 250

hotel_cost = hotel_cost(num_nights)
rental_cost = rental_cost(rental_days)
flight_cost = flight_cost(city_flight)

# This part is extra to the program
# I decided to input this as it displays the cost of hotel/rental per night/day
# This would be good info for the user
hotel_per_night = hotel_cost / num_nights
rental_per_day = rental_cost / rental_days

# The code below adds up the hotel + flight and rental to work out a total cost
holiday_cost = hotel_cost + flight_cost + rental_cost

# Here we are printing the necessary information for the user
# Including plane cost,  hotel cost, rental cost and an extra per day/night for the hotel and rental in brackets
# This then rounds up shows the user the total holiday cost for everything
print("The total plane cost is: £{:.2f}".format(flight_cost))
print("The total hotel cost is: £{:.2f} ({:.2f} per night)".format(hotel_cost, hotel_per_night))
print("The total rental cost is: £{:.2f} ({:.2f} per day)".format(rental_cost, rental_per_day))
print("The total cost of your holiday is: £{:.2f}".format(holiday_cost))
