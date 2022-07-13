"""
    Cache the parsed annotations since this can take some time.
    
    Example usage:
    python cache-records.py data/val annotation-small3.json cache-records3.p
"""
from icevision.all import *
from icevision import data

def main(data_dir, annotation_file, cache_file):
    data_splitter = data.SingleSplitSplitter()
    if data_dir == "data/train":
        data_splitter=RandomSplitter([0.8, 0.2], seed=42)
    # Create the parser
    parser = parsers.COCOBBoxParser(annotations_filepath= data_dir + "/" + annotation_file, img_dir= data_dir +  "/images")

    parser.parse(data_splitter=data_splitter, cache_filepath= data_dir + "/" + cache_file)

if __name__ == "__main__":
    data_dir = sys.argv[1]
    annotation_file = sys.argv[2]
    cache_file = sys.argv[3]
    
    main(data_dir, annotation_file, cache_file)