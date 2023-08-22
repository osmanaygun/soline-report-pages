from xhtml2pdf import pisa


def convert_html_to_pdf(source_html, temp_report_file_path):
    # open output file for writing (truncated binary)
    result_file = open(temp_report_file_path, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
        source_html, dest=result_file, encoding="utf-8"  # the HTML to convert
    )  # file handle to recieve result

    # close output file
    result_file.close()  # close output file

    # return False on success and True on errors
    print("pisa_status.err: ", pisa_status.err)
    return pisa_status.err  


with open("full_report_data.html", "r", encoding="utf-8") as myfile:
    html_content = myfile.read()


convert_html_to_pdf(html_content, "full_report_data.pdf")
 