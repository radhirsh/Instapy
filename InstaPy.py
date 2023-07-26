from PIL import Image, ImageEnhance

def apply_instagram_filter(image_path, tint_color):
    # Open the image
    image = Image.open(image_path)

    # Apply a tint to the image
    r, g, b = tint_color
    image = ImageEnhance.Color(image).enhance(1.3)  # Enhance color saturation
    image = ImageEnhance.Brightness(image).enhance(1.1)  # Enhance brightness
    image = ImageEnhance.Contrast(image).enhance(1.2)  # Enhance contrast
    image = ImageEnhance.Sharpness(image).enhance(1.1)  # Enhance sharpness
    image = Image.blend(image, Image.new("RGB", image.size, (r, g, b)), alpha=0.3)

    return image

def main():
    # Replace 'path/to/your/image.jpg' with the path to your image
    image_path = "Type your file  path here"

    # Define the tint color (you can adjust the values for different effects)
    pinkish_tint = (255, 182, 193)

    # Apply the Instagram filter
    filtered_image = apply_instagram_filter(image_path, pinkish_tint)

    # Display the original and filtered images
    filtered_image.show()

if __name__ == "__main__":
    main()
