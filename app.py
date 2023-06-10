from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/data-endpoint', methods=['POST'])
def receive_data():
    device_data = request.form.get('deviceData')
    # Këtu mund të bëni diçka me të dhënat e pajisjes të marra nga klienti

    return "Të dhënat e pajisjes u pranuan me sukses!"

if __name__ == '__main__':
    app.run()
