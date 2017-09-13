
Run (Accesskey R)
  
Save (Accesskey S)
  
Download
  
Fresh URL
  
Open LocalChoose file
  
Reset (Accesskey X)
 CodeSkulptor 
Docs
  
Demos
  
Viz Mode
 
1
# program template for Spaceship
2
import simplegui
3
import math
4
import random
5
​
6
# globals for user interface
7
WIDTH = 800
8
HEIGHT = 600
9
score = 0
10
lives = 3
11
time = 0.5
12
​
13
class ImageInfo:
14
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
15
        self.center = center
16
        self.size = size
17
        self.radius = radius
18
        if lifespan:
19
            self.lifespan = lifespan
20
        else:
21
            self.lifespan = float('inf')
22
        self.animated = animated
23
​
24
    def get_center(self):
25
        return self.center
26
​
27
    def get_size(self):
28
        return self.size
29
​
30
    def get_radius(self):
31
        return self.radius
32
​
33
    def get_lifespan(self):
34
        return self.lifespan
35
​
36
    def get_animated(self):
37
        return self.animated
38
​
39
    
40
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
41
    
42
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
43
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
44
debris_info = ImageInfo([320, 240], [640, 480])
45
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
46
​
47
# nebula images - nebula_brown.png, nebula_blue.png
48
nebula_info = ImageInfo([400, 300], [800, 600])
49
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")
50
​
51
# splash image
52
splash_info = ImageInfo([200, 150], [400, 300])
53
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")
54
​

CodeSkulptor was built by Scott Rixner and is based upon CodeMirror and Skulpt.