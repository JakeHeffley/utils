#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for converting two-photon data stored as a large single page tiff file to multiple files containing multipage tiff files. 

Created on Fri Nov 12 14:32:43 2021

@author: jake
"""

import tifffile


# path to single page tiff file to be converted 
fname = 'training2_moco.tif'  
 # number of frames in each individual output file
L = 4000 

with tifffile.TiffFile(fname) as tffl:
    T = tffl.series[0].shape[0] #total number of frames in original movie
    full_movie = tffl.asarray(out='memmap')
    
    for slice_start in range(0,T,L):
        
        if slice_start + L > T:
            this_slice  = slice(slice_start, T+1)
        else:
            this_slice = slice(slice_start, slice_start+L)
        
        fileparts = fname.split(".")
        this_batch = full_movie[this_slice]
  
        with tifffile.TiffWriter((".").join(fileparts[:-1]) + '_' + str(slice_start//L) + '.' + fileparts[-1]) as tffw:
            tffw.save(this_batch)
            