# Llama.cpp Server w/ Docker

## Installation

### Prerequisites

1. **Docker** - Required for running the LLaMA container
   - For Ubuntu/Debian:
   ```bash
   sudo apt update
   sudo apt install docker.io
   ```
   - For Windows: Get Linux.


2. **NVIDIA GPU drivers** (if using GPU acceleration)
   - Install NVIDIA drivers compatible with your GPU.
   - Install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) for Docker support.

## Running the Server

1. Clone or download this repository

2. Set up environment variables by editing `.env`:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. Configure the `.env` file with your specific settings:
   - `DOCKER_IMAGE`: [Docker image to use](https://github.com/ggml-org/llama.cpp/blob/master/docs/docker.md#images) (default: ghcr.io/ggml-org/llama.cpp:full-cuda13)
   - `VOLUME_MAPPING`: Host path to model directory (e.g., `/home/USERNAME/models:/models`)
   - `GPU_DEVICES`: GPU devices to use (e.g., `all` or `0,1`)
   - `PORT_MAPPING`: Port mapping (e.g., `8080:8080`)
   - `HOST_ADDRESS`: Host address to bind to (default: `0.0.0.0`)
   - `MODEL_PATH`: Path to your model file inside the container (e.g., `/models/MODEL_NAME.gguf`)
   - `CONTEXT_LENGTH`: Context length for the model (default: `4000`)
   - `NGL`: Number of layers to offload to GPU (default: `99`)
   - `PARALLEL`: Number of parallel requests (default: `1`)
   - `TEMP`: Temperature setting (default: `1.0`)


4. Run the server:
   ```bash
   python server.py
   ```

5. Alternatively, you can install and use the `lsd` command:
   ```bash
   pip install .
   lsd
   ```

## Notes

- Make sure your model files are located in the directory specified by `VOLUME_MAPPING`
- The Docker container will automatically pull the required image if it's not already present
- Ensure Docker has sufficient permissions to access your model files