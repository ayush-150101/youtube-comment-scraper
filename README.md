# YouTube Video and Comments Data Fetcher

This project is a Python-based tool to fetch video metadata and comments from a specified YouTube channel using the **YouTube Data API v3**. The data is saved into an Excel file for easy access and analysis.

---

## Features

- **Fetch Video Metadata**: Retrieves details such as video title, description, views, likes, duration, and more.
- **Fetch Comments**: Extracts the latest 100 comments and replies for each video.
- **Error Handling**: Skips videos with disabled comments and handles API errors gracefully.
- **Excel Output**: Saves video and comment data into an organized Excel file.

---

## Requirements

### **Dependencies**

- `google-api-python-client`
- `google-auth`
- `google-auth-httplib2`
- `openpyxl`

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## Setup Instructions

1. **Create a Google Cloud Project**:

   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or use an existing one.
   - Enable the **YouTube Data API v3** for the project.
   - Generate an API key and note it down.

2. **Set Up the Script**:

   - Clone or download the repository.
   - Replace the placeholder in the script with your API key:
     ```python
     API_KEY = 'your_api_key'
     ```

3. **Run the Script**:

   - Update the `channel_id` variable with the YouTube channel handle (e.g., `@YouTubeHandle`).
   - Execute the script:
     ```bash
     python main.py
     ```

4. **View the Results**:
   - The script generates an Excel file named `YouTube_Data.xlsx`.
   - It contains two sheets:
     - `Video Data`: Video metadata.
     - `Comments Data`: Comments and replies.

---

## File Structure

```
.
├── main.py                # Main script
├── requirements.txt       # List of dependencies
├── YouTube_Data.xlsx      # Output file (generated after running the script)
```

---

## API Quota Information

- Each API key has a daily quota of **10,000 units**.
- The following API requests are used in the script:
  - `playlistItems.list`: 1 unit per call.
  - `videos.list`: 1 unit per call.
  - `commentThreads.list`: 1 unit per call.

Ensure your API usage does not exceed the quota.

---

## Error Handling

- **Comments Disabled**: Videos with disabled comments are logged and skipped.
- **API Errors**: The script handles HTTP errors and prints detailed messages for debugging.
- **Empty Channel Data**: If the channel handle is invalid, the script will raise an exception.

---

## Example Output

### Video Data Sheet

| Video ID | Title         | Description          | Published Date | View Count | Like Count | Comment Count | Duration | Thumbnail URL |
| -------- | ------------- | -------------------- | -------------- | ---------- | ---------- | ------------- | -------- | ------------- |
| abc123   | Example Video | Video description... | 2023-01-01     | 1000       | 50         | 20            | PT5M30S  | thumbnail.jpg |

### Comments Data Sheet

| Video ID | Comment ID | Comment Text | Author Name  | Published Date | Like Count | Reply To |
| -------- | ---------- | ------------ | ------------ | -------------- | ---------- | -------- |
| abc123   | comment1   | Great video! | User1        | 2023-01-02     | 5          | None     |
| abc123   | reply1     | Thank you!   | ChannelOwner | 2023-01-02     | 3          | comment1 |

---

## Contribution

Feel free to fork this repository and contribute by submitting pull requests for any improvements or bug fixes.

---
