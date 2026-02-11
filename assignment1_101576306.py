"""
Author: Mohamed Hisini Ahamed Assal
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"        # str
preferred_weight_kg = 20.5         # float
highest_reps = 25                  # int
membership_active = True           # bool

# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 30),
    "Taylor": (25, 50, 35)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[friend + "_Total"] = total_minutes



# Step e: Create a 2D nested list called workout_list
# 2D list: each row represents a friend, each column represents an activity
workout_list = [list(workout_stats[friend]) 
                for friend in workout_stats 
                if not friend.endswith("_Total")]



# Step f: Slice the workout_list
# Yoga and Running for all friends (first two columns)
print("Yoga and Running minutes for all friends:")
for row in workout_list:
    print(row[0:2])

# Weightlifting for the last two friends (third column)
print("\nWeightlifting minutes for the last two friends:")
for row in workout_list[-2:]:
    print(row[2])



# Step g: Check if any friend's total >= 120
print("\nChecking for friends with total workout >= 120 minutes:")
for friend in workout_stats:
    if friend.endswith("_Total") and workout_stats[friend] >= 120:
        name = friend.replace("_Total", "")
        print(f"Great job staying active, {name}!")



# Step h: User input to look up a friend
user_input = input("\nEnter a friend's name to look up: ")

if user_input in workout_stats:
    print(f"\nWorkout details for {user_input}:")
    print("Yoga:", workout_stats[user_input][0], "minutes")
    print("Running:", workout_stats[user_input][1], "minutes")
    print("Weightlifting:", workout_stats[user_input][2], "minutes")
    print("Total:", workout_stats[user_input + '_Total'], "minutes")
else:
    print(f"Friend {user_input} not found in the records.")



# Step i: Friend with highest and lowest total workout minutes
totals = {friend.replace("_Total", ""): minutes 
          for friend, minutes in workout_stats.items() 
          if friend.endswith("_Total")}

highest = max(totals, key=totals.get)
lowest = min(totals, key=totals.get)

print("\nFriend with highest total workout minutes:", highest)
print("Friend with lowest total workout minutes:", lowest)