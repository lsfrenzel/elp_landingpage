import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "elp-consultoria-secret-key-2024")

# Railway deployment configuration
if os.environ.get('RAILWAY_ENVIRONMENT'):
    # Production settings for Railway
    app.config['DEBUG'] = False
    app.config['ENV'] = 'production'
else:
    # Development settings
    app.config['DEBUG'] = True
    app.config['ENV'] = 'development'

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

@app.route('/politica-privacidade')
def politica_privacidade():
    """Privacy Policy page"""
    return render_template('politica_privacidade.html')

@app.route('/termos-uso')
def termos_uso():
    """Terms of Use page"""
    return render_template('termos_uso.html')

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
    # Get port from environment variable for Railway deployment
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
