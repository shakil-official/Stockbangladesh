#YearlyNav.py

import re

class YearlyNav:
    def __init__(self , dseUrl):
        self.soup = dseUrl
        #self.help = Help.Help()


    def yearlyNav(self):
        script = self.soup.findAll("script")

        for Index , h in enumerate(script):
            #print(Index , "    " , h)
            if(Index == 27):
                self.row = "\n".join([i.strip()  for i in h])
                self.arr = " ".join(self.row.split(':'))
                #print(re.split('; |, |\*|\n',self.arr))
                self.arr =re.split('; ( | ) | { | } |, | = | | , | |\*|\n',self.arr)
                #self.arr = re.split('\n|,\t,\r,',self.arr)
                print(type(self.arr))
                for index , j in enumerate(self.arr):
                    print( "[ " , index , " ] ",j)
