import os
from PyPDF2 import PdfMerger


def merge_pdfs(folder_path, output_file):
    pdf_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_files.append(os.path.join(folder_path, filename))

    merger = PdfMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)

    with open(output_file, 'wb') as f:
        merger.write(f)

    print(f"合并后的PDF文件保存在：{output_file}")


# 使用示例  
folder_path = r'D:\works\20231016_1202s'  # 指定包含PDF文件的文件夹路径  
output_file = r'D:\works\20231016_1202s\merged.pdf'  # 合并后的PDF文件名  
merge_pdfs(folder_path, output_file)
