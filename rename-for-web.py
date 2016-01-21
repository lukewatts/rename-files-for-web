# Python script which when ran within a directory 
# replaces whitespace with hyphens and makes everything lowercase.
# 
# @author Luke Watts
# @licence MIT
import os

curdir = os.getcwd()
fullpath = os.path.abspath(curdir) + '\\'
filenames = os.listdir(curdir)
# Loop through files in the current directory
for filename in filenames:
    # Make sure we're dealing with files
    if os.path.isfile(filename):
        # Replace spaces with hyphens (-)
        hyphenated_filename = filename.replace(' ', '-')

        # Rename files using .lower()
        new_filename = hyphenated_filename.lower()
        # Combine with path to make full pathname
        path_filename = fullpath + filename

        # Rename the file
        os.rename(path_filename, new_filename)
