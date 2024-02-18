# Parameters
file_name = "ram.json"
blueprint_name = "ram"
description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
start = 0 # Address from which to start
end = 65535 # Address to stop at ; Both are included ; My 16-bit RAM can only handle up to 65536 different addresses



# Additional parameters ; Modifying them is unneeded
direction = 2
version = "281479278493696"



pos_x = 0
pos_y = 0
entity_number = 1

file = open(file_name, "w")

# Writing head of file
file.write("{\n\t\"blueprint\": {\n\t\t\"description\": \"" + description + "\",\n\t\t\"icons\": [\n\t\t\t{\n\t\t\t\t\"signal\": {\n\t\t\t\t\t\"type\": \"item\",\n\t\t\t\t\t\"name\": \"constant-combinator\"\n\t\t\t\t},\n\t\t\t\t\"index\": 1\n\t\t\t}\n\t\t],\n\t\t\"entities\": [\n")

# Writing entities
for content in range(start, end + 1):
    file.write("\t\t\t{\n\t\t\t\t\"entity_number\": " + str(entity_number) + ",\n\t\t\t\t\"name\": \"constant-combinator\",\n\t\t\t\t\"position\": {\n\t\t\t\t\t\"x\": " + str(pos_x) + ",\n\t\t\t\t\t\"y\": " + str(pos_y) + "\n\t\t\t\t},\n\t\t\t\t\"direction\": " + str(direction) + ",\n\t\t\t\t\"control_behavior\": {\n\t\t\t\t\t\"filters\": [\n")
    # Writing signals
    for signal in range(0, 16):
        file.write("\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\"signal\": {\n\t\t\t\t\t\t\t\t\"type\": \"virtual\",\n\t\t\t\t\t\t\t\t\"name\": \"signal-" + "{0:X}".format(signal) + "\"\n\t\t\t\t\t\t\t},\n\t\t\t\t\t\t\t\"count\": " + str(-1 * ((content >> signal) % 2)) + ",\n\t\t\t\t\t\t\t\"index\": " + str(signal + 1) + "\n\t\t\t\t\t\t}")
        if (signal < 15):
            file.write(",")
        file.write("\n")
    file.write("\t\t\t\t\t]\n\t\t\t\t}\n\t\t\t}")
    if (content < end):
        file.write(",")
    file.write("\n")
    entity_number += 1
    pos_y += 1

# Writing tail of file
file.write("\t\t],\n\t\t\"item\": \"blueprint\",\n\t\t\"label\": \"" + blueprint_name + "\",\n\t\t\"version\": " + version + "\n\t}\n}")

file.close()