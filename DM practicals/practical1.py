# Create a class SET. Create member functions to perform the following SET operations:

class Set:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    # 1) is member: check whether an element belongs to the set or not and return value as true/false.
    def is_member(self, element):
        if element in self.set1:
            return True
        else:
            return False

    # 2) powerset: list all the elements of the power set of a set .
    def powerset(self,sets):
        power_set = [[]]
        for i in sets:
            for j in power_set:
                power_set = power_set + [list(j) + [i]]
        return power_set

    # 3) subset: Check whether one set is a subset of the other or not.
    def subset(self):
        if set(self.set1).issubset(set(self.set2)):
            return True
        else:
            return False

    # 4) union: Union of two sets.
    def union(self):
        return set(self.set1).union(set(self.set2))

    # 5) intersection: Intersection of two sets.
    def intersection(self):
        return set(self.set1).intersection(set(self.set2))

    # 6) complement: Assume Universal Set as per the input elements from the user.
    def complement(self, universal_set ,sets):
        return set(universal_set).difference(set(sets))

    # 7) set Difference and Symmetric Difference between two sets.
    def set_difference(self):
        return set(self.set1).difference(set(self.set2))

    # 8) symmetric Difference between two sets.
    def symmetric_difference(self):
        return set(self.set1).symmetric_difference(set(self.set2))

    # 9) cartesian Product of Sets.
    def cartesian_product(self):
        return [(i, j) for i in self.set1 for j in self.set2]
    

# Write a menu driven program to perform the above functions on an instance of the SET class.

def main():
    # sample input
    set1 = [1, 2, 3]
    set2 = [3, 4, 5]
    universal_set = [1, 2, 3, 4, 5, 6]

    # input the elements of the set by user
    # set1 = list(map(int, input("Enter the elements of set1: ").split()))
    # set2 = list(map(int, input("Enter the elements of set2: ").split()))
    # universal_set = list(map(int, input("Enter the elements of universal set: ").split()))
    
    obj = Set(set1, set2)
    while True:
        print("\n1. Check whether an element belongs to the set or not")
        print("2. List all the elements of the power set of a set")
        print("3. Check whether one set is a subset of the other or not")
        print("4. Union of two sets")
        print("5. Intersection of two sets")
        print("6. Complement of a set")
        print("7. Set Difference between two sets")
        print("8. Symmetric Difference between two sets")
        print("9. Cartesian Product of two sets")
        print("10. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            element = int(input("Enter the element to check: "))
            print(obj.is_member(element))
        elif choice == 2:
            choice = int(input("Enter the set number (1/2): "))
            if choice == 1:
                print(obj.powerset(set1))
            elif choice == 2:   
                print(obj.powerset(set2))
        elif choice == 3:
            print(obj.subset())
        elif choice == 4:
            print(obj.union())
        elif choice == 5:
            print(obj.intersection())
        elif choice == 6:
            choice = int(input("Enter the set number (1/2): "))
            if choice == 1:
                print(obj.complement(universal_set, set1))
            elif choice == 2:
                print(obj.complement(universal_set, set2))
        elif choice == 7:
            print(obj.set_difference())
        elif choice == 8:
            print(obj.symmetric_difference())
        elif choice == 9:
            print(obj.cartesian_product())
        elif choice == 10:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
