import os
import zipfile
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# replace with your zipfile path
filepath = './pdfs.zip'

# create a ZipFile object and extract all the files into a directory named 'dump'
with zipfile.ZipFile(filepath) as zip_file:
    zip_file.extractall("dump")

documents = []
skipped_files = []

# use os.walk to traverse the dump directory and its subdirectories
for root, dirs, files in os.walk("dump"):
    for filename in files:
        file_path = os.path.join(root, filename)
        logger.debug(f"Found file: {file_path}")
        # process the file (add your file processing logic here)
        # if successful, append to documents
        documents.append(file_path)
        if len(documents) % 20 == 0:
            logger.info(f"Processed {len(documents)} documents")

if not documents:
    logger.warning("No documents processed")
