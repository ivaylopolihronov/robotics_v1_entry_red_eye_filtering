#!/usr/bin/env python3

import utils.eye_pattern as ep
import utils.red_eye_filtering as ref

from typing import (
    List,
    Tuple,
    Union
)

from utils.image import (
    ImageType,
    PackedImage,
    StrideImage,
)

from utils.function_tracer import FunctionTracer

def compute_solution(images: List[Union[PackedImage, StrideImage]]):
    ft = FunctionTracer("compute_solution", "seconds")

    for i in images:
        ref.find_and_fix_red_eyes_in_each_image(i)

    del ft
            