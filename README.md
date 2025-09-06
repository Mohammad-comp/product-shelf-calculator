# 🏪 Product Shelf Arrangement Calculator

A Python program that calculates the number of ways to arrange products on retail shelves using combinatorial mathematics.

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Python](https://img.shields.io/badge/code%20style-python-blue.svg)](https://www.python.org)

## 👥 Authors
- **Mohammad Abdullah (mabdullah.2118@gmail.com)**
- **Musa Paracha (musa.m.paracha@gmail.com)**

*Date: December 11, 2024*

## 📖 Overview

This interactive Python application helps retailers, store managers, and students understand product placement combinatorics. It calculates how many different ways products can be arranged across multiple shelves and generates visual examples to demonstrate various arrangements.

Perfect for:
- **Retail Planning**: Optimize product displays
- **Mathematics Education**: Learn combinatorics and permutations
- **Inventory Management**: Understand arrangement possibilities

## ✨ Features

- 🧮 **Combinatorial Calculations**: Supports arrangements with and without repetition
- 🏬 **Multi-Shelf Support**: Configure multiple shelves (5 products per shelf)
- 🎲 **Random Product Generation**: Creates products from 5 categories
- 👀 **Visual Examples**: See how your arrangement might look
- ✅ **Input Validation**: Robust error handling for all user inputs
- 📊 **Mathematical Accuracy**: Uses factorial calculations for precise results

## 🚀 Quick Start

### Installation
- **Clone the repository**
  - git clone https://github.com/yourusername/product-shelf-calculator.git

- **Navigate to project directory**
  - cd product-shelf-calculator

- **Run the program**
  - python main.py

 ### Usage
1. **Enter number of products** you want to arrange
2. **Choose repetition policy**: Allow same products in multiple spots? (Y/N)
3. **Specify shelf count**: How many shelves do you have?
4. **Select categories**: Choose 1-5 product categories to use
5. **View results**: See total arrangements and example layout

## 🎯 Example Preview
Please enter the number of products you have: 15

Do you want repeats(Y or N): N

Please enter the number of shelves you have: 3

Please enter how many categories you want from 1-5: 4

The number of arrangements you can have is: 10897286400.0

This is an example of how you can arrange it:

Shelf 1: Electronics K3L9M | Sports R7T2W | Food A8B4C | Clothing X1Y5Z | Electronics P6Q3R

Shelf 2: Food S9T7U | Clothing M2N8P | Sports V4W1X | Electronics D5F6G | Food H3J9K

Shelf 3: Sports L2M7N | Electronics Q8R4S | Clothing T1U5V | Food W9X3Y | Sports Z6A2B

## 📚 Mathematical Background

This program implements fundamental combinatorial principles:

### With Repetition (Products can repeat)
**Formula**: `n^r`
- `n` = number of different products
- `r` = total shelf spots (shelves × 5)
- **Use case**: When you have unlimited quantities of each product

### Without Repetition (Each product used once)
**Formula**: `P(n,r) = n!/(n-r)!`
- Calculates permutations of `n` products taken `r` at a time
- **Requirement**: Must have at least as many products as total spots
- **Use case**: When each product is unique or limited quantity

## 🛠️ Technical Details

### Product Categories
- **Electronics**: Tech gadgets and devices
- **Clothing**: Apparel and accessories  
- **Sports**: Athletic and recreational equipment
- **Food**: Consumable food products
- **Drink**: Beverages and liquid refreshments

### System Requirements
- **Python**: Version 3.6 or higher
- **Dependencies**: None (uses built-in `math` and `random` modules)
- **Platform**: Cross-platform (Windows, macOS, Linux)
