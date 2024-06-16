# Define an empty list to store goals
goals = []

# Function to display the goals list
def display_goals():
    if not goals:
        print("Your goals list is empty.")
    else:
        print("Goals List:")
        for i, goal in enumerate(goals, start=1):
            status = "Achieved" if goal["achieved"] else "Not Achieved"
            print(f"{i}. {goal['description']} ({status})")

# Function to add a goal to the goals list
def add_goal(description):
    goal = {"description": description, "achieved": False}
    goals.append(goal)
    print(f"Goal '{description}' added to your goals list.")

# Function to mark a goal as achieved
def mark_achieved(goal_number):
    if 1 <= goal_number <= len(goals):
        goals[goal_number - 1]["achieved"] = True
        print(f"Goal {goal_number} marked as achieved.")
    else:
        print("Invalid goal number. Please enter a valid goal number.")

# Function to mark a goal as incomplete
def mark_incomplete(goal_number):
    if 1 <= goal_number <= len(goals):
        goals[goal_number - 1]["achieved"] = False
        print(f"Goal {goal_number} marked as incomplete.")
    else:
        print("Invalid goal number. Please enter a valid goal number.")

# Function to remove a goal from the goals list
def remove_goal(goal_number):
    if 1 <= goal_number <= len(goals):
        removed_goal = goals.pop(goal_number - 1)
        print(f"Goal '{removed_goal['description']}' removed from your goals list.")
    else:
        print("Invalid goal number. Please enter a valid goal number.")

# Main program loop
def main():
    while True:
        print("\nOptions:")
        print("1. Display goals list")
        print("2. Add a goal")
        print("3. Mark a goal as achieved")
        print("4. Mark a goal as incomplete")
        print("5. Remove a goal")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_goals()
        elif choice == '2':
            description = input("Enter the goal: ")
            add_goal(description)
        elif choice == '3':
            display_goals()
            try:
                goal_number = int(input("Enter the goal number to mark as achieved: "))
                mark_achieved(goal_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            display_goals()
            try:
                goal_number = int(input("Enter the goal number to mark as incomplete: "))
                mark_incomplete(goal_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            display_goals()
            try:
                goal_number = int(input("Enter the goal number to remove: "))
                remove_goal(goal_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
