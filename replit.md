# ELP Consultoria e Engenharia - Landing Page

## Overview

This is a Flask-based landing page for ELP Consultoria e Engenharia, a fictional civil engineering consultancy specializing in cement-based materials and facade systems. The application serves as a professional, responsive website showcasing the company's services, expertise, and contact information. The system is designed as a single-page application with multiple sections including hero, about, services, differentials, and contact forms.

## Recent Changes (October 28, 2025)

- **Resend Email Integration**: Configured contact form to send emails via Resend API to comercial@elpconsultoria.eng.br
- **Railway Compatibility**: Updated email integration to support both Replit (via connectors) and Railway (via environment variables)
- **Security Enhancement**: Enforced SESSION_SECRET environment variable requirement for production security
- **Documentation**: Created RAILWAY_SETUP.md with deployment instructions and environment variable configuration guide

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Z-Index Management
- **Hero Section**: z-index: 1 (background layer)
- **Content Sections**: z-index: 5 (ensures content appears above hero during scroll)
- **Hero Text Elements**: z-index: 10 (highest priority for visibility)
- **Navigation Bar**: Fixed positioning with appropriate z-index

### Frontend Architecture
- **Single Page Application (SPA)**: Built as a responsive landing page with multiple sections accessible through smooth scrolling navigation
- **Bootstrap Framework**: Uses Bootstrap 5.3.0 for responsive grid system and components
- **CSS Custom Properties**: Implements CSS variables for consistent theming with company colors (primary blue #00264d, cement gray #cccccc, white)
- **Typography**: Uses Montserrat font family from Google Fonts for modern, professional appearance
- **JavaScript Enhancement**: Custom JavaScript for smooth scrolling, navbar effects, form validation, and animations

### Backend Architecture
- **Flask Microframework**: Lightweight Python web framework serving static content and handling form submissions
- **Template Engine**: Uses Jinja2 templating (Flask's default) for HTML generation
- **Flash Messaging System**: Implements Flask's flash messaging for user feedback on form submissions
- **Error Handling**: Custom 404 error handler (incomplete in current code)
- **Environment Configuration**: Uses environment variables for session secrets

### Form Processing
- **Contact Form Handler**: Server-side validation for contact form submissions with Portuguese language feedback
- **Validation Logic**: Implements basic email validation and required field checking
- **Logging System**: Uses Python's logging module for debugging and contact form submission tracking

### Static Asset Organization
- **CSS Structure**: Organized custom stylesheet with CSS variables for maintainable theming
- **JavaScript Modules**: Modular JavaScript functions for different page behaviors
- **Image Assets**: Placeholder for logo and background images in static directory

### Design System
- **Color Palette**: Professional blue and gray theme reflecting engineering/construction industry
- **Responsive Design**: Mobile-first approach using Bootstrap's responsive utilities
- **Animation Strategy**: Subtle hover effects and smooth transitions for enhanced user experience

## External Dependencies

### Frontend Libraries
- **Bootstrap 5.3.0**: CSS framework for responsive design and components
- **Font Awesome 6.4.0**: Icon library for service and feature icons
- **Google Fonts (Montserrat)**: Typography system for consistent branding

### Python Packages
- **Flask**: Core web framework for routing and template rendering
- **Werkzeug**: WSGI utilities (Flask dependency) for request handling

### Development Dependencies
- **Python Logging**: Built-in Python module for application logging
- **OS Module**: Environment variable handling for configuration

### Deployment Considerations
- **Railway Platform**: Configured for deployment on Railway with proper configuration files
  - `Procfile`: Defines the web process command for Railway
  - `railway.json`: Railway-specific deployment configuration
  - `runtime.txt`: Specifies Python version for deployment
- **Environment Variables**: Configurable session secrets and Railway environment detection
- **Static File Serving**: Flask's built-in static file serving for CSS, JS, and images
- **Port Configuration**: Dynamic port assignment for Railway deployment

### Email Integration
- **Resend API**: Integrated for transactional email delivery from contact form
- **Environment-Based Configuration**: Compatible with both Replit (connectors) and Railway (env vars)
- **Required Environment Variables**:
  - `RESEND_API_KEY`: API key from Resend service
  - `RESEND_FROM_EMAIL`: Optional sender email (defaults to onboarding@resend.dev)
  - `SESSION_SECRET`: Required for Flask session security
- **Contact Email Destination**: comercial@elpconsultoria.eng.br
- **Error Handling**: Graceful fallback with user-friendly error messages

### Missing Integrations (Potential Future Additions)
- **Database**: No persistent storage implemented for contact submissions
- **Analytics**: No web analytics integration present
- **Content Management**: Static content with no CMS integration