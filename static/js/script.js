// Функциональность корзины
let cart = JSON.parse(localStorage.getItem('cart')) || [];

function addToCart(productId) {
    const product = {
        id: productId,
        quantity: 1,
        addedAt: new Date().toISOString()
    };

    const existingItem = cart.find(item => item.id === productId);

    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push(product);
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    showNotification('Товар добавлен в корзину! 🛒');
    updateCartCounter();
    updateCartAnimation();
}

function updateCartCounter() {
    const totalItems = cart.reduce((total, item) => total + item.quantity, 0);
    const cartCounter = document.getElementById('cart-counter');
    if (cartCounter) {
        cartCounter.textContent = totalItems;
        // Показываем/скрываем бейдж
        if (totalItems > 0) {
            cartCounter.style.display = 'flex';
        } else {
            cartCounter.style.display = 'none';
        }
    }
}

function updateCartAnimation() {
    const cartIcon = document.querySelector('.cart-icon');
    if (cartIcon) {
        cartIcon.classList.add('pulse');
        setTimeout(() => {
            cartIcon.classList.remove('pulse');
        }, 600);
    }
}

function showNotification(message) {
    // Создаем элемент уведомления
    const notification = document.createElement('div');
    notification.className = 'alert alert-success position-fixed';
    notification.style.cssText = `
        top: 20px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        background: rgba(40, 167, 69, 0.9);
        backdrop-filter: blur(10px);
        border: none;
        border-radius: 10px;
        color: white;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
    `;
    notification.innerHTML = `
        <div class="d-flex align-items-center">
            <i class="fas fa-check-circle me-2"></i>
            <span>${message}</span>
        </div>
    `;

    document.body.appendChild(notification);

    // Автоматическое скрытие через 3 секунды
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transform = 'translateX(100px)';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// Валидация формы входа
function validateLoginForm() {
    const username = document.getElementById('id_username');
    const password = document.getElementById('id_password');
    let isValid = true;

    if (!username.value.trim()) {
        showFormError('Пожалуйста, введите имя пользователя');
        isValid = false;
    }

    if (!password.value.trim()) {
        showFormError('Пожалуйста, введите пароль');
        isValid = false;
    }

    return isValid;
}

function showFormError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'alert alert-danger';
    errorDiv.innerHTML = `
        <i class="fas fa-exclamation-triangle me-2"></i>
        ${message}
    `;

    const form = document.querySelector('form');
    const existingError = form.querySelector('.alert-danger');
    if (existingError) {
        existingError.remove();
    }

    form.insertBefore(errorDiv, form.firstChild);

    // Автоскрытие через 5 секунд
    setTimeout(() => {
        if (errorDiv.parentNode) {
            errorDiv.style.opacity = '0';
            setTimeout(() => {
                if (errorDiv.parentNode) {
                    errorDiv.remove();
                }
            }, 300);
        }
    }, 5000);
}

// Плавная прокрутка
function smoothScrollTo(target) {
    const element = document.querySelector(target);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Инициализация при загрузке документа
document.addEventListener('DOMContentLoaded', function () {
    // Инициализация счетчика корзины
    updateCartCounter();

    // Валидация формы входа
    const loginForm = document.querySelector('form[method="post"]');
    if (loginForm && window.location.pathname.includes('login')) {
        loginForm.addEventListener('submit', function (e) {
            if (!validateLoginForm()) {
                e.preventDefault();
            }
        });
    }

    // Плавная прокрутка для якорных ссылок
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = this.getAttribute('href');
            if (target !== '#') {
                smoothScrollTo(target);
            }
        });
    });

    // Анимация появления элементов при скролле
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Наблюдаем за элементами с анимацией
    document.querySelectorAll('.product-card, .feature-item').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Добавляем hover-эффекты для карточек
    document.querySelectorAll('.product-card').forEach(card => {
        card.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-10px)';
        });

        card.addEventListener('mouseleave', function () {
            this.style.transform = 'translateY(0)';
        });
    });

    // Инициализация tooltips Bootstrap
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

// Функция для обновления темы (если понадобится темная/светлая тема)
function toggleTheme() {
    const body = document.body;
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

    body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);

    showNotification(`Тема изменена на ${newTheme === 'dark' ? 'тёмную' : 'светлую'}`);
}

// Загрузка сохраненной темы
function loadTheme() {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.body.setAttribute('data-theme', savedTheme);
}

// Вызываем при загрузке
loadTheme();
loadTheme();