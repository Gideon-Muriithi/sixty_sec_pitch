import unittest
from app.models import Comment,User,Pitch
from app import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_gideon = User(username = 'Gideon',password = 'potato', email = 'gideon@ms.com')
        self.new_pitch = Pitch(id=1,pitch_title='Test',pitch_content='This is a test pitch',category="interview",user = self.user_Gideon,likes=0,dislikes=0)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_Gideon,pitch=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_)
        self.assertEquals(self.new_comment.pitch,self.new_pitch)
