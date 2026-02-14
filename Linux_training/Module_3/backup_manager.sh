#!/bin/bash

#Validate no.of args
if [ $# -ne 3 ]; then
    echo "Usage: $0 <source_directory> <backup_directory> <file_extension>"
    exit 1
fi

#Using variables to store the arguments
SOURCE_DIR="$1"
BACKUP_DIR="$2"
FILE_EXT="$3"

#checkng if the src directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist."
    exit 1
fi

#checking if the backup dir exists,if not creating it
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Backup directory '$BACKUP_DIR' does not exist. Creating it..."
    mkdir -p "$BACKUP_DIR"
    sleep 2
    echo "Backup directory created successfully."
fi

#using globbing * to match all files with the given extension
FILES=("$SOURCE_DIR"/*"$FILE_EXT")

#checking if the files actually exist or not
if [ ${#FILES[@]} -eq 0 ] || [ ! -e "${FILES[0]}" ]; then
    echo "No files with extension '$FILE_EXT' found in '$SOURCE_DIR'."
    exit 0
fi


#ENV var & counter using export
export FILE_COUNT=0
TOTAL_SIZE=0

#backup process by traversiing thru each files
for FILE in "${FILES[@]}"; do
    
    FILE_SIZE=$(stat -c %s "$FILE")
    echo "Processing $(basename "$FILE") ($FILE_SIZE bytes)"
    
    DEST_FILE="$BACKUP_DIR/$(basename "$FILE")"
    if [ -e "$DEST_FILE" ]; then
        if [ "$FILE" -nt "$DEST_FILE" ]; then
            echo "Updating $DEST_FILE (newer source file)."
            cp --preserve=all "$FILE" "$DEST_FILE"
        else
            echo "Skipping $DEST_FILE (already up-to-date)."
            continue
        fi
    else
        echo "Copying $FILE to $DEST_FILE."
        cp --preserve=all "$FILE" "$DEST_FILE"
    fi

    FILE_COUNT=$((FILE_COUNT + 1))
    TOTAL_SIZE=$((TOTAL_SIZE + FILE_SIZE))
done

# Output report
REPORT_FILE="$BACKUP_DIR/backup_report.log"
{
    echo "Backup Report - $(date)"
    echo "------------------------------------"
    echo "Source Directory: $SOURCE_DIR"
    echo "Backup Directory: $BACKUP_DIR"
    echo "Total Files Processed: $FILE_COUNT"
    echo "Total Size of Files Backed Up: $TOTAL_SIZE bytes"
} > "$REPORT_FILE"

cat "$REPORT_FILE"

exit 0
