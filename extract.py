import pdfplumber

def extract_text_frm_pdf(path):
    clean_lines = []
    with pdfplumber.open(path) as sample_data:
        for page in sample_data.pages:
            info = page.extract_text()
            if info is not None:
                lines = info.split("\n")
                for i in range(len(lines)):
                    if lines[i].startswith(","):
                        merged = clean_lines[-1] + lines[i]
                        clean_lines.pop(-1)
                        clean_lines.append(merged)
                    else:
                        clean_lines.append(lines[i])
    final_output = "\n".join(clean_lines)
    return final_output
print(extract_text_frm_pdf("sample_data/Sample_CV.pdf"))