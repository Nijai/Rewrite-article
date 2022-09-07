from happytransformer import HappyTextToText, TTSettings
import torch
print("start")
#args = TTSettings(num_beams = 5, min_length = 1)
happy_tt = HappyTextToText("T5","vennify/t5-base-grammar-correction")
print("args completed")
PATH = r"happy.pth"
print("Path defined!",end="")
torch.save(happy_tt,PATH)
#happy_tt = torch.load(PATH)
print("model loaded")
#result = happy_tt.generate_text("grammar : This sentences has has bads grammer.",args=args)
#print(result.text)
