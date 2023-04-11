from tkinter import Tk
from tkinter.filedialog import askopenfilename

import pyttsx3
from PyPDF2 import PdfReader


class PdfToAudioConverter:
    """A class that converts PDF files to audio files.

    This class uses the PyPDF2 and pyttsx3 libraries to extract the text from a PDF file, convert it to speech, and save
    it as an audio file.

    Attributes:
        engine (pyttsx3.engine.Engine): The text-to-speech engine used to convert the text to speech.
        pdf_file (file): The PDF file to be converted.
        pdf_reader (PyPDF2.pdf.PdfFileReader): The PDF reader object used to extract text from the PDF file.
        text (str): The text extracted from the PDF file.
    """

    def __init__(self):
        """Initializes the PdfToAudioConverter object.

        Sets the properties for the text-to-speech engine.
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('voice', 'en')

    def select_pdf_file(self):
        """Shows a file dialog to select the PDF file.

        Raises:
            FileNotFoundError: If the selected file is not found.
        """
        Tk().withdraw()
        pdf_file_path = askopenfilename(filetypes=[("PDF Files", "*.pdf")])

        try:
            self.pdf_file = open(pdf_file_path, 'rb')
        except FileNotFoundError:
            print('File not found.')
            exit()

    def extract_text_from_pdf(self):
        """Extracts the text from the PDF file and stores it in the 'text' attribute."""
        self.pdf_reader = PdfReader(self.pdf_file)

        self.text = ''

        for page in self.pdf_reader.pages:
            page_text = page.extract_text()
            self.text += page_text

    def convert_text_to_speech(self):
        """Converts the text to speech using the text-to-speech engine."""
        self.engine.say(self.text)

    def save_audio_file(self):
        """Saves the converted audio file.

        Prompts the user to enter a file name for the audio file, saves the file as an MP3 file, and runs the text-to-speech
        engine to convert the text to speech and save it as an audio file.

        Raises:
            IOError: If there is an error saving the audio file.
        """
        audio_file_name = input("Enter the name of the audio file to save: ")

        try:
            self.engine.save_to_file(self.text, audio_file_name + '.mp3')
            self.engine.runAndWait()
        except IOError:
            print('Error saving audio file.')
            exit()

    def convert_pdf_to_audio(self):
        """Converts the PDF file to an audio file.

        Calls the 'select_pdf_file', 'extract_text_from_pdf', 'convert_text_to_speech', and 'save_audio_file' methods
        to convert the PDF file to an audio file.
        """
        self.select_pdf_file()
        self.extract_text_from_pdf()
        self.convert_text_to_speech()
        self.save_audio_file()


if __name__ == '__main__':
    converter = PdfToAudioConverter()
    converter.convert_pdf_to_audio()
