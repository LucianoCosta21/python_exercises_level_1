class InputOutString:

    def __init__(self,item):
        self.item = item
    
    def get_string(self):
        self.s = input("Digite o nome.")
        return self.s
    
    def print_string(self):
        self.s= self.s.upper()
        print(self.s)
    

str_obj = InputOutString()
str_obj.get_string()
str_obj.print_string()

