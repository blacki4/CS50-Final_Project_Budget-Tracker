# Personal Budget Tracker

#### Video Demo: [Project Video](https://youtu.be/ozGZeTTJ9NQ)

#### Description:

Personal Budget Tracker is a comprehensive web application designed to help users effectively manage their personal finances. The primary goal of the project is to allow users to track their income and expenses, categorize their transactions, and visualize their financial habits over time. By providing an intuitive interface, the application empowers users to make informed decisions about their spending, saving, and budgeting.

The application begins with a user authentication system where users can securely register for a new account or log in to an existing one. This ensures that each user's financial data is private and isolated. While passwords are currently stored in plain text for learning purposes, this implementation demonstrates the authentication process, and in production, proper hashing and security measures would be applied.

Once logged in, users have access to the dashboard, which serves as the central hub for all financial activities. Here, users can add income and expense transactions, specifying the amount, category, date, and type of transaction. The application organizes these transactions efficiently in a database, allowing users to view them in a chronological order and easily manage their finances. Users can also delete transactions if a mistake was made, providing flexibility in maintaining accurate records.

A core feature of the dashboard is visual analytics, which gives users graphical representations of their spending by category. Using Chart.js, the application generates charts that illustrate how money is distributed across various categories such as food, entertainment, bills, and more. This visual representation helps users quickly identify patterns in their spending and make informed financial decisions. Additionally, the search and filter functionality allows users to locate specific transactions by category or date, further improving usability and efficiency.

The project leverages Flask as the backend framework to handle HTTP requests, manage sessions, and interact with the SQLite database. Flask provides a lightweight yet powerful framework that allows clear separation between the frontend and backend logic. The database contains two main tables: users and transactions. The users table stores account information, while the transactions table stores detailed records of income and expenses. Each transaction is linked to a specific user through a foreign key, ensuring data integrity and privacy.

The frontend is built using HTML, CSS, and JavaScript, providing a clean and responsive interface. Custom CSS ensures the application is visually appealing and user-friendly, while JavaScript handles dynamic interactions, such as updating the charts in real-time or filtering transactions without reloading the page. This combination of technologies demonstrates a full-stack approach and applies multiple concepts learned throughout the CS50 course, including web development, data handling, and user interface design.

During development, several design decisions were made to balance functionality and simplicity. Flask was chosen over heavier frameworks to maintain focus on core functionality and to demonstrate backend handling. SQLite was selected for its simplicity and ease of integration within a small-scale project. Chart.js was used because it allows clean and interactive chart visualizations with minimal setup, providing users immediate feedback on their financial data.

The project also emphasizes good programming practices, including modular code organization, clear naming conventions, and detailed comments in the code. AI tools like ChatGPT and Claude were utilized to optimize sections of code and improve documentation, ensuring clarity and maintainability without compromising the integrity of the work.

Overall, Personal Budget Tracker is not only a practical tool for everyday financial management but also a demonstration of key skills in web development, database management, and full-stack application design. By completing this project, users learn the importance of data organization, visual analytics, and user experience in creating effective software solutions. This project reflects the knowledge gained from CS50 and provides a solid foundation for more advanced web applications in the future.

#### Features:

1. **User Authentication**: Secure login and registration.
2. **Transaction Management**: Add and delete income or expense transactions.
3. **Dashboard Overview**: View summaries of total income, total expenses, and remaining budget.
4. **Visual Analytics**: Graphical representation of spending by categories.
5. **Search & Filter**: Find transactions by category or date.

> ⚠️ **Note**: Passwords are currently stored in plain text (for learning purposes). This is not secure for production use.  


#### Tech Stack
1. Python(Flask)
2. SQLite
3. HTML5,CSS3,JavaScript
4. Chart.js

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
   git clone https://github.com/blacki4/CS50-Final_Project_Budget-Tracker.git
   cd CS50-Final_Project_Budget-Tracker
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows

    pip install -r requirements.txt
   ```
3. Initialize the database (open Python shell and paste the following code):
   ```bash
   Python
   
   import sqlite3

   conn = sqlite3.connect("database.db")
   cursor = conn.cursor()
   
   cursor.execute("""
   CREATE TABLE IF NOT EXISTS users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       username TEXT UNIQUE NOT NULL,
       password TEXT NOT NULL
   )
   """)
   
   cursor.execute("""
   CREATE TABLE IF NOT EXISTS transactions (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       user_id INTEGER,
       amount REAL,
       category TEXT,
       date TEXT,
       type TEXT,
       FOREIGN KEY(user_id) REFERENCES users(id)
   )
   """)
   
   conn.commit()
   conn.close()

   ```
4. Run the Flask server:
   ```bash
   python app.py
   ```
5. Open the app in your browser:
    ```bash
    http://127.0.0.1:5000
    ```

## Acknowledgements
This project was built as part of Harvard’s CS50 course.  
I also used AI tools like ChatGPT and Claude to improve parts of the code and documentation.  


