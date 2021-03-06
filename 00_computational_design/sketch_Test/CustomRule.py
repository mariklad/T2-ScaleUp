import hdgeom.mesh.rules.AbstractRule as AbstractRule
import hdgeom.mesh.rules.AbstractFactoryRule as AbstractFactoryRule
import hdgeom.mesh.rules.FaceRules as FaceRules
import hdgeom.mesh.Mesh as Mesh
import hdgeom.mesh.Face as Face

# class which extends the AbstractRule class
# method needs to be called 'replace', needs to take a mesh as input
# and return a mesh as output
class RulePyramid(AbstractRule):
    def __init__(self):
        self.factorExtrude=100
    def replace(self, oldMesh):
        newMesh=Mesh()
        for face in oldMesh.faces:
            newFaces=FaceRules.extrudeToPoint(face, self.factorExtrude)
            counter=0
            for cFace in newFaces:
                cFace.group=counter
                newMesh.addFace(cFace)
                counter+=1
        newMesh.constructTopology()
        return newMesh
    
# class which extends the AbstractFactoryRule class, used to fabricate the Rule
# method names have to be 'fabricateRule' and 'addComponents'
class FactoryRulePyramid(AbstractFactoryRule):
    def fabricateRule(self):
        rulePyramid=RulePyramid()
        rulePyramid.factorExtrude=self.slideFaceMove.getValue()
        return rulePyramid
    def addComponents(self,component):
        self.slideFaceMove=self.engine.cp5.addSlider(component.getName()+"test")
        self.slideFaceMove.setPosition(20,20)
        self.slideFaceMove.setLabel("moveMe")
        self.slideFaceMove.moveTo(component)