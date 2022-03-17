"""
Author: Medis Redzic
Matr.Nr.: K11934616
Exercise: Exercise 3
"""

import os
import glob
import numpy as np
from PIL import Image


class ImageStandardizer:

    def __init__(self, input_dir: str):
        self.input_abs = os.path.abspath(input_dir)
        self.files = []
        self.mean = None
        self.std = None

        self.files = (os.path.abspath(f) for f in glob.glob(os.path.join(self.input_abs, '**', '*.jpg'),
                                                            recursive=True))
        if not self.files:
            raise ValueError('There are no .jpg files')

        self.files = sorted(self.files)

    def analyze_images(self):
        red_ms = [0, 0]
        green_ms = [0, 0]
        blue_ms = [0, 0]
        len_files = len(self.files)

        for f in self.files:
            with Image.open(f) as img:
                img_as_arr = np.asarray(img)

                for i in range(img_as_arr.shape[0]):
                    for j in range(img_as_arr.shape[1]):
                        r, g, b = img_as_arr[:, :, 0], img_as_arr[:, :, 1], img_as_arr[:, :, 2]

                red_ms[:] = red_ms[0] + r.mean(), red_ms[1] + r.std()
                green_ms[:] = green_ms[0] + g.mean(), green_ms[1] + g.std()
                blue_ms[:] = blue_ms[0] + b.mean(), blue_ms[1] + b.std()

        self.mean = np.array([red_ms[0]/len_files, green_ms[0]/len_files, blue_ms[0]/len_files],
                             dtype=np.float64)

        self.std = np.array([red_ms[1]/len_files, green_ms[1]/len_files, blue_ms[1]/len_files],
                            dtype=np.float64)

        return self.mean, self.std

    def get_standardized_images(self):

        if self.mean is None or self.std is None:
            raise ValueError('self.mean or self.std are None')

        for file in self.files:
            with Image.open(file) as img:
                np_image = np.asarray(img, dtype=np.float32)
            np_image[::] = (np_image - self.mean) / self.std

            yield np_image
