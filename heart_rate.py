# File name: heart_rate.py
# Author: Amon Brollo

age = int(input("What is your age? "))
max_per_minute = 220 - age
min_beats = max_per_minute * 0.65
max_beats = max_per_minute * 0.85

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {min_beats} and {max_beats} beats per minute.")
