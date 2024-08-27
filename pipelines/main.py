import os
from bing_image_downloader import downloader


def get_folder_size(folder):
    """Calculate the total size of the folder."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def delete_non_jpg_images(directory):
    """Delete images that are not .jpg files."""
    for filename in os.listdir(directory):
        if not filename.lower().endswith('.jpg'):
            os.remove(os.path.join(directory, filename))


def create_dataset(items, num_images_per_batch=10, max_storage_bytes=1.5 * 1024 * 1024 * 1024 * 1024):
    # Define the path to the external SSD
    dataset_dir = "/Volumes/PortableSSD/dataset"

    # Create a folder named 'dataset' on the SSD if it doesn't exist
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    while True:
        images_downloaded_per_item = {item: 0 for item in items}

        for item in items:
            # Check current storage usage
            current_size = get_folder_size(dataset_dir)
            if current_size >= max_storage_bytes:
                print(
                    f"Reached storage limit of {max_storage_bytes / (1024 * 1024 * 1024 * 1024):.2f} TB. Stopping downloads.")
                return

            # Create subfolders for each item on the SSD
            item_dir = os.path.join(dataset_dir, item)
            if not os.path.exists(item_dir):
                os.makedirs(item_dir)

            # Download images in batches
            try:
                downloader.download(item, limit=num_images_per_batch, output_dir=dataset_dir, adult_filter_off=True,
                                    force_replace=False, timeout=60)

                # Check the item directory for non-jpg files and delete them
                delete_non_jpg_images(item_dir)

                # Count the number of jpg images downloaded in this batch
                current_images_count = len([f for f in os.listdir(item_dir) if f.lower().endswith('.jpg')])

                # Adjust the number of images downloaded in this batch
                new_images_downloaded = current_images_count - images_downloaded_per_item[item]
                images_downloaded_per_item[item] += new_images_downloaded

                print(f"Downloaded {new_images_downloaded} new images for {item}")

                # Check if we have reached the required number of images for this item
                if images_downloaded_per_item[item] >= num_images_per_batch:
                    continue

            except Exception as e:
                print(f"Failed to download images for {item}: {e}")

        # If the total number of images across all items is not equal, retry the loop
        if all(count >= num_images_per_batch for count in images_downloaded_per_item.values()):
            print("Completed one cycle of downloading.")
            continue
        else:
            print("Not enough images downloaded for some items, retrying...")


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
    create_dataset(items, num_images_per_batch=10)
