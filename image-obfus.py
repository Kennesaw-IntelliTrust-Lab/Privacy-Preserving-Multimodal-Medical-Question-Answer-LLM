import os
import cv2
import numpy as np

def add_noise_to_image(image):
    """
    Adds random Gaussian noise to an image.
    """
    row, col, ch = image.shape
    mean = 0
    var = 0.1
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    noisy_image = image + gauss * 255
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

def obfuscate_images(input_folder, output_folder):
    """
    Obfuscates all images in the input folder by adding noise and saves them in the output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.dcm')):
            img_path = os.path.join(input_folder, filename)
            image = cv2.imread(img_path)
            
            if image is not None:
                obfuscated_image = add_noise_to_image(image)
                output_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_path, obfuscated_image)
                print(f"Processed and saved: {output_path}")
            else:
                print(f"Could not open image: {img_path}")

if __name__ == "__main__":
    input_folder = "images"
    output_folder = "obfus-images"
    obfuscate_images(input_folder, output_folder)
