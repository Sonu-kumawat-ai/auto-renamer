import os

folder_path = input("Enter the path : ")
extension=input("Enter the file extension (without dot): ")
rename=input("Enter What Rename you want : ")
i=1

files = os.listdir(folder_path)
for file in files:
    if file.endswith(f'.{extension}'):
        os.rename(f'{folder_path}\{file}',f'{folder_path}\{rename}_{i}.{extension}')
        
        print(f'Renamed {i}: {folder_path}\{file} -> {folder_path}\{rename}_{i}.{extension}')
        i+=1
