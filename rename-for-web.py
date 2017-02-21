# Python script which when ran within a directory:
# 1. Replaces whitespace with hyphens
# 2. Makes everything lowercase
# 3. If 'append-dims' argument is passed it will append dimensions if the file is an image
#
# @author Luke Watts
# @version 2.0
# @licence MIT

import imghdr
import struct
import os
from sys import argv

def get_image_size(fname):
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return '{0}x{1}'.format(width, height)


def rename_files():
    print('Starting rename files operation...')    
    # Get current full path
    curdir = os.getcwd()
    fullpath = os.path.abspath(curdir) + '\\'

    print('Current path is:' + fullpath)

    filenames = os.listdir(curdir)
    # Loop through files in the current directory
    for filename in filenames:
        # Make sure we're dealing with files
        if os.path.isfile(filename):
            #
            #get File size
            file_dimensions = get_image_size(filename)

            # Replace spaces with hyphens (-)
            hyphenated_filename = filename.replace(' ', '-')

            # Rename files using .lower()
            lowercase_filename = hyphenated_filename.lower()

            # Get file name without extension
            filename_only = os.path.splitext(os.path.basename(lowercase_filename))[0]

            # Get extension only
            ext = os.path.splitext(os.path.basename(lowercase_filename))[1]

            if ext in ['.jpeg', '.jpg', '.png', '.gif', '.tiff', '.bmp']:
                
                if 'append-dims' in argv:
                    new_filename = '{0}_{1}{2}'.format(filename_only, file_dimensions, ext)
                else:
                    new_filename = lowercase_filename

                # # Combine with path to make full pathname
                path_filename = fullpath + filename

                # # Rename the file
                os.rename(path_filename, new_filename)

                print('File renamed: ' + new_filename)

    print('Ending rename files operation...')
    
rename_files();