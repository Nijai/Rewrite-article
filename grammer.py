from happytransformer import HappyTextToText, TTSettings
import torch
def rewrite():
    print("start")
    
    print("-Lets load model-",end="")
    parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)
    print("Model loaded!-",end="")
    PATH = r"parrot.pth"
    print("Path defined!-",end="")
    torch.save(parrot,PATH)
    print("Saved Model-",end="")
    return

