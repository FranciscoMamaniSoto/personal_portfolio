// Smooth scrolling for navigation
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Only handle internal links
            if (href.startsWith('#')) {
                e.preventDefault();
                
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 100,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
    
    // Highlight current page in navigation
    const currentPath = window.location.pathname;
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        
        if (href === currentPath || 
            (currentPath.includes(href) && href !== '/')) {
            link.classList.add('active');
        }
    });
});