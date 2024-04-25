from pdf2image import convert_from_path

# pip install pdf2image
# brew install poppler
# Store Pdf with convert_from_path function
images = convert_from_path("./p.pdf")

for i in range(len(images)):

    # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')