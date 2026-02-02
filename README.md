# Personal Finance Manager

A simple yet powerful web application built with Flask for managing your personal finances. Track income and expenses, categorize transactions, and visualize your financial summary.

## Features

- 💰 Track income and expenses
- 📊 Categorize transactions
- 📅 View transaction history with date filtering
- 📈 Financial dashboard with summary statistics
- ➕ Add, edit, and delete transactions
- 🎨 Responsive and modern UI
- 💾 SQLite database for persistent storage

## Tech Stack

- **Backend**: Flask
- **Database**: SQLAlchemy with SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render

## Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/finance-manager.git
   cd finance-manager
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## Deployment on Render

### Using render.yaml

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Connect to Render**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Create a new "Web Service"
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml`
   - Click "Deploy"

### Manual Deployment

1. **Create a Web Service on Render**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: finance-manager
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn run:app`

2. **Set Environment Variables** (if needed)
   - `SECRET_KEY`: Your secret key for session management
   - `DATABASE_URL`: Database connection string (optional, uses SQLite by default)

3. **Deploy**
   - Click "Create Web Service"
   - Render will build and deploy your app

## Usage

### Adding a Transaction

1. Click the "+ Add Transaction" button
2. Fill in the transaction details:
   - **Description**: What was this transaction for?
   - **Amount**: How much?
   - **Category**: Choose or add a category
   - **Type**: Income or Expense
   - **Date**: When did this occur? (defaults to today)
3. Click "Add Transaction"

### Editing a Transaction

1. Find the transaction in the list
2. Click the "Edit" button
3. Update the details
4. Click "Update Transaction"

### Deleting a Transaction

1. Find the transaction in the list
2. Click the "Delete" button
3. Confirm the deletion

### Viewing Statistics

- The dashboard shows:
  - **Total Income**: Sum of all income transactions
  - **Total Expense**: Sum of all expenses
  - **Balance**: Income minus expenses
  - **Recent Transactions**: Last 30 days of transactions

## Project Structure

```
finance-manager/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── routes.py            # Application routes
│   ├── static/
│   │   └── css/
│   │       └── style.css    # Styling
│   └── templates/
│       ├── index.html       # Dashboard
│       ├── add_transaction.html    # Add form
│       └── edit_transaction.html   # Edit form
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── Procfile                 # Heroku/Render deployment config
├── render.yaml              # Render configuration
└── README.md                # This file
```

## Environment Variables

- `SECRET_KEY`: Secret key for Flask (change in production)
- `DATABASE_URL`: Database URL (optional, defaults to SQLite)
- `FLASK_ENV`: Set to 'production' for deployment

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

MIT License - feel free to use this project for personal or commercial use.

## Support

For issues and questions, please open an issue on GitHub.

---

**Happy tracking! 💰📊**
