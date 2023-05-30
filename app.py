import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Concrete Prototype: {self.name}")

# Example usage
if __name__ == "__main__":
    # Create a prototype instance
    prototype = ConcretePrototype("Prototype 1")

    # Clone the prototype
    clone = prototype.clone()
    clone.display()


