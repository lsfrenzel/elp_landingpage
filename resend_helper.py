import os
import requests
import json


def get_resend_credentials():
    """
    Fetch Resend API credentials from Replit Connectors.
    Returns a dictionary with api_key and from_email.
    """
    hostname = os.environ.get("REPLIT_CONNECTORS_HOSTNAME")
    
    # Get the authentication token
    x_replit_token = None
    if os.environ.get("REPL_IDENTITY"):
        x_replit_token = f"repl {os.environ.get('REPL_IDENTITY')}"
    elif os.environ.get("WEB_REPL_RENEWAL"):
        x_replit_token = f"depl {os.environ.get('WEB_REPL_RENEWAL')}"
    
    if not x_replit_token:
        raise Exception("X_REPLIT_TOKEN not found for repl/depl")
    
    # Fetch connection settings
    url = f"https://{hostname}/api/v2/connection?include_secrets=true&connector_names=resend"
    headers = {
        "Accept": "application/json",
        "X_REPLIT_TOKEN": x_replit_token
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    connection_settings = data.get("items", [None])[0]
    
    if not connection_settings or not connection_settings.get("settings", {}).get("api_key"):
        raise Exception("Resend not connected")
    
    return {
        "api_key": connection_settings["settings"]["api_key"],
        "from_email": connection_settings["settings"].get("from_email", "onboarding@resend.dev")
    }


def send_email(to_email, subject, html_content, from_name=None):
    """
    Send an email using Resend API.
    
    Args:
        to_email: Recipient email address
        subject: Email subject
        html_content: HTML content of the email
        from_name: Optional sender name (default: None)
    
    Returns:
        Dictionary with response data or raises an exception on failure
    """
    try:
        credentials = get_resend_credentials()
        api_key = credentials["api_key"]
        from_email = credentials["from_email"]
        
        # Add sender name if provided
        if from_name:
            from_address = f"{from_name} <{from_email}>"
        else:
            from_address = from_email
        
        # Prepare the email data
        email_data = {
            "from": from_address,
            "to": [to_email] if isinstance(to_email, str) else to_email,
            "subject": subject,
            "html": html_content
        }
        
        # Send the email via Resend API
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            "https://api.resend.com/emails",
            headers=headers,
            data=json.dumps(email_data)
        )
        
        response.raise_for_status()
        return response.json()
        
    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")
