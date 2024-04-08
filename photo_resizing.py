import cv2

def resize_image(input_image_path, output_image_path, size):
    # Read the image from file
    image = cv2.imread(input_image_path)
    
    # Resize the image
    resized_image = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
    
    # Save the resized image
    cv2.imwrite(output_image_path, resized_image)
    print(f"The image has been resized to {size} and saved as {output_image_path}")

# Example usage
input_image_path = 'src/my_projects/resent50.png'
output_image_path = 'src/my_projects/resent50_small.png'
size = (400, 300)  # Desired size as (width, height)

resize_image(input_image_path, output_image_path, size)

# import cv2

# image_path = r'C:\vinodjangid07.github.io\src\png\pslogo.png'
# image = cv2.imread(image_path)
# print(image.shape)