from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask(__name__,template_folder='templates')


model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def Home():
	return render_template("index.html")

# @app.route('/results')
# def results():


@app.route('/predict_dropbox',methods=['POST'])
def predict_dropbox():
	return render_template('Predict_dropbox.html')


@app.route('/predict', methods=['POST'])
def predict():
	int_features = [int(x) for x in request.form.values()]
	final_features = [np.array(int_features)]
	print(final_features[0][1])
	attendance = final_features[0][1]
	if attendance >= 75:
		final_features[0][1] = 1
	elif attendance < 75:
	 	final_features[0][1] =0  	
	prediction = model.predict(final_features)
	output = round(prediction[0], 2)
	return render_template('index.html', prediction_text='Your GPA Score : {}'.format(output))

if __name__ == '__main__':
	app.run(debug=True)
