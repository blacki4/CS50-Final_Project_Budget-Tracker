# Personal Budget Tracker

#### Video Demo: <YOUR VIDEO URL HERE>

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

#### Design Choices:

The choice of Flask and SQLite was based on their simplicity and ease of integration for small web projects. JavaScript was used to enhance user interactivity on the frontend, including dynamic charts and transaction filtering. Security considerations were taken into account by using sessions for user authentication.

This project demonstrates practical application of all concepts learned in CS50, including data handling, backend development, and frontend design. It also provides a tangible solution to a real-world problem, helping users manage their finances efficiently.
