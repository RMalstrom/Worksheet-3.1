"""
Richard Malstrom
CMSC-1380

This program will use loops and arrays in order to generate a randomized password.

Date last modified: 10.22.2024
"""
import random # Import the RNG library for all of our numbers.

# First declare the lists we will pull from

passwords = [] # Initialize empty array that will hold passwords

words = ["Apple","Beach","Brain","Bread","Brush","Chair","Chest","Chord","Click",
"Clock","Cloud","Dance","Diary","Drink","Earth","Flute","Fruit","Ghost","Grape","Green",
"Happy","Heart","House","Juice","Light","Money","Music","Party","Pizza","Plant","Radio",
"River","Salad","Sheep","Shoes","Smile","Snack","Snake","Spice","Spoon","Storm","Table",
"Toast","Tiger","Train","Water","Whale","Wheel","Woman","World"]

specChar = "!@#$%&*+:?~;" # Initialize list of special characters


passCounter = 0 # Initialize an iterator to keep track of the number of passwords generated

while passCounter < 21: # Loops through 20 times
    password = specChar[random.randint(0,11)] + words[random.randint(0,49)] + specChar[random.randint(0,11)] + str(random.randint(1000, 6000) % 5000 + 1001) + specChar[random.randint(0,11)]
    passwords.append(password) # Add new generated password to list of passwords
    passCounter = passCounter + 1 # Add one to the number of passwords generated

print(passwords) # Print the finished list of passwords