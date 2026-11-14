
import cv2
from pathlib import Path


def analyze_product(image_path):
    image = cv2.imread(str(image_path))

    if image is None:
        print("Error: Unable to load the image.")
        return

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce image noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Detect edges
    edges = cv2.Canny(blurred_image, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    contour_count = 0

    # Analyze and draw contours
    for contour in contours:
        if cv2.contourArea(contour) > 100:
            contour_count += 1

            cv2.drawContours(
                image,
                [contour],
                -1,
                (0, 255, 0),
                2
            )

    # Display analysis results
    print("\nPRODUCT QUALITY INSPECTION")
    print("--------------------------")
    print("Detected contours:", contour_count)

    # Save processed images
    cv2.imwrite("inspection_result.jpg", image)
    cv2.imwrite("detected_edges.jpg", edges)

    print("Image analysis completed successfully.")
    print("Results saved to the project folder.")

    # Display the processed image
    cv2.imshow("Product Quality Inspection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    print("PRODUCT QUALITY INSPECTION SYSTEM")

    image_path = r"C:\Users\jexym\product.jpg.jpg"

    if Path(image_path).is_file():
        analyze_product(image_path)
    else:
        print("Error: Image file not found.")


if __name__ == "__main__":
    main()
