from flask import Flask, render_template, request
import json 




app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():

    return render_template('home.html')




@app.route('/profile/<password>', methods=['POST', 'GET'])
def profile(password):

    if password == "root":
        
        if request.method == 'POST':
            with open('./static/data/profile.json') as json_file:
                data = json.load(json_file)

            name = request.form["Name"]
            company = request.form["Company"]
            email = request.form["Email"]
            phone = request.form["Phone"]

            data['profile'].append({
                
            'name': name,
            'company': company,
            'email': email,
            'phone': phone

            })

            with open('./static/data/profile.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)


            return render_template('profile.html')

    return render_template('profile.html')




@app.route('/card', methods=['GET','POST'])
def card():

    with open('./static/data/card.json') as json_file:
        data = json.load(json_file)
    cards = data

    if request.method == 'POST':

        name = request.form["Name"]
        company = request.form["Company"]
        email = request.form["Email"]
        phone = request.form["Phone"]

        data['card'].append({
            
        'name': name,
        'company': company,
        'email': email,
        'phone': phone

        })

        with open('./static/data/card.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)


        return render_template('card.html',cards=cards)

    return render_template('card.html',cards=cards)




app.run("127.0.0.1",5000)