"""
Author: Medis Redzic
Matr.Nr.: K11934616
Exercise: Exercise 2
"""

import os
import glob
from PIL import Image, ImageStat
import numpy as np
import hashlib
import shutil


def write_log(log_file: str, filename: str, errornum: int):
    with open(log_file, 'a') as f:
        f.write(f'{filename};{errornum}\n')


def validate_images(input_dir: str,output_dir: str,log_file: str,formatter: str = ''):
    current_image = 0
    copied_images = []
    abs_path = os.path.abspath(input_dir)
    #input_dir_sorted = sorted(glob.glob(os.path.join(input_dir, '**', '*.jpg'), recursive=True))
    input_dir_sorted = sorted([log for log in glob.glob(pathname=abs_path + '/**/*', recursive=True) if not os.path.isdir(log)])

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(log_file, 'w'):
        pass

    for img in input_dir_sorted:
        file_name = os.path.basename(img)

        if not img.endswith(('.jpg', '.JPG', '.jpeg', '.JPEG')):
            # print('Image does not end with allowed extensions')
            write_log(log_file, file_name, 1)
            continue

        if os.path.getsize(img) > 250000:
            # print('Image can not exceed 250kB ', file_name)
            write_log(log_file, file_name, 2)
            continue

        try:
            with Image.open(img) as im:
                if not im.width and im.height >= 96:
                    # print('Width or height is below 96 pixels')
                    write_log(log_file, file_name, 4)
                    continue

                if not im.mode == 'RGB':
                    # print('Image must be an RGB image')
                    write_log(log_file, file_name, 4)
                    continue

                i_array = np.asarray(im)

                if ImageStat.Stat(im).var <= [0, 0, 0]:
                    write_log(log_file, file_name, 5)
                    continue

                h, w, ch = i_array.shape
                if h < 96 or w < 96:
                    write_log(log_file, file_name, 4)
                    continue

                pil_img = Image.fromarray(i_array)
                img_name = f'{current_image:{formatter}}'.format(number=current_image) + '.jpg'
                flatten_image = i_array.flatten()
                hash_img = hashlib.md5(str(flatten_image).encode()).hexdigest()

                if hash_img in copied_images:
                    # print('Image has already been copied')
                    write_log(log_file, file_name, 6)
                    continue

                copied_images.append(hash_img)
                #pil_img.save(fp=os.path.join(output_dir, img_name))
                #print(os.path.join(output_dir))
                shutil.copy(img, os.path.join(output_dir, img_name))
                current_image += 1

        except OSError:
            # print('Image can not be opened with PIL module')
            write_log(log_file, file_name, 3)
            continue

    return len(copied_images)


###########################################################################
if __name__ == '__main__':
    print('----------------------------------------------------------')
    validate_images(input_dir='unittest/unittest_input_8',
                    output_dir='unittest/outputs/unittest_input_8',
                    log_file='unittest/outputs/unittest_input_8.log',
                    formatter='06d')