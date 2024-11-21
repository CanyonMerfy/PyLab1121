class MindMapLeaf:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def __str__(self):
        return self.get_shape_representation().format(name=self.name)


    def get_shape_representation(self):
        shapes = {
            "circle": "(({name}))",
            "oval": "({name})",
            "square": "[{name}]",
            "cloud": "){name}(",
            "hexagon": "{{{{{name}}}}}",
            "bang": ")){name}(("
        }

        return shapes.get(self.shape, "{name}")

    def display(self, indent=0):
        if indent == 0:
            print("mindmap\nroot", end="")
        print(" "*indent + str(self))

def main():
    mml = MindMapLeaf("Canyon", "circle")
    #mml.display(4)
main()
