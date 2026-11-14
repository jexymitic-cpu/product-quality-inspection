# product-quality-inspection
Beginner Python computer vision project using OpenCV for product image analysis.
# Product Quality Inspection System

## Project Description

Product Quality Inspection System is a beginner-friendly Python project that uses the OpenCV library to analyze product images.

The program detects edges and contours in an image, highlights detected contours in green, and saves the processed results.

This project was developed as part of my Python programming practice while studying AI & Machine Learning at ITAcademy.

## Features

- Load and analyze product images
- Convert images to grayscale
- Reduce image noise using Gaussian Blur
- Detect edges using the Canny algorithm
- Find and count significant contours
- Highlight detected contours in green
- Save processed images automatically
- Display the analysis results

## Technologies Used

- Python
- OpenCV (`cv2`)
- Python `pathlib` module

## Installation

Install the required OpenCV library:

```bash
pip install opencv-python
```

## How to Run

1. Download or clone this repository.
2. Open the project in Visual Studio Code.
3. Add a product image to your computer.
4. Update the `image_path` variable in the `main()` function to match your image location.
5. Run the Python program:

```bash
python product_quality_inspection.py
```

6. View the analysis results.

## Output

The program generates two image files:

- `inspection_result.jpg` — original image with detected contours highlighted in green.
- `detected_edges.jpg` — image showing detected edges.

The terminal also displays the number of detected contours.

## How It Works

1. The program loads the selected image.
2. The image is converted to grayscale.
3. Gaussian Blur reduces image noise.
4. Canny edge detection identifies image edges.
5. OpenCV finds contours.
6. Contours with an area greater than 100 pixels are counted and highlighted.
7. The processed images are saved and the result is displayed.

## Project Limitations

This is a basic computer vision demonstration, not a fully automated industrial quality inspection system.

The program detects image contours but does not automatically classify products as defective or non-defective.

## Future Improvements

- Add automatic image resizing
- Improve contour filtering
- Support multiple product images
- Add configurable detection parameters
- Explore machine learning for defect classification

## Learning Objectives

This project helped me practice Python functions, image processing, file handling, and basic computer vision techniques.

## Author
Jelena Cajic biginer student 
AI & Machine Learning Student — ITAcademy

GitHub: https://github.com/jexymitic-cpu
