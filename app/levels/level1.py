from app.models.level import Level


class Level1(Level):
    level_id = 1
    name = "Lesson 1"
    code = "BDHP"
    level_info = "Hint: Collect chips to get past the chip socket. Use keys to open doors."

    map_string = """
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
"""

    def __init__(self, manager):
        super().__init__(manager)
