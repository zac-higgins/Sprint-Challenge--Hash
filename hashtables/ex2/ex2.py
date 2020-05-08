#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    legs = {}
    route = [None] * length
    for i in range(0, length):
        current_ticket = tickets[i]
        legs[current_ticket.source] = current_ticket.destination
    route[0] = legs["NONE"]
    route[1] = legs[route[0]]
    if length > 2:
        for i in range(2, length):
            route[i] = legs[route[i - 1]]
    return route


# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_3, ticket_2]

# reconstruct_trip(tickets, 3)