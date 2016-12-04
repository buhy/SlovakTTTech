notify_message = "010000000000"
instructionAck_message = "010000000002"
infraRed_message = "01000000000311"
roadSide_message = "010101000004050102030405"
laser_message = "010201000005030102030405060708090A0B0C"

# configurable variable to set starting index of protocol
INDEX_OF_PACKET_BYTE = 0

# actual message
message = roadSide_message

# convert 2 bytes to int representation of their hex value
packet_type = int("".join([message[INDEX_OF_PACKET_BYTE], message[INDEX_OF_PACKET_BYTE + 1]]),16)

# message is not for central unit
if packet_type != 1:
    print("not message for central unit")
    quit()
else:
    # define source board
    source_board = int("".join([message[INDEX_OF_PACKET_BYTE + 2], message[INDEX_OF_PACKET_BYTE + 3]]),16)
    source_board_number = int("".join([message[INDEX_OF_PACKET_BYTE + 4], message[INDEX_OF_PACKET_BYTE + 5]]),16)
    source_board_name = ""
    if source_board == 0:
        source_board_name = "Arduino"
    elif source_board == 1:
        source_board_name = "Raspberry"
    else:
        source_board_name = "Altera"
    print("message for central unit from", source_board_name, source_board_number)


# Function for processing notifying UDP packet.
def notify():
    print("notify")


# Function for processing acknowledgement packet.
def instruction_ack():
    print("instr ack")


# Function for processing infrared camera packet.
def process_infrared_camera():
    # convert 2 bytes to int representation of their hex value
    data = int("".join([message[INDEX_OF_PACKET_BYTE + 12], message[INDEX_OF_PACKET_BYTE + 13]]), 16)
    # TODO: save to structure
    print("infrared data: ",data)


# Function for processing road side camera packet.
def process_road_side_camera():
    # count of records
    # convert 2 bytes to int representation of their hex value
    number_of_records = int("".join([message[INDEX_OF_PACKET_BYTE + 12], message[INDEX_OF_PACKET_BYTE + 13]]), 16)
    print("count of road side data: ", number_of_records)
    index = 0
    count = 0
    print("road side data: \n")
    # iterating over numbers of road side data from camera, message[6] represents count of numbers
    for index in range(0, number_of_records):
        # TODO: save to structure
        # get entry
        entry = int("".join([message[INDEX_OF_PACKET_BYTE + 14 + count], message[INDEX_OF_PACKET_BYTE + 14 + count + 1]]), 16)
        print(entry)
        count += 2


# Function for processing laser packet.
def process_laser():
    # count of records
    # convert 2 bytes to int representation of their hex value
    number_of_records = int("".join([message[INDEX_OF_PACKET_BYTE + 12], message[INDEX_OF_PACKET_BYTE + 13]]), 16)
    print("count of lase data: ", number_of_records)
    print("laser data: \n")
    index = 0
    count = 0
    # iterating over numbers of road side data from camera, message[6] represents count of numbers
    for index in range(0, number_of_records):
        # TODO: save to structure
        # get specific entry
        start_angle = int("".join([message[INDEX_OF_PACKET_BYTE + 14 + count], message[INDEX_OF_PACKET_BYTE + 14 + count + 1]]), 16)
        end_angle = int("".join([message[INDEX_OF_PACKET_BYTE + 14 + count + 2], message[INDEX_OF_PACKET_BYTE + 14 + count + 3]]), 16)
        start_direction = int("".join([message[INDEX_OF_PACKET_BYTE + 14 + count + 4], message[INDEX_OF_PACKET_BYTE + 14 + count + 5]]), 16)
        end_direction = int("".join([message[INDEX_OF_PACKET_BYTE + 14 + count + 6], message[INDEX_OF_PACKET_BYTE + 14 + count + 7]]), 16)
        print(start_angle)
        print(end_angle)
        print(start_direction)
        print(end_direction)
        print("\n")
        count += 8


# map the message type to processing function
message_types = {
        0 : notify,
        2 : instruction_ack,
        3 : process_infrared_camera,
        4 : process_road_side_camera,
        5 : process_laser
}

# convert 2 bytes to int representation of their hex value
message_type = int("".join([message[INDEX_OF_PACKET_BYTE + 10], message[INDEX_OF_PACKET_BYTE + 11]]),16)
message_types[message_type]()