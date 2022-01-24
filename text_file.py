

def allowed_file_type():
    return ['txt']



class TextFile:

    alphabetic_genes = []

    def __init__(self ,file_path):
        if not file_path.endswith('.txt'):
            raise NameError("File must be a '.txt' extension")
        self._path = file_path

    
    def read_and_sort_file(self):
        """ Reads and prints out the names in Alphabetic order"""
        try:
            with open("{}".format(self._path)) as f:
                
                for line in sorted(f):
                    self.alphabetic_genes.append(line)
                    # uncomment print statment if you would like a print out in the terminal 
                    # print(self.alphabetic_genes)
                    
                return self.alphabetic_genes
               
        except FileNotFoundError:
            msg = "Sorry, the file " + {} + "does not exist.".format(self._path)
            print(msg)
        finally:
            f.close()

       

    @staticmethod
    def write_sorted_names(data):
        """ writes the sorted list to a new file"""
      
        with open("sorted_names.text", "w") as f:
            try:
                if data:
                    value = f.writelines("%s\n" % l for l in data)
                    return value
                else:
                    print("No Data to write")
            except Exception:
                print("There was an error writing to new file")
            finally:
                f.close()










# a = TextFile("gene_name.txt")
# sorted_value = a.read_and_sort_file()
# a.write_sorted_names(sorted_value)
