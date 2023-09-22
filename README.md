**README - Python Code Explanation**

This Python script is used to create a CBR (Comic Book Archive) file from sorted images and a PDF document. It provides a command-line interface with various options for image and cover selection.

To run the script, you need to have Python installed on your system. Once installed, follow the steps below:

1. Copy the code into a Python script file, e.g., `create_cbr.py`.

2. Install the required dependencies by running the following command in your terminal:
```
pip install PyPDF2 pillow argparse patool
```

3. Open a terminal and navigate to the directory where the script file is located.

4. Execute the script by running the following command:
```
python create_cbr.py -S [images_directory] -O [output_cbr_file] -F [cover_image_pattern] -T [title_replace_pattern] -M [mode] -P [prompt_all]
```
Replace the placeholders (`[images_directory]`, `[output_cbr_file]`, etc.) with the appropriate values for your use case. The command-line arguments are explained below:

- `-S` or `--source`: Specifies the source directory containing sorted images and PDF documents.
- `-O` or `--out`: Specifies the output CBR file path.
- `-F` or `--front`: (Optional) Specifies the cover image selection. It can be a filename, a pattern, a number (n), or a negative number (-n) with an optional background color.
- `-T` or `--tidytitles`: (Optional) Specifies the title tidy up pattern for image titles.
- `-M` or `--mode`: (Optional) Specifies the mode for the script operation. It can be "approve", "preview", or "quiet".
- `-P` or `--prompt`: (Optional) Specifies whether to prompt for all arguments or use the default if empty. It can be "all" or "empty".

Note: All command-line arguments are required except for `-F`, `-T`, `-M`, and `-P`, which have default values if not provided.

The script utilizes the following Python libraries to perform its operations:
- `os`: Provides functions for interacting with the operating system.
- `shutil`: Provides functions for file and directory operations.
- `argparse`: Facilitates command-line argument parsing.
- `PyPDF2`: Allows reading PDF files.
- `PIL`: Provides image processing capabilities.
- `patoolib`: Enables the creation of archive files.

The script consists of several functions to handle different aspects of creating a CBR file:

- `convert_pdf_to_png`: Converts a PDF file into PNG images using the "mutool" command.
- `create_cbr`: Orchestrates the process of creating a CBR file by finding the cover image, copying the images, converting PDF to PNG (if necessary), creating the CBR file, and cleaning up temporary files.
- `find_cover_image`: Finds the cover image from the list of images based on the specified cover image pattern.
- `copy_images`: Copies the image files from the source directory to a temporary directory.
- `pdf_found_in_directory`: Checks if a PDF file is present in the images directory.
- `find_pdf_file`: Finds the PDF file in the images directory.
- `move_png_pages_to_directory`: Moves the PNG images created from the PDF to the temporary directory.
- `create_cbr_file`: Creates the CBR file using the patoolib library.

The `main` function is responsible for parsing the command-line arguments using the `argparse` library and calling the `create_cbr` function with the provided arguments.

Once the script finishes executing, you will have a CBR file at the specified output path containing the sorted images and PDF documents.

For more information and usage examples, please refer to the code comments and documentation of the used libraries.

> For detailed explanations and examples of manipulating images, PDF files, and creating CBR archives in Python, you can refer to the following resources:
> 
> - [Python os Module Documentation](https://docs.python.org/3/library/os.html)
> - [Python shutil Module Documentation](https://docs.python.org/3/library/shutil.html)
> - [Python argparse Module Documentation](https://docs.python.org/3/library/argparse.html)
> - [PyPDF2 Documentation](https://pythonhosted.org/PyPDF2/)
> - [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
> - [patoolib Documentation](https://pythonhosted.org/patoolib/)