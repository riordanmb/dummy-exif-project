import random
from datetime import datetime, timedelta
from PyPDF2 import PdfReader, PdfWriter


# Function to generate a random date
def generate_random_date():
    start_date = datetime(1900, 1, 1)  # You can adjust the start date as per your needs
    end_date = datetime(2100, 12, 31)  # You can adjust the end date as per your needs

    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    return random_date


# Function to generate random custom metadata
def generate_random_metadata():
    metadata = {}

    # Generate 5 random keys and values in various formats
    for _ in range(5):
        key = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))  # Random key
        value_type = random.choice(["string", "integer", "float", "date"])  # Random value type

        if value_type == "string":
            value = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in
                            range(10))  # Random string
        elif value_type == "integer":
            value = random.randint(1, 100)  # Random integer
        elif value_type == "float":
            value = round(random.uniform(1.0, 100.0), 2)  # Random float with 2 decimal places
        elif value_type == "date":
            value = generate_random_date()  # Random date

        metadata['/' + key] = value

    return metadata


# Function to set custom metadata in a PDF document
def set_pdf_metadata(filepath, organization, custom_metadata):
    with open(filepath, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        # Copy over the existing document to the writer
        writer.clone_document_from_reader(reader)

        # Ensure organization is a string
        organization_str = str(organization) if organization else ''

        # Set organization metadata
        metadata = {'/org': organization_str}

        # Convert custom_metadata values to strings
        for key, value in custom_metadata.items():
            metadata[key] = str(value)

        writer.add_metadata(metadata)

        # Save the PDF with new metadata to 'sample_dummy_with_data.pdf'
        with open("sample_dummy_with_data.pdf", 'wb') as f:
            writer.write(f)

def main():
    random_metadata = generate_random_metadata()
    set_pdf_metadata("dummy.pdf", "W3C", random_metadata)


if __name__ == "__main__":
    main()