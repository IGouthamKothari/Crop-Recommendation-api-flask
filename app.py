from flask import Flask,request,jsonify, render_template
import numpy as np
import pickle
import itertools

model = pickle.load(open('RandomForest.pkl','rb'))
fert_model = pickle.load(open('fertilizerPred.pkl', 'rb'))
print("Models Loaded")
app = Flask(__name__)

@app.route('/')
def index():
    print("Working")


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
    variation_range = range(-10, 10, 5)  # -10% to +10% with 1% steps

    # Dictionary to store crop variations
    crop_variations = {}

    # Generate all possible combinations of variations for N, P, and K
    combinations = itertools.product(variation_range, repeat=3)

    # Iterate over the combinations
    for combination in combinations:
        # Compute the percentage variation for N, P, and K
        variation_percentages = 1 + np.array(combination) / 100.0
        varied_data = data.copy()
        # print(varied_data)
        varied_data[:, :3][0] = varied_data[:, :3][0].astype(float) * variation_percentages
        #print((varied_data[:, :3][0]))
        #print(variation_percentages)

        # Perform prediction with the varied input values
        prediction = model.predict(varied_data)
        crop_name = prediction[0]  # Assuming prediction returns a single crop name

        # Store the crop name and corresponding variations in N, P, and K values
        crop_variations[crop_name] = (variation_percentages).tolist()
    crop_list = []
    # Print the crop names and their corresponding variations
    for crop_name, variations in crop_variations.items():
        crop_name = crop_name + ' : '
        ans = fert_model.predict([variations])
        if ans[0] == 0:
            fert = "TEN-TWENTY SIX-TWENTY SIX"
        elif ans[0] == 1:
            fert = "Fourteen-Thirty Five-Fourteen"
        elif ans[0] == 2:
            fert = "Seventeen-Seventeen-Seventeen"
        elif ans[0] == 3:
            fert = "TWENTY-TWENTY"
        elif ans[0] == 4:
            fert = "TWENTY EIGHT-TWENTY EIGHT"
        elif ans[0] == 5:
            fert = "DAP"
        else:
            fert = "UREA"
        crop_name += fert
        crop_list.append(crop_name)
    print(crop_list)
    return jsonify({'crops': crop_list[0]})

if __name__ == '__main__':
    app.run(debug=True)


