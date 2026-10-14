# 📈 Stock Portfolio Tracker Using Python and Flask

## 📌 Project Overview

The Stock Portfolio Tracker is a simple, interactive web application developed using Python and Flask as part of the **CodeAlpha Python Programming Internship**.

The application allows users to select stocks, enter the number of shares they own, and calculate the total investment value based on predefined stock prices. It provides a clean web interface where users can manage their portfolio, remove stocks, and download portfolio details as a CSV file.

This project demonstrates Python programming, web development, data handling, and basic financial calculations.

**Note:** The stock prices used in this project are predefined example prices and do not represent live market prices.

## 🎯 Project Objectives

- Build a stock portfolio tracking web application.
- Understand Python web development using Flask.
- Calculate total investment values based on stock prices and quantities.
- Create an interactive and responsive user interface.
- Manage stock portfolio data using Python dictionaries.
- Export portfolio information to a CSV file.
- Learn how frontend and backend components work together.

## ✨ Features

- 📊 **Investment Summary:** Displays the total investment value.
- 📈 **Stock Selection:** Select from predefined stocks.
- 🔢 **Quantity Input:** Enter the number of shares.
- 🧮 **Automatic Calculation:** Calculates the value of each stock and the overall portfolio.
- ➕ **Add Stocks:** Add stocks to your portfolio.
- ➖ **Remove Stocks:** Remove selected stocks.
- 🗑️ **Clear Portfolio:** Clear all portfolio entries.
- 📥 **CSV Export:** Download portfolio information as a CSV file.
- ✅ **Input Validation:** Checks stock symbols and share quantities.
- 📱 **Responsive Design:** Supports desktop and mobile screen sizes.
- 🌐 **Local Web Application:** Runs locally and can be accessed through a web browser.

## 🛠️ Technologies Used

- **Python 3:** Main programming language.
- **Flask:** Python web framework.
- **HTML5:** Structures the webpage.
- **CSS3:** Styles the interface and supports responsive layouts.
- **Jinja2:** Renders dynamic HTML content through Flask.
- **CSV Module:** Exports portfolio details to a CSV file.
- **Session Management:** Maintains portfolio information during the user's session.

## 💻 System Requirements

- Python 3.x
- Visual Studio Code or another code editor.
- Google Chrome or another modern web browser.
- A terminal or command prompt.
- Internet connection to install Flask initially.

## 📂 Project Structure

```text
CodeAlpha_StockPortfolioTracker/
│
├── app.py
└── README.md
```

### File Description

- `app.py` — Contains the Flask application, stock prices, portfolio calculations, routes, and HTML/CSS interface.
- `README.md` — Contains project documentation and instructions.

## ⚙️ Installation and Setup

### Step 1: Install Python

Download Python from the official website:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

On Windows, you can also use:

```bash
py --version
```

### Step 2: Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/chatzz06/CodeAlpha_StockPortfolioTracker.git
```

Navigate to the project folder:

```bash
cd CodeAlpha_StockPortfolioTracker
```

**Note:** Create and upload the repository to GitHub before using the clone command. Alternatively, download the project files directly.

### Step 3: Install Dependencies

Install Flask using the requirements file:

```bash
python -m pip install -r requirements.txt
```

If necessary on Windows, use:

```bash
py -m pip install -r requirements.txt
```

### Step 4: Run the Application

Start the Flask development server:

```bash
python app.py
```

On Windows, you can also run:

```bash
py app.py
```

### Step 5: Open the Application

Open Google Chrome and visit:

http://127.0.0.1:5000

The Stock Portfolio Tracker website should now be available locally.

**Important:** Keep the terminal running while using the application. Press `Ctrl + C` in the terminal to stop the server.

## 📖 How to Use the Application

1. Start the Flask application.
2. Open the local website in your browser.
3. Select a stock from the available stock list.
4. Enter the quantity of shares.
5. Click **Add Stock**.
6. View the portfolio summary and total investment value.
7. Remove individual stocks when required.
8. Download the portfolio as a CSV file.
9. Clear the portfolio when you want to start again.

## 📊 Available Example Stocks

The application includes the following predefined stock symbols and example prices:

| Stock Symbol | Company | Example Price (USD) |
|---|---|---:|
| AAPL | Apple Inc. | $180.00 |
| TSLA | Tesla Inc. | $250.00 |
| GOOGL | Alphabet Inc. | $140.00 |
| MSFT | Microsoft Corp. | $420.00 |
| AMZN | Amazon.com Inc. | $185.00 |

These prices are hardcoded for demonstration purposes. They are not updated automatically and should not be used for real investment decisions.

## 🧮 Example Calculation

Suppose a user adds the following stocks:

| Stock | Quantity | Price per Share | Total Value |
|---|---:|---:|---:|
| AAPL | 10 | $180.00 | $1,800.00 |
| TSLA | 2 | $250.00 | $500.00 |
| **Total Investment** | | | **$2,300.00** |

The total investment value is calculated using:

**Total Value = Number of Shares × Price per Share**

**Total Investment = Sum of all individual stock values**

For the example above:

`(10 × 180) + (2 × 250) = $2,300.00`

## 📥 CSV Export

The application allows users to download their portfolio information as a CSV file.

The exported file contains:

- Stock symbol.
- Company name.
- Number of shares.
- Price per share.
- Total value for each stock.
- Overall portfolio investment value.

The CSV file can be opened using Microsoft Excel, Google Sheets, or any compatible spreadsheet application.

## 🧠 Concepts Learned

This project provides practical experience with:

- Python fundamentals.
- Dictionaries and data structures.
- Functions and modular programming.
- Loops and conditional statements.
- Input validation and exception handling.
- Flask routes and HTTP methods.
- HTML templates and CSS styling.
- Dynamic webpage rendering.
- Session-based data management.
- CSV file generation.
- Responsive web design.
- Running a web application locally.

## 🚀 Future Improvements

Possible enhancements include:

- Integrating a live stock market API.
- Adding stock price charts and historical data.
- Tracking profit and loss using purchase prices.
- Adding user registration and authentication.
- Storing portfolio data in a database.
- Supporting multiple currencies.
- Adding portfolio analytics and asset allocation charts.
- Deploying the application to a hosting platform.

## 🎓 Internship Information

- **Organization:** CodeAlpha
- **Program:** Python Programming Internship
- **Project Name:** Stock Portfolio Tracker
- **Domain:** Python Programming
- **Repository Name:** `CodeAlpha_StockPortfolioTracker`

## 👨‍💻 Author

**GitHub Username:** chatzz06

**GitHub Profile:** https://github.com/chatzz06

**Project Repository:** https://github.com/chatzz06/CodeAlpha_StockPortfolioTracker

## 📜 Disclaimer

This project is intended for educational purposes only. The stock prices are predefined examples and do not represent actual market prices or financial recommendations.

## 🙏 Acknowledgment

I would like to thank **CodeAlpha** for providing the opportunity to develop practical Python programming skills through internship projects.

---

⭐ If you find this project useful, feel free to star the repository!
