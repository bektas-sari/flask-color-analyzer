from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from collections import Counter
from sklearn.cluster import KMeans
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define the upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Convert RGB color to HEX format
def rgb_to_hex(rgb):
    """Convert RGB values to HEX format."""
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

# Check if the uploaded file has a valid format
def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Analyze the dominant colors in an image
def analyze_image(image_path, k=10):
    """Analyze the dominant colors in an image and generate a complete color map."""
    
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # If the image cannot be read, raise an error
    if image is None:
        raise ValueError("The image could not be read! Please upload a valid image.")

    # Resize the image for faster processing
    image = cv2.resize(image, (200, 200))
    
    # Convert to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = image.reshape(-1, 3)

    # Use KMeans to find dominant colors
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)
    
    # Identify colors and their frequency
    colors = kmeans.cluster_centers_.astype(int)
    color_counts = Counter(kmeans.labels_)
    
    # Sort colors by frequency
    sorted_colors = sorted(
        zip(colors, color_counts.values()), key=lambda x: x[1], reverse=True
    )

    total_pixels = sum(color_counts.values())  # Calculate the total number of pixels

    # Get the top 5 most dominant colors and their percentages
    top_5_colors = [color[0] for color in sorted_colors[:5]]
    top_5_hex = [rgb_to_hex(color[0]) for color in sorted_colors[:5]]
    top_5_percents = [round((color[1] / total_pixels) * 100, 2) for color in sorted_colors[:5]]

    # Get other colors and their percentages
    other_colors = [color[0] for color in sorted_colors[5:]]
    other_hex = [rgb_to_hex(color[0]) for color in sorted_colors[5:]]
    other_percents = [round((color[1] / total_pixels) * 100, 2) for color in sorted_colors[5:]]

    # Combine data to send to the template
    top_5_combined = list(zip(top_5_colors, top_5_hex, top_5_percents))
    other_combined = list(zip(other_colors, other_hex, other_percents))

    return top_5_combined, other_combined

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Image upload and analysis
@app.route("/upload", methods=["POST"])
def upload_file():
    """Handle image upload and analysis."""
    if "image" not in request.files:
        return "No file uploaded!"
    
    file = request.files["image"]

    if file.filename == "":
        return "No file selected!"

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)  # Save the uploaded file

        # Analyze the uploaded image
        try:
            top_5_combined, other_combined = analyze_image(file_path)
        except ValueError as e:
            return str(e)

        return render_template(
            "result.html", 
            top_5_combined=top_5_combined, 
            other_combined=other_combined
        )

    return "Invalid file type!"

# Start the Flask application
if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the uploads folder if it does not exist
    app.run(debug=True)
