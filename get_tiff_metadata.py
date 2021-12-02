#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:41:10 2021

@author: jake
"""

# import json
from ScanImageTiffReader import ScanImageTiffReader


def get_tiff_metadata(this_f, key_to_extract=None):
    """
    Converts the metadata of a tiff collected via ScanImage from a long string into a dictionary with key:value pairs. 

    Parameters
    ----------
    this_f : string
        filename of the tiff.
    key_to_extract : String, optional
        Keys of specific metadata to extract. The default is None. If None then the function will return all key:value pairs

    Returns
    -------
    full_dict : dictionary of strings
        All key:value pairs within the dictionary of metadata
    extracted_dict : dictionary of strings
        Only the key:value pairs in key_to_extract

    """
    meta_data = ScanImageTiffReader(this_f).metadata()
    full_dict = {}
    for this_item in meta_data.split('\n'):
        if len(this_item.split('=')) == 2:
            full_dict[this_item.split('=')[0].strip()] = this_item.split('=')[1].strip() 
    
    if key_to_extract is None:
        return full_dict
    else:
        extracted_dict = {key: full_dict[key] for key in full_dict.keys()
                                   & key_to_extract}
        return extracted_dict
        
    # todo - switch to a with/as syntax. Problem: using the suggested syntax causes the kernel to restart
    # with ScanImageTiffReader(this_f) as reader:
    #     cc = reader.description(0)
    #     o=json.loads(reader.metadata())
    #     print(o["RoiGroups"]["imagingRoiGroup"]["rois"]["scanfields"]["affine"])