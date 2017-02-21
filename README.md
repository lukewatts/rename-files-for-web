# Rename for Web
Python script which when ran within a directory replaces whitespace with hyphens and makes everything lowercase.

If the argument `append-dims` is passed, the dimensions of any images will be appended to the end of the file name.

## Features
- Leaves directories unchanged.
- Leaves underscores intact
- Non recursive (only renames files in the directory it is in)

## Usage
Given a folder with the following files:

```
Product Descriptions 2017.pdf
Product Descriptions 2017.docx
T-Shirt_Large_Red_Design Front and Back.JPG
Long-Sleeve Shirt_Grey_Design on Front.jpg
```

### Standard Usage
Running:
```
py rename-for-web.py
```

Results in:
```
product-descriptions-2017.pdf
product-descriptions-2017.docx
t-shirt_large_red_design-on-front-and-back.jpg
long-sleeve-shirt_grey_design-on-front.jpg
```

### Append dimensions
Running:
```
py rename-for-web.py append-dims
```

Results in:
```
product-descriptions-2017.pdf
product-descriptions-2017.docx
t-shirt_large_red_design-on-front-and-back_400x600.jpg
long-sleeve-shirt_grey_design-on-front_800x1200.jpg
```

## License
(c) 2017 Luke Watts

This software is licensed under the MIT license. For the full copyright and license information, please view the LICENSE file that was distributed with this source code.