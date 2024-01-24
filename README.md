# Folder Synchronization

This Python script provides a simple implementation of folder synchronization. The program synchronizes two folders, maintaining an identical copy of the source folder in the replica folder.

## Features
- One-way synchronization: The content of the replica folder is modified to exactly match the content of the source folder after synchronization.
- Periodic synchronization: The synchronization is performed periodically.
- Logging: File creation/copying/removal operations are logged to both a file and console output.

## Usage
1. Provide folder paths, synchronization interval, and log file path using command-line arguments.
2. Run the script.

## Requirements
- Python

## Usage Example
```bash
python folder_sync.py /path/to/source /path/to/replica 60 /path/to/log.txt
