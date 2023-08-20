# PDF Text Extractor

This script allows users to extract text from a given PDF file and save the extracted text to a specified output file.

## Requirements

- Python 3.x
- `PyPDF2` library

To install the required library, you can use:

```
pip install PyPDF2
```

## Usage

1. Run the script:

```
python pdf_text_extractor.py
```

2. You'll be prompted to provide the path to the PDF file from which you wish to extract text.

3. Next, you'll be prompted to specify the path where you want the extracted text to be saved.

4. Once done, the script will extract the text and save it to the specified file.

## Limitations

The quality of the text extraction largely depends on how the PDF is encoded. Some PDFs might not extract text perfectly. Always review the extracted content for accuracy.
