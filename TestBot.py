import gradio as gr
import random

# Keyword-based response dictionary
instructions = {
    ("hello", "hi"): [
        "Hello, how can I help you?",
        "Hi there, what's on your mind?",
        "Hello, I am here to assist"
    ],
    ("hot", "overheating", "overheated", "temperature", "high"): [
        "I will look for this, if you can tell me whether the processor used is NUC, box, or tray"
    ],
    ("nuc",): [
        """Customer Support Services for Intel NUC Products Has Transitioned to ASUS as of January 16, 2024.
        For more details refer to article: 000097279"""
    ],
    ("tray", "laptop"): [
        "Send customer to system manufacturer as we do not handle laptop or pre-built systems"
    ],
    ("box", "desktop"): [
        "Can you give me a complete model number of the processor?"
    ],
    ("13900k", "14900", "intelcore", "ultra", "235a"): [
        "Suggest customer to check:\n"
        "- The thermal solution\n"
        "- Check fan operation status\n"
        "- Load BIOS to default or Update BIOS\n"
        "For more troubleshooting steps refer to article: 000005791"
    ],
    ("intel", "core", "i5", "3450", "processor"): [
        "This is an EOIS product, suggest customer to post in Intel community forum"
    ],
    ("intel", "gpu", "arc", "a770", "a750", "b580", "graphics", "discrete", "dedicated", "low", "fps"): [
        "I can help you with improving FPS on a system with Intel GPU. Suggest customer to:\n"
        "- Update to latest graphics drivers\n"
        "- Close background apps\n"
        "- Install latest game patch\n"
        "More info: https://www.intel.com/content/www/us/en/gaming/resources/how-to-fix-your-low-frame-rate.html"
    ],
    ("overclocking", "warranty"): [
        "Can you tell me the type of processor? Is it tray or box? I will help you on this."
    ]
}

# Response logic function
def chatbot_response(user_input):
    x = user_input.lower().strip()
    words = x.split()

    # Exit phrases
    if x in ("bye", "ok bye", "exit", "quit", "thanks"):
        return "Thanks for using Mango 🥭", True

    # Overclocking logic
    if any(word in ("overclocking", "warranty") for word in words):
        if "tray" in words:
            return "Tray processors are not covered under Intel warranty if overclocked. Customer can contact OEM.", False
        elif "box" in words:
            return ("Altering clock frequency may void warranty even with Intel XMP. Please refer to Intel warranty terms article below:\n"
                    "https://www.intel.com/content/www/us/en/support/articles/000005494/processors.html"), False
        else:
            return "Can you tell me the type of processor? Is it tray or box?", False

    # Keyword matching
    for keywords, reply_list in instructions.items():
        if any(word in keywords for word in words):
            return random.choice(reply_list), False

    # Fallback response
    return "Sorry, I did not understand. Can you provide more details?", False

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("""
    <div style='text-align: center;'>
        <h1 style='display: inline; margin-right: 10px;'>🥭 Mango AI</h1>
        <span style='font-size: 12px;'>by Sunil Venkatesh</span>
    </div>
    """)
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="", placeholder="Type here…", lines=1)
    end_note = gr.Markdown(visible=False)
    restart_btn = gr.Button("🔄 Restart Chat", visible=False)

    # Chat response handler
    def respond(message, chat_history):
        reply, end_chat = chatbot_response(message)
        chat_history.append((message, reply))
        if end_chat:
            msg.interactive = False
            end_note.update("**Chat Ended. Thank you for chatting with Mango!**")
            end_note.visible = True
            restart_btn.visible = True
        return "", chat_history

    # Restart handler
    def restart():
        msg.interactive = True
        restart_btn.visible = False
        end_note.visible = False
        return "", []

    msg.submit(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    restart_btn.click(restart, outputs=[msg, chatbot])

demo.launch()
