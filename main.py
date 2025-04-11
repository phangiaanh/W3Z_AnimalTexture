ANIMAL_METADATA = {
    "felidae": {
        "lion": {
            "id": "lion",
            "shape": "mesh_felidae_02.obj",  
            "description": "Adult African Lion, {} view"
        },
        "leopard": {
            "id": "leopard",
            "shape": "mesh_felidae_01.obj",
            "description": "Adult African Leopard, {} view"
        },
        "snow_leopard": {
            "id": "snow_leopard",
            "shape": "mesh_felidae_01.obj",
            "description": "Adult Snow Leopard, {} view"
        },
        "caracal": {
            "id": "caracal",
            "shape": "mesh_felidae_01.obj",
            "description": "Adult Caracal, {} view"
        },
        "lynx": {
            "id": "lynx",
            "shape": "mesh_felidae_01.obj",
            "description": "Adult Eurasian Lynx, {} view"
        },
        "puma_cougar": {
            "id": "puma_cougar",
            "shape": "mesh_felidae_01.obj",
            "description": "Adult Puma/Mountain Lion, {} view"
        },
        "felis_cat": {
            "id": "felis_cat",
            "shape": "mesh_felidae_01.obj",
            "description": "Adult Domestic Cat, {} view"
        },
        "leopardus_cat": {
            "id": "leopardus_cat",
            "shape": "mesh_felidae_01.obj",
            "description": "Adult Ocelot/Margay, {} view"
        },
        "prionailurus": {
            "id": "prionailurus",
            "shape": "mesh_felidae_01.obj",
            "description": "Adult Fishing Cat, {} view"
        }
    },
    
    "canidae": {
        "dalmatian": {
            "id": "dalmatian",
            "shape": "mesh_canidae.obj",
            "description": "Adult Dalmatian Dog, {} view"
        },
        "australian_shepherd": {
            "id": "australian_shepherd",
            "shape": "mesh_canidae.obj",
            "description": "Adult Australian Shepherd Dog, {} view"
        },
        "catahoula_leopard": {
            "id": "catahoula_leopard",
            "shape": "mesh_canidae.obj",
            "description": "Adult Catahoula Leopard Dog, {} view"
        },
        "komondor": {
            "id": "komondor",
            "shape": "mesh_canidae.obj",
            "description": "Adult Komondor Dog, {} view"
        },
        "black_tan_coonhound": {
            "id": "black_tan_coonhound",
            "shape": "mesh_canidae.obj",
            "description": "Adult Black and Tan Coonhound Dog, {} view"
        },
        "dapple_dachshund": {
            "id": "dapple_dachshund",
            "shape": "mesh_canidae.obj",
            "description": "Adult Dapple Dachshund Dog, {} view"
        },
        "american_hairless": {
            "id": "american_hairless",
            "shape": "mesh_canidae.obj",
            "description": "Adult American Hairless Terrier Dog, {} view"
        },
        "keeshond": {
            "id": "keeshond",
            "shape": "mesh_canidae.obj",
            "description": "Adult Keeshond Dog, {} view"
        }
    },
    
    "equidae": {
        "bay_thoroughbred": {
            "id": "bay_thoroughbred",
            "shape": "mesh_equidae.obj",
            "description": "Adult Bay Thoroughbred Horse, {} view"
        },
        "palomino_quarter": {
            "id": "palomino_quarter",
            "shape": "mesh_equidae.obj",
            "description": "Adult Palomino Quarter Horse, {} view"
        },
        "chestnut_morgan": {
            "id": "chestnut_morgan",
            "shape": "mesh_equidae.obj",
            "description": "Adult Chestnut Morgan Horse, {} view"
        },
        "buckskin_tennessee": {
            "id": "buckskin_tennessee",
            "shape": "mesh_equidae.obj",
            "description": "Adult Buckskin Tennessee Walking Horse, {} view"
        },
        "white_arabian": {
            "id": "white_arabian",
            "shape": "mesh_equidae.obj",
            "description": "Adult White Arabian Horse, {} view"
        },
        "black_friesian": {
            "id": "black_friesian",
            "shape": "mesh_equidae.obj",
            "description": "Adult Black Friesian Horse, {} view"
        },
        "dapple_andalusian": {
            "id": "dapple_andalusian",
            "shape": "mesh_equidae.obj",
            "description": "Adult Dapple Gray Andalusian Horse, {} view"
        },
        "pinto_paint": {
            "id": "pinto_paint",
            "shape": "mesh_equidae.obj",
            "description": "Adult Pinto Paint Horse, {} view"
        }
    },
    
    "bovidae": {
        "jersey": {
            "id": "jersey",
            "shape": "mesh_bovidae.obj",
            "description": "Adult Jersey Cow, {} view"
        },
        "sahiwal": {
            "id": "sahiwal",
            "shape": "mesh_bovidae.obj",
            "description": "Adult Sahiwal Cow, {} view"
        },
        "holstein_friesian": {
            "id": "holstein_friesian",
            "shape": "mesh_bovidae.obj",
            "description": "Adult Holstein Friesian Cow, {} view"
        },
        "brahman": {
            "id": "brahman",
            "shape": "mesh_bovidae.obj",
            "description": "Adult Brahman Cow, {} view"
        },
        "ayrshire": {
            "id": "ayrshire",
            "shape": "mesh_bovidae.obj",
            "description": "Adult Ayrshire Cow, {} view"
        },
        "guernsey": {
            "id": "guernsey",
            "shape": "mesh_bovidae.obj",
            "description": "Adult Guernsey Cow, {} view"
        },
        "brown_swiss": {
            "id": "brown_swiss",
            "shape": "mesh_bovidae.obj",
            "description": "Adult Brown Swiss Cow, {} view"
        },
        "charolais": {
            "id": "charolais",
            "shape": "mesh_bovidae.obj",
            "description": "Adult Charolais Cow, {} view"
        },
        "angus": {
            "id": "angus",
            "shape": "mesh_bovidae.obj",
            "description": "Adult Angus Cow, {} view"
        }
    },
    
    "hippopotamidae": {
        "hippo": {
            "id": "hippo",
            "shape": "mesh_hippopotamidae.obj",
            "description": "Adult Hippo, {} view"
        }
    }
}

from huggingface_hub import hf_hub_download
import os
import yaml
import subprocess
from concurrent.futures import ThreadPoolExecutor
import shutil
import zipfile

MESH_SHAPE = ["mesh_felidae_02.obj", "mesh_felidae_01.obj", "mesh_canidae.obj", "mesh_equidae.obj", "mesh_bovidae.obj", "mesh_hippopotamus.obj"]


def download_shapes():
    # Create shapes directory if it doesn't exist
    os.makedirs("shapes", exist_ok=True)
    
    repo_id = "WatermelonHCMUT/AnimalSkeletons"
    
    # Download each shape
    for filename in MESH_SHAPE:
        print(f"Downloading {filename}...")
        try:
            downloaded_path = hf_hub_download(
                repo_id=repo_id,
                filename=filename,
                local_dir="shapes"
            )
            print(f"Successfully downloaded {filename} to {downloaded_path}")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")

def generate_configs():
    # Create configs directory if it doesn't exist
    os.makedirs("configs/", exist_ok=True)
    
    # Base configuration template
    base_config = {
        "log": {
            "exp_name": None  # Will be replaced
        },
        "guide": {
            "text": None,  # Will be replaced
            "diffusion_name": "stabilityai/stable-diffusion-2-depth",
            "shape_scale": 0.6,
            "append_direction": True,
            "shape_path": None,  # Will be replaced
            "texture_resolution": 1024,
            "guidance_scale": 10,
            "texture_interpolation_mode": "bilinear"
        },
        "optim": {
            "seed": 2
        },
        "render": {
            "front_offset": 0
        }
    }
    
    # Generate config for each animal in each family
    for family in ANIMAL_METADATA:
        for animal in ANIMAL_METADATA[family]:
            # Get animal data
            animal_data = ANIMAL_METADATA[family][animal]
            
            # Create config for this animal
            config = base_config.copy()
            config["log"]["exp_name"] = animal_data["id"]
            config["guide"]["text"] = animal_data["description"]
            config["guide"]["shape_path"] = f"./shapes/{animal_data['shape']}"
            
            # Save config to file
            config_path = f"configs/{animal_data['id']}.yaml"
            with open(config_path, 'w') as f:
                yaml.dump(config, f, default_flow_style=False, sort_keys=False)
            print(f"Generated config: {config_path}")

def run_texture_generation(config_path):
    """Run texture generation for a single config file and cleanup vis folder"""
    try:
        # Run texture generation
        command = f"python -m scripts.run_texture --config_path={config_path}"
        print(f"Running: {command}")
        process = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"Successfully completed texture generation for {config_path}")
        print(process.stdout)
        
        # Clean up vis folder
        # Extract animal ID from config path
        animal_id = os.path.splitext(os.path.basename(config_path))[0]
        vis_path = os.path.join("experiments", animal_id, "vis")
        if os.path.exists(vis_path):
            print(f"Removing visualization folder: {vis_path}")
            shutil.rmtree(vis_path)
            print(f"Successfully removed {vis_path}")
            
    except subprocess.CalledProcessError as e:
        print(f"Error running texture generation for {config_path}")
        print(f"Error output: {e.stderr}")

def generate_all_textures():
    # List to store all config paths
    config_paths = []
    
    # Collect all config paths
    for family in ANIMAL_METADATA:
        for animal in ANIMAL_METADATA[family]:
            animal_data = ANIMAL_METADATA[family][animal]
            config_path = f"./configs/{animal_data['id']}.yaml"
            if os.path.exists(config_path):
                config_paths.append(config_path)
            else:
                print(f"Warning: Config file not found: {config_path}")
    
    # Run texture generation for each config
    print(f"Starting texture generation for {len(config_paths)} animals...")
    
    for config_path in config_paths:
        run_texture_generation(config_path)
    

def cleanup_and_zip_experiments():
    experiments_dir = "experiments"
    
    # Check if experiments directory exists
    if not os.path.exists(experiments_dir):
        print("Experiments directory not found!")
        return
    
    # Create zip file
    zip_path = "experiments.zip"
    print(f"Creating zip file: {zip_path}")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the experiments directory
        for root, dirs, files in os.walk(experiments_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Add file to zip with relative path
                arcname = os.path.relpath(file_path, start=os.path.dirname(experiments_dir))
                print(f"Adding to zip: {arcname}")
                zipf.write(file_path, arcname)
    
    print(f"Successfully created {zip_path}")

if __name__ == "__main__":
    # First run the texture generation
    download_shapes()
    generate_configs()
    generate_all_textures()
    
    # Then cleanup and zip results
    cleanup_and_zip_experiments()
            