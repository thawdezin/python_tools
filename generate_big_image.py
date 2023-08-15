from PIL import Image, ImageDraw
import random
from io import BytesIO

target_file_size = 8.5 * 1024 * 1024  # 8.5 MB in bytes

# Initial dimensions for the image (you can adjust these)
width = 78600
height = 78600

# Create a new image with a random gradient background
image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)

# Generate a random gradient
start_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
end_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

for y in range(height):
    r = start_color[0] + (end_color[0] - start_color[0]) * y / height
    g = start_color[1] + (end_color[1] - start_color[1]) * y / height
    b = start_color[2] + (end_color[2] - start_color[2]) * y / height

    draw.line([(0, y), (width, y)], fill=(int(r), int(g), int(b)))

# Save the image with different compression qualities until the desired file size is reached
compression_quality = 95  # Initial compression quality

while True:
    buffer = BytesIO()
    image.save(buffer, format="PNG", quality=compression_quality)
    file_size = buffer.tell()

    if file_size <= target_file_size:
        break

    # Reduce the compression quality to decrease file size
    compression_quality -= 5
    if compression_quality <= 0:
        print("Unable to achieve the desired file size.")
        break

# Save the final image
final_image_path = "output_image.png"
image.save(final_image_path, format="PNG", quality=compression_quality)

print(f"Image saved at: {final_image_path}")
print(f"Actual file size: {file_size / 1024 / 1024:.2f} MB")


