"""
    Example usage:
    python preprocess-annotations.py data/train annotation-small.json annotation-small3.json
    
    Creates a new annotation file with the following changes:
    1. Changes the building category id from 100 to 1.
    2. Updates the bounding box field for each annotation using the extremity of the segmentation field.
"""

import sys
import json
import numpy as np
from matplotlib.path import Path
import pathlib

def main(data_dir, annotation_file_orig, annotation_file_dest):
  
    with open( data_dir + "/" + annotation_file_orig, "r") as f:
        annotations = json.load(f)
        
    annotations_new = annotations.copy()
    
    # Change the category id, so that this works well with Ice Vision.
    annotations_new['categories'][0]['id'] = 1
    
    for annotation in annotations_new['annotations']:
        extents = Path(np.array(annotation['segmentation']).reshape((-1, 2))).get_extents()
        # coco bounding box format from here: https://github.com/airctic/icedata/tree/master/icedata/datasets/coco
        #(x-top left, y-top left, width, height)
        annotation['bbox'] =[extents.xmin, extents.ymin, extents.xmax-extents.xmin, extents.ymax-extents.ymin ]

        # Also change the category id, so that this works well with Ice Vision.
        annotation['category_id'] = 1

    # Recreate the new annotations file.
    pathlib.Path(data_dir + "/" + annotation_file_dest).unlink(missing_ok=True)
    
    with open(data_dir + "/" + annotation_file_dest, "w") as f:
        json.dump(annotations_new, f)
        
if __name__ == "__main__":
    data_dir = sys.argv[1]
    annotation_file_orig = sys.argv[2]
    annotation_file_dest = sys.argv[3]
    
    main(data_dir, annotation_file_orig, annotation_file_dest)