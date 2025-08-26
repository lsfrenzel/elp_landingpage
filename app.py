import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "elp-consultoria-secret-key-2024")

@app.route('/')
def index():
    """Main landing page"""
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    """About page"""
    return render_template('sobre.html')

@app.route('/servicos')
def servicos():
    """Services page"""
    return render_template('servicos.html')

@app.route('/diferenciais')
def diferenciais():
    """Differentials page"""
    return render_template('diferenciais.html')

@app.route('/contato')
def contato():
    """Contact page"""
    return render_template('contato.html')

@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submission"""
    try:
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        message = request.form.get('message', '').strip()
        
        # Basic validation
        if not name or not email or not message:
            flash('Por favor, preencha todos os campos obrigatórios.', 'error')
            return redirect(url_for('contato'))
        
        # Email validation (basic)
        if '@' not in email or '.' not in email:
            flash('Por favor, insira um e-mail válido.', 'error')
            return redirect(url_for('contato'))
        
        # Log the contact form submission
        app.logger.info(f"Contact form submitted - Name: {name}, Email: {email}")
        
        # In a real application, you would save to database or send email here
        # For now, we'll just show a success message
        flash('Obrigado pelo seu contato! Retornaremos em breve.', 'success')
        
    except Exception as e:
        app.logger.error(f"Error processing contact form: {str(e)}")
        flash('Erro interno. Tente novamente mais tarde.', 'error')
    
    return redirect(url_for('contato'))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('index.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
