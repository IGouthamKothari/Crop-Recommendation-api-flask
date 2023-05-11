from flask import Flask,request,jsonify
import numpy as np
import pickle

model = pickle.load(open('RandomForest.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    data = np.array([[104, 18, 30, 23.603016, 60.3, 6.7, 140.91]])
    prediction = model.predict(data)
    return str(prediction[0])

@app.route('/predict',methods=['POST'])
#['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']
def predict():

    N = request.form.get('N')
    P = request.form.get('P')
    K = request.form.get('K')
    temperature = request.form.get('temperature')
    humidity = request.form.get('humidity')
    ph = request.form.get('ph')
    rainfall = request.form.get('rainfall')

    data = np.array([[N,P,K,temperature, humidity, ph, rainfall]])

    prediction = model.predict(data)

    return jsonify({'crop':str(prediction[0])})
    #return jsonify({'N':str(N),'P':str(P)})



if __name__ == '__main__':
    app.run(debug=True)


