# Color Analyzer (Flask & Scikit-learn)

## Overview
Color Analyzer is a web application that analyzes an uploaded image and extracts its dominant colors. It provides a visual representation of the most prominent colors in the image along with their HEX codes and percentage usage. This tool is useful for designers, developers, and artists who need to generate color palettes from images effortlessly.

## Features
- **Automatic Color Extraction**: Uses KMeans clustering to detect dominant colors.
- **Percentage Analysis**: Displays the percentage of each color in the image.
- **Copy HEX Code**: Click on a color box to copy its HEX code to the clipboard.
- **Responsive UI**: Modern and clean design with interactive elements.
- **Fast Processing**: Optimized image resizing for quick color detection.
- **Supports Multiple Image Formats**: Accepts PNG, JPG, and JPEG files.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Image Processing**: OpenCV, NumPy
- **Clustering Algorithm**: Scikit-learn (KMeans)

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- pip (Python package manager)

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/bektas-sari/flask-color-analyzer.git
   cd flask-color-analyzer
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Click on the **Upload Image** button.
2. Select an image from your device.
3. The application automatically extracts the dominant colors.
4. Click on a color box to copy the HEX code.
5. View percentage values to understand the prominence of each color in the image.
6. Upload a new image to analyze different colors.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Added new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, feel free to reach out:
- **Email**: bektas.sari@gmail.com
- **GitHub**: [bektas-sari](https://github.com/bektas-sari)

