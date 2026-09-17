# I used "a" (append) mode so the new shipment is added to the end 
# without deleting the old data in the file.
def onlyWrite(inputWrite):
    file = open("shipment_logic_data.txt" , "a" , encoding="UTF-8")
    file.write(inputWrite)
    print()
    file.close()

def onlyRead():
    file2 = open("shipment_logic_data.txt" , "r" , encoding="UTF-8")
    PrintWord = file2.read()
    file2.close()
    return PrintWord

