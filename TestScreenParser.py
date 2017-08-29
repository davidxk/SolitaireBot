from screenparser import ScreenParser, CardRecognizer
from PIL import Image

p = ScreenParser()
b = p.parse_screenshot('./init.png')
print(b)

b = p.parse_screenshot('./foundation.png')
print(b)

b = p.parse_screenshot('./test1.png')
print(b)

b = p.parse_screenshot('./test2.png')
print(b)

b = p.parse_screenshot('./test3.png')
print(b)

b = p.parse_screenshot('./test4.png')
print(b)
