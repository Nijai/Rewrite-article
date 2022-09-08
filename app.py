from flask import  Flask, jsonify, render_template, request
from parrot import Parrot
import subprocess
import sys
from happytransformer import HappyTextToText, TTSettings
import torch
import rewriterpy as rp
import grammer as g

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def my_form_post():
    sample_input = request.form['text']
    sample_output = ''
    phrases = sample_input.split('.')
    PATH = r"parrot.pth"
    print("path defined")
    print("lets load model from path")
    parrot_inference = torch.load(PATH)
    for phrase in phrases:
        ph = phrase
        para_phrases = parrot_inference.rephrase(input_phrase=phrase)
        print("sentence found")
        if para_phrases != None:
            for para_phrase in para_phrases:
                sample_output= sample_output + para_phrase[0]
                break
        elif para_phrases != None:
            sample_output= sample_output + ph
    print("Now send")
    return render_template('index.html', sample_input=sample_input, sample_output=sample_output)

@app.route('/grammer.html')
def grammer():
    return render_template('grammer.html')

@app.route('/grammer.html',methods=['POST'])
def my_grammer_post():
    args = TTSettings(num_beams = 5, min_length = 1)
    PATH = r"happy.pth"
    happy_tt = torch.load(PATH)
    if request.method == 'POST':
        sample_input = request.form['text']
        sample_output = happy_tt.generate_text(sample_input,args=args)
        return render_template('grammer.html', sample_input=sample_input, sample_output=sample_output.text)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')
@app.errorhandler(500)
def page_not_found(error):
    return render_template('servererror.html')

if __name__ == "__main__":
    app.run(debug=True)
