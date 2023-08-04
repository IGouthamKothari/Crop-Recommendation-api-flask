# Crop Recommendation API

The Crop Recommendation API is a Flask-based web service that provides intelligent crop recommendations based on various soil parameters. Utilizing machine learning models, it helps farmers make informed decisions about which crops to plant.

## Features

- **Crop Recommendations**: Predicts the best crop based on soil conditions.
- **Fertilizer Prediction**: Suggests the appropriate fertilizer for the soil.
- **Machine Learning Models**: Utilizes Random Forest models for accurate predictions.
- **RESTful API**: Easy-to-use endpoints for integrating with other applications.

## Getting Started

### Prerequisites

- Python 3
- Flask

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/IGouthamKothari/Crop-Recommendqtion-api-flask.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Crop-Recommendqtion-api-flask
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the server:
   ```bash
   python app.py
   ```

5. The API will be available at `http://localhost:5000`.

## API Documentation

### Predict Crop (`POST /predict`)

This endpoint takes soil parameters as input and returns the recommended crop along with the appropriate fertilizer.

- **URL**: `/predict`
- **Method**: `POST`
- **Request Parameters**:
  - `N`: Nitrogen content in the soil.
  - `P`: Phosphorus content in the soil.
  - `K`: Potassium content in the soil.
  - `temperature`: Temperature of the soil.
  - `humidity`: Humidity of the soil.
  - `ph`: pH level of the soil.
  - `rainfall`: Rainfall in the area.

- **Response**: A JSON object containing the recommended crop and fertilizer.

  ```json
  {
    "crops": "Crop Name : Fertilizer"
  }
  ```

### Example Usage

Here's an example of how you can call the `/predict` endpoint using Python:

```python
import requests

data = {
    'N': 80,
    'P': 40,
    'K': 40,
    'temperature': 25,
    'humidity': 60,
    'ph': 6.5,
    'rainfall': 100
}

response = requests.post('http://localhost:5000/predict', data=data)

print(response.json())
```

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.
