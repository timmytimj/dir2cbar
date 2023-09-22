import os
import shutil
import argparse
from PyPDF2 import PdfFileReader
from PIL import Image
import patoolib

def convert_pdf_to_png(pdf_file):
    #temp_directory to store the png images
    temp_directory = os.path.join('/tmp/', 'temp_dir')
    os.makedirs(temp_directory, exist_ok=True)
    
    command = f"mutool draw -o {temp_directory}/page%d.png {pdf_file}"
    os.system(command)

def create_cbr(images_directory, output_cbr_file, cover_image_pattern=None, title_replace_pattern=None, mode="preview", prompt_all="empty"):
    images_list = sorted(os.listdir(images_directory))
    cover_image = find_cover_image(images_list, cover_image_pattern, prompt_all)

    temp_directory = os.path.join('/tmp/', 'temp_dir')
    os.makedirs(temp_directory, exist_ok=True)

    copy_images(images_directory, images_list, temp_directory)

    if pdf_found_in_directory(images_list):
        pdf_file = find_pdf_file(images_directory, images_list)
        convert_pdf_to_png(pdf_file)
        move_png_pages_to_directory(temp_directory)

    create_cbr_file(temp_directory, output_cbr_file)
    shutil.rmtree(temp_directory)

def find_cover_image(images_list, cover_image_pattern, prompt_all):
    # Function implementation to find the cover image based on the cover_image_pattern
    # If not provided, prompt the user if prompt_all is True
    for image_file in images_list:
        if "cover" in image_file.lower() or "front" in image_file.lower() or "title" in image_file.lower():
            return image_file
    return images_list[0]
    
    
    
def copy_images(images_directory, images_list, temp_directory):
    for image_file in images_list:
        if image_file.endswith(('.png', '.jpg', '.jpeg')):
            shutil.copy(os.path.join(images_directory, image_file), temp_directory)

def pdf_found_in_directory(images_list):
    for image_file in images_list:
        if image_file.endswith('.pdf'):
            return True
    return False

def find_pdf_file(images_directory, images_list):
    for image_file in images_list:
        if image_file.endswith('.pdf'):
            return os.path.join(images_directory, image_file)

def move_png_pages_to_directory(temp_directory):
    for file_name in os.listdir(temp_directory):
        if file_name.startswith('page') and file_name.endswith('.png'):
            shutil.move(os.path.join(temp_directory, file_name), temp_directory)

def create_cbr_file(temp_directory, output_cbr_file):
    os.chdir(temp_directory)
    patoolib.create_archive(output_cbr_file, ('./',))



def main():
    parser = argparse.ArgumentParser(description="Create a CBR file from sorted images and a PDF document.")
    parser.add_argument("-S", "--source", dest="images_directory", required=True, help="Source directory containing sorted images and PDF documents.")
    parser.add_argument("-O", "--out", dest="output_cbr_file", required=True, help="Output CBR file path.")
    parser.add_argument("-F", "--front", dest="cover_image_pattern", default=None, help="Cover image selection: filename | 'pattern' | n | -n | -N [background_color].")
    parser.add_argument("-T", "--tidytitles", dest="title_replace_pattern", default=None, help="Title tidy up pattern: 'regex pattern' | 'ascii' | 'title' | 'capslock' | 'lowercase' | 'onlybadchars'.")
    parser.add_argument("-M", "--mode", dest="mode", choices=["approve", "preview", "quiet"], default="preview", help="Mode: --approve (-a) | --preview (-p) | --quiet (-q).")
    parser.add_argument("-P", "--prompt", dest="prompt_all", choices=["all", "empty"], default="empty", help="Prompt all arguments or use default if empty.")
    
    args = parser.parse_args()

    images_directory = args.images_directory
    output_cbr_file = args.output_cbr_file
    cover_image_pattern = args.cover_image_pattern
    title_replace_pattern = args.title_replace_pattern
    mode = args.mode
    prompt_all = args.prompt_all

    create_cbr(images_directory, output_cbr_file, cover_image_pattern, title_replace_pattern, mode, prompt_all)

if __name__ == "__main__":
    main()
