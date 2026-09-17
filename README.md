# UNIT_PROJECT

# - Tuwaiq Logistics Management System -

## Overview
A Command Line Interface (CLI) application for managing warehouse shipments. This system allows users to add, view, and search for shipments interactively.

## Features
* **Add Shipments:** Insert new shipments with ID, Cargo, Destination, and Driver.
* **View Shipments:** Display all records in a formatted table.
* **Search:** Find specific shipments by their exact ID.
* **Data Persistence:** Saves data to a local text file.
* **Interactive UI:** Features text-to-speech feedback and colored terminal tables.

## Technologies Used
* Python 
* `rich` (for terminal tables)
* `pyfiglet` (for ASCII art logos)
* `pyttsx3` (for voice feedback)

## How to Install and Run
1. Install the required packages:
   `pip install -r requirements.txt`
2. Run the application:
   `python main.py`