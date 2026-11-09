# Automated File Organizer

A smart, production-ready Python script engineered to automate file organization and directory decluttering. It scans target folders dynamically and routes items into custom structured directories based on their exact file extensions.

## Features
- **Deterministic Extension Mapping:** Pre-defined categorization logic for documents, media, images, archives, and system binaries.
- **Fail-Safe Processing:** Ensures directory structures are dynamically verified and created (`os.makedirs`) prior to transfer, eliminating file system exceptions.
- **Strict Error Handling:** Captures Permission and OS IO locks safely, ensuring system stability during heavy optimization pipelines.

## Repository Architecture
- `file_organizer.py`: Core architecture file containing multi-threaded tracking script.
- `README.md`: Structural documentation.

## Installation & Setup
1. Clone this repository locally.
2. Ensure you have Python 3.x configured on your environment paths.
3. Run the tracking utility natively:
   ```bash
   python file_organizer.py
   ```
