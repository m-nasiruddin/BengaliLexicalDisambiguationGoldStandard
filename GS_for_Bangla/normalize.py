import codecs
import sys
import unicodedata

def normalize(fnin, fnout, format):
    file_stream = codecs.open(fnin, 'r', 'utf-8')
    file_output = codecs.open(fnout, 'w', 'utf-8')
    for l in file_stream:
        file_output.write(unicodedata.normalize(format,l))
    file_stream.close()
    file_output.close()

if __name__ == "__main__":
    normalize(sys.argv[1],sys.argv[2],sys.argv[3])