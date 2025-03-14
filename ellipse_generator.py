import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Define the output folder path to store the processed images
OUTPUT_FOLDER = 'Ellipses'
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Define input CSV file path
INPUT_CSV = 'output.csv'

try:
    # Read the CSV file containing ellipse parameters
    print("Loading ellipse data...")
    ellipse_info = pd.read_csv(INPUT_CSV)

    # Iterate over each row of the DataFrame
    for index, row in ellipse_info.iterrows():
        # Extract ellipse parameters
        a_original = row['a_predicted']
        b_original = row['b_predicted']

        # Scale ellipse size
        a_scaled = a_original * 0.545 # Adjustable 
        b_scaled = b_original * 0.545

        # Ellipse settings
        ellipse_center = (0, 0)  # Center at origin
        ellipse_angle = 0  # Rotation angle (adjustable)

        # Create figure
        fig, ax = plt.subplots(dpi=300)

        # Plot the predicted ellipse
        ellipse = Ellipse(
            xy=ellipse_center, width=2 * a_scaled, height=2 * b_scaled,
            angle=ellipse_angle, edgecolor='black', fc='None', lw=2, label='Predicted Ellipse'
        )
        ax.add_patch(ellipse)

        # Configure plot appearance
        ax.set_xlim(-75, 75)
        ax.set_ylim(-75, 75)
        ax.set_aspect('equal')
        ax.legend(fontsize=12, loc='center')
        ax.axis('off')

        # Generate output image filename
        output_filename = f'{a_original:.4f}_{b_original:.4f}.png'
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        # Save the image
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()

    print(f"Predicted ellipses saved in: {OUTPUT_FOLDER}")

except FileNotFoundError:
    print(f"Error: Input file '{INPUT_CSV}' not found. Please check the file path.")
except KeyError as e:
    print(f"Error: Missing expected column '{e.args[0]}' in CSV file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
