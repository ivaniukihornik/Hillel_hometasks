# 5
# You have a group of guests for the VIP box. The seats in the VIP box are all occupied by these guests.
# There is a group of guests in the common room and there are still places in it.
# Display 2 groups of guests in code.

import pprint
vip_box = 'Any', 'Bob', 'Chris', 'Dylan'
common_room = ['Elen', 'Fry', 'Grim', 'Harvey', 'Iron']

guests = {
    'Vip box': vip_box,
    'Common room': common_room
}

pprint.pprint(guests)