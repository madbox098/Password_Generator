"""Модуль для генерации безопасных паролей."""

__version__ = "1.1.0"

import secrets
import string


def generate_password(length=12, use_digits=True, use_special=True):
    """
    Генерирует случайный пароль.
    
    Args:
        length: Длина пароля (по умолчанию 12)
        use_digits: Включать цифры (по умолчанию True)
        use_special: Включать спецсимволы (по умолчанию True)
    
    Returns:
        Сгенерированный пароль
    """
    characters = string.ascii_letters
    
    if use_digits:
        characters += string.digits
    
    if use_special:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def check_password_strength(password):
    """
    Оценивает надёжность пароля.
    
    Args:
        password: Пароль для проверки
    
    Returns:
        Строка с оценкой
    """
    score = 0
    
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    if score < 3:
        return "Weak"
    if score < 4:
        return "Medium"
    return "Strong"


if __name__ == "__main__":
    new_password = generate_password(16)
    print(f"Generated password: {new_password}")
    print(f"Strength: {check_password_strength(new_password)}")

