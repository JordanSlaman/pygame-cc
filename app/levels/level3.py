from app.models.level import Level


class Level3(Level):

    def __init__(self, manager):
        super().__init__(manager,
                         level_id=3,
                         name="Lesson 3",
                         code="ECBQ",
                         map_string="""
       ###      
       #@#      
   #####X####   
   #v<<<<<<<#   
   #v######^#   
####v#wwww#^####
#v<<<#w}cw#^<<<#
#v####wwww####^#
#v#`__    fff#^#
#v#_[#    f]f#^#
#v#_c# Ci fcf#^#
#v#.__  { fff#^#
#v####    ####^#
#v>>>>^^^>>>>>^#
######^c^^######
     #^^^^#     
     ######     
""")
