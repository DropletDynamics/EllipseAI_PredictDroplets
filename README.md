# EllipseAI_PredictDroplets
Neural network-based model for predicting the semi-axis features of ellipses that encapsulate primary droplet heads.

## Overview  
Within **EllipseAI_PredictDroplets**, you will find a **pretrained neural network-based model** used to predict the **semi-axis values of ellipses** fitted to the heads of droplets identified in images. 

The images can be downloaded from the following repository: [Zenodo Repository](https://zenodo.org/records/13862494).

Additionally, related Python codes for **controlling, capturing, and processing droplet images** can be found in the following repository: [**InkJetDroplet**](https://github.com/DropletDynamics/InkJetDroplet).  

The semi-axis values are predicted based on the **operational parameters** that define the voltage signal used by the **[MicroDrop inkjet dispenser device](https://www.microdrop.de/)**, which was used to generate the predicted droplets.

The same repository also contains a **database** with the **semi-axis values** and the **operational parameters**.

For more details, you can refer to the following research paper: [_Data-Driven Analysis of Droplet Morphology in Inkjet Systems: Toward Generating Stable Single-Drop Regimes_](https://doi.org/10.48550/arXiv.2501.13801).

## Features  

- **Pretrained Neural Network (`model.h5`)** – A trained model designed to predict the **semi-axis values of ellipses** fitted to droplet heads.  

- **Prediction Interface (`predict.py`)** – A script that takes **operational parameters** as input, processes the data, and uses the **pretrained model** to generate predictions, saving the results in a structured CSV file.  

- **Ellipse Visualization (`ellipse_generator.py`)** – A script that reads the **predicted semi-axis values** and generates **visual representations** of the ellipses, saving them as images.

## How to Use  

The **operational parameters** required for prediction must be **pre-stored** in the `input.csv` file. 

The provided `input.csv` is **preloaded with specific parameters**, but these values can be modified as needed. 

For reference on parameter selection, see:  [_Data-Driven Analysis of Droplet Morphology in Inkjet Systems: Toward Generating Stable Single-Drop Regimes_](https://doi.org/10.48550/arXiv.2501.13801).  

To generate predictions, run `predict.py`, which will process `input.csv` and create `output.csv`, containing the **predicted semi-axis values** of ellipses. 

Once `output.csv` is generated, use `ellipse_generator.py` to **plot and visualize the predicted ellipses**. 
This script will read the **predicted values** from `output.csv` and generate **ellipse images**, saving them in an output folder. 

Visualization settings, such as scaling and colors, can be adjusted in `ellipse_generator.py` to match user preferences.  

## How to Cite
If you use **EllipseAI_PredictDroplets**, please cite the following: [EllipseAI_PredictDroplets](https://github.com/AngelaAresdeParga/EllipseAI_PredictDroplets).
