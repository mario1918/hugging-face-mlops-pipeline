from transformers import pipeline
import gradrio as gr

# Making an instance of a model
model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbox = gr.TextBox(placeholder="Enter text block to summarize", lines=4)
    gr.Interface(fn=predict, inputs=textbox, outputs="text")

demo.launch()