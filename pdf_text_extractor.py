import PyPDF2

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def main():
    # Prompt the user for the PDF file path
    pdf_file_path = input("Please enter the path to the PDF file: ")

    # Extract text from the specified PDF file
    pdf_text = extract_text_from_pdf(pdf_file_path)

    # Prompt the user for the output file path
    output_file_path = input("Please enter the path where you want to save the extracted text: ")

    # Save the extracted text to the specified output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(pdf_text)

    print(f"Text extracted from {pdf_file_path} and saved to {output_file_path}")

if __name__ == "__main__":
    main()
