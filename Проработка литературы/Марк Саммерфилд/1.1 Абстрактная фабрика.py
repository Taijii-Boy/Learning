def main():
    txtDiagram = create_diagram(DiagramFactory())
    txtDiagram.save(textFilename)

    svgDiagram = create_diagram(SvgDiagramFactory())
    svgDiagram.save(svgFilename)


def create_diagram(factory):
    diagram = factory.male_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, "yellow")
    text = factory.make_text(7, 3, "Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram

class DiagramFactory:

    def make_diagram(self, width, height):
        return Diagram(width, height)

    def make_rectangle(self, x, y, width, height, fill="white", stroke="black"):
        return Rectangle(x, y, width, height, fill, stroke)

    def make_text(self, x, y, text, fontsize=12):
        return Text(x, y, text, fontsize)