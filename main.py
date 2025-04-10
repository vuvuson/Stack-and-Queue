# prompt the user to choose from a menu of action to take
# if the user does not choose a listed menu, the program re-prompts the user until an appropriate option is chosen
# open a ticket
# print out a list of tickets still to be worked on
# close the ticket
from Queue import Queue
from Ticket import Ticket
from Stack import Stack

def menu():
    open_tickets = Queue()
    closed_tickets = Stack()
    ticket_counter = 1

    print("Welcome to Thibodeaux's Tech Triage\n----------------------------")

    while True:
        print("Type the number for the action you wish to perform and then hit Enter.")
        print("1. Open a new ticket")
        print("2. List All Opened Tickets")
        print("3. Close ticket")
        print("4. Review All Closed Tickets")
        print("5. Review Previously Closed Tickets")
        print("6. Quit")
        response = input("What do you want to do? __").strip()

        if response == "1":
            number = f"{ticket_counter:04d}"
            print(f"Ticket Number: {number}")
            issue = input("Ticket: ")
            ticket = Ticket(number, issue)
            open_tickets.enqueue(ticket)
            print("Ticket opened!")
            ticket_counter += 1

        elif response == "2":
            print("Open Tickets: ")
            if open_tickets.is_empty():
                print("No open tickets.")
            else:
                for t in open_tickets.list_all():
                    print(t)

        elif response == "3":
            closed = open_tickets.dequeue()
            if closed:
                closed_tickets.push(closed)
                print(f"Ticket closed: {closed}")
            else:
                print("No open tickets to close")

        elif response == "4":
            print("All Closed Tickets: ")
            if closed_tickets.is_empty():
                print("No closed tickets. ")
            else:
                for t in closed_tickets.list_all():
                    print(t)

        elif response == "5":
            last_closed = closed_tickets.peek()
            if last_closed:
                print(f"Previously Closed ticket: {last_closed}")
            else:
                print("No closed tickets yet. ")

        elif response == "6":
            print("Bye!")
            break
        else:
            print("I'm sorry, that is not an appropriate action.\n")

menu()
