import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

if not app.secret_key:
    raise RuntimeError("SESSION_SECRET environment variable must be set for security")

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
            app.logger.warning("Contact form validation failed: missing required fields")
            flash('Por favor, preencha todos os campos obrigatórios.', 'error')
            return redirect(url_for('contato'))
        
        # Email validation using email-validator
        try:
            from email_validator import validate_email
            validate_email(email)
        except Exception as validation_error:
            app.logger.warning(f"Invalid email format: {email} - Error: {str(validation_error)}")
            flash('Por favor, insira um e-mail válido.', 'error')
            return redirect(url_for('contato'))
        
        # Log the contact form submission
        app.logger.info(f"Contact form submitted - Name: {name}, Email: {email}, Phone: {phone}")
        
        # Send email via Resend
        try:
            from resend_helper import send_email
            
            # Format the email content
            phone_info = f"<p><strong>Telefone:</strong> {phone}</p>" if phone else ""
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                    .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                    h2 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
                    .field {{ margin-bottom: 15px; }}
                    .field strong {{ color: #2c3e50; }}
                    .message-content {{ background-color: #f8f9fa; padding: 15px; border-left: 4px solid #3498db; margin-top: 10px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Novo Contato - ELP Consultoria e Engenharia</h2>
                    <div class="field"><strong>Nome:</strong> {name}</div>
                    <div class="field"><strong>E-mail:</strong> {email}</div>
                    {phone_info}
                    <div class="field"><strong>Mensagem:</strong></div>
                    <div class="message-content">{message.replace(chr(10), '<br>')}</div>
                </div>
            </body>
            </html>
            """
            
            app.logger.info("Attempting to send email via Resend...")
            
            # Send the email
            result = send_email(
                to_email="comercial@elpconsultoria.eng.br",
                subject=f"Novo Contato - {name}",
                html_content=html_content,
                from_name="ELP Consultoria - Website"
            )
            
            app.logger.info(f"Email sent successfully! Resend Response: {result}")
            flash('Obrigado pelo seu contato! Retornaremos em breve.', 'success')
            
        except Exception as email_error:
            app.logger.error(f"ERRO ao enviar email via Resend: {str(email_error)}", exc_info=True)
            # Still show success to user but log the error for debugging
            flash('Mensagem recebida! Retornaremos em breve.', 'success')
        
    except Exception as e:
        app.logger.error(f"Error processing contact form: {str(e)}", exc_info=True)
        flash('Erro ao processar formulário. Tente novamente.', 'error')
    
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
