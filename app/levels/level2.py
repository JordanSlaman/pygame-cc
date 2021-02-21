from app.models.level import Level
from app.models.entities import Bug
from app.models.enums import Direction


class Level2(Level):

    def __init__(self, manager):
        super().__init__(manager,
                         level_id=2,
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
        bug_path = self.create_path(start_x=7,
                                    start_y=3,
                                    direction_list=[
                                        Direction.UP,
                                        Direction.LEFT,
                                        Direction.LEFT,
                                        Direction.DOWN,
                                        Direction.DOWN,
                                        Direction.DOWN,
                                        Direction.DOWN,
                                        Direction.DOWN,
                                        Direction.DOWN,
                                        Direction.RIGHT,
                                        Direction.RIGHT,
                                        Direction.UP,
                                        Direction.UP,
                                        Direction.RIGHT,
                                        Direction.UP,
                                        Direction.UP,
                                        Direction.LEFT,
                                        Direction.UP
                                    ])
        self.entities = [
            Bug(level=self, path=bug_path),
            Bug(level=self, path=bug_path, path_starting_index=3),
            Bug(level=self, path=bug_path, path_starting_index=6)
        ]
