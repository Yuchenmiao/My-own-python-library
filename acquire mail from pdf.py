import re
import glob
from PyPDF2 import PdfReader
import os

folder_path = r'E:\大一下学期\SI100\Project\第五组第二步提交内容(UCB,Umich,Rochester,CMU,Upitts,UIUC)\各校cv文件\cv_of_ucb_candidates'

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

for file_path in glob.glob(os.path.join(folder_path, '*.pdf')):
    print(f"Processing file: {os.path.basename(file_path)}")
    
    with open(file_path, 'rb') as file:
        pdf = PdfReader(file)

        for page in pdf.pages:
            text = page.extract_text()

            emails = re.findall(email_pattern, text)

            for email in emails:
                print(email)