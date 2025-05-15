from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Sample data for demonstration
energy_data = []

@app.route('/')
def index():
    return render_template('index.html', energy_data=energy_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        email = request.form['email']
        password = request.form['password']
        # For demonstration, just flash a message
        flash(f'Logged in as {email}')
        return redirect(url_for('index'))
    return render_template('auth/login.html')

@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # For demonstration, just flash a message
        flash(f'Registered as {name}')
        return redirect(url_for('login'))
    return render_template('auth/register.html')

@app.route('/track', methods=['POST'])
def track_energy():
    appliance = request.form['appliance']
    energy = request.form['energy']
    date = request.form['date']
    energy_data.append({'appliance': appliance, 'energy': energy, 'date': date})
    flash('Energy data added successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
