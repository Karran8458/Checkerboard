from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def hello_world():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('checkerboard.html')  
    
@app.route('/4')
def dojo():
	return render_template('checkerboard1.html')
	
@app.route('/<x>/<y>')
def yella(x,y):
	num1 = int(x)
	num2 = int(y)
	num1 = num1/2
	num2 = num2/2
	nu1 = int(num1)
	nu2 = int(num2)
	return render_template('checkerboard2.html', number1 = nu1, number2 = nu2)

if __name__=="__main__":
    app.run(debug=True)       
