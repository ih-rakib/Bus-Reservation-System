from itertools import count


class User : 
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

class Bus : 
    def __init__(self, coach, driver, arrival, departure, from_des, to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(20)]
    
class BusMetro : 
    total_bus = 5
    total_bus_list = [] # dummy database

    def install(self) : 
        bus_no = int(input('Enter Bus No. : '))
        flag = 1
        for bus in self.total_bus_list : 
            if bus_no == bus['coach'] : 
                print('Bus already installed')
                flag = 0
                break
        if flag : 
            bus_driver = input('Enter Bus Driver Name : ')
            bus_arrival = input('Enter Bus Arrival Time : ')
            bus_departure = input('Enter Bus Departure Time : ')
            bus_from = input('Enter Bus Starts From : ')
            bus_to = input('Enter Bus Destination : ')
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival, bus_departure, bus_from, bus_to) 
            self.total_bus_list.append(vars(self.new_bus))
            print('\nBus installed successfully')


class BusCounter(BusMetro) : 
    user_list = [] # user database
    bus_seat = 20

    def reservation(self) : 
        bus_no = int(input('Enter Bus Number : '))
        flag = 1
        for bus in self.total_bus_list : 
            if bus_no == bus['coach'] : 
                passanger = input('Enter Your Name : ')
                seat_no = int(input('Enter Your Seat No. : '))
                if seat_no - 1 > self.bus_seat :
                    print(f'Only {self.bus_seat} seats are available') 
                elif bus['seat'][seat_no - 1] != 'Empty' : 
                    print('Seat Already Booked')
                else : 
                    bus['seat'][seat_no - 1] = passanger
            else : 
                flag = 0
                break
        if flag == 0 : 
            print('No Bus Available')
        
    def show_bus_info(self) : 
        bus_no = int(input('Enter Bus No. : '))
        for bus in self.total_bus_list : 
            if bus['coach'] == bus_no :
                print('*' * 50)
                print('\n')
                print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                print(f"Bus Number : {bus_no} \t\t Driver : {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t\t\t Departure : {bus['departure']}")
                print(f"From : {bus['from_des']} \t\t\t To : {bus['to']}")
                print()
                a = 1
                for i in range(5) : 
                    for j in range(2) :
                        print(f"{a}. {bus['seat'][a-1]}", end = '\t')
                        a += 1  
                    print('\t', end = '')
                    for j in range(2) :
                        print(f"{a}. {bus['seat'][a-1]}", end = '\t')
                        a += 1
                    print()
    
    def get_users(self) : 
        return self.user_list
    
    def create_account(self) : 
        name = input('Enter Your Name : ') 
        flag = 0
        for user in self.get_users() : 
            if user.username == name : 
                print('Username already exist') 
                flag = 1
                break 
        if flag == 0 : 
            password = input('Enter Your Password : ') 
            self.new_user = User(name, password) 
            self.user_list.append(vars(self.new_user))
            print('Account Created Successfully')
        
    def available_buses(self) :
        if len(self.total_bus_list) == 0 : 
            print('No Bus Available') 
        else : # bus available  
            for bus in self.total_bus_list : 
                print('*' * 50)
                print('\n')
                print(f"{' '*10} {'#'*10} BUS INFO {bus['coach']} {'#'*10}")
                print(f"Bus Number : {bus['coach']} \t\t Driver : {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t\t\t Departure : {bus['departure']}")
                print(f"From : {bus['from_des']} \t\t\t To : {bus['to']}")
                print()
                a = 1
                for i in range(5) : 
                    for j in range(2) :
                        print(f"{a}. {bus['seat'][a-1]}", end = '\t')
                        a += 1  
                        print('\t', end = '')
                    for j in range(2) :
                        print(f"{a}. {bus['seat'][a-1]}", end = '\t')
                        a += 1
                    print()    
    

while True : 
    counter = BusCounter()
    print('1. Create An Account\n2. Login\n3. Exit')
    user_input = int(input('Enter Your Choice : '))

    if user_input == 3 : 
        break
    elif user_input == 1 : 
        counter.create_account()
    elif user_input == 2 : 
        name = input('Enter Your Name : ') 
        password = input('Enter Your Password : ') 

        isAdmin = False
        flag = 0
        if name == 'admin' and password == '123' : 
            isAdmin = True 

        if isAdmin == False : 
            for user in counter.get_users() : 
                if user['username'] == name and user['password'] == password : 
                    flag = 1
                    break
            if flag : 
                while True : 
                    print(f"1. Available Buses\n2. Show Bus Info\n3. Reservation\n4. EXIT")
                    a = int(input('Enter Your Choice : '))
                    if a == 4 : 
                        break
                    elif a == 1 : 
                        counter.available_buses()
                    elif a == 2 : 
                        counter.show_bus_info()
                    elif a == 3 : 
                        counter.reservation()
            else : 
                print('Invalid User!')
        
        else : 
            while True : 
                print('Hello Admin, Welcome')
                print('1. Install Bus\n2. Available Buses\n3. Show Bus\n4. Show User List\n5. EXIT')
                a = int(input('Enter Your Choice : '))
                if a == 5 : 
                    break
                elif a == 1 : 
                    counter.install()
                elif a == 2 : 
                    counter.available_buses()
                elif a == 3 : 
                    counter.show_bus_info()
                elif a == 4 :
                    counter.get_users()


# company = BusMetro()
# company.install()

b = BusCounter()
b.install()
b.install()
# b.reservation()
# b.show_bus_info()
b.available_buses()
b.create_account()