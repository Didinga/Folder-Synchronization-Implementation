# Folder Synchronization

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)

A Python command-line tool for one-way folder synchronization. Keeps a replica folder as an exact mirror of a source folder, with periodic sync and full logging.

---

## Features

- One-way synchronization: replica always matches source
- Copies new and updated files from source to replica
- Removes files from replica that no longer exist in source
- Recursive: handles nested subdirectories
- Periodic sync at a configurable interval
- Timestamped logging to both console and log file

---

## Usage

```bash
python folder_sync.py <source> <replica> <interval> <log_file>
```

### Arguments

| Argument | Description |
|----------|-------------|
| `source` | Path to the source folder |
| `replica` | Path to the replica folder |
| `interval` | Sync interval in seconds |
| `log_file` | Path to the log file |

### Example

```bash
python folder_sync.py /home/user/documents /home/user/backup 60 sync.log
```

This will sync `/documents` to `/backup` every 60 seconds and log all operations to `sync.log`.

---

## Log Output Example

```
[2026-01-01 12:00:00] COPIED: /home/user/documents/report.pdf
[2026-01-01 12:00:00] REMOVED: /home/user/backup/old_file.txt
[2026-01-01 12:00:00] CREATED DIR: /home/user/backup/new_folder
```

---

## Requirements

- Python 3.8+
- No external dependencies (standard library only)

---

## License

This project is licensed under the MIT License.

---

## Author

**Didinga Omodi**
- GitHub: [@Didinga](https://github.com/Didinga)
- LinkedIn: [didiomodi](https://www.linkedin.com/in/didiomodi/)
