"""
  The Nested demo shows the use of nested state machines. We define a
  new node class DingDong that has a three-node state machine inside
  it. We then define the main class, Nested, whose state machine
  contains two instances of DingDong. DingDong uses a ParentCompletes
  node to cause DinDong to post a completion event, which allows
  Nested's first DingDong instance 'dd1' to move on to the next state,
  which is 'bridge'. (The 'dd2' instance of DingDong also posts a
  completion event, but nothing is listening for it.)

  Behavior: Cozmo says 'ding', then 'dong', then says 'once again'
  (that's the bridge), then 'ding', and then 'dong'.
"""

from cozmo_fsm import *

class DingDong(StateNode):
    def setup(self):
        """
            ding: Say('ding') =C=> dong: Say('dong') =C=> ParentCompletes()
        """
        
        # Code generated by genfsm on Sat Dec 24 22:40:36 2016:
        self.name = self.__class__.__name__
        
        ding = Say('ding') .set_name("ding") .set_parent(self)
        dong = Say('dong') .set_name("dong") .set_parent(self)
        parentcompletes1 = ParentCompletes() .set_name("parentcompletes1") .set_parent(self)
        
        completiontrans1 = CompletionTrans() .set_name("completiontrans1")
        completiontrans1 .add_sources(ding) .add_destinations(dong)
        
        completiontrans2 = CompletionTrans() .set_name("completiontrans2")
        completiontrans2 .add_sources(dong) .add_destinations(parentcompletes1)
        
        return self

class Nested(StateNode):
    def setup(self):
        """
            dd1: DingDong() =C=> bridge: Say('once again') =C=> dd2: DingDong()
        """
        
        # Code generated by genfsm on Sat Dec 24 22:40:36 2016:
        self.name = self.__class__.__name__
        
        dd1 = DingDong() .set_name("dd1") .set_parent(self)
        bridge = Say('once again') .set_name("bridge") .set_parent(self)
        dd2 = DingDong() .set_name("dd2") .set_parent(self)
        
        completiontrans3 = CompletionTrans() .set_name("completiontrans3")
        completiontrans3 .add_sources(dd1) .add_destinations(bridge)
        
        completiontrans4 = CompletionTrans() .set_name("completiontrans4")
        completiontrans4 .add_sources(bridge) .add_destinations(dd2)
        
        return self
