class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall = hall
        self.hall_list.append(hall)

class Hall:
    def __init__(self,rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema().entry_hall(self)
    
    def entry_show(self, id, movie_show, time):
        show = (id, movie_show, time)
        self.__show_list.append(show)
        seat = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self.__seats[id] = seat
    
    def book_seat(self, show_id, total_ticket):
        if show_id in self.__seats:
            all_seat = self.__seats[show_id]
            for i in range(total_ticket):
                row = int(input('Enter Seat Row : '))
                col = int(input('Enter Seat Col : '))
                if row < len(all_seat) and col < len(all_seat[0]):
                    if all_seat[row][col] == 0:
                        all_seat[row][col] = 1
                        print(f'Seat {row, col} booked for show {show_id}')
                    else:
                        print(f'Seat {row,col} is already booked!!')
                else:
                    print('Invalid seat number!')
        else:
            print('Show Id not found')
    
    def view_show_list(self):
        print('-------------------------------')
        for shows in self.__show_list:
            print(f'MOVIE NAME : {shows[1]} SHOW ID : {shows[0]} TIME : {shows[2]}')
        print('-------------------------------')

    def view_available_seats(self, show_id):
        seat = self.__seats[show_id]
        for i in seat:
            print(i)


hall = Hall(4, 4, 100)
hall.entry_show(111, 'JAWAN MAJI(111)', '10/18/24 2.00 PM')
hall.entry_show(112, 'SUJON MAJI(112)', '10/18/24 6.00 PM')

while True:
    print('1. VIEW ALL SHOW TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    print('4. EXIT')
    n = int(input('ENTER OPTION : '))

    if n == 1:
        hall.view_show_list()
    elif n == 2:
        id = int(input('ENTER SHOW ID : ')) 
        hall.view_available_seats(id)
    elif n == 3:
        id = int(input('SHOW ID : '))
        total = int(input('NUMBER OF TICKET : '))
        hall.book_seat(id, total)
    else:
        break