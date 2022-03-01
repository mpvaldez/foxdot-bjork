Root.default = "G"
Scale.default.set("minor", tuning=Tuning.ET12)
Clock.bpm = 130

class VenusAsABoy():
    mb0 = Pattern([0,-1,0,-1,-3]*3 + [0,-1,0,2,1]) # Melo Bass 0
    db0 = P[5/3,1/3,2/3,1/3,2,2/3,1/3,2/3,1/3,1]
    mb1 = Pattern([0,0,2,0,4,2,2,3,2,3,3,2,3,5,4]) # Melo Bass 1
    db1 = P[5/3,1/3,2/3,1/3,2,5/3,4/3,5/3,1/3,1,8/3,1/3,2/3,1/3,1]    
    mr0 = P[0,2,4,7,9,11,13,11,0,2,4,13,12] # Melo Riff 0
    dr0 = Pattern([1/3]*6+[2/3]+[4/3] + [1/3]*3+[2/3]+[7/3])
    mr1 = P[_,3,4,7,4,3,0,3,P[4,7],P[3,4],_]
    dr1 = Pattern([8/3] + [1/3]*7 + [2/3]*2 + [5/3])
    mc1 = P[_,0,4,_,5,4,3,2,3,2,0.5,0,(-1,2),(2,4)] # Melo cuerdas interludio 
    dc1 = Pattern([8,3,5,1] + [2/3]*4 + [5/3] + [1/3,1] + [7/3,3,4])    
    def __init__(self):    
        self.intro0()
    def intro0(self):
        p0 >> play("^", dur=4, sample=2)
        p1 >> play(" {&&[&&&]} ", dur=1, amp=0.3, sample=1).spread()
        p2 >> play(" {   +[+++]t[ttt]p[ppp]}", dur=1, amp=0.3, sample=var([0,10])).spread()
        p3 >> play(" r[  r][  r] rr[rrr]", dur=1, sample=3)
        p4 >> play(" r[  r][  r] rr[rrr]", dur=1, sample=1)
        g2 >> blip((5,6), dur=P[11/3,1/3,4], sus=1, oct=3, amp=(1,1/2), room=2).spread()
        g3 >> marimba((5,6), dur=P[11/3,1/3,4], sus=1, oct=4, amp=(2/3,1/3)).spread()    
    def intro1(self):
        p5 >> play("SS", amp=[0.4,0.2], dur=P[2/3,1/3], sample=PStep(5,0,1))
        p6 >> play("kx", dur=2, sample=3)        
    def bass0(self):
        Group(b2,b3,b4).stop()
        b0 >> jbass(self.mb0, dur=self.db0, sus=1/3, amp=0.5, lpf=1500, slide=0.05, slidedelay=0.8, pan=linvar([-0.7,0.7],4), oct=5)
        b1 >> donk(self.mb0, dur=self.db0, oct=4, amp=0.2, pan=linvar([-0.7,0.7],4))    
    def bass0to1(self):
        b0.slide = -1
        b0.slidedelay = 0
        b0.sus = 2
        b0.degree = 2
        b0.dur = 4
        b0.stop(1)
    def bass1(self):
        Group(b0,b1).stop()
        b2 >> jbass(self.mb1, dur=self.db1, sus=1/3, amp=0.5, slide=0.05, lpf=1500, slidedelay=0.8, pan=linvar([-0.7,0.7],4), oct=5)
        b3 >> space(self.mb1, dur=self.db1, chop=0.5, oct=3, amp=0.4)
        b4 >> donk(self.mb1, dur=self.db1, oct=PRange(2,7), amp=0.4, room=1, pan=linvar([-0.7,0.7],4)).spread().every([2,3], "stutter", var([3,5]))
    def riff0(self):
        r1.stop()
        r0 >> bell(self.mr0, dur=self.dr0, pan=[-0.8,0.8], oct=5, amp=linvar([0.3,0.7],2))
    def riff1(self):
        r1 >> bell(self.mr1, dur=self.dr1, pan=[-0.8,0.8], oct=5, amp=linvar([0.3,0.7],2))
        ro.stop()
    def drums1(self):
        p6 >> play("V[--V]O{-[**V]}", dur=1, amp=[0.6,0.5], sample=5).spread()
        p7 >> play(" (# )", dur=1)
    def muteDrums1(self):
        Group(p6,p7).stop()
    def muteBass(self):
        Group(b0,b1,b2,b3,b4).stop()
    def muteRiffs(self):
        Group(r0,r1).stop()
    def introOnly(self):
        Group(b0,b1,b2,b3,b4,r0,r1,p6,p7,c0,c1,c2).stop()    
vab = VenusAsABoy()

vab.intro1()

vab.bass0()

vab.bass0to1()

# His Wicked
vab.bass1()

# Interludio
vab.riff0()

vab.drums1()

vab.introOnly()

vab.riff1()

# A necklace
vab.bass0()

# He believes
vab.bass1()
vab.riff0()

# He believes 2
vab.drums1()
 
# He's exploring
vab.muteDrums1()

# Interludio
vab.drums1()

vab.introOnly()

vab.riff1()

# All across
vab.bass0()

# He believes
vab.bass1()
vab.drums1()
vab.riff0()

# Salida 1
vab.muteBass()
vab.muteRiffs()


vab.introOnly()
vab.bass1()
b3.stop()

Group(p0,b4,p2,p1).stop()

Group(p2,p4,p5,p6,g2,g3).stop()


p3.stop()
