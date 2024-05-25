import os, shutil

def copy_contents(source, destination):
    if not os.path.exists(source):
        raise ValueError('Invalid Source File path')
    
    if os.path.exists(destination):
        shutil.rmtree(destination)

    if not os.path.exists(destination):
        os.mkdir(destination)

    for dir in os.listdir(source):
        source_dir = os.path.join(source, dir)
        destination_dir = os.path.join(destination, dir)

        print(f"Source path: {source_dir} -> Destination path: {destination_dir}")

        if os.path.isfile(source_dir):  
            shutil.copy(source_dir, destination_dir) 
        else:
            copy_contents(source_dir, destination_dir)
            return "Successfully copied"