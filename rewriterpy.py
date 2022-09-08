import subprocess
import sys
from parrot import Parrot
import pickle

def greturn():
    print("start")
    happy_tt = HappyTextToText("T5","vennify/t5-base-grammar-correction")
    print("args completed")
    PATH = r"happy.pth"
    print("Path defined!",end="")
    torch.save(happy_tt,PATH)
    print("model loaded")
    return






