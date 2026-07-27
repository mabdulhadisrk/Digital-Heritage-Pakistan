from nicegui import ui
import easyocr
import io
from PIL import Image

# 1. Initialize the Urdu AI Reader in the background
print("Initializing Urdu AI Model...")
reader = easyocr.Reader(['ur']) 

# 2. Define what happens when a file is uploaded
def handle_upload(e):
    # Change the text to show the AI is processing
    result_box.set_text("AI is analyzing the Urdu manuscript...")
    
    # Read the raw uploaded image bytes
    image_bytes = e.content.read()
    image = Image.open(io.BytesIO(image_bytes))
    
    # Run the EasyOCR model over the image data
    results = reader.readtext(image_bytes, detail=0)
    
    # Join the extracted text lines together
    extracted_text = " ".join(results)
    
    # Display the final text inside our modern web component
    if extracted_text:
        result_box.set_text(extracted_text)
    else:
        result_box.set_text("No Urdu text detected. Please try a clearer image.")

# 3. Build the Modern 2026 Layout (Using CSS Grid via Python)
with ui.card().classes('w-full max-w-2xl mx-auto my-12 p-8 shadow-2xl rounded-xl bg-white border border-slate-100'):
    # Header Section
    ui.label('Digital Heritage Pakistan').classes('text-3xl font-extrabold tracking-tight text-slate-800 text-center')
    ui.label('Using Edge Computer Vision to preserve national history.').classes('text-sm text-slate-500 text-center mb-6')
    
    # Modern Drag-and-Drop Area (Styled with modern CSS utility classes)
    ui.upload(on_upload=handle_upload, label="Drag or click to upload Urdu text") \
        .classes('w-full border-2 border-dashed border-slate-300 rounded-lg p-4 bg-slate-50 hover:border-blue-500 transition-colors')
    
    # Interactive Output Panel
    ui.label('AI Extracted Corpus:').classes('text-xs font-semibold uppercase tracking-wider text-slate-400 mt-6')
    result_box = ui.label('Your processed Urdu text will appear here...').classes('p-4 bg-slate-100 rounded-lg text-slate-700 min-h-[100px] font-serif text-lg leading-relaxed text-right rtl')

# Start the local web deployment server
ui.run(title="Digital Heritage Prototype", port=8080)
