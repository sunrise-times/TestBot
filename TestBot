import gradio as gr
import random

instructions = {
    ("hello", "hi"): [
        "Hello, how can I help you?",
        "Hi there, what's on your mind?",
        "Hello, I am here to assist"
    ],
    ("hot", "overheat", "temperature", "high"): [
        "I will look for this, if you can tell me whether the processor used is NUC, box, or tray"
    ],
    ("nuc",): [
        "Customer Support Services for Intel NUC Products Has Transitioned to ASUS as of January 16, 2024. For more details refer to article: 000097279"
    ],
    ("tray", "laptop"): [
        "Send customer to system manufacturer as we do not handle laptop or pre-built systems"
    ],
    ("box", "desktop"): [
        "Can you give me a complete model number of the processor?"
    ],
    ("13900k", "14900", "intelcore", "ultra", "235a"): [
        "Suggest customer to check:\n- The thermal solution\n- Check fan operation status\n- Load BIOS to default or Update BIOS\nFor more troubleshooting steps refer to article: 000005791"
    ],
    ("Intel", "Core", "i5", "3450", "Processor"): [
        "Oh oh! This is an EOIS product, suggest customer to post in Intel community forum"
    ]
}

def respond(message, history):
    message = message.lower().strip()
    if message in ("exit", "quit", "ok bye"):
        history.append((message, "Goodbye! Take care."))
        return "", history, gr.update(visible=False), gr.update(visible=True)

    words = message.split()
    for keywords, replies in instructions.items():
        if any(word in keywords for word in words):
            history.append((message, random.choice(replies)))
            return "", history, gr.update(visible=True), gr.update(visible=False)

    history.append((message, "Sorry, I did not understand. Can you provide more details?"))
    return "", history, gr.update(visible=True), gr.update(visible=False)

def restart_chat():
    return [], gr.update(visible=True), gr.update(visible=False)

with gr.Blocks(css="body {background-color: #1e1e1e;}") as demo:
    gr.HTML("<h2 style='color:white; font-weight:bold; text-align:center;'>Infinity</h2>")
    
    chatbot = gr.Chatbot(show_label=False)
    msg = gr.Textbox(placeholder="Ask Infinity...", show_label=False)
    restart_btn = gr.Button("🔄 Restart Chat", visible=False)

    msg.submit(respond, [msg, chatbot], [msg, chatbot, msg, restart_btn])
    restart_btn.click(restart_chat, outputs=[chatbot, msg, restart_btn])

demo.launch()
