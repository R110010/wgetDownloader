#This is a wget based downloader that downloads from persist links.
#It downloads in a batch of files per folder, automatically creating subfolder as req.
# NOTE:--- program file, text file, output folder should be in the same directory
import wget
from tqdm import tqdm
import os

input_text_file = "RajDeep.txt" # text file should contain csv of persistURL
OutPut_dir = "OUTPUT/"
sub_dir= 1 # to keep the count of sub directory/folder inside the output folder.
file_count = 0 # to keep the count of files in the folder when downloading
failed_downloads = 0
# open the text file in read mode
file = open(input_text_file , "r")

print(f"starting file download =============== ")
print(f"downloading from {input_text_file}")

url_list = file.readlines()



for url in tqdm(url_list): 
    url = url.split("\\")[0]
    out_path = OutPut_dir + str(sub_dir) + "/"
    if not os.path.isdir(out_path):
        os.mkdir(out_path)
    try:
        wget.download(url , out=out_path)
        file_count += 1

        if file_count == 200: # change 200 to the number of files per folder you want
            file_count =1
            sub_dir += 1
    except Exception as e:
        failed_downloads += 1

file.close()
successful_downloads = len(url_list) - failed_downloads

print(f"{successful_downloads} files downlaoded successfully --------")
print(f"download failed for  {failed_downloads} files --------")
print(f"DOWNLOAD COMPLETED!!")
#this is the first change