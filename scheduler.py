from datetime import datetime

# Define shift times
SHIFT_TIMES = {
    "morning": ("10:30", "14:00"),
    "mid": ("14:00", "16:30"),
    "evening": ("16:30", "19:15")
}

# Define positions
POSITIONS = [ 
    "gallery 1A", "gallery 1AX", "gallery 1B", "gallery 1BX", "gallery 1C", "gallery 1CX",
    "gallery 2", "gallery 5/6", "gallery 7/8", "lobby", "rover 1", "rover 2"
]

# Class that tracks individual student data
class Student:
    def __init__(self, name, trained_for=None):
        self.name = name
        self.trained_for = trained_for if trained_for else [] # positions a student is trained for
        self.schedule = {} # Holds shifts a student is signed up for 
        self.last_position = None
        pass
    
    def sign_up(self, day, shift):
        if day not in self.schedule:
            self.schedule[day] = []
        self.schedule[day].append(shift)

# Define shift and break logic

def assign_breaks(shift_type):
    if shift_type == "single":
        return {"morning": "15 min"} if "morning" in SHIFT_TIMES else {}
    elif shift_type == "double":
        return {"morning": "15 min", "mid": "30 min"} if "morning" and "mid" in SHIFT_TIMES else {"mid": "15 min"}
    elif shift_type == "triple":
        return {"morning": "15 min", "mid": "30 min", "evening": "15 min"}
    return {}

# Training requirements and position rotation

def can_assign_position(student, position):
    # Check training requirement
    if position in ["lobby", "rover"] and position not in student.trained_for:
        return False
    # Enforce the no-repeat rule within 5 days
    if student.last_position == position:
        # later add date checks here to verify 5-day rule
        return False
    return True


# Initialize a student
student = Student("Alex", trained_for=["lobby", "rover"])

# Sign them up for shifts
student.sign_up("Monday", "morning")
student.sign_up("Monday", "mid")

# Assign a position
if can_assign_position(student, "lobby"):
    student.last_position = "lobby"  # Record last position

# Check and assign breaks
for shift in student.schedule["Monday"]:
    print(f"{shift} shift: {assign_breaks('double')}")