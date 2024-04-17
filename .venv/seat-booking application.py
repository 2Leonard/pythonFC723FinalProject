import random
import string


class SeatBooking:
    def __init__(self):
        # Initialize the seating plan with the seat numbers and initial state
        self.seats = {
            "1A": "F", "1B": "F", "1C": "R", "1D": "F", "1E": "F", "1F": "F",
            "2A": "X", "2B": "F", "2C": "F", "2D": "X", "2E": "S", "2F": "S",
            "3A": "F", "3B": "R", "3C": "F", "3D": "R", "3E": "F", "3F": "F",
        }
        # Keep track of all booking references
        self.booking_references = set()
        # Store customer data referred to each booking reference
        self.customer_data = {}

    # Define a method to generate 8-character unique reference
    def generate_unique_reference(self):
        while True:
            reference = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            if reference not in self.booking_references:
                self.booking_references.add(reference)
                return reference

    # Define a method to check the availability of a seat
    def check_availability(self, seat):
        if seat in self.seats:
            if self.seats[seat] == "F":
                print(f"This seat {seat} is available.")
            else:
                print(f"This seat {seat} is not available.")
        else:
            print("Invalid seat.")

    # Define a method to book a seat
    def book_seat(self, seat):
        if seat in self.seats and self.seats[seat] == "F":
            self.seats[seat] = "R"
            print(f"This seat {seat} has been booked.")
        else:
            print("Already be booked or invalid seat.")

    # Define a method to free a seat
    def free_seat(self, seat):
        if seat in self.seats and self.seats[seat] == "R":
            self.seats[seat] = "F"
            print(f"This seat {seat} is free now.")
        else:
            print("Already be free or invalid seat.")

    # Define a method to show the booking state of seats
    def show_booking_state(self):
        for seat, state in self.seats.items():
            # Display the status
            print(f"Seat: {seat}: {'Booked' if state == 'R' else 'Free' if state == 'F' else 'Unavailable'}")

    # Define a method to run the seat-booking program
    def run(self):
        # Display a menu containing different choices
        menu = """
        1. Check availability of seat
        2. Book a seat
        3. Free a seat
        4. Show booking state 
        5. Exit program
        """
        while True:
            print(menu)
            choice = input("Enter your choice(1/2/3/4/5): ")
            if choice == "1":
                seat = input("Enter the seat number to check(eg 1A): ")
                self.check_availability(seat)
            elif choice == "2":
                seat = input("Enter the seat number to book(eg 1A): ")
                self.book_seat(seat)
            elif choice == "3":
                seat = input("Enter the seat number to free(eg 1A): ")
                self.free_seat(seat)
            elif choice == "4":
                self.show_booking_state()
            elif choice == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid input.")
            print("\n")


# Main execution
if __name__ == "__main__":
    # Create instanceof SeatBooking and run it
    program = SeatBooking()
    program.run()
