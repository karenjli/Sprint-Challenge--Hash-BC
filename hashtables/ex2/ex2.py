#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

import json


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    
    # Add each ticket into hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        
    # Find the first ticket
    ticket = hash_table_retrieve(hashtable, 'NONE')
    
    
    # Go through each ticket and add it into the route
    for i in range(length):
       
        route[i] = ticket
        ticket = hash_table_retrieve(hashtable, ticket)
    
    # Delete the last "NONE" value
    route.pop()
    return route