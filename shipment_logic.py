import file_manager

def addShipment(Id_shipment , Cargo , Destination , Driver ):
    shipment = {
        "ID" : Id_shipment ,
        "Cargo" : Cargo ,
        "To" : Destination ,
        "Driver" : Driver ,
        "Status" : "In The warehouse"
    }
    line = f"ID:{shipment['ID']} | Cargo:{shipment['Cargo']} | To:{shipment['To']} | Driver:{shipment['Driver']} | Status:{shipment['Status']}\n"
    file_manager.onlyWrite(line)
    return True

def viewShipment():
    return file_manager.onlyRead()

# I split the data into lines so I can check them one by one.
# I used f"ID:{...}" to make sure I find the exact ID, not a wrong match.
def searchShipment (Id_shipment):
    allData = file_manager.onlyRead()
    lines = allData.split('\n')
    for line in lines:
        if(f"ID:{Id_shipment}" in line) : 
            return line
    return None