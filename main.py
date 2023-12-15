import re
import os
from ocrmac import ocrmac

class ImageFiles: 
    def read_img_text(self, file_path):
        return ocrmac.OCR(file_path, language_preference=['en-US']).recognize()

    def get_file_paths(self, directory_path):
        jpg_files = [jpg_file for jpg_file in os.listdir(directory_path) if jpg_file.endswith('.jpg')]
        print('Getting JPG files....')
        return [os.path.join(directory_path, jpg_file) for jpg_file in jpg_files]

class ImageProcessors:
    directory_path = 'images'

    def __init__(self, imageFiles): 
        self.imageFiles = ImageFiles()

    def __get_serial_number(self, text_result):
        pattern = re.compile(r'METER S/N : (.+)')
        return [pattern.search(text).group(1) for text, _, _ in text_result if pattern.search(text)]

    def process_images_in_directory(self):

        files = self.imageFiles.get_file_paths(self.directory_path)
        print(files)

        for jpg_file in files:
            text_result = self.imageFiles.read_img_text(jpg_file)
            result = self.__get_serial_number(text_result)
            print(f"Text result for {jpg_file} : {result} ")

if __name__ == '__main__':

    imageFiles = ImageFiles()
    imageProcessor = ImageProcessors(imageFiles)

    print('processing images...')

    imageProcessor.process_images_in_directory()

