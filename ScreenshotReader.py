from PIL import Image
from pytesseract import pytesseract

TES_PATH = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
IMAGE_PATH = "KOTCscreenshot.png"

def screenshot_to_string(tesseract_path: str, screenshot: str) -> str:
    # Opening the image & storing it in an image object 
    image = Image.open(screenshot)
    
    # Providing the tesseract executable 
    # location to pytesseract library 
    pytesseract.tesseract_cmd = tesseract_path 
    
    # Passing the image object to image_to_string() function 
    # This function will extract the text from the image 
    text = pytesseract.image_to_string(image) 

    return text[:-1]
    
    # Displaying the extracted text 
    #print(text[0:-1])