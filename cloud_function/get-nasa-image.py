import functions_framework
import requests

@functions_framework.http
def nasa_image(request):

    api_key = 'INSERT_YOUR_API_KEY'

    # NASA API URL for the Astronomy Picture of the Day (APOD)
    nasa_apod_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&count=1"

    try:
        # Make a GET request to the NASA APOD API
        response = requests.get(nasa_apod_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the first item from the returned list of images
            image_data = response.json()[0]

            # Return the image URL and description
            return (f"Title: {image_data.get('title', 'No title available')}\n"
                    f"URL: {image_data.get('url', 'No URL available')}\n"
                    f"Description: {image_data.get('explanation', 'No description available.')}")
        else:
            return f"Failed to retrieve data from NASA API. Status Code: {response.status_code}"

    except Exception as e:
        return f"An error occurred: {e}"
