#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:03:10 2021
@author: jake
"""

from inspect import currentframe, getframeinfo, getouterframes
import time
def my_debug_func(user_message=None, frameinfo=None, time_stamp=None):
    """
    function to print frame information about a script or function as it runs. 
    
    Parameters
    ----------
    frameinfo : frame obj, optional
        pass in a frame object from inspect module else it will use the next higher frame
    user_message : string, optional
        custom message to print in addition to contextual info

    Returns
    -------
    Prints info about the frame currently being executed.

    """
    if frameinfo == None:
        frameinfo = getouterframes(currentframe())[1]
    else:
        frameinfo = getframeinfo(currentframe())
    
    debug_message = frameinfo.filename.split('/')[-1] + ' | ' + frameinfo.function + ' | line ' + str(frameinfo.lineno)
    
    if isinstance(time_stamp, str):
        debug_message += str(time.localtime()[4]) + 'm ' + str(time.localtime()[5]) + 's'
    if isinstance(user_message, str):
        debug_message += ' ' + user_message

    print(debug_message)