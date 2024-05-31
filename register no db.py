from flask import Flask, flash, redirect, render_template, request, url_for
import math


app = Flask(__name__)
app.secret_key = "donottellanyone"

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/quote', methods=['POST', 'GET'])
def quote():

    if request.method=='POST':
        ship_cost = 50
        print("in post quote")
        shape=request.form['shape']
        width=int(request.form['width'])
        length=int(request.form['length'])
        turf =int(request.form['turf'])
        print("turf", turf)
        if shape == 'rectangle':
            turf_area= length * width
        elif shape == 'triangle':
            turf_area= 0.5 * length * width
        elif shape == 'circle':
            turf_area= (math.pi) * (width/2) * (width/2)
        elif turf_area >= 10:
            ship_cost = 25
        elif turf_area < 10:
            ship_cost = 60
        elif turf_area <= 20:
            ship_cost = 100
        elif turf_area <= 30:
            ship_cost = 145
        
        labor_cost = (turf_area / 5) * 80
        cost_subtotal = turf * turf_area
        total = (labor_cost + cost_subtotal + ship_cost) * 1.1
        print("total", total)
        return render_template('result.html', length = length , width = width , shape = shape, turf = turf,
                               turf_area = turf_area , ship_cost = ship_cost , labor_cost = labor_cost, total = total, cost_subtotal = cost_subtotal)
    else:  #in get process
        print("GET turf quote")
        return render_template('quote.html')
 

@app.route('/guide')
def guide():
    return render_template("guide.html" )

@app.route('/about')
def about():
    return render_template("about.html" )


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        print("in post register")
        user_name = request.form['user_name']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        postcode = request.form['postcode']
        if user_name == "Fred":
            flash('Username already taken!')
            return redirect(url_for("register"))
        else:
            flash('Registeration successful')
            return render_template('register.html')
    else:  #in get process
        print("in get register")
        return render_template('register.html')


if __name__ == "__main__":
    app.run()
