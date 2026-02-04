This repository contains:
1) My practice code for Test Automation (using Selenium & Pytest) and Python Logic (algorithms, data structures, and error handling).
This part is divided into two: UI tests for `saucedemo.com` and standalone Python scripts for backend-like logic.
How to Run
1.  Install requirements:
    ```bash
    pip install selenium pytest
    ```
2.  Run Selenium Tests:
    ```bash
    pytest
    ```
3.  Run Logic Scripts:
    ```bash
    python inventory_management_system.py
    ```
2) API Automation (Postman)
I automated the workflow for the Simple Books API to practice backend testing.
The collection simulates a real user flow rather than just isolated requests.
How to Run:
* Import the `.json` files into Postman.
* Run the collection via "Collection Runner".
3) Manual bug reports (real-world practice). Exploratory testing on a live production environment (032.ua). I identified and documented Critical and Major issues regarding security and input validation. Check Bug_Reports.md for detailed reports with screenshots and steps.
