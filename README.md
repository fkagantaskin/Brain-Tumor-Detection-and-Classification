# Brain Tumor Classification (Using MRI Images)

This project is designed to classify brain tumors using **MRI images**. With the help of deep learning techniques, a model was developed to determine whether there is a tumor in an MRI image and, if so, to classify it into one of the following categories:  
**Glioma**, **Meningioma**, **Pituitary**, and **No Tumor**.

## Dataset Used
- Source: [Kaggle Brain Tumor MRI Dataset]
- Classes:  
   - Glioma  
   - Meningioma  
   - Pituitary  
   - No Tumor

The dataset is split into training, testing, and validation sets. (The validation folder was created randomly through code.)

## Technologies and Methods Used
   - Python
   - TensorFlow / Keras
   - MobileNetV2 (Transfer Learning)
   - Data Augmentation
   - Flask (for Web Interface)
   - NumPy, Matplotlib, Sklearn

## Model Training
The model was first trained as a simple baseline version, and then enhanced with the following improvements to increase accuracy (improved version):
   - Transfer learning was applied using the pretrained MobileNetV2 model.
   - Image diversity was increased via rotation, zooming, and shifting techniques.
   - Early stopping was implemented using a validation set.

   > Model Accuracy:
      - Improved Model: ~98.7%
(Detailed training graphs and classification reports are included in the submitted files.)

## Web Interface (Flask Application)
A web interface was developed within the project, allowing users to upload their own MRI images and instantly receive predictions.

### How to Use:
1. Run the `app.py` file:
   ```bash
   python app.py
   ```
2. Open the address http://127.0.0.1:5000/ in your browser.
3. Upload your MRI image and click the "Predict" button.
4. The model's prediction will be displayed on the screen.

### Notes:

* The `uploads/` folder is automatically created during runtime, and images submitted through the browser for prediction are temporarily saved in this folder.