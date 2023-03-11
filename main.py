# Requirement 2 - Read list of participants
# Import the libraries
import csv
import random

# Create empty lists
participants = []

# Return the content of the file as list of dictionaries
with open("sign_up_form.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=";")
    for row in csvreader:  # Each row is read as one participant
        participants.append(row)

# Shuffle the list of participants randomly
random.shuffle(participants)

# Use random group size (0) or non-random group size
initial_group_size = 0
possible_group_sizes = [3, 4, 5]

groups = []
# Group size should have 2 or more participants
while participants:
    group = []

    # Create list of group sizes <= to nr of participants
    if initial_group_size == 0:
        # Choose random group size
        group_size = random.choice(possible_group_sizes)
    # Else set size to be minimum of group and nr of participants
    else:
        group_size = min(initial_group_size, len(participants))

    for i in range(min(group_size, len(participants))):
        # Removes participants after assigning to group
        group.append(participants.pop())

    # Make sure nobody is lonely
    if len(participants) == 1:
        group.append(participants.pop())

    # Add the group to the list of groups
    groups.append(group)

# Print the groups
for i, group in enumerate(groups):
    print(f"Group {i+1} ({len(group)} participants):")
    for participant in group:
        print(f"- {participant['name']} ({participant['email']})")
    print()

# Requirement 7 - conversation starters are in txt file to the left

# Open the file and read in the conversation starters
with open("conversation_starters.txt", "r") as file:
    conversation_starters = file.readlines()

# Randomly choose a conversation starter from the list
random_starter = random.choice(conversation_starters).strip()


#Requirement 8
def generate_messages_and_save_files(groups, random_starter):
    for group in groups:
        group_message = f"Hello {group},\n\nYou have been matched to this group for a meeting about. Your conversation starter is:\n\n{random_starter}"
        print(group_message)
        with open(f"generate_message_group_{i+1}.txt", "w") as file:
            file.write(group_message)
            print(f"{i+1}")
