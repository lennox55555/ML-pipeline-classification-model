import os
from bing_image_downloader import downloader

def create_dataset(items, num_images=2):
    # Define the path to the external SSD
    dataset_dir = "/Volumes/PortableSSD/dataset"
    
    # Create a folder named 'dataset' on the SSD if it doesn't exist
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    for item in items:
        # Create subfolders for each item on the SSD
        item_dir = os.path.join(dataset_dir, item)
        if not os.path.exists(item_dir):
            os.makedirs(item_dir)

        # Download images
        try:
            downloader.download(item, limit=num_images, output_dir=dataset_dir, adult_filter_off=True, force_replace=False, timeout=60)
            print(f"Downloaded {num_images} images for {item}")
        except Exception as e:
            print(f"Failed to download images for {item}: {e}")

if __name__ == "__main__":
    items = [
    "a nut (hardware)", 
    "a bolt (hardware)", 
    "a screw (hardware)", 
    "a washer (hardware)", 
    "a nail (hardware)", 
    "a hinge (hardware)", 
    "a bracket (hardware)", 
    "a anchor (hardware)", 
    "a rivets (hardware)", 
    "a clamp (hardware)", 
    "a grommet (hardware)", 
    "a pin (hardware)", 
    "a stud (hardware)", 
    "a bushing (hardware)", 
    "a spacer (hardware)", 
    "a latche (hardware)", 
    "a fastener (hardware)", 
    "a spring (hardware)", 
    "a lock (hardware)", 
    "a hook (hardware)", 
    "a clip (hardware)", 
    "a coupling (hardware)", 
    "a o-ring (hardware)", 
    "a gasket (hardware)", 
    "a seal (hardware)", 
    "a bearing (hardware)", 
    "a knob (hardware)", 
    "a handle (hardware)", 
    "a pulley (hardware)", 
    "a chain (hardware)", 
    "a cable (hardware)", 
    "a fitting (hardware)", 
    "a standoff (hardware)", 
    "a tack (hardware)", 
    "a tie-down (hardware)", 
    "a eyelet (hardware)", 
    "a plate (hardware)", 
    "a strap (hardware)"
]
    create_dataset(items, num_images=2)
