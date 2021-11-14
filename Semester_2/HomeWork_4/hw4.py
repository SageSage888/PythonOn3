import sys
from pathlib import Path
from threading import Thread

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
TXT = []
PDF = []
MP4_VIDEOS = []
MP3_MUSIC = []
OTHER = []
ARCH = []
FOLDERS = []
UNKNOWN = set()
EXTENSION = set()

threads = []

REGISTERED_EXTENSIONS = {
    "JPEG": JPEG_IMAGES,
    "JPG": JPG_IMAGES,
    "PNG": PNG_IMAGES,
    "SVG": SVG_IMAGES,
    "ZIP": ARCH,
    "TXT": TXT,
    "PDF": PDF,
    "MP4": MP4_VIDEOS,
    "MP3": MP3_MUSIC
}


def get_extension(file_name) -> str:
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("JPEG", "JPG", "PNG", "SVG", "OTHER", "ARCH", "PDF", "TXT", "MP4", "MP3"):
                FOLDERS.append(item)
                thread_dir = Thread(target=scan, args=(item,))
                threads.append(thread_dir)
                thread_dir.start()
            continue

        extension = get_extension(item.name)
        new_name = folder / item.name
        if not extension:
            OTHER.append(new_name)
        else:
            try:
                current_container = REGISTERED_EXTENSIONS[extension]
                EXTENSION.add(extension)
                current_container.append(new_name)
            except KeyError:
                UNKNOWN.add(extension)
                OTHER.append(new_name)


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")

    search_folder = Path(scan_path)
    scan(search_folder)
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Images svg: {SVG_IMAGES}")
    print(f"Text files: {TXT}")
    print(f"PDF files: {PDF}")
    print(f"Video mp4: {MP4_VIDEOS}")
    print(f"Music mp3: {MP3_MUSIC}")
    print(f"Archives: {ARCH}")
    print(f"Unknown files: {OTHER}")
    print(f"There are file of types: {EXTENSION}")
    print(f"Unknown types of file: {UNKNOWN}")


# add to def main below "scan.scan(folder)" next lines:
# for thread in scan.threads:
#     thread.join()
