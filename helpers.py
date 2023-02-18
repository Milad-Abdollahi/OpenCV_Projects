from pathlib import Path
import requests


def dl_photos(filename: str,
              url: str,
              photos_dir_path=Path('photos')):
    if Path(photos_dir_path / filename).is_file():
        print(f'{filename} already exists')
    else:
        with open(photos_dir_path / filename, 'wb') as f:
            request = requests.get(url)
            f.write(request.content)
            print(f'{filename} downloaded to photos')


def main():
    print('test.py running')
    dl_photos('park.jpg',
            'https://github.com/jasmcaus/opencv-course/raw/master/Resources/Photos/park.jpg')




if __name__ == '__main__':
    main()
