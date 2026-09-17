import shipment_logic

import pyfiglet
import pyttsx3
from rich.console import Console
from rich.table import Table

engine = pyttsx3.init()
console = Console()

# Displaying a stylish ASCII art banner to welcome the user when the app starts.
print("\n" + "="*55)
ascii_banner = pyfiglet.figlet_format("TUWAIQ LOGISTICS")
console.print(ascii_banner, style="bold purple")
print("="*55 + "\n")

while True:
        try:
            print("-"*40)
            inputUser = input("""Please select an option :
1 - Enter a new shipment '1'
2 - Show shipments '2'
3 - Search for a shipment '3'
4 - To Exit Write "Exit"\n> """).strip()
            
            if inputUser.upper() == "EXIT" or inputUser == "4":
                print("Exiting the system...")
                break
                
            elif inputUser == "1" :
                print("\n--- Enter Shipment Details ---")
                inputShipment_id = input("Shipment ID: ")
                inputShipment_Cargo = input("Cargo Type: ")
                inputShipment_Destination = input("Destination: ")
                inputShipment_Driver = input("Driver Name: ")
                shipment_logic.addShipment(inputShipment_id , inputShipment_Cargo , inputShipment_Destination , inputShipment_Driver)
                
                print("Shipment added successfully ✅")
                
                engine.say("Shipment added successfully")
                engine.runAndWait()
                
            elif inputUser == "2" :
                 records = shipment_logic.viewShipment()
                 print("\n--- All Shipment Records ---")
                 if records.strip():

                    table = Table(title="📦 Shipments List", style="purple", header_style="bold white")
                    table.add_column("ID", style="white", justify="center")
                    table.add_column("Cargo", style="white")
                    table.add_column("To", style="white")
                    table.add_column("Driver", style="white")
                    table.add_column("Status", style="bold green")

                    lines = records.strip().split('\n')
                    for line in lines:
                        if line.strip(): 
                            parts = []
                            for p in line.split("|"):
                                if ":" in p:
                                    parts.append(p.split(":")[1].strip())
                            
                            if len(parts) == 5:
                                table.add_row(parts[0], parts[1], parts[2], parts[3], parts[4])
                    
                    console.print(table)
                 else:
                    print("No shipments found. The list is empty.")
                    
            elif inputUser == "3" :
                inputShipment_search = input("Enter The search Shipment ID : ")
                result = shipment_logic.searchShipment(inputShipment_search)
                if result:
                    print("\n✅ Found : " + result)
                else:
                     print("\n❌ Shipment Not Found!")
            else:
                print(f"Invalid choice: '{inputUser}'! Please select 1, 2, 3, or Exit. ⚠️")
        
        except FileNotFoundError:
            print("Error: The shipment data file was not found. Please add a shipment first. ⚠️")
        except PermissionError:
            print("Error: Permission denied! The program cannot write to or read the file. ⚠️")   
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting gracefully... ⚠️")
            break
        except Exception as error_name:
            print(f"Invalid input or unexpected error! Please check the data and try again. Details: {error_name} ⚠️")