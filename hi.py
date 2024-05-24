
import pytesseract
from PIL import Image
# importing modules
import urllib.request


#url



urllib.request.urlretrieve( 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.hrcabin.com%2Fsample-filled-form-15g-15h-for-pf-withdrawal%2F&psig=AOvVaw0vBWpsYLmeWVvP5bnA5k2C&ust=1716022062335000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNj3872mlIYDFQAAAAAdAAAAABAy', "gfg.png")
urllib.request.urlretrieve(my_url, "logo.png")
# Open the image file

image = Image.open()

# Perform OCR using PyTesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
