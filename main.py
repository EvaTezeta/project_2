# Import the libraries
import csv
import random

# Create empty list
participants = []

# Return the content of the file as list of dictionaries
with open("sign_up_form.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=";")
    for row in csvreader:  # Each row is read as one participant
        participants.append(row)

# Shuffle the list of participants randomly
random.shuffle(participants)

# Use random group size (0) or non-random group size by changing 0
initial_group_size = 0
possible_group_sizes = [2, 3, 4, 5]

# Create empty list
groups = []

while participants:
    group = []
    # Choose random group size
    if initial_group_size == 0:
        group_size = random.choice(possible_group_sizes)

    # Otherwise set size to be minimum of group and nr of participants
    else:
        group_size = min(initial_group_size, len(participants))

    # Assign each participant to a group within the given size limit
    for i in range(min(group_size, len(participants))):

        # Removes participants after assigning to group
        group.append(participants.pop())

    # Make sure nobody is lonely
    if len(participants) == 1:
        group.append(participants.pop())

    # Add the group to the list of groups
    groups.append(group)

# Print the groups
#def name_and_address():
for i, group in enumerate(groups):
    print(f"Group {i} ({len(group)} participants):")
    for participant in group:
        print(f"- {participant['name']} ({participant['email']})")
        print()

# Creating a nested list for the group names
# This allows for them to be mentioned later
list_with_names = []
inner_list = []

list_with_names = []
for group in groups:
    inner_list = []
    for dictionary in group:
        inner_list.append(dictionary['name'])
    list_with_names.append(inner_list)

# Open the file and read in the conversation starters
with open("conversation_starters.txt", "r") as file:
    conversation_starters = file.readlines()


# Create function to generate messages
def generate_messages_and_save_files(groups):
    for i in range(len(groups)):

        # Randomly choose a conversation starter from the list
        random_starter = random.choice(conversation_starters).strip()
        group_message = f"Hello group {i} {list_with_names}! You have been matched to this group for today's chatCOFFEE. \n\nYour conversation starter for today is: {random_starter} \n\nEnjoy your chat with coffee!"
        print(group_message)

        # Create new text files for each group with the random starter
        with open(f"generate_message_group_{i}.txt", "w") as file:
            file.write(group_message)
            print()


# Call function with previously defined groups
generate_messages_and_save_files(groups)
