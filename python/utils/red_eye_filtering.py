#!/usr/bin/env python3

from utils.image import (
    PackedImage,
)

import utils.eye_pattern as ep

TOO_RED_THRESHOLD = 200
RED_FILTER_VALUE = 150
WHITESPACE_STRING: str = " "

def apply_filtering(image: PackedImage, too_red_pixels_by_index):
    for pixel_index in too_red_pixels_by_index:
        try:
            if image.pixels[pixel_index].red >= TOO_RED_THRESHOLD:
                image.pixels[pixel_index].red = image.pixels[pixel_index].red - RED_FILTER_VALUE
        except:
            #TODO: avoid this
            pass

def find_and_fix_red_eyes_in_each_image(image: PackedImage):

    too_red_pixels_by_index = []

    for index, pixel in enumerate(image.pixels):
        if(pixel.red >= TOO_RED_THRESHOLD):
            for eye_pattern in ep.eye_patterns:
                is_match = True
                too_red_pixels_by_index_local = []

                for ep_row in range(len(eye_pattern)):
                    for ep_cow in range(len(eye_pattern[0])):
                        current_pixel_index = index + ep_cow + ep_row * image.resolution.width

                        try:
                            current_pixel = image.pixels[current_pixel_index]
                        except:
                            # TODO: avoid this
                            pass

                        if eye_pattern[ep_cow][ep_row] != WHITESPACE_STRING:
                            if current_pixel.red >= TOO_RED_THRESHOLD:
                                too_red_pixels_by_index_local.append(current_pixel_index);
                            else:
                                is_match = False
                if is_match:
                    too_red_pixels_by_index.extend(too_red_pixels_by_index_local)

    apply_filtering(image, too_red_pixels_by_index)





