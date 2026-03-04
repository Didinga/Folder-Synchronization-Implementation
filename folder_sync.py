import os
import shutil
import time
import argparse
from datetime import datetime


def log_operation(log_file, operation, file_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}] {operation}: {file_path}"
    print(message)
    with open(log_file, 'a') as log:
        log.write(message + "\n")


def synchronize_folders(source_folder, replica_folder, log_file):
    # Create replica folder if it doesn't exist
    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder)
        log_operation(log_file, "CREATED", replica_folder)

    # Copy new and updated files from source to replica
    for dirpath, dirnames, filenames in os.walk(source_folder):
        relative_path = os.path.relpath(dirpath, source_folder)
        replica_dirpath = os.path.join(replica_folder, relative_path)

        # Create subdirectories in replica if missing
        if not os.path.exists(replica_dirpath):
            os.makedirs(replica_dirpath)
            log_operation(log_file, "CREATED DIR", replica_dirpath)

        for filename in filenames:
            source_file = os.path.join(dirpath, filename)
            replica_file = os.path.join(replica_dirpath, filename)

            # Copy if file doesn't exist or is outdated
            if not os.path.exists(replica_file) or \
               os.path.getmtime(source_file) > os.path.getmtime(replica_file):
                shutil.copy2(source_file, replica_file)
                log_operation(log_file, "COPIED", source_file)

    # Remove files and folders from replica that no longer exist in source
    for dirpath, dirnames, filenames in os.walk(replica_folder, topdown=False):
        relative_path = os.path.relpath(dirpath, replica_folder)
        source_dirpath = os.path.join(source_folder, relative_path)

        for filename in filenames:
            replica_file = os.path.join(dirpath, filename)
            source_file = os.path.join(source_dirpath, filename)

            if not os.path.exists(source_file):
                os.remove(replica_file)
                log_operation(log_file, "REMOVED", replica_file)

        # Remove empty directories that don't exist in source
        if not os.path.exists(source_dirpath) and dirpath != replica_folder:
            shutil.rmtree(dirpath)
            log_operation(log_file, "REMOVED DIR", dirpath)


def main():
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument("source_folder", help="Path to the source folder")
    parser.add_argument("replica_folder", help="Path to the replica folder")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("log_file", help="Path to the log file")

    args = parser.parse_args()

    print(f"Starting sync: {args.source_folder} -> {args.replica_folder}")
    print(f"Interval: {args.interval}s | Log: {args.log_file}")
    print("Press Ctrl+C to stop.\n")

    while True:
        synchronize_folders(args.source_folder, args.replica_folder, args.log_file)
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
