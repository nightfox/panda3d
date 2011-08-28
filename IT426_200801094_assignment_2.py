from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Vec3

class Application(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        

        self.pandaActor = Actor("babyd", {"walk": "babydani"})
        self.pandaActor.reparentTo(render)
        self.pandaActor.setPos(Vec3(5, 0, 0))
        self.pandaActor.loop("walk")
        
        self.pandaActor1 = Actor("bigd", {"walk": "bigdani"})
        self.pandaActor1.reparentTo(render)
        self.pandaActor1.setPos(Vec3(10, 0, 0))
        self.pandaActor1.loop("walk")
        
        self.pandaActor2 = Actor("trex", {"walk": "trex-eat"})
        self.pandaActor2.reparentTo(render)
        self.pandaActor2.setPos(Vec3(-10, 0, 0))
        self.pandaActor2.loop("walk")
        self.cam.setPos(0, -30, 6)

if __name__ == "__main__":
    gameApp = Application()
    gameApp.run()
    
