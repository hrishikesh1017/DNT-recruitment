import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def convolve2d(image, kernel):
    kernel = np.flipud(np.fliplr(kernel))
    output = np.zeros_like(image)
    image_padded = np.pad(image, (1, 1), 'constant', constant_values=(0))

    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            output[y, x] = (kernel * image_padded[y:y+3, x:x+3]).sum()

    return output


def sobel_edge_detection(image):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # Apply Sobel operators
    gradient_x = convolve2d(image, sobel_x)
    gradient_y = convolve2d(image, sobel_y)

    # Compute edge magnitude
    edge_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

    # Normalize edge magnitude to the range [0, 255]
    edge_magnitude = (edge_magnitude / edge_magnitude.max()
                      * 255).astype(np.uint8)

    return edge_magnitude


# Load the JPEG image
image_path = 'thug duck.jpeg'  # Replace with your image path
input_image = Image.open(image_path)
gray_image = input_image.convert('L')  # Convert to grayscale

# Convert the grayscale image to a NumPy array
image_array = np.array(gray_image)

# Apply edge detection
edge_map = sobel_edge_detection(image_array)

# Display the original image and the edge map
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(image_array, cmap='gray')
plt.title('Original Grayscale Image')

plt.subplot(1, 2, 2)
plt.imshow(edge_map, cmap='gray')
plt.title('Edge Map')

plt.tight_layout()
plt.show()
