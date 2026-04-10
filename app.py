from flask import Flask, jsonify, request
import requests

from password_generator import generate_password

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def get_password():
    try:
        # Получаем параметры из URL (например, ?length=16)
        length = int(request.args.get('length', 12))
        
        # Вызываем вашу функцию, которую мы импортировали!
        password = generate_password(length=length, use_digits=True, use_special=True)
        
        return jsonify({"password": password})
    except ValueError:
        return jsonify({"error": "Длина пароля (length) должна быть числом"}), 400

@app.route('/', methods=['GET'])
def index():
    service_one_message = "Не удалось подключиться к Сервису 1"
    service_one_status = "error"
    service_two_message = "Не удалось подключиться к Сервису 2"
    service_two_status = "error"

  
    try:
        response1 = requests.get('http://service_one:5000/')
        if response1.status_code == 200:
            service_one_message = response1.json().get('message', 'Нет сообщения')
            service_one_status = "ok"
    except requests.exceptions.ConnectionError:
        pass

    
    try:
        response2 = requests.get('http://service_two:5000/')
        if response2.status_code == 200:
            service_two_message = response2.json().get('message', 'Нет сообщения')
            service_two_status = "ok"
    except requests.exceptions.ConnectionError:
        pass

    
    return jsonify({
        "main_app": "Password Generator API is running",
        "microservices_status": {
            "service_one": { "status": service_one_status, "message": service_one_message },
            "service_two": { "status": service_two_status, "message": service_two_message }
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
