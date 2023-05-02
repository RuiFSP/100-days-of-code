# Create a dictionary with file extensions as keys and corresponding folder names as values

extensions = {
    # Documents
    # --Text documents
    ".doc": "--TextDocuments",
    ".docx": "--TextDocuments",
    ".odt": "--TextDocuments",
    ".rtf": "--TextDocuments",
    ".txt": "--TextDocuments",
    ".wps": "--TextDocuments",
    ".wpd": "--TextDocuments",


    # --Spreadsheets
    ".csv": "--Spreadsheets",
    ".wks": "--Spreadsheets",
    ".xls": "--Spreadsheets",
    ".xlsx": "--Spreadsheets",
    ".xlsm": "--Spreadsheets",

    # Presentations
    ".ppt": "--Presentations",
    ".pptx": "--Presentations",

    # PDFs
    ".pdf": "--PDFs",
    ".epub": "--PDFs",
    ".djvu": "--PDFs",

    # Images
    ".jpeg": "--Images",
    ".jpg": "--Images",
    ".png": "--Images",
    ".bmp": "--Images",
    ".gif": "--Images",
    ".svg": "--Images",

    # Audio
    ".mp3": "--Audio",
    ".wav": "--Audio",
    ".wma": "--Audio",
    ".aac": "--Audio",
    ".ogg": "--Audio",

    # Video
    ".mp4": "--Videos",
    ".mov": "--Videos",
    ".avi": "--Videos",
    ".flv": "--Videos",
    ".wmv": "--Videos",
    ".mkv": "--Videos",
    ".m4v": "--Videos",

    # Archives
    ".zip": "--Archives",
    ".rar": "--Archives",
    ".tar": "--Archives",
    ".gz": "--Archives",
    ".7z": "--Archives",

    # Programs
    ".exe": "Programs",
    ".msi": "Programs",
    ".apk": "Programs",

    # Others
    ".iso": "--DiscImages",
    ".torrent": "--Torrents",
}
