from screenparser import ScreenParser, CardRecognizer
from PIL import Image

p = ScreenParser()
b = p.parse_screenshot('./init.png')
print(b)
