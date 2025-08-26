// Main JavaScript file for ELP Consultoria website

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functions
    initSmoothScrolling();
    initNavbarScroll();
    initFormValidation();
    initAnimations();
    initFlashMessages();
});

// Smooth scrolling for navigation links
function initSmoothScrolling() {
    const navLinks = document.querySelectorAll('a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const headerOffset = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                const navbarCollapse = document.querySelector('.navbar-collapse');
                if (navbarCollapse.classList.contains('show')) {
                    const bsCollapse = new bootstrap.Collapse(navbarCollapse);
                    bsCollapse.hide();
                }
            }
        });
    });
}

// Navbar scroll effect
function initNavbarScroll() {
    const navbar = document.querySelector('.custom-navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Add/remove shadow based on scroll position
        if (scrollTop > 50) {
            navbar.style.boxShadow = '0 2px 20px rgba(0, 38, 77, 0.2)';
        } else {
            navbar.style.boxShadow = '0 2px 10px rgba(0, 38, 77, 0.1)';
        }
        
        lastScrollTop = scrollTop;
    });
}

// Form validation and submission
function initFormValidation() {
    const contactForm = document.querySelector('.contact-form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();
            
            // Basic client-side validation
            if (!name || !email || !message) {
                e.preventDefault();
                showAlert('Por favor, preencha todos os campos obrigatórios.', 'error');
                return;
            }
            
            if (!isValidEmail(email)) {
                e.preventDefault();
                showAlert('Por favor, insira um e-mail válido.', 'error');
                return;
            }
            
            // Show loading state
            const submitButton = contactForm.querySelector('button[type="submit"]');
            submitButton.disabled = true;
            submitButton.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Enviando...';
        });
    }
}

// Email validation helper
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Show alert messages
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type === 'error' ? 'danger' : 'success'} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Insert at the top of the page
    const flashContainer = document.querySelector('.flash-messages') || createFlashContainer();
    flashContainer.appendChild(alertDiv);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (alertDiv && alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

// Create flash messages container if it doesn't exist
function createFlashContainer() {
    const container = document.createElement('div');
    container.className = 'flash-messages';
    document.body.appendChild(container);
    return container;
}

// Initialize scroll animations
function initAnimations() {
    const animatedElements = document.querySelectorAll('.service-card, .feature-card, .differential-card');
    
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in-up');
                }
            });
        },
        {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        }
    );
    
    animatedElements.forEach(element => {
        observer.observe(element);
    });
}

// Handle flash messages auto-dismiss
function initFlashMessages() {
    const flashMessages = document.querySelectorAll('.flash-messages .alert');
    
    flashMessages.forEach(message => {
        setTimeout(() => {
            if (message && message.parentNode) {
                const bsAlert = new bootstrap.Alert(message);
                bsAlert.close();
            }
        }, 5000);
    });
}

// Phone number formatting (Brazilian format)
function formatPhone(input) {
    let value = input.value.replace(/\D/g, '');
    
    if (value.length <= 11) {
        value = value.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
        if (value.length < 14) {
            value = value.replace(/(\d{2})(\d{4})(\d{4})/, '($1) $2-$3');
        }
    }
    
    input.value = value;
}

// Add phone formatting to phone input
const phoneInput = document.getElementById('phone');
if (phoneInput) {
    phoneInput.addEventListener('input', function() {
        formatPhone(this);
    });
}

// Utility function for debouncing
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Handle window resize events
window.addEventListener('resize', debounce(() => {
    // Recalculate any dynamic sizes if needed
    console.log('Window resized');
}, 250));

// Analytics tracking (placeholder for future implementation)
function trackEvent(eventName, properties = {}) {
    // Implementation would depend on chosen analytics service
    console.log('Event tracked:', eventName, properties);
}

// Track form submissions
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', () => {
        trackEvent('contact_form_submit', {
            page: 'landing',
            section: 'contact'
        });
    });
}

// Track CTA button clicks
const ctaButtons = document.querySelectorAll('.cta-button, .hero-cta');
ctaButtons.forEach(button => {
    button.addEventListener('click', () => {
        trackEvent('cta_click', {
            button_text: button.textContent.trim(),
            section: button.closest('section')?.id || 'header'
        });
    });
});
