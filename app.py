from transformers import pipeline
import gradio as gr

# Making an instance of a model
model = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def predict(prompt):
    result = model(prompt)[0]
    return f"{result['label']}: {result['score']:.4f}"

with gr.Blocks() as demo:
    textbox = gr.TextBox(placeholder="Enter text block to summarize", lines=4)
    gr.Interface(fn=predict, inputs=textbox, outputs="text")

demo.launch()

# print(predict("I love this product! It works great and exceeded my expectations."))