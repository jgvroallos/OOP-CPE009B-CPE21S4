from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):
    def read(self, filepath):
        with open(filepath, "r") as read_file:
            print(read_file.read())
        read_file.close()
    
    def write(self, filepath, data):
        with open(filepath, "w") as write_file:
            write_file.write(data)
        write_file.close()
        