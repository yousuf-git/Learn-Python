"""property decorator is used for such kind of properties whose value depends on other attributes and can vary on runtime"""

# Case 1 : without property decorator
class Student:
    def __init__(self, math, phy, cs):
        self.math = math
        self.phy = phy
        self.cs = cs
        self.percentage = str((self.math + self.phy + self.cs)/3) + "%"
        
st = Student(70, 80, 90)
print("\nCase 1: Results")
print("Current Percentage:", st.percentage)
st.math = 75
print("Updated Percentage:", st.percentage) # no change

# Case 2 : with property decorator
class Student:
    def __init__(self, math, phy, cs):
        self.math = math
        self.phy = phy
        self.cs = cs
    @property
    def percentage(self):
        return str(round((self.math + self.phy + self.cs)/3)) + "%"
    # although percentage is a method but it will behave as a property

st = Student(70, 80, 90)
print("\nCase 2: Results")
print("Current Percentage:", st.percentage)
st.math = 75
print("Updated Percentage:", st.percentage) # updated one will be returned


# Self explore
# @getter
# @setter