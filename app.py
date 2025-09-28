from flask import Flask,render_template,request,send_file
import csv
app = Flask('__name__')

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email_address = request.form['email_address']
    subject = request.form['subject']
    phone = request.form['phone']
    message = request.form['message']


    with open('c_data.csv','a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, email_address, subject, phone, message])
    return render_template('index.html')

@app.route('/data')
def data():
    return send_file('c_data.csv',as_attachment=True)

if __name__ == "__main__":
    app.run()