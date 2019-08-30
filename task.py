"""
Fare Card system London's Oyster Card System.

"""
class TubeStations:
    """ Class for TubStations with parameter total_fare
        for updating the total cost of a trip.

    """

    def __init__(self):
        self.total_fare = 0

    def balance(self, origin, destination):
        """ function for calculating the Total Balance of a trip

        Parameters
        ----------
        origin : the starting point of a trip

        destination : the end point of a trip

        """
        # dictionary for different zones for different stations.
        zones_dic = {"Zone1": ["Holborn", "Aldgate", "EarlCourt"],
                     "Zone2": ["EarlCourt", "Hammersmith", "Arsenal"],
                     "Zone3": ["Wimbledon"]}

        # Logic for total_fare calculations for different zones.
        if origin in zones_dic["Zone1"] and destination in zones_dic["Zone1"]:
            self.total_fare += 2.50

        elif origin in zones_dic["Zone2"] and destination in zones_dic["Zone2"]:
            self.total_fare += 2.00

        elif (origin in zones_dic["Zone1"] and (destination in zones_dic["Zone2"]))\
            or\
            (origin in zones_dic["Zone2"] and (destination in zones_dic["Zone1"])):
            self.total_fare += 3.00

        elif (origin in zones_dic["Zone2"] and destination in zones_dic["Zone3"])\
            or\
             (origin in zones_dic["Zone3"] and destination in zones_dic["Zone2"]):
            self.total_fare += 2.25

        elif (origin in zones_dic["Zone1"] and destination in zones_dic["Zone3"])\
             or\
             (origin in zones_dic["Zone3"] and destination in zones_dic["Zone1"]):
            self.total_fare += 3.20

        elif origin == "Bus" or destination == "Bus":
            self.total_fare += 1.80
        print(self.total_fare)

        return self.total_fare

    def card_swipe(self, swipe):
        """Function for swipe the card on exit from a station

        Parameters
        ----------
        swipe: Flag for checking if customer swiped the card or not

        """
        max_fare = 3.20 # the maximum fare that can be incured.
        # Logic below for swap with max_fare for a single trip on tube station.
        if swipe:
            max_fare = self.total_fare
        else:
            return max_fare
        return max_fare

    def remaining_balance(self, starting_balance):
        """Returns the remaining balance.

        Parameters
        ----------
        starting_balance: The inital balance for a customer.

        """
        return starting_balance - self.total_fare

def ent_purse_amount():
    """
    Function for inputing fare Amount.

    """
    print("Enter the starting balance")

    total_purse_amount = input()
    try:
        total_purse_amount = int(total_purse_amount)
        return total_purse_amount
    except ValueError:
        print("Please enter integer value")
        return ent_purse_amount()

def ent_tube_stations():
    """
    Function for inputing Origin and Destination
    Station names.
    """
    try:
        origin, destination = input().split()
        return origin, destination
    except ValueError:
        print("Please enter Stations with Space between Origin and Destination")
        return ent_tube_stations()

def station_names(S, Amount):
    """
    Function for returning remaining balance.
    """


    print("Enter the origin and destination with Space")


    origin, destination = ent_tube_stations()

    if S.balance(origin, destination) == 0:
        print("Please enter correct names for stations\n")
        return station_names(S, Amount)
    else:
        print("Enter 0 to not swipe the card 1 to swipe the card at the exit gate.")

        swipe_exit = bool(int(input()))

        S.card_swipe(swipe_exit)
        print("Remaining Balance")
        print(S.remaining_balance(Amount))



if __name__ == "__main__":

    S = TubeStations()
    TOTAL_PURSE_AMOUNT = ent_purse_amount()
    IS_SESSION = 1

    try:
        while IS_SESSION == 1:
            station_names(S, TOTAL_PURSE_AMOUNT)
            print("Press ctl+c to stop the jounrey")

    except KeyboardInterrupt:
        IS_SESSION = 0
