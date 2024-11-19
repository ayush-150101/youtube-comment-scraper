
# YouTube Comments Scraper

This project is a Python script that automates the process of scraping comments and usernames from YouTube videos using **Selenium**. The script saves the scraped data into a CSV file for analysis or other use cases.

---

## Features

- Searches for a video on YouTube based on a query.
- Extracts usernames and their corresponding comments.
- Saves the extracted data into a structured CSV file.
- Simulates user interaction by scrolling to load dynamically generated content.

---

## Prerequisites

To run this script, you need to have the following installed:

1. **Python** (version 3.7 or higher)
2. **Google Chrome** (latest version recommended)
3. **ChromeDriver** (compatible with your Chrome version)
4. Required Python libraries:
   - `selenium`
   - `pandas`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/youtube-comments-scraper.git
   cd youtube-comments-scraper
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and set up **ChromeDriver**:
   - Download the correct version of ChromeDriver from [ChromeDriver](https://chromedriver.chromium.org/downloads).
   - Place it in your system's PATH or in the project directory.

---

## Usage

1. Open the script file `scraper.py` (or whatever the script name is) and modify the search query:
   ```python
   search.send_keys("Launch of LVM3-M4/CHANDRAYAAN-3 Mission")
   ```

2. Run the script:
   ```bash
   python scraper.py
   ```

3. After execution, the comments and usernames will be saved in a CSV file named `youtube_comments_with_usernames.csv` in the project directory.

---

## CSV Output

The generated CSV file will have the following structure:

| **username**        | **comment**                   |
|----------------------|-------------------------------|
| User1               | "This is amazing!"           |
| User2               | "Great explanation, thanks!" |

---

## Notes

- Ensure that the YouTube video page is publicly accessible.
- The script relies on YouTube's current DOM structure. If YouTube updates its structure, you may need to update the XPaths in the script.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the script.
