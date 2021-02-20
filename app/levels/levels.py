from ..models.level import Level

level_1 = Level(level_id=0,
                name="Lesson 1",
                code="BDHP",
                map_string="""
     ##### #####     
     #   ###   #     
     # c #@# c #     
   #####G#X#G#####   
   # y B     R y #   
   # c #b i r# c #   
   #####c C c#####   
   # c #b   r# c #   
   #   R  c  B   #   
   ######Y#Y######   
       #  #  #       
       # c#c #       
       # g#g #       
       #######       
""")

level_2 = Level(level_id=1,
                 name="Lesson 2",
                 code="JXMJ",
                 map_string="""
   #######         
   #  c  #         
   #     #         
   #  #  ##########
 ###  #   ww     c#
 #@X  ##  ww ooCi #
 ###  #   ww     c#
   #  #  ##########
   #     #         
   #  c  #         
   #######         
""")
