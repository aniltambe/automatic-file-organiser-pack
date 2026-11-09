import os
import shutil

def organize_directory(target_path):
    # Mapping definition
    extension_map = {
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audio': ['.mp3', '.wav', '.aac', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Executables': ['.exe', '.msi']
    }

    if not os.path.exists(target_path):
        print(f"Error: Target path '{target_path}' does not exist.")
        return

    print(f"Initiating cleanup process on: {target_path}\n")

    for filename in os.listdir(target_path):
        source_file = os.path.join(target_path, filename)
        
        # Isolate system elements, focus purely on loose files
        if os.path.isfile(source_file):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            routed = False

            for destination_folder, extensions in extension_map.items():
                if ext in extensions:
                    dest_dir = os.path.join(target_path, destination_folder)
                    os.makedirs(dest_dir, exist_ok=True)
                    
                    try:
                        shutil.move(source_file, os.path.join(dest_dir, filename))
                        print(f"[SUCCESS] Routed: {filename} -> {destination_folder}/")
                    except Exception as e:
                        print(f"[ERROR] Failed to move {filename}: {e}")
                    routed = True
                    break
            
            # Catch-all container for system miscellaneous files
            if not routed:
                misc_dir = os.path.join(target_path, 'Miscellaneous')
                os.makedirs(misc_dir, exist_ok=True)
                try:
                    shutil.move(source_file, os.path.join(misc_dir, filename))
                    print(f"[MISC] Routed: {filename} -> Miscellaneous/")
                except Exception as e:
                    print(f"[ERROR] Failed to move {filename}: {e}")

if __name__ == "__main__":
    print("=== Production Automated File Organizer ===")
    path_to_clean = input("Provide absolute system folder path to structure: ").strip()
    organize_directory(path_to_clean)
    print("\nExecution routine complete.")
