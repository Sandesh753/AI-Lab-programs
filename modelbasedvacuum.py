class ModelBasedVacuumCleaner:

    def __init__(self):
        # Internal model of the environment
        self.model = {
            "A": "Unknown",
            "B": "Unknown"
        }

        self.position = "A"

    # Perceive the environment
    def perceive(self, environment):
        self.model[self.position] = environment[self.position]

    # Decide action using the internal model
    def decide_action(self):

        # If current room is dirty, clean it
        if self.model[self.position] == "Dirty":
            return "Suck"

        # If current room is clean, check the other room
        if self.position == "A":
            if self.model["B"] != "Clean":
                return "Move Right"

        elif self.position == "B":
            if self.model["A"] != "Clean":
                return "Move Left"

        # Both rooms are clean
        return "Stop"

    # Perform the selected action
    def perform_action(self, action, environment):

        if action == "Suck":
            print("Sucking dirt in room", self.position)
            environment[self.position] = "Clean"

        elif action == "Move Right":
            print("Moving from A to B")
            self.position = "B"

        elif action == "Move Left":
            print("Moving from B to A")
            self.position = "A"

        elif action == "Stop":
            print("Both rooms are clean.")
            print("Vacuum cleaner stopped.")


# Actual environment
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

# Create vacuum cleaner
vacuum = ModelBasedVacuumCleaner()

print("Initial Environment:", environment)
print()

# Continue until both rooms are clean
while True:

    # 1. Perceive
    vacuum.perceive(environment)

    print("Current Position:", vacuum.position)
    print("Internal Model:", vacuum.model)

    # 2. Decide
    action = vacuum.decide_action()

    print("Action:", action)

    # 3. Perform action
    vacuum.perform_action(action, environment)

    print("Environment:", environment)
    print()

    # 4. Stop only when both rooms are clean
    if environment["A"] == "Clean" and environment["B"] == "Clean":
        print("Goal achieved!")
        break





