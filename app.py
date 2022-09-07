from flask import  Flask, jsonify, render_template, request
import language_tool_python
from parrot import Parrot
import subprocess
import sys
from happytransformer import HappyTextToText, TTSettings
import torch
app = Flask(__name__)

def greturn():
    print("start")
    happy_tt = HappyTextToText("T5","vennify/t5-base-grammar-correction")
    print("args completed")
    PATH = r"happy.pth"
    print("Path defined!",end="")
    torch.save(happy_tt,PATH)
    print("model loaded")
    return


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

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def my_form_post():
    sample_input = request.form['text']
    sample_output = ''
    phrases = sample_input.split('.')
    PATH = r"C:\Users\prasad\Documents\rewrite_Website\parrot.pth"
    print("path defined")
    print("lets load model from path")
    parrot_inference = torch.load(PATH)
    for phrase in phrases:
        ph = phrase
        para_phrases = parrot_inference.augment(input_phrase=phrase)
        if para_phrases != None:
            for para_phrase in para_phrases:
                sample_output= sample_output + para_phrase[0]
                break
        elif para_phrases != None:
            sample_output= sample_output + ph
    print("Now send")
    return render_template('index.html', sample_input=sample_input, sample_output=sample_output)

@app.route('/plagarism.html')
def plagarism():
    return render_template('plagarism.html')

@app.route('/grammer.html')
def grammer():
    return render_template('grammer.html')

@app.route('/grammer.html',methods=['POST'])
def my_grammer_post():
    args = TTSettings(num_beams = 5, min_length = 1)
    PATH = r"C:\Users\prasad\Documents\rewrite_Website\happy.pth"
    happy_tt = torch.load(PATH)
    if request.method == 'POST':
        sample_input = request.form['text']
        sample_output = happy_tt.generate_text(sample_input,args=args)
        return render_template('grammer.html', sample_input=sample_input, sample_output=sample_output.text)
@app.errorhandler(404)
def page_not_found(error):
    return render_template('/')

if __name__ == "__main__":
    #rewrite()
    #greturn()
    app.run(debug=True)
