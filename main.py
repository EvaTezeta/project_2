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

while participants:
    group = []
    groups = []
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

# Give an explanation what the lists are
print("""Thank you for using chatCOFFEE!
The lists below are the groups for today's chat.\n""")

# Print the groups
for i, group in enumerate(groups):
    print(f"Group {i} ({len(group)} participants):")
    for participant in group:
        print(f"- {participant['name']} ({participant['email']})")
    print()

#An image to add to the text file
art = r""" 
          )    ) (      
         (    (  )
         )    ) (
      |      (     |
      |- - - - - - |"".
      |            |  "
      |            | ."
      |            ."
      |            |
      (||||||||||||)
      
      """

# Open the file and read in the conversation starters
with open("conversation_starters.txt", "r") as file:
    conversation_starters = file.readlines()


# Create function to generate messages
def generate_messages_and_save_files(groups):
    for i in range(len(groups)):
        # Get the list of names, faculties and interests of the group members
        names = [member["name"] for member in group]
        faculties = [member["faculty"] for member in group]
        interests = [member["interest"] for member in group]

        # Randomly choose a conversation starter from the list
        random_starter = random.choice(conversation_starters).strip()

        # Generate message with names, faculties and interests
        group_message = (f"Hello {' & '.join(names)}! You have been matched to this group for today's coffee talk.\n\nYou are in the faculties of: {' &  '.join(faculties)}.\n\nYour interests are: {' & '.join(interests)}.\n\nHere's a question to get talking: {random_starter}\n\nEnjoy your chat with a nice cup of coffee!\n{art}")
        print(group_message)

        # Create new text files for each group with the random starter
        with open(f"generate_message_group_{i}.txt", "w") as file:
            file.write(group_message)
            print()


# Call function with previously defined groups
generate_messages_and_save_files(groups)
