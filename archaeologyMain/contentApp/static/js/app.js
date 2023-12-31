// Dark Mode - Light Mode
const toggle = document.getElementById('darkModeToggle')

if (toggle) {
    toggle.addEventListener('click', function () {
        if (document.body.getAttribute('data-bs-theme') == 'dark') {
            document.body.setAttribute('data-bs-theme', 'light');
            localStorage.setItem("theme", "light");
        } else {
            document.body.setAttribute('data-bs-theme', 'dark');
            localStorage.setItem("theme", "dark");
        }
    })
}

if (localStorage.getItem('theme') == 'dark') {
    document.body.setAttribute('data-bs-theme', 'dark')
} else {
    document.body.setAttribute('data-bs-theme', 'light')
}

// Message
const alertDiv = document.getElementById('alertDiv')

if (alertDiv) {
    window.onload = function (){
        setTimeout(function (){
            alertDiv.style.display = 'none'
        }, 2000)
    }
}