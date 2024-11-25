#you tube comments on  you tube orignal Ai series.
from googleapiclient.discovery import build
import openpyxl
from time import sleep
from googleapiclient.errors import HttpError

def fetch_video_data(channel_handle, youtube):
    # Fetch channel details
    print(channel_handle)
    channel_response = youtube.search().list(
        part="snippet",
        q=channel_handle,
        type="channel",
        maxResults=1
    ).execute()

    channel_id = channel_response["items"][0]["id"]["channelId"]

    # Step 2: Get the uploads playlist ID
    channel_info = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()

    print('channel response : ', channel_info)
    
    playlist_id = channel_info['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while True:
        playlist_response = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()
        
        for item in playlist_response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            video_details = youtube.videos().list(
                part='snippet,contentDetails,statistics',
                id=video_id
            ).execute()
            
            # Store video details in a list
            for video in video_details['items']:
                videos.append({
                    'Video ID': video_id,
                    'Title': video['snippet']['title'],
                    'Description': video['snippet']['description'],
                    'Published Date': video['snippet']['publishedAt'],
                    'View Count': video['statistics'].get('viewCount', 0),
                    'Like Count': video['statistics'].get('likeCount', 0),
                    'Comment Count': video['statistics'].get('commentCount', 0),
                    'Duration': video['contentDetails']['duration'],
                    'Thumbnail URL': video['snippet']['thumbnails']['default']['url']
                })
        
        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token:
            break
    
    return videos

def fetch_comments(video_id, youtube):
    comments = []
    next_page_token = None

    try:
        while True:
            comment_response = youtube.commentThreads().list(
                part="snippet,replies",
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token
            ).execute()

            for item in comment_response["items"]:
                comment = item["snippet"]["topLevelComment"]["snippet"]
                comments.append({
                    "Video ID": video_id,
                    "Comment ID": item["id"],
                    "Comment Text": comment["textDisplay"],
                    "Author Name": comment["authorDisplayName"],
                    "Published Date": comment["publishedAt"],
                    "Like Count": comment.get("likeCount", 0),
                    "Reply To": None
                })

                if "replies" in item:
                    for reply in item["replies"]["comments"]:
                        comments.append({
                            "Video ID": video_id,
                            "Comment ID": reply["id"],
                            "Comment Text": reply["snippet"]["textDisplay"],
                            "Author Name": reply["snippet"]["authorDisplayName"],
                            "Published Date": reply["snippet"]["publishedAt"],
                            "Like Count": reply["snippet"].get("likeCount", 0),
                            "Reply To": item["id"]
                        })

            next_page_token = comment_response.get("nextPageToken")
            if not next_page_token:
                break

    # Handling api errors        
    except HttpError as e:
        error_reason = e.error_details[0].get("reason", "")
        if error_reason == "commentsDisabled":
            print(f"Comments are disabled for video ID: {video_id}. Skipping.")
        else:
            print(f"An error occurred for video ID: {video_id}. Details: {e}")
    return comments

def save_to_excel(video_data, comments_data, filename='output.xlsx'):
    workbook = openpyxl.Workbook()
    
    # Video Data Sheet
    video_sheet = workbook.active
    video_sheet.title = "Video Data"
    video_sheet.append([
        'Video ID', 'Title', 'Description', 'Published Date',
        'View Count', 'Like Count', 'Comment Count',
        'Duration', 'Thumbnail URL'
    ])
    for video in video_data:
        video_sheet.append(list(video.values()))
    
    # Comments Data Sheet
    comments_sheet = workbook.create_sheet(title="Comments Data")
    comments_sheet.append([
        'Video ID', 'Comment ID', 'Comment Text', 'Author Name',
        'Published Date', 'Like Count', 'Reply To'
    ])
    for comment in comments_data:
        comments_sheet.append(list(comment.values()))
    
    workbook.save(filename)

if __name__ == "__main__":

    # Set up API client
    API_KEY = 'YOUR_API_KEY' # Replace this with api key you have created using youtube v3 API
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    channel_id ="@GoQuest_Media"

    print('pass 1')

    # Fetch video data
    video_data = fetch_video_data(channel_id, youtube)

    print('pass 2')

    # Fetch comments for all videos
    comments_data = []
    for video in video_data:
        video_comments = fetch_comments(video["Video ID"], youtube)
        comments_data.extend(video_comments)

    print('pass 3')
    

    # Save data to Excel
    save_to_excel(video_data, comments_data, filename="YouTube_Data.xlsx")

    print("Data successfully saved to YouTube_Data.xlsx")