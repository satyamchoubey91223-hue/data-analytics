from datetime import datetime
from config import TOTAL_SLOTS, RATE_PER_HOUR

parking = {}

# park vehicle
def park_vehicle_logic(vehicle):

    vehicle = vehicle.upper()

    if vehicle == "":
        return -1

    # prevent duplicate vehicles
    for slot in parking:
        if parking[slot]["vehicle"] == vehicle:
            return -2

    for slot in range(1, TOTAL_SLOTS + 1):

        if slot not in parking:

            parking[slot] = {
                "vehicle": vehicle,
                "time": datetime.now()
            }

            return slot

    return -1


# exit vehicle using vehicle number
def exit_vehicle_logic(vehicle):

    vehicle = vehicle.upper()

    slot_found = None

    for slot, data in parking.items():

        if data["vehicle"] == vehicle:
            slot_found = slot
            break

    if slot_found is None:
        return -1, -1

    data = parking.pop(slot_found)

    entry_time = data["time"]
    exit_time = datetime.now()

    hours = (exit_time - entry_time).seconds / 3600
    hours = max(1, int(hours))

    fee = hours * RATE_PER_HOUR

    return slot_found, fee