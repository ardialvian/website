from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/licenses')
def licenses():
    return render_template('licenses.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/catering')
def catering():
    return render_template('catering.html')

@app.route('/keamanan')
def keamanan():
    return render_template('keamanan.html')

@app.route('/pengadaan')
def pengadaan():
    return render_template('pengadaan.html')

@app.route('/transportasi')
def transportasi():
    return render_template('transportasi.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
