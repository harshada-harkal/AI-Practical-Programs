# Goal Stack Planning - Blocks World

goal_stack = []
plan = []

# Push goals
def push(goal):
    goal_stack.append(goal)

# Pop goals
def pop():
    return goal_stack.pop()

# Blocks World operations
def unstack(a, b):
    plan.append("UNSTACK(" + a + "," + b + ")")

def putdown(a):
    plan.append("PUTDOWN(" + a + ")")

def hold(a):
    plan.append("HOLD(" + a + ")")

def stack(a, b):
    plan.append("STACK(" + a + "," + b + ")")


# Initial State
print("INITIAL STATE")
print("B is on A")
print("A, C and D are on table")

# Push goals
push("ON(B,D)")
push("ON(C,A)")

print("\nGOAL STACK PLANNING STARTED")

# Process goals
while goal_stack:

    goal = pop()
    print("\nGoal:", goal)

    if goal == "ON(C,A)":
        print("Place C on A")

        unstack("B", "A")
        putdown("B")
        hold("C")
        stack("C", "A")

    elif goal == "ON(B,D)":
        print("Place B on D")

        hold("B")
        stack("B", "D")


# Display Final Plan
print("\nFINAL PLAN")

for step in plan:
    print(step)

print("\nGOAL STATE ACHIEVED")
print("C is on A")
print("B is on D")
