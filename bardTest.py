from bardapi import Bard

token = 'bwjZWuRBwObQNEXmxPqY2WfUDGoqy-pxDVsPmw_gIYkBNk-j-TbN9AhF99IZ3EEGCkSj4Q.'
bard = Bard(token)
print(bard.get_answer("What's 2+2")['content'])