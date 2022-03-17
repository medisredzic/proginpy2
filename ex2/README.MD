Exercise 2 [15 points]
In this exercise, we will clean up the raw dataset. For this, you should write a Python function
validate_images (in the file ex2.py) that takes three keyword arguments as input:
• input_dir (string): The input directory where your function should look for files.
• output_dir (string): The directory where your function should place the output files.
• log_file (string): The path of the log file.
• formatter (string, optional): Optional format string to use when writing the output files.
It expects a single number that is used to apply the format string on. The result is the
base name of the file, without any extension.
If output_dir or the directory containing log_file does not exist, your function should create them.
Your function should scan input_dir for files recursively and sort this list of file names. The
files should then be processed in the order that they appear in the sorted list of file names. Files
should be copied to output_dir if they are valid. Create a manual copy based on raw pixel
data to avoid copying image metadata. Files are considered valid if the following rules are met:
1. The file name ends with .jpg, .JPG, .jpeg or .JPEG.
2. The file size does not exceed 250kB (=250 000 Bytes).
3. The file can be read as image (i.e., the PIL/pillow module does not raise an exception
when reading the file).
4. The image data has a shape of (H, W, 3) with H (height) and W (width) larger than or
equal to 96 pixels. The three channels must be in the order RGB (red, green, blue).
5. The image data has a variance larger than 0, i.e., there is not just one common RGB pixel
in the image data.
6. The same image data has not been copied already.
The base name (without any extension) of the copied file should be as defined by the format
string formatter, which expects a single number that is used to apply the format string on. If
no format string is specified, then simply the number is used as base name. The number must
be an integer starting at 0, and it is incremented by 1 for every file that has been copied. The
extension of every copied file must be .jpg. Example:
• Input files:
– cat.jpeg (valid)
– dog2.png (invalid)
– tree1.jpg (valid)
– tree2.JPG (valid)
• Format string: "06d"
• Output files:
– 000000.jpg (from cat.jpeg)
– 000001.jpg (from tree1.jpg)
– 000002.jpg (from tree2.JPG)
File names of invalid files should be written to log_file. The format of log_file should be
as follows: Each line should contain the file name of the invalid file, followed by a comma, an
error code and a newline character. The error code is an integer with 1 digit, corresponding to
the list of rules for file validity from above (i.e., there are a total of 6 error codes). Only one
error code per file should be written, and the rules should be checked in the ascending order 1,
2, 3, 4, 5, 6. Each file name should only contain the relative file path starting from input_dir
(this means input_dir is not part of the relative path anymore).
The function should return the number of valid files that were copied as integer. In the example
above, 3 should be returned.
Hints
• You can store the hashes of all copied files to check if the current file has already been
copied.
• os.path.getsize() will report the size of a file.
• Loading an image from a file can be done with PIL.Image.open().
• You can use the attribute my_image.mode to check the mode of an image (e.g., "RGB").
• You can use im = PIL.Image.fromarray() and im.save() to create a manual copy
from a numpy array which holds raw image pixel data.
• input_dir might be an absolute or relative path. You can use os.path.abspath() to
get the absolute path of input_dir.
Submission Information
• Due date: 27.04.2022 23:55
• File name: ex2.py
• Moodle: https://moodle.jku.at/jku/mod/assign/view.php?id=6559794