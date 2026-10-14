
from flask import Flask, request, redirect, url_for, session, Response, render_template_string
import csv
import io
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "local-stock-tracker-demo-key")

# Example stock prices in USD (not live market prices)
STOCKS = {
    "AAPL": {"name": "Apple Inc.", "price": 180.00},
    "TSLA": {"name": "Tesla Inc.", "price": 250.00},
    "GOOGL": {"name": "Alphabet Inc.", "price": 140.00},
    "MSFT": {"name": "Microsoft Corp.", "price": 420.00},
    "AMZN": {"name": "Amazon.com Inc.", "price": 185.00},
}

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stock Portfolio Tracker</title>
    <style>
        * { box-sizing: border-box; }
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f6fb;
            color: #172033;
        }
        header {
            background: linear-gradient(120deg, #14213d, #2457a7);
            color: white;
            padding: 32px 20px;
        }
        .container { max-width: 1050px; margin: auto; }
        header h1 { margin: 0 0 10px; font-size: 30px; }
        header p { margin: 0; color: #dbeafe; }
        main { padding: 26px 16px 45px; }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
            gap: 16px;
            margin-bottom: 22px;
        }
        .card, .panel {
            background: white;
            border-radius: 14px;
            padding: 22px;
            box-shadow: 0 4px 16px #1720330b;
        }
        .stat-label { color: #68758a; font-size: 14px; }
        .stat-value { font-size: 27px; font-weight: bold; margin-top: 10px; }
        .panel { margin-bottom: 22px; }
        h2 { margin: 0 0 18px; font-size: 20px; }
        .form-grid {
            display: grid;
            grid-template-columns: 2fr 1fr auto;
            gap: 12px;
            align-items: end;
        }
        label {
            display: block;
            margin-bottom: 7px;
            font-size: 14px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 12px;
            border: 1px solid #d6deea;
            border-radius: 8px;
            background: white;
            font-size: 15px;
        }
        button, .button {
            border: 0;
            border-radius: 8px;
            padding: 12px 16px;
            cursor: pointer;
            font-size: 14px;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
        }
        .primary { background: #2457a7; color: white; }
        .secondary { background: #e8eef8; color: #193c70; }
        .danger { background: #fff0f0; color: #c03939; }
        .actions { display: flex; flex-wrap: wrap; gap: 9px; }
        .table-wrap { overflow-x: auto; }
        table { width: 100%; border-collapse: collapse; }
        th, td {
            text-align: left;
            padding: 14px 10px;
            border-bottom: 1px solid #edf0f5;
            white-space: nowrap;
        }
        th { color: #68758a; font-size: 13px; }
        .symbol { font-weight: bold; color: #2457a7; }
        .positive { color: #16845b; font-weight: bold; }
        .empty { text-align: center; color: #68758a; padding: 28px 10px; }
        .notice {
            padding: 12px 14px;
            background: #fff8e5;
            color: #805b10;
            border-radius: 8px;
            margin-bottom: 20px;
            font-size: 13px;
        }
        footer { text-align: center; padding: 20px; color: #68758a; font-size: 13px; }
        @media (max-width: 650px) {
            header h1 { font-size: 25px; }
            .form-grid { grid-template-columns: 1fr; }
            .stat-value { font-size: 23px; }
            .panel { padding: 16px; }
        }
    </style>
</head>
<body>
<header>
    <div class="container">
        <h1>📈 Stock Portfolio Tracker</h1>
        <p>Manage your stocks and calculate your total investment.</p>
    </div>
</header>

<main class="container">
    <div class="notice">
        Demo project: prices are predefined examples in USD, not live stock prices.
        This tool is for educational purposes, not investment advice.
    </div>

    <section class="stats">
        <div class="card">
            <div class="stat-label">Total Investment</div>
            <div class="stat-value">${{ "%.2f"|format(total) }}</div>
        </div>
        <div class="card">
            <div class="stat-label">Different Stocks</div>
            <div class="stat-value">{{ portfolio|length }}</div>
        </div>
        <div class="card">
            <div class="stat-label">Total Shares</div>
            <div class="stat-value">{{ total_shares }}</div>
        </div>
    </section>

    <section class="panel">
        <h2>Add Stocks to Your Portfolio</h2>
        <form action="{{ url_for('add_stock') }}" method="POST">
            <div class="form-grid">
                <div>
                    <label for="symbol">Select Stock</label>
                    <select name="symbol" id="symbol" required>
                        {% for symbol, stock in stocks.items() %}
                        <option value="{{ symbol }}">
                            {{ symbol }} — {{ stock.name }} (${{ "%.2f"|format(stock.price) }})
                        </option>
                        {% endfor %}
                    </select>
                </div>
                <div>
                    <label for="quantity">Number of Shares</label>
                    <input type="number" id="quantity" name="quantity"
                           min="1" max="1000000" step="1"
                           placeholder="e.g. 10" required>
                </div>
                <button class="primary" type="submit">+ Add Stock</button>
            </div>
        </form>
    </section>

    {% if message %}
    <div class="notice">{{ message }}</div>
    {% endif %}

    <section class="panel">
        <h2>Your Portfolio</h2>
        <div class="table-wrap">
            <table>
                <thead>
                    <tr>
                        <th>Stock</th>
                        <th>Company</th>
                        <th>Quantity</th>
                        <th>Price</th>
                        <th>Total Value</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                {% for symbol, quantity in portfolio.items() %}
                    <tr>
                        <td class="symbol">{{ symbol }}</td>
                        <td>{{ stocks[symbol].name }}</td>
                        <td>{{ quantity }}</td>
                        <td>${{ "%.2f"|format(stocks[symbol].price) }}</td>
                        <td class="positive">
                            ${{ "%.2f"|format(stocks[symbol].price * quantity) }}
                        </td>
                        <td>
                            <form action="{{ url_for('remove_stock', symbol=symbol) }}"
                                  method="POST">
                                <button class="danger" type="submit">Remove</button>
                            </form>
                        </td>
                    </tr>
                {% else %}
                    <tr>
                        <td colspan="6" class="empty">
                            Your portfolio is empty. Add a stock to get started.
                        </td>
                    </tr>
                {% endfor %}
                </tbody>
            </table>
        </div>

        <div class="actions" style="margin-top: 22px;">
            <a class="button primary" href="{{ url_for('download_csv') }}">
                Download CSV
            </a>
            <form action="{{ url_for('clear_portfolio') }}" method="POST"
                  onsubmit="return confirm('Clear your entire portfolio?');">
                <button class="danger" type="submit">Clear Portfolio</button>
            </form>
        </div>
    </section>
</main>

<footer>
    CodeAlpha Python Programming Internship · Stock Portfolio Tracker
</footer>
</body>
</html>
"""


@app.route("/")
def index():
    portfolio = session.get("portfolio", {})
    total = sum(
        STOCKS[symbol]["price"] * quantity
        for symbol, quantity in portfolio.items()
        if symbol in STOCKS
    )
    total_shares = sum(portfolio.values())

    return render_template_string(
        HTML,
        stocks=STOCKS,
        portfolio=portfolio,
        total=total,
        total_shares=total_shares,
        message=request.args.get("message", "")
    )


@app.route("/add", methods=["POST"])
def add_stock():
    symbol = request.form.get("symbol", "").upper().strip()
    quantity_text = request.form.get("quantity", "").strip()

    if symbol not in STOCKS:
        return redirect(url_for("index", message="Please select a valid stock."))

    try:
        quantity = int(quantity_text)
        if quantity < 1 or quantity > 1_000_000:
            raise ValueError
    except ValueError:
        return redirect(url_for(
            "index",
            message="Enter a whole-number quantity between 1 and 1,000,000."
        ))

    portfolio = session.get("portfolio", {})
    portfolio[symbol] = portfolio.get(symbol, 0) + quantity
    session["portfolio"] = portfolio

    return redirect(url_for("index", message=f"Added {quantity} shares of {symbol}."))


@app.route("/remove/<symbol>", methods=["POST"])
def remove_stock(symbol):
    portfolio = session.get("portfolio", {})
    portfolio.pop(symbol, None)
    session["portfolio"] = portfolio
    return redirect(url_for("index", message=f"{symbol} removed from your portfolio."))


@app.route("/clear", methods=["POST"])
def clear_portfolio():
    session.pop("portfolio", None)
    return redirect(url_for("index", message="Your portfolio has been cleared."))


@app.route("/download")
def download_csv():
    portfolio = session.get("portfolio", {})
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "Stock Symbol", "Company", "Quantity",
        "Price (USD)", "Total Value (USD)"
    ])

    total = 0

    for symbol, quantity in portfolio.items():
        stock = STOCKS.get(symbol)
        if stock is None:
            continue

        value = stock["price"] * quantity
        total += value

        writer.writerow([
            symbol,
            stock["name"],
            quantity,
            f"{stock['price']:.2f}",
            f"{value:.2f}"
        ])

    writer.writerow([])
    writer.writerow(["", "", "", "Total Investment", f"{total:.2f}"])

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
                "attachment; filename=stock_portfolio.csv"
        }
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
