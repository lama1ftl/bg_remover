from rembg import remove
from PIL import Image
from pathlib import Path
import logging


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def remove_bg():
    list_of_extensions = ['*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG', '*.JPEG']
    all_imgs = []

    for ext in list_of_extensions:
        all_imgs.extend(Path('input').glob(ext))

    for index, img in enumerate(all_imgs):
        input_path = Path(img)
        img_name = input_path.stem
        output_path = f'output/{img_name}_formatted.png'

        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)

        logging.info(f'Formatted: {index+1}/{len(all_imgs)}')


if __name__ == '__main__':
    remove_bg()
