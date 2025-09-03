# Personal Budget Tracker

#### Video Demo: [Project Video](https://youtu.be/ozGZeTTJ9NQ)

#### Description:

Personal Budget Tracker is a web application designed to help users manage their personal finances effectively. Users can register and log in to their accounts, add income and expenses, categorize transactions, and visualize their spending patterns through charts. The application provides a simple yet powerful interface to monitor monthly budgets, ensuring that users have full control over their financial habits.

The project is implemented using Flask for the backend, SQLite for the database, and a combination of HTML, CSS, and JavaScript for the frontend. The main goal was to create a user-friendly application that is functional, visually appealing, and demonstrates good programming practices learned throughout the CS50 course.

#### Features:

1. **User Authentication**: Secure login and registration.
2. **Transaction Management**: Add, edit, and delete income or expense transactions.
3. **Dashboard Overview**: View summaries of total income, total expenses, and remaining budget.
4. **Visual Analytics**: Graphical representation of spending by categories.
5. **Search & Filter**: Find transactions by category or date.

#### Project Structure:

- `app.py`: Main Flask application handling routes and backend logic.
- `templates/`: Contains HTML files for the frontend.
- `static/css/style.css`: Custom CSS styling for the application.
- `static/js/main.js`: JavaScript functionality for interactivity.
- `database.db`: SQLite database containing users and transactions tables.
- `requirements.txt`: Python dependencies for Flask and SQLite.

#### Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/finance-tracker.git
   cd finance-tracker
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows

    pip install -r requirements.txt
   ```
3. Initialize the database:
   ```bash
   sqlite3 database.db < schema.sql
   ```
4. Run the Flask server:
   ```bash
   python app.py
   ```
5. Open the app in your browser:
    ```bash
    http://127.0.0.1:5000
    ```
    

