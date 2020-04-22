from database_util import DatabaseUtil

class Menu:
    def main(self):
	with DatabaseUtil() as db:
	    db.createUserTable()
	self.topMenu()

    def topMenu(self):
        while(True):
            print("******Main Menu******")
            print("1. Member options")
            print("2. Car Options")

            if(selection =="1"):
                menuMember()
            elif(selection == "2"):
                menuCar()
            else:
                print("Option not valid")

    def menuMember(self):
        print("******Member Menu******")
        print("1. List all members")
        print("2. Create Member")


    def menuCar(self):
        print("******Member Menu******")
        print("1. List all cars")
        print("2. Create a car")

if __name__ == "__main__":
    Menu().main()
