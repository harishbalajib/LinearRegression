
# Linear Regression Model Deployment with Flask

This project demonstrates the deployment of a Ridge regression model using Flask. The application serves predictions via a web interface and an API endpoint, enabling users to input data and receive predictions in real-time.

## Project Structure
- `application.py`: The main Flask application file that handles requests, loads the model and scaler, and renders the web pages.
- `models/ridge.pkl`: The pre-trained Ridge regression model saved as a pickle file.
- `models/scaler.pkl`: The standard scaler for feature scaling, also saved as a pickle file.
- `templates/index.html`: HTML file for the main user interface.

## Prerequisites
- Python 3.x
- Flask
- Scikit-learn
- Pandas, Numpy
- Pickle (for loading model files)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/harishbalajib/LinearRegression.git
    cd LinearRegression
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure the `models` directory contains the `ridge.pkl` and `scaler.pkl` files for the model and scaler, respectively.

## Running the Application
Start the Flask application with:
```bash
python application.py
```
This will start a local server. Open a browser and navigate to `http://127.0.0.1:5000/` to access the web interface.

## Usage
1. **Web Interface**: The main page allows you to input data for predictions. Enter the data in the form fields and submit to get predictions from the Ridge regression model.
2. **API Endpoint**: You can also send a POST request to the `/predict` endpoint with JSON data to receive predictions.

## Example API Request
Send a JSON payload to `http://127.0.0.1:5000/predict` in the following format:
```json
{
  "feature1": value1,
  "feature2": value2
}
```

## Contributing
Feel free to open issues or submit pull requests with improvements or new features.

## License
This project is licensed under the MIT License.
