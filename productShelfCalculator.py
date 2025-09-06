# Authors: Musa Paracha and Mohammad Abdullah
# Date: 12/11/2024
# Purpose: To find the number of ways to arrange products in a shelf

import math
import random

def generate_product_name(category):
    random_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    product_name = ''.join(random.choices(random_characters, k=5))
    return category + " " + product_name


def get_user_input():
    products_int = -1
    while products_int < 0:
        products_int = int(input("Please enter the number of products you have:"))
        if products_int < 0:
            print("Please enter a number greater than 0")
    repeats_bool = ''
    while repeats_bool.upper() != 'Y' and repeats_bool.upper() != 'N':
        repeats_bool = input("Do you want repeats(Y or N):")
        if repeats_bool.upper() != 'Y' and repeats_bool.upper() != 'N':
            print("Please enter either Y or N")
    number_of_shelfs = -1
    while number_of_shelfs < 0:
        number_of_shelfs = int(input("Please enter the number of shelves you have:"))
        if number_of_shelfs < 0:
            print("Please enter a number greater than 0")
    categories_int = -1
    while categories_int < 0:
        categories_int = int(input("Please enter how many categories you want from 1-5:"))
        if categories_int < 0 or categories_int > 5:
            print("Please enter a number from 1 to 5")
    return products_int, repeats_bool, number_of_shelfs, categories_int


def generate_products(products_int, categories_int):
    categories_list = ["Electronics", "Clothing", "Sports", "Food", "Drink"]
    products = []
    for i in range(products_int):
        category = random.choice(categories_list)
        products.append(generate_product_name(category))
    return products

def calculate_arrangement(products_int, repeats_bool, number_of_shelfs):
    arrangements_int = 0
    SHELF_SPOTS = 5
    total_spots = SHELF_SPOTS * number_of_shelfs
    if repeats_bool == 'Y':
        arrangements_int = products_int ** total_spots
    else:
        if products_int >= total_spots:
            arrangements_int = (math.factorial(products_int)/math.factorial(products_int - total_spots))
        else: print("You can't fill", total_spots,"with", products_int,"products without repeating")

    return arrangements_int

def display_shelfs(products_int,categories_int, number_of_shelfs):
    shelf_index = 0
    SHELF_SPOTS = 5
    for i in range(number_of_shelfs):
        print("Shelf" + " " + str(i + 1) + ': ', end = '')
        shelf = random.sample(generate_products(products_int, categories_int), SHELF_SPOTS)
        products_display = " | ".join(shelf)
        print(products_display)

def main():
    products_int, repeats_bool, number_of_shelfs, categories_int = get_user_input()
    arrangements_int = calculate_arrangement(products_int, repeats_bool, number_of_shelfs)
    products = generate_products(products_int, categories_int)
    print("The number of arrangments you can have is:", arrangements_int)
    print("")
    print("This is an example of how you can arrange it")
    display_shelfs(products_int,categories_int, number_of_shelfs)

main()
