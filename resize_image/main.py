from PIL import Image, ImageOps
import os

image_ext = {
    '.jpg',
    '.jpeg',
    '.png',
}

def resize_aspect_fit(file_path: str, max_dimension) -> str:
     if os.path.isfile(file_path):
         im = Image.open(file_path)
         im = ImageOps.autocontrast(im)
         f, e = os.path.splitext(file_path)
         size = im.size
         ratio = float(max_dimension) / max(size)
         new_image_size = tuple([int(x*ratio) for x in size])
         im = im.resize(new_image_size, Image.ANTIALIAS)

         new_im = Image.new("RGB", (new_image_size[0], new_image_size[1]))
         new_im.paste(im)
         new_im.save(f + '_resized.jpg', 'JPEG', quality=90)


def get_image_files(folder_path) -> list:
    if not os.path.isdir(folder_path):
        print(f'Error: {folder_path} could not be found or is not a directory')
        return list()
    files = list(os.path.join(folder_path, p) for p in os.listdir(folder_path) if os.path.splitext(p)[1].lower() in image_ext)
    return files

if __name__ == "__main__":
    folder_path = "<FOLDERPATH>"
    max_size = 1600

    images = get_image_files(folder_path)
    for file in images:
        resize_aspect_fit(file, max_size)


