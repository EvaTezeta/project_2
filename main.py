# Import the libraries
import csv
import random

# A list to add all the participants
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

# A list for the groups
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
for i, group in enumerate(groups):
    print(f"Group {i} ({len(group)} participants):")
    for participant in group:
        print(f"- {participant['name']} ({participant['email']})")
    print()

# An image to added to the message
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
        group = groups[i]
        names = [member["name"] for member in group]
        faculties = [member["faculty"] for member in group]
        interests = [member["interest"] for member in group]

        #Check if the participants are from the same faculties
        def common_faculties():
            x = 0
            for one in faculties:
                for another in faculties:
                    if one == another:
                        x += 1
                        if x > len(groups[i]):
                            sentence = "Some of you are from the same faculty!"
                        else:
                            sentence = "You are all from different faculties."
            return sentence

        #Check if the participants have a common interest
        def common_interests():
            y = 0
            for one_i in interests:
                for another_i in interests:
                    if one_i == another_i:
                        y += 1
                        if y > len(groups[i]):
                            sentence_i = "Some of you have common interests!"
                        else:
                            sentence_i = "You all have different interests."
            return sentence_i

        # Randomly choose a conversation starter from the list
        random_starter = random.choice(conversation_starters).strip()

        # Generate message with names, faculties and interests
        group_message = (
            f"""Hello {' & '.join(names)}! You have been matched to group {i} for today's coffee talk. Here is some information that might be interesting for you.\n\n{common_faculties()} \nThe faculties you are from are: {' & '.join(faculties)}.\n\n{common_interests()} Your interests are: {' & '.join(interests)}. \n\nHere's a question to get talking: {random_starter}\n\nEnjoy your chat with a nice cup of coffee!\n{art} """
        )

        print(group_message)

        # Create new text files for each group with the random starter
        with open(f"generate_message_group_{i}.txt", "w") as file:
            file.write(group_message)
            print()


# Call function with previously defined groups
generate_messages_and_save_files(groups)
