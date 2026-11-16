#Vaccume Cleaner Simple Reflex Agent

# Create the environment.
environment = {'A': 'Dirty', 'B': 'Dirty'}

# Set the initial location of the agent.
location = 'A'

# Run until both rooms become clean.
while True:

    # Display current status.
    print("Current Location:", location)
    print("Environment:", environment)

    # Check goal state.
    if environment['A'] == 'Clean' and environment['B'] == 'Clean':
        print("Goal achieved! Both rooms are clean.")
        break

    # Sense the current room.
    if environment[location] == 'Dirty':

        #clean the room.
        print("Action: SUCK")
        environment[location] = 'Clean'

    else:

        # Move to the other room.
        if location == 'A':
            print("Action: MOVE RIGHT")
            location = 'B'
        else:
            print("Acion: MOVE LEFT")
            location = 'A'

    print("-" * 40)

print("\n Rational Behaviour Analysis")    
print("1. Cleans A room immediately if dirty.")
print("2. Moves only when current room is already clean.") 
print("3. Stops after both rooms are clean.")
print("Hence the agent behaves rationally for this environment.")               
