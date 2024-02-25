from enum import Enum
class gender(Enum):
    Male = 1
    Female = 2

class Person():
    def __init__(self, firstName, lastName, phoneNo, dateOfBirth, gender):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNo = phoneNo
        self.dateOfBirth = dateOfBirth
        self.gender = gender

    def setFirstName(self, firstName):
        self.firstName = firstName
    def getFirstName(self):
        return self.firstName

    def setLastName(self, lastName):
        self.lastName = lastName
    def getLastName(self):
        return self.lastName

    def setPhoneNo(self, phoneNo):
        self.phoneNo = phoneNo
    def getPhoneNo(self):
        return self.phoneNo

    def setDateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth
    def getDateOfBirth(self):
        return self.dateOfBirth

    def setGender(self, gender):
        self.gender = gender
    def getGender(self):
        return self.gender

    def __str__(self):
        return f"Name: {self.getFirstName()} {self.getLastName()}, Phone Number: {self.getPhoneNo()}, Date of Birth: {self.getDateOfBirth()}, Gender: {self.getGender()}"

class employType(Enum):
    Teller = 1
    FlightAttendent = 2
    SecurityPersonnel = 3

class Staff(Person):
    def __init__(self,firstName, lastName, phoneNo, dateOfBirth, gender, employType):
        Person.__init__(self, firstName, lastName, phoneNo, dateOfBirth, gender)
        self.employType= employType

    def setEmployType(self, employType):
        self.employType = employType
    def getEmployType(self):
        return self.employType

    def cancelFlight(self):
        pass  # This function should follow the required steps for the teller to cancel the passenger's flight
        # It will allow them to choose their flight and delete it records once the system verifies that the customer meets the policy conditions
        # It should also display a confirmation message to indicate successful cancellation

    def changeFlight(self):
        pass  # this function allows the teller to get the customer's credentials and find flights matching the customer's specfication to change their current flight to one of the options

    def weightCheck(self):
        pass  # This function will only allow the security personnal assigned to measure the weight of the baggage

    # it will compare teh weight measured to the given maximimum limit, if it is indeed more than the max it will display a message

    def securityCheck(self):
        pass  # This will ask teh passenger for their credentials(passport and boarding pass) verify that they match the records before clearing them
        # it also should simulate carry-on scan and metal detectors

    def __str__(self):
        return Person.__str__(self) + f"Employee Type: {self.getEmployType()}"

class classType(Enum):
    FirstClass = 1
    Business = 2
    Economy = 3

class Passenger(Person):
    def __init__(self, firstName, lastName, phoneNo, dateOfBirth, gender, seatNo, classType):
        Person.__init__(self, firstName, lastName, phoneNo, dateOfBirth, gender)
        self.seatNo =seatNo
        self.classType = classType

    def setSeatNo(self, seatNo):
        self.seatNo = seatNo
    def getSeatNo(self):
        return self.seatNo

    def setClassType(self, classType):
        self.classType = classType

    def getClassType(self):
        return self.classType

    def cancelFlight(self):
        pass #This function should follow the required steps for the passener to cancel their flight
        #It will allow them to choose their flight and delete it records once the system verifies that they meet the policy conditions
        #It should also display a confirmation message to indicate successful cancellation

    def changeFlight(self):
        pass #This function will allow the customer to send a request for changing their flight, if their credentials are valid and there are avalible flights  that match their wants it should print a confirmation for a flight change

    def __str__(self):
        return Person.__str__()+ f"Seat Number: {self.getSeatNo()}, Class Type:{self.getClassType()}, "
class Flight():
    def __init__(self, destination, departing, flightNo, arrivalTime, departingTime, flightDate, boardingTill, therminal ):
        self.destination = destination
        self.departing = departing
        self.flightNo = flightNo
        self.arrivalTime = arrivalTime
        self.departingTime = departingTime
        self.flightDate = flightDate
        self.boardingTill = boardingTill
        self.therminal = therminal

    def setDestination(self, destination):
        self.destination = destination
    def getDestination(self):
        return self.destination

    def setDeparting(self, departing):
        self.departing = departing
    def getDeparting(self):
        return self.departing

    def setFlightNo(self, flightNo):
        self.flightNo = flightNo
    def getFlightNo(self):
        return self.flightNo

    def setArrivalTime(self, arrivalTime):
        self.arrivalTime = arrivalTime
    def getArrivalTime(self):
        return self.arrivalTime

    def setDepartingTime(self, departingTime):
        self.departingTime = departingTime
    def getDepartingTime(self):
        return self.departingTime

    def setFlightDate(self, flightDate):
        self.flightDate = flightDate
    def getFlightDate(self):
        return self.flightDate

    def setBoardingTill(self, boardingTill):
        self.boardingTill = boardingTill
    def getBoardingTill(self):
        return self.boardingTill

    def setTherminal(self, therminal):
        self.therminal = therminal
    def getTherminal(self):
        return self.therminal

    def __str__(self):
        return f"Destination: {self.destination}, Departing Country: {self.departing}, Flight Number: {self.flightNo}, Arrivaal Time: {self.arrivalTime}, Departing Time: {self.departingTime}, Flight Date: {self.flightDate}"

class Ticket():
    def __init__(self, ticketNo, electroNo, gateNo):
        self.ticketNo = ticketNo
        self.electroNo = electroNo
        self.gateNo = gateNo

    def setTicketNo(self, ticketNo):
        self.ticketNo = ticketNo
    def getTicketNo(self):
        return self.ticketNo

    def setElectroNo(self, electroNo):
        self.electroNo = electroNo
    def getElectroNo(self):
        return self.electroNo


    def setGateNo(self, gateNo):
        self.gateNo = gateNo
    def getGateNo(self):
        return self.gateNo

    def __str__(self):
        return f"Ticket Number: {self.ticketNo}, Electronic Ticket Number: {self.electroNo}, Gate Number: {self.gateNo}"

person1 = Person("James", "Smith", "0501234567", ["1-10-1995"], gender.Male)
passenger1 = Passenger("James", "Smith","0501234567", ["1-10-1995"], 'gender.Male', "09A", classType.FirstClass)
staff1 = Staff("Ahmed", "Mohamed", "0501234567", ["11-5-1984"], gender.Male, employType.Teller)
flight1 = Flight("New York JFK", "Chicago ORD", "NA4321", 13.30,11.40, ["6-12-2020"], 11.20, "2" )
ticket1 = Ticket("5A6BCD78", "629", "03")
BoardingPass = print(f"Name: {passenger1.getFirstName()} {passenger1.getLastName()}, From: {flight1.departing}, Flight: {flight1.getFlightNo()}, Date: {flight1.getFlightDate()}, Time: {flight1.getDepartingTime()}, Gate: {ticket1.getGateNo()}, Boarding Till: {flight1.getBoardingTill()}, Seat: {ticket1.getTicketNo()}, Electronic ticket: {ticket1.getElectroNo()}, To: {flight1.getDestination()}, Arrival Time: {flight1.getArrivalTime()}, Therminal: {flight1.getTherminal()}, Ticket Number: {ticket1.getTicketNo()}, Class: {passenger1.getClassType()}")
