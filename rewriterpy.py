import subprocess
import sys
from parrot import Parrot
import torch

def rewrite():
    print("start")
    
    print("-1-",end="")
    #Init models (make sure you init ONLY once if you integrate this to your code)

    parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)
    print("Model loaded!",end="")
    PATH = r"C:\Users\prasad\Documents\rewrite_Website\parrot.pth"
    print("Path defined!",end="")
    torch.save(parrot,PATH)
    #parrot_inference = torch.load(PATH)
    #print("Model loaded!",end="")
    print("-2-",end="")
    '''phrases = ["I'm here becuse you dumped me.","What's the most delicious papayas?","Augumented reality is becoming future now."]
    print("-3-",end="")
    for phrase in phrases:
        print("-4-")
        ph = phrase
        para_phrases = parrot_inference.augment(input_phrase=phrase)
        print("-"*100)
        print("Input_phrase: ", phrase)
        print("-"*100)
        
        if para_phrases != None:
            for para_phrase in para_phrases:
                print(para_phrase[0])
                break
        elif para_phrases == None:
            print(ph)



'''


rewrite()
'''
if __name__ == "__main__":
    app.run(debug=True)'''



