from rembg import remove
from PIL import Image
from pathlib import Path
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def remove_bg(param):
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

        if param == 2 and input_img.mode not in ('RGBA', 'LA'):
            img_suffix = input_path.suffix
            output_path = f'output/{img_name}_formatted{img_suffix}'
            bg = Image.new('RGB', input_img.size, (255, 255, 255))
            bg.paste(output_img, output_img.split()[-1])
            output_img = bg

        output_img.save(output_path)

        logging.info(f'Formatted: {index + 1}/{len(all_imgs)}')


def main():
    print('Convert final images to png or keep original extensions?\n[1 - png|2 - original]')
    return remove_bg(1 if input() == '1' else 2)


if __name__ == '__main__':
    main()
