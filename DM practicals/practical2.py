# Create a class RELATION, use Matrix notation to represent a relation. Include member functions to check if the relation is Reflexive, Symmetric, Anti-symmetric, Transitive. Using these functions check whether the given relation is: Equivalence or Partial Order relation or None

# with this snippet from practical2.py:
class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix

    def is_reflexive(self):
        for i in range(len(self.matrix)):
            if self.matrix[i][i] != 1:
                return False
        return True

    def is_symmetric(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1 and self.matrix[j][i] == 1 and i != j:
                    return False
        return True

    def is_transitive(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1:
                    for k in range(len(self.matrix)):
                        if self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                            return False
        return True

    def is_equivalence(self):
        if self.is_reflexive() and self.is_symmetric() and self.is_transitive():
            return True
        return False

    def is_partial_order(self):
        if self.is_reflexive() and self.is_antisymmetric() and self.is_transitive():
            return True
        return False

    def is_none(self):
        if not self.is_reflexive() and not self.is_symmetric() and not self.is_antisymmetric() and not self.is_transitive():
            return True 
        return False

def main():
    # sample matrix of 3x3
    matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    
    # if you want to take input from user
    # matrix = []
    # n = int(input("Enter the number of rows and columns: "))
    # for i in range(n):
    #     matrix.append(list(map(int, input().split())))
    relation = RELATION(matrix)
    while True:
        print("1. Check if the relation is Reflexive")
        print("2. Check if the relation is Symmetric")
        print("3. Check if the relation is Anti-symmetric")
        print("4. Check if the relation is Transitive")
        print("5. Check if the relation is Equivalence")
        print("6. Check if the relation is Partial Order")
        print("7. Check if the relation is None")
        print("8. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(relation.is_reflexive())
        elif choice == 2:
            print(relation.is_symmetric())
        elif choice == 3:
            print(relation.is_antisymmetric())
        elif choice == 4:
            print(relation.is_transitive())
        elif choice == 5:
            print(relation.is_equivalence())
        elif choice == 6:
            print(relation.is_partial_order())
        elif choice == 7:
            print(relation.is_none())
        elif choice == 8:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()