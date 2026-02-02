from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app import db
from app.models import Transaction
from datetime import datetime, timedelta
from sqlalchemy import func

main_bp = Blueprint('main', __name__)
transactions_bp = Blueprint('transactions', __name__, url_prefix='/transactions')

@main_bp.route('/')
def index():
    """Dashboard route"""
    transactions = Transaction.query.order_by(Transaction.date.desc()).all()
    
    # Calculate totals
    total_income = db.session.query(func.sum(Transaction.amount)).filter(
        Transaction.transaction_type == 'income'
    ).scalar() or 0
    
    total_expense = db.session.query(func.sum(Transaction.amount)).filter(
        Transaction.transaction_type == 'expense'
    ).scalar() or 0
    
    balance = total_income - total_expense
    
    # Get last 30 days transactions
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    recent_transactions = Transaction.query.filter(
        Transaction.date >= thirty_days_ago
    ).order_by(Transaction.date.desc()).all()
    
    return render_template('index.html', 
                         transactions=recent_transactions,
                         total_income=total_income,
                         total_expense=total_expense,
                         balance=balance)

@transactions_bp.route('/add', methods=['GET', 'POST'])
def add_transaction():
    """Add a new transaction"""
    if request.method == 'POST':
        description = request.form.get('description')
        amount = float(request.form.get('amount'))
        category = request.form.get('category')
        transaction_type = request.form.get('type')
        date_str = request.form.get('date')
        
        if date_str:
            date = datetime.strptime(date_str, '%Y-%m-%d')
        else:
            date = datetime.utcnow()
        
        transaction = Transaction(
            description=description,
            amount=amount,
            category=category,
            transaction_type=transaction_type,
            date=date
        )
        
        db.session.add(transaction)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    
    return render_template('add_transaction.html')

@transactions_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_transaction(id):
    """Edit a transaction"""
    transaction = Transaction.query.get_or_404(id)
    
    if request.method == 'POST':
        transaction.description = request.form.get('description')
        transaction.amount = float(request.form.get('amount'))
        transaction.category = request.form.get('category')
        transaction.transaction_type = request.form.get('type')
        date_str = request.form.get('date')
        
        if date_str:
            transaction.date = datetime.strptime(date_str, '%Y-%m-%d')
        
        db.session.commit()
        return redirect(url_for('main.index'))
    
    return render_template('edit_transaction.html', transaction=transaction)

@transactions_bp.route('/delete/<int:id>', methods=['POST'])
def delete_transaction(id):
    """Delete a transaction"""
    transaction = Transaction.query.get_or_404(id)
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for('main.index'))

@transactions_bp.route('/api/stats')
def get_stats():
    """Get statistics for API"""
    transactions = Transaction.query.all()
    
    # Category breakdown
    income_by_category = db.session.query(
        Transaction.category,
        func.sum(Transaction.amount)
    ).filter(Transaction.transaction_type == 'income').group_by(Transaction.category).all()
    
    expense_by_category = db.session.query(
        Transaction.category,
        func.sum(Transaction.amount)
    ).filter(Transaction.transaction_type == 'expense').group_by(Transaction.category).all()
    
    return jsonify({
        'income_by_category': dict(income_by_category),
        'expense_by_category': dict(expense_by_category)
    })
