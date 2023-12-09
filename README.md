PDF Custom Metadata Demonstration
============================

This is a demonstration of how to use custom metadata in a PDF file.


* [dummy.pdf](dummy.pdf) is a PDF file with no custom metadata.
* [sample_dummy_with_data.pdf](sample_dummy_with_data.pdf) is a PDF file containing several random metadata strings.
* [generate_random_metadata.py](generate_random_metadata.py) will produce a new file from the dummy file, called _dummy\_with\_data\.pdf_, which adds several randomly-generated items of metadata.

There are various tools for interacting with PDF metadata.

Many tools, including Apple's Preview and DEVONthink, do not allow easy access to custom metadata. But you can view it using Adobe Acrobat. Select File->Document Properties->Custom.

For getting and setting custom metadata, I have used the PDFReader and PDFWriter classes of the [PyPDF library](https://pypi.org/project/pypdf/). 

You can also use [ExifTool](https://github.com/exiftool/exiftool) by Phil Harvey, which is available as either a Perl module, or a standalone commandline executable. 