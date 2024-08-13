
def ticket_number(next_num):
    return f"Ticket{str(next_num).zfill(3)}"

def add_ticket(tickets,next_num,customer,issue,):
    ticket_num = ticket_number(next_num)
    if ticket_num not in tickets:
        tickets[ticket_num] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"{ticket_num} has been added to Customer Service Tickets.")
        return next_num + 1

def update_status(tickets,ticket_num,status):
    if ticket_num in tickets:
        tickets[ticket_num]["Status"] = status
        print(f"{ticket_num} status has been updated to {status}")
    else:
        print(f"{ticket_num} was not found or input not valid.")

def display_tickets(tickets,filter_view=None):
    for ticket_num, details in tickets.items():
        if details["Status"] == filter_view or filter_view is None:
            print(f"{ticket_num}: {details}")



service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
next_number = 3

while True:
    print("  \nCustomer Ticket Tracker \n  \
          1. Add new customer ticket \n  \
          2. Open/Close Ticket \n  \
          3. Display all \n  \
          4. Display with Filter \n  \
          5. Quit\n ")

    choice = int(input("Please enter the number for the action you would like to perform: "))

    if choice == 1:
        customer = input("Please enter the customer's name: ")
        issue = input("Please describe the customer's issue: ")
        next_number = add_ticket(service_tickets,next_number,customer,issue)
    elif choice == 2:
        ticket_num =input("Please enter the ticket number for it's status to be updated: ")
        status = input("Please enter the new status for this ticket-(open/closed): ").lower()
        update_status(service_tickets,ticket_num,status)
    elif choice == 3:
        display_tickets(service_tickets)
    elif choice == 4:
        filter_view = input("To view open or closed enter one-(open/closed): ")
        if filter_view.lower() == "open" or filter_view.lower() == "closed":
            display_tickets(service_tickets,filter_view)
        else:
            print("That is an invalid response.")
    elif choice == 5:
        print("Thank you for using our Customer Ticket Tracker platform. \n  \
              Exiting platform...")
        break
    else:
        print("Does not compute, invalid response. ")
