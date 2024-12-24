import gradio as gr
from PIL import Image
import io
import numpy as np
import tempfile

def muda_dpi(input_image, dpi):
    dpi_tuple = (dpi, dpi)
    
    image = Image.fromarray(input_image.astype('uint8'), 'RGB')
    
   
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    image.save(temp_file, format='PNG', dpi=dpi_tuple)
    temp_file.close()  
    
    
    return temp_file.name

#teste
iface = gr.Interface(
    fn=muda_dpi,
    inputs=[
        gr.Image(label="Upload"),
        gr.Number(label="Ajusta DPI", value=300)
    ],
    outputs=gr.File(label="Download"),
    title="Conversor DPI",
    description="Faça o upload da imagem (.jpg, .png), ajuste o DPI e submeta"
)


iface.launch(debug=True)

