import numpy as np
from PIL import Image

def ex4(image_array: np.ndarray, offset: tuple, spacing: tuple):

    if not isinstance(image_array, np.ndarray):
        raise TypeError('image_array is not a numpy array')

    if image_array.ndim != 3:
        raise NotImplementedError('image_array doesn\'t have 3 dimensions')

    if image_array.shape[2] != 3:
        raise NotImplementedError('image_array 3rd dimensions is not equal to 3')

    if not type(offset[0]) is int or not type(offset[1]) is int:
        raise ValueError('Offset does not contain integers')

    if not type(spacing[0]) is int or not type(spacing[1]) is int:
        raise ValueError('Spacing does not contain integers.')

    if not 0 <= offset[0] <= 32 or not 0 <= offset[1] <= 32:
        raise ValueError('Offset smaller than 0 or larger than 32')

    if not 2 <= spacing[0] <= 8 or not 2 <= spacing[1] <= 8:
        raise ValueError('Spacing smaller than 2 or larger than 8')

    known_array = np.array(image_array, copy=True)

    image_array[:offset[0], :, :] = 0
    image_array[:, :offset[1], :] = 0

    shp = len(image_array[:, :10, :].flatten()) + len(image_array[:10, :, :].flatten())

    target_array = np.zeros_like(image_array)

    for k in range(0, image_array.shape[1], spacing[0]):
        for n in range(0, image_array.shape[0], spacing[1]):
            target_array[n, :, :] = image_array[n, :, :]
            image_array[n, :, :] = 0

    for n in range(0, image_array.shape[0], spacing[0]):
        for k in range(0, image_array.shape[1], spacing[1]):
            target_array[:, k, :] = image_array[:, k, :]
            image_array[:, k, :] = 0


    #target_array = image_array[known_array == 1].copy()

    return np.transpose(image_array, (2, 0, 1)), known_array, target_array

"""image = Image.open('img.jpg')
data = np.asarray(image)

img2 = ex4(data, (2, 4), (3, 3))

img2 = Image.fromarray(data)

img2.save('img2.jpg')

image = Image.open('img.jpg')
data = np.asarray(image)

img2, img3 = ex4(data, (2, 4), (3, 3))
print(img3.shape)
img3 = Image.fromarray((img3 * 255).astype(np.uint8))

img3.save('img3.jpg')
print(img2.shape)"""
