import os
import numpy as np
from skimage import io, filters, exposure
from tqdm import tqdm
import matplotlib.pyplot as plt

def process_images(input_folder, output_folder, border_thickness=3):
    # test_folder = output_folder + "/test"
    os.makedirs(output_folder, exist_ok=True)
    # os.makedirs(test_folder, exist_ok=True)
    image_files = sorted([os.path.join(input_folder, filename) for filename in os.listdir(input_folder)])

    for i, image_path in enumerate(tqdm(image_files, desc="Processing")):
        output_filename = f"{i:05d}.png"
        image = io.imread(image_path, as_gray=True).astype(np.uint8)

        sato_result = filters.sato(image, black_ridges=True, sigmas=range(1, 5), mode="reflect", cval=0)
        sato_result = exposure.rescale_intensity(sato_result, out_range=(0, 255)).astype(np.uint8)
        # sato_result = sato_result.astype(np.uint8)

        # io.imsave(os.path.join(test_folder, output_filename), sato_result)

        h, w = sato_result.shape
        for x in range(h):
            for y in range(w):
                if x < border_thickness or x >= h - border_thickness or y < border_thickness or y >= w - border_thickness:
                    sato_result[x, y] = 0

        
        io.imsave(os.path.join(output_folder, output_filename), sato_result)
        

    print("Done.")
