from FileReaderWriter import FileReaderWriter
from CSVFileReaderWriter import CSVFileReaderWriter 
from JSONFileReaderWriter import JSONFileReaderWriter
from TextFileReaderWriter import TextFileReaderWriter

# Test default class
df = FileReaderWriter()
df.read()
df.write()

# Test polymorphed methods
c = CSVFileReaderWriter()
c.read("sample.csv")
c.write(filepath = "sample2.csv", data=["HELLO","WORLD"])

j = JSONFileReaderWriter()
j.read("sample.json")
j.write(data=['foo',{'bar': ('baz', None, 1.0, 2)}], filepath="sample2.json")

# Test supplementary activity
t = TextFileReaderWriter()
t.read("sample.txt")
t.write(filepath="sample2.txt", data="This changes the first line!")
