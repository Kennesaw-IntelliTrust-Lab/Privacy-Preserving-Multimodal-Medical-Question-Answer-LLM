# Privacy-Preserving-Multimodal-Medical-Question-Answer-LLM
# Install
1. Clone this repository and navigate to LLaVA-Med folder
     ```sh
     https://github.com/microsoft/LLaVA-Med.git
     cd LLaVA-Med
     ```
2. Install Package: Create conda environment
    ```sh
     conda create -n llava-med python=3.10 -y
     conda activate llava-med
     pip install --upgrade pip  # enable PEP 660 support
     pip install -e .
     ```
3. Install openai
   ```sh
     import openai
     ```
     If you are running a Python script and want to access the API key
      ```sh
     import os
     api_key = os.getenv("OPENAI_API_KEY")

     ```
# Serving

### Web UI

**Launch a Controller**
   ```sh
     python -m llava.serve.controller --host 0.0.0.0 --port 10000
   ```
**Launch a model worker**
   ```sh
     python -m llava.serve.model_worker --host 0.0.0.0 --controller http://localhost:10000 --port 40000 --worker http://localhost:40000 --model-path microsoft/llava-med-v1.5-mistral-7b --multi-modal
   ```
Wait until the process finishes loading the model and you see "Uvicorn running on ...".

**Launch a model worker (Multiple GPUs, when GPU VRAM <= 24GB)**
If your the VRAM of your GPU is less than 24GB (e.g., RTX 3090, RTX 4090, etc.), you may try running it with multiple GPUs.
   ```sh
     python -m llava.serve.model_worker --host 0.0.0.0 --controller http://localhost:10000 --port 40000 --worker http://localhost:40000 --model-path microsoft/llava-med-v1.5-mistral-7b --multi-modal --num-gpus 2
   ```
Wait until the process finishes loading the model and you see "Uvicorn running on ...".

**Send a test message**
   ```sh
     python -m llava.serve.test_message --model-name llava-med-v1.5-mistral-7b --controller http://localhost:10000
   ```
**Launch a gradio server**
   ```sh
     python -m llava.serve.gradio_web_server --controller http://localhost:10000
   ```
**You can open your browser and chat with a model now.**
