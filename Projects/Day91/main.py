from typing import Optional
from PIL import Image, ImageDraw, ImageFont
from tkinter import Tk, Button, Label, Entry, messagebox, filedialog


def open_file() -> Optional[Image.Image]:
    """Open a file dialog and return an Image object representing the selected image file.

    Returns:
        An Image object representing the selected image file, or None if the user cancelled the open operation.
    """
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            image = Image.open(file_path)
            return image
        except OSError:
            messagebox.showerror("Error", "Failed to open image file.")
            return None
    else:
        return None


def add_watermark(image: Image.Image, text: str) -> Image.Image:
    """Add a centered text watermark to the given Image object and return the watermarked Image object.

    Args:
        image: An Image object representing the image to be watermarked.
        text: A string representing the text to use for the watermark.

    Returns:
        An Image object representing the watermarked image.
    """
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 36)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    image_width, image_height = image.size
    watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))
    watermark_draw = ImageDraw.Draw(watermark)
    watermark_draw.text(((image_width - text_width) // 2, (image_height - text_height) // 2), text, font=font,
                        fill=(255, 255, 255, 128))
    watermarked_image = Image.alpha_composite(image.convert('RGBA'), watermark)
    return watermarked_image


def save_file(image: Image.Image) -> Optional[str]:
    """Open a file dialog and save the given Image object to a selected file path.

    Args:
        image: An Image object representing the image to be saved.

    Returns:
        A string representing the file path where the image was saved, or None if the user cancelled the save operation.
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        try:
            image.save(file_path)
            return file_path
        except OSError:
            messagebox.showerror("Error", "Failed to save image file.")
            return None
    else:
        return None


def main() -> None:
    """Create and run the main GUI window for the Image Watermarking App."""
    root = Tk()
    root.title("Image Watermarking App")

    def open_image() -> None:
        """Open a file dialog and watermark the selected image using the current watermark text."""
        image = open_file()
        if image is not None:
            watermark_image(image)

    def watermark_image(image: Image.Image) -> None:
        """Add a watermark to the given Image object and save the watermarked image to a file."""
        watermark_text = watermark_entry.get()
        if watermark_text:
            watermarked_image = add_watermark(image, watermark_text)
            save_file(watermarked_image)

    open_button = Button(root, text="Open", command=open_image)
    open_button.pack()

    watermark_label = Label(root, text="Enter watermark text:")
    watermark_label.pack()

    watermark_entry = Entry(root)
    watermark_entry.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
