# ================ Text File Mode =================
#
#     1. r   =  open for read. file pointer is positioned at the beginning of the file.
#  
#     2. w   =  open for writing. if any data is already present in the file, it will overwrite the data. If the file doesn't exist it will create that file. 
#   
#     3. x   =  open for exclusive creation with write. The specified file must not be available, if the specified file is available it will show error FileExistsError
#    
#     4. a   =  open for appending. The file pointer is positioned at the end of the file. It appends new data at the end of file. If the file does not exists it will create a new file for writing data.
#    
#     5. r+  =  open for reading and then writing.
#  
#     6. w+  =  open for writing and then reading. It will not overwrite existing data
#   
#     7. a+  =  open for appending then reading. It won't overwrite existing data.





# ============== Binary File Mode  ===============
#
#    1. rb = Open for reading. The file pointer is positioned at the beginning of the file
#            doesn't exists it will show FileNotFoundError.
#
#    2. wb = Open for writing. If any data is already present in the file, it will overwrite the data.
#            If the file doesn't exists it will create that file.
#
#    3. xb = Open for exclusive creation with write. The specified file must not be available, 
#            if the specified file is available it will show error FileExistsError.
#
#    4. ab = Open for appending. The file pointers is positioned at the end of the file. 
#            It appends new Data at the end of file. If the file doesn not exists it will 
#            create a new file for writing data.
#
#    5. rb+ = Open for reading and then writing.
#
#    6. wb+ = Open for writing and then reading. It will overwrite existing data.
#             
#    7. ab+ = Open for appending then reading. It won't overwrite existing data.












