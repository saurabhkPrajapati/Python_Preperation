from PIL import Image

# Open the image file
image_path = '../Access_form.jpg'  # Replace with your image file path
image = Image.open(image_path)

# Convert the image to PDF
pdf_path = '../Access_form.pdf'  # Replace with your desired output file path
image.save(pdf_path, "PDF", resolution=100.0)

print(f"Converted {image_path} to {pdf_path}")
