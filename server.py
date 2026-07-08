import subprocess
import sys


def main():
    # Load environment variables from .env file
    env_vars = {}
    try:
        with open('.env', 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    env_vars[key] = value
    except FileNotFoundError:
        print("Error: .env file not found")
        sys.exit(1)
    
    # Check that all required environment variables are set
    required_vars = [
        'DOCKER_IMAGE', 'VOLUME_MAPPING', 'GPU_DEVICES', 'PORT_MAPPING', 
        'HOST_ADDRESS', 'MODEL_PATH', 'CONTEXT_LENGTH', 'NGL', 
        'PARALLEL', 'TEMP'
    ]
    
    missing_vars = []
    for var in required_vars:
        if var not in env_vars:
            missing_vars.append(var)
    
    if missing_vars:
        print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
        sys.exit(1)
    
    # Get values from environment variables
    docker_image = env_vars['DOCKER_IMAGE']
    volume_mapping = env_vars['VOLUME_MAPPING']
    gpu_devices = env_vars['GPU_DEVICES']
    port_mapping = env_vars['PORT_MAPPING']
    host_address = env_vars['HOST_ADDRESS']
    model_path = env_vars['MODEL_PATH']
    context_length = env_vars['CONTEXT_LENGTH']
    ngl = env_vars['NGL']
    parallel = env_vars['PARALLEL']
    temp = env_vars['TEMP']
    
    cmd = [
        "docker", "run", "--rm", "-it",
        "-v", volume_mapping,
        "--gpus", gpu_devices,
        "-p", port_mapping,
        "-e", f"LLAMA_ARG_HOST={host_address}",
        docker_image,
        "-s",
        "-m", model_path,
        "-c", context_length,
        "-ngl", ngl,
        "--jinja",
        "--parallel", parallel,
        "--temp", temp
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()