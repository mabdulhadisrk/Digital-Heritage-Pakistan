from nicegui import ui
import easyocr

# 1. Initialize the Urdu AI engine once
print("Loading Urdu AI Brain...")
reader = easyocr.Reader(['ur']) 

# Notice the 'async' keyword added right here
async def handle_upload(e):
    result_box.set_text("AI is reading the Urdu text...")
    
    try:
        # Notice the 'await' keyword right here to unpack asynchronous image files cleanly
        file_content = await e.file.read()
        
        # Save the downloaded bytes directly into a temporary file on your hard drive
        with open('temp_page.png', 'wb') as f:
            f.write(file_content)
        
        # Tell the AI engine to scan that exact image file path string
        results = reader.readtext('temp_page.png', detail=0)
        
        # Glue the text together
        final_text = " ".join(results)
        
        if final_text:
            result_box.set_text(final_text)
        else:
            result_box.set_text("No text detected. Try a sharper image!")
            
    except Exception as error:
        result_box.set_text(f"Error: {str(error)}")

# --- Visual Component Elements ---
ui.label('Digital Heritage Pakistan').classes('text-2xl font-bold text-center mt-4')

ui.upload(label="Upload Urdu Document Here", on_upload=handle_upload, auto_upload=True).classes('w-96 mx-auto my-4')

result_box = ui.label('Your text will show up here...').classes('p-4 bg-gray-100 rounded text-center block w-96 mx-auto')

ui.run(port=8080)
