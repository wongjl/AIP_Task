#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: wjinglun
"""

from fastapi import FastAPI
import gradio as gr
import requests

app = FastAPI()
api_url = 'http://backend:8080/predict'

def call_predict(image_url, question):
    post_result = requests.post(api_url, json = {'image_url': image_url, 'question': question})
    
    result = post_result.json()
    output = result['answer']
    score = result['score']
    return (image_url, output, score)

with gr.Blocks() as demo:
    gr.Markdown("""# Document (in image format) Question Answer App. 
                Click **Run** to see the output.""")
    with gr.Row():
        with gr.Column():
            inp_url = gr.Textbox(label = 'Image URL')
            inp_qn = gr.Textbox(label = 'Question')
            btn = gr.Button("Run")
            with gr.Column():
                out_result = gr.Textbox(label = 'Output', placeholder='Model Output will appear here')
                out_score = gr.Textbox(label = 'Model Score', placeholder='Model score will appear here')
        with gr.Column():
            out_img = gr.Image(label = 'Document Image')
    inp = [inp_url, inp_qn]
    out = [out_img, out_result, out_score]
            
    btn.click(fn=call_predict, inputs=inp, outputs=out)
    
app = gr.mount_gradio_app(app, demo, '/predict')