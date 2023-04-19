# Calculate cost of visiting cinema

# A local town has a cinema which costs $15 per ticket, but offers a discount of $5 per ticket for anyone of age 60 or over.

# Anyone buying a ticket to see a movie must also buy candy, which costs $10 unless the person is a member in which it costs then $5.

# The cinema has a free bus service which will transport customers, and if they choose to drive a car then they must pay $3 for the parking spot.

# Your goal is to calculate the cost of visiting the cinema.

# The function will take three arguments:

#     age : integer

#     has_membership : boolean

#     transport_type : string

# e.g

# calculate_total_cost_of_visiting_cinema(20, True, "Car") # returns 15 + 5 + 3

# calculate_total_cost_of_visiting_cinema(65, False, "Bus") # returns 10 + 10 + 0

# calculate_total_cost_of_visiting_cinema(45, False, "Car") # returns 15 + 10 + 3

# calculate_total_cost_of_visiting_cinema(60, True, "Car") # 10 + 5 + 3


age = 60
has_membership = True
transport_type = "Car"
# def calculate_total_cost_of_visiting_cinema(age, has_membership, transport_type):

entry_ticket_cost =  15
candy_cost =  10
parking_cost =  3


if age >= 60:
    entry_ticket_cost -= 5

if has_membership == True:
    candy_cost = 5

if transport_type == "Bus":
    parking_cost = 0

print (entry_ticket_cost, candy_cost, parking_cost)




# You are an astronaut on Mars and are tasked with fixing solar panel arrays and other electronics that are vital to the colony's survival.

# As you identify issues you embark on the mission of fixing the issue.

# To identify if you are ready to embark on the mission you write a function that will return True if you are ready, and False if you need to make more preparations.

# To be ready for a mission you must:

#     Have the supplies ready to fix the issue.

#     Be able to walk to the mission site, if the mission site is less than or equal to 10 units of distance away OR be able to take a vehicle to the mission site if the vehicle has enough fuel for a return trip, where 1 unit of fuel is required for 1 unit of distance.

# The function will take three arguments:

#     have_supplies : boolean

#     distance_to_mission_site : integer

#     fuel_in_vehicle : integer

# e.g 

# ready_to_embark_on_mission(False, 1, 100) # returns False

# ready_to_embark_on_mission(True, 1, 100) # returns True

# ready_to_embark_on_mission(True, 5, 0) # returns True

# ready_to_embark_on_mission(True, 20, 30) # returns False

# ready_to_embark_on_mission(True, 20, 40) # returns True

# ready_to_embark_on_mission(True, 100, 300) # returns True

# have_supplies = False
# distance_to_mission_site = 1
# fuel_in_vehicle = 100
def ready_to_embark_on_mission(have_supplies, distance_to_mission_site, fuel_in_vehicle):
    
    if have_supplies == True and (fuel_in_vehicle >= distance_to_mission_site * 2 or distance_to_mission_site <= 10):
        return True
    else:
        return False
