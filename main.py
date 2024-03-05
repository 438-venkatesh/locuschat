import instaloader

def get_instagram_profile_details(profile_name, download_path=None):
    try:
        # Create an instance of Instaloader
        loader = instaloader.Instaloader()

        # Load the profile metadata
        profile = instaloader.Profile.from_username(loader.context, profile_name)

        # Retrieve profile details
        profile_info = {
            "username": profile.username,
            "full_name": profile.full_name,
            "is_private": profile.is_private,
            "followers": profile.followers,
            "followees": profile.followees,
            "posts_count": profile.mediacount,
            "profile_pic_url": profile.profile_pic_url,
        }

        # Download media from the specified Instagram profile
        if download_path:
            loader.download_profile(profile_name, profile_pic_only=False, target=download_path)
            profile_info["download_directory"] = download_path
        else:
            loader.download_profile(profile_name, profile_pic_only=False)
            profile_info["download_directory"] = profile_name

        return profile_info
    except Exception as e:
        print(f"Error retrieving profile details: {e}")
        return None

# Example usage:
profile_handle = "akhilsarthak_official"
profile_details = get_instagram_profile_details(profile_handle)
if profile_details:
    print("Profile Details:")
    print(f"Username: {profile_details['username']}")
    print(f"Full Name: {profile_details['full_name']}")
    print(f"Private Account: {'Yes' if profile_details['is_private'] else 'No'}")
    print(f"Followers: {profile_details['followers']}")
    print(f"Following: {profile_details['followees']}")
    print(f"Number of Posts: {profile_details['posts_count']}")
    print(f"Profile Picture URL: {profile_details['profile_pic_url']}")
    print(f"Media downloaded successfully to: {profile_details['download_directory']}")
else:
    print("Failed to retrieve profile details.")
