# Assignment 1: Python - Data Structures

## Problem Statement
You are a Junior Python Developer at a small e-commerce store. The store wants a simple inventory utility to manage products and categories, run small queries, and export a snapshot of selected products. Your code should demonstrate correct use of Python data structures: lists, tuples, sets, and dictionaries.

## Project Description
This project focuses on building a basic inventory management system for an online store. The application should allow the user to:

- Store product information such as name, category, price, stock quantity, and rating
- Group items by category to support efficient browsing and organization
- Search and filter products using small queries
- Select a subset of products and generate an export snapshot
- Demonstrate the practical use of Python built-in data structures

## Project Specification

### Core Functional Requirements
1. Product Management
   - Maintain a collection of products in a structured format
   - Each product should include relevant attributes like ID, name, category, price, and stock
   - Product records should be easy to add, update, and retrieve

2. Category Management
   - Organize products into categories such as Electronics, Clothing, Home, etc.
   - Allow quick lookup of all products under a specific category

3. Query Operations
   - Run simple queries such as:
     - Find all products in a given category
     - Search for products by name or keyword
     - Check items with low stock
     - List products within a price range

4. Snapshot Export
   - Select one or more products and export a snapshot of the chosen items
   - Exported data should be readable and structured for quick review

### Data Structure Requirements
The solution must demonstrate the correct use of these Python data structures:

- Lists: for ordered collections of products or category items
- Tuples: for fixed or read-only product metadata or records
- Sets: for unique categories, selected product IDs, or filtered result tracking
- Dictionaries: for key-value product records and category mappings

### Expected Outcome
The final program should act as a simple inventory utility that:

- stores products efficiently,
- supports category-based organization,
- handles small queries effectively, and
- exports a snapshot of selected products in a clear format.

## Implementation Guidelines
- Use dictionaries to represent each product record
- Use lists to maintain ordered collections of products
- Use tuples where immutable product-related data is appropriate
- Use sets to manage unique values and membership checks
- Keep the implementation simple, readable, and beginner-friendly

## Deliverables
- Python code implementing the inventory utility
- Clear and organized output for product listings and queries
- Snapshot export of selected products
