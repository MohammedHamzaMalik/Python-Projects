import streamlit as stfrom pytube import YouTube

'''
We will be using streamlit’s title() and subheader() functions for the text. Both of them take a
string as a parameter and display it.

For the user input, we will use the text_input() function. A label can be passed as a parameter.
'''
st.title("Youtube Video Donwloader")
st.subheader("Enter the URL:")
url = st.text_input(label='URL')

'''
First, we will need to create an instance of the YouTube object we imported from pytube. 
The constructor of Youtube object requires the URL to be passed in as a parameter.
'''
yt = YouTube(url)

'''
First, we check if the user has input the URL. If we create a Youtube object with an empty URL, 
it will give an error.
Then we get the information about the video such as the Thumbnail Image URL, Title, Length of 
video, and Average Ratings. We use streamlit’s image() method to display the image.
Next, we get the StreamQuery Object, some Youtube videos are not available to download and will 
return an empty StreamQuery Object. Songs like God’s Plan by Drake return an empty StreamQuery. 
I am not sure why this is the case, do let me know in the comments if you find a workaround 🙂
We use streamlit’s button() method to create a button. It returns a boolean method which is 
initially set to False. Every time the button is clicked, Streamlit re-runs the app and the 
button() method returns True
Based on the button clicked by the user, we either download the video with audio or the 
audio-only.
'''
if url != '':
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=300)
    st.subheader('''
    {}
    # Length: {} seconds
    # Rating: {} 
    '''.format(yt.title , yt.length , yt.rating))
    video = yt.streams
    if len(video) > 0:
        downloaded , download_audio = False , False
        download_video = st.button("Download Video")
        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Download Audio Only")
        if download_video:
            video.get_lowest_resolution().download()
            downloaded = True
        if download_audio:
            video.filter(only_audio=True).first().download()
            downloaded = True
        if downloaded:
            st.subheader("Download Complete")
    else:
        st.subheader("Sorry, this video can not be downloaded")