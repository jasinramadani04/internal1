import requests

def get_device_data():
    # Këtu mund të vendosni kodin për të marrë të dhënat e pajisjes si foto, video, etj.
    # Përdorni libraritë e pajisjes ose librari të tjera për të marrë të dhënat e nevojshme.

    device_data = {
        'photos': [],  # Lista e fotove të marra nga pajisja
        'videos': [],  # Lista e videove të marra nga pajisja
        # Shtoni më shumë të dhëna nëse dëshironi
    }

    return device_data

def send_data_to_website(data):
    # Këtu duhet të vendosni kodin për t'u lidhur me ueb sajtin dhe dërgimin e të dhënave.
    # Përdorni libraritë për të bërë kërkesa HTTP/HTTPS dhe dërgoni të dhënat në ueb sajtin.

    # P.sh., mund të përdorni libraritë requests ose urllib për të bërë kërkesa HTTP/HTTPS.
    # Kujdesuni të dërgoni të dhënat në formë të sigurtë dhe të koduara nëse është e nevojshme.

    response = requests.post('https://www.example.com/data', json=data)
    if response.status_code == 200:
        print('Të dhënat janë dërguar me sukses në ueb sajtin.')
    else:
        print('Ka ndodhur një gabim gjatë dërgimit të të dhënave.')

def main():
    # Këtu fillon ekzekutimi i programit

    # Kërkoni lejen e përdoruesit për të pasur qasje në të dhënat e pajisjes
    user_input = input('A jeni i gatshëm të lejoni qasje në të dhënat e pajisjes? (po/jo): ')

    if user_input.lower() == 'po':
        device_data = get_device_data()
        send_data_to_website(device_data)
    else:
        print('Nuk është dhënë leje për të pasur qasje në të dhënat e pajisjes.')

if __name__ == '__main__':
    main()

