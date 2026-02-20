import time

from fpdf import FPDF
import os
path = 'C:/Users/liama/Downloads/'
output_path = 'D:/books/'
# output_path = 'C:/Users/liama/Downloads/'
subpath = 'berserk_c141 _ c150/'
bookname = 'Berserk-'
path = path + subpath
folderlist = [path + i + '/' for i in os.listdir(path)]

for folder in folderlist:
    imagelist = [folder + i for i in os.listdir(folder)]

    pdf = FPDF()
    x = 0
    y = 0
    w = 210
    h = 297
    # imagelist is the list with all image filenames
    a = time.time()
    for image in imagelist:
        pdf.add_page()
        pdf.image(image, x, y, w, h)
    b = time.time()
    chapter_number = folder.split("/")[-2].split('c')[1]
    print(chapter_number)
    output_filename = output_path + bookname + "Chapter" + chapter_number + ".pdf"
    pdf.output(output_filename)
    c = time.time()
    print("Times: ", b-a, c-b)