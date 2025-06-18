from flask import Flask, render_template, request, redirect, url_for, session
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Loading Model
model_path = os.path.join("Models", "brain_tumor_finetuned.keras")
model = load_model(model_path)

# Class Labels
labels = ['glioma', 'meningioma', 'notumor', 'pituitary']

# Upload Directory
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        img_file = request.files.get("file")
        if img_file and img_file.filename != "":
            try:
                # File Path
                img_path = os.path.join(UPLOAD_FOLDER, img_file.filename)
                img_file.save(img_path)

                img = image.load_img(img_path, target_size=(224, 224))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array = preprocess_input(img_array)

                # Prediction
                prediction = model.predict(img_array)
                predicted_class = labels[np.argmax(prediction)]

                session["result"] = f"Prediction Class: <b>{predicted_class.capitalize()}</b>"
                return redirect(url_for("index"))

            except Exception as e:
                session["result"] = f"<b>Error:</b> Failed to upload image <br>{str(e)}"
                return redirect(url_for("index"))

    if "result" in session:
        result = session.pop("result")

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
