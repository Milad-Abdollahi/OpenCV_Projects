from helpers import dl_photos
import requests
from pathlib import Path
url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'


haar_cascade_path = Path('haar_face.xml')


if haar_cascade_path.is_file():
    print(f'{haar_cascade_path} already exists')
else:
    with open(haar_cascade_path, 'wb') as f:
        request = requests.get(url)
        f.write(request.content)


dl_photos('group1.jpg',
          'https://raw.githubusercontent.com/jasmcaus/opencv-course/master/Resources/Photos/group%201.jpg')
