import bitstring
import sys

class EncrypterBase64:
    
    tablica = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    def __init__(self, path):
        super().__init__()
        self.path = path


    def get_file_bitstring(self):
        with open (self.path, "r") as file:
            return bitstring.Bits(file)

    
    def get_file_string(self):
        with open (self.path, "r") as file:
            return file.read()


    def get_bin(self, x, n=0):
        return format(x, 'b').zfill(n)

    def encode(self):
        bits_arr = self.get_file_bitstring().bin
        word = ""
        last_ite = 0
        
        for ite in range(0 , len(bits_arr)-5, 6):
            word += self.tablica[int(bits_arr[ite:ite+6], 2)]
            last_ite = ite + 6

        word_rest = bits_arr[last_ite:]

        while len(word_rest) > 0:
            try:
                if len(word_rest) < 6:
                    word_rest += '00000000'
                if word_rest[0:6] == '000000':
                    word += "="
                else:
                    word += self.tablica[int(word_rest[0:6], 2)]
                word_rest = word_rest[6:]
            except:
                print("Can't encode this file.")
                sys.exit(1)

        return word

    def decode(self):
        chars = self.get_file_string()
        word_bits = ""

        for char in chars:
            word_bits += self.get_bin(self.tablica.find(char), 6)
            
        word = ""

        for ite in range(0, len(word_bits)-7, 8):
            try:
                word += str(chr(int(word_bits[ite:ite+8], 2)))
            except:
                return word

        return word

func = ['--encode', '--decode']
if (len(sys.argv) == 3 or len(sys.argv) == 4) and func.count(sys.argv[1]):
    try:
        output = ""
        enc = EncrypterBase64(sys.argv[2])
        if(sys.argv[1] == func[0]):
            output = enc.encode()
        elif(sys.argv[1] == func[1]):
            output = enc.decode()
        
        if len(sys.argv) == 4:
            with open (sys.argv[3], "w") as file:
                file.write(output)
        else:
            print(output)
    except Exception as e:
        print(e)
else:
    print("Usage: python ex2.py function [--encode, --decode] input_file output_file")