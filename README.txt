This repository contains:

1) My practice code for test automation (using Selenium & Pytest) and python logic (algorithms, data structures, and error handling).
This part is divided into two: UI tests for `saucedemo.com` and standalone python scripts for backend-like logic.
How to run
1.  Install requirements:
    ```bash
    pip install selenium pytest
    ```
2.  Run selenium tests:
    ```bash
    pytest
    ```
3.  Run logic scripts:
    ```bash
    python inventory_management_system.py
    ```

2) API automation (Postman)
I automated the workflow for the Simple Books API to practice backend testing.
The collection simulates a real user flow rather than just isolated requests.
How to Run:
* Import the `.json` files into Postman.
* Run the collection via "Collection Runner".

3) Manual bug reports (real-world practice). Exploratory testing on a live production environment (032.ua). I identified and documented Critical and Major issues regarding security and input validation. Check bug_reports.md for detailed reports with screenshots and steps.
