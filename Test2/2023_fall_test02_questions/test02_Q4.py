# List of shared URLs
shared_urls = [
    'https://yzu365-my.sharepoint.com/:w:/g/personal/s1106xxx_mail_yzu_edu_tw/EfzqnOqQXklGuvK69HoarQsBIWCGX8NlW1Uafl4GpTeP9A',
    'https://yzu365-my.sharepoint.com/:w:/g/personal/imxyz_saturn_yzu_edu_tw/EYFn9y8Z3UBFsTgR4jFYmxkBb7XtEejPCqYELTlnTHz0tQ'
]

def extract_email(shared_url):
    """
    Extract email information from a shared URL and convert it into a valid email format.
    """
    # Split the URL to isolate the "personal" section
    parts = shared_url.split('/g/personal/')
    if len(parts) < 2:
        return None

    # Extract the email-like portion
    email_part = parts[1].split('/')[0]  # Get the part after '/g/personal/' and before the next '/'
    
    # Replace underscores (_) with appropriate characters
    email_formatted = email_part.replace('_mail_', '@mail.').replace('_', '.')

    return email_formatted

# Process each URL and print the result
for url in shared_urls:
    email = extract_email(url)
    if email:
        print(email)
