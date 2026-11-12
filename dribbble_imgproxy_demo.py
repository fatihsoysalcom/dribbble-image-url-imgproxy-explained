import urllib.parse

def generate_dribbble_imgproxy_url(original_url, width=None, height=None, format=None, quality=None):
    """Generates a Dribbble-like imgproxy URL with specified options.

    Args:
        original_url (str): The base URL of the Dribbble image.
        width (int, optional): Desired width for resizing.
        height (int, optional): Desired height for resizing.
        format (str, optional): Desired image format (e.g., 'webp', 'jpg').
        quality (int, optional): Desired image quality (1-100).

    Returns:
        str: The generated imgproxy URL.
    """
    base_url = "https://dribbble.com/photos/"
    # In a real scenario, imgproxy would be a separate service.
    # Here, we simulate the URL structure.
    # The path after /photos/ is typically a hash or identifier.
    # We'll use a placeholder for simplicity.
    image_identifier = "example_image_id"

    # imgproxy options are often encoded in the URL path.
    # For Dribbble, it's a bit more complex, but we'll simulate common parameters.
    # The format is often like: /w:WIDTH/h:HEIGHT/format:FORMAT/quality:QUALITY
    options = []
    if width:
        options.append(f"w:{width}")
    if height:
        options.append(f"h:{height}")
    if format:
        options.append(f"format:{format}")
    if quality:
        options.append(f"quality:{quality}")

    # Combine options into a path segment
    options_path = "/" + "/".join(options) if options else ""

    # The actual image URL is appended, often URL-encoded.
    # Dribbble's structure is specific, but this simulates the concept.
    # A common pattern is /url/ENCODED_ORIGINAL_URL
    encoded_original_url = urllib.parse.quote(original_url, safe='')

    # Constructing a plausible imgproxy-like URL structure
    # This is a simplification of Dribbble's actual complex URL generation
    # which might involve signatures and specific encoding.
    final_url = f"{base_url}{image_identifier}{options_path}/url/{encoded_original_url}"

    return final_url

# --- Example Usage ---

# Original Dribbble image URL (placeholder)
original_image = "https://cdn.dribbble.com/users/1/screenshots/1234567/my_awesome_shot.jpg"

# Example 1: Basic resizing to width 800
url_w800 = generate_dribbble_imgproxy_url(original_image, width=800)
print(f"Resized to width 800:\n{url_w800}\n")

# Example 2: Resizing to height 600 and converting to WebP
url_h600_webp = generate_dribbble_imgproxy_url(original_image, height=600, format='webp')
print(f"Resized to height 600, format WebP:\n{url_h600_webp}\n")

# Example 3: Resizing with width, height, and quality adjustment
url_complex = generate_dribbble_imgproxy_url(original_image, width=400, height=300, quality=85)
print(f"Resized to 400x300, quality 85:\n{url_complex}\n")

# Example 4: Demonstrating the 'Vary: Accept' concept implicitly
# In a real imgproxy setup, the server would inspect the Accept header.
# This script only generates the URL. The server handles content negotiation.
# If you requested 'image/webp' and the URL had format=webp, it would serve webp.
# If you requested 'image/jpeg' and the URL had format=webp, it might serve jpeg or webp based on server logic.
print("Note: The 'Vary: Accept' header is handled by the server receiving the request, not by URL generation.")
print("The generated URL might include format parameters, influencing server behavior.")

# Example 5: Simulating a shot that might skip resizing (no width/height params)
# This would typically happen if the original image is already optimized or
# if the platform wants to serve the original for specific use cases.
url_no_resize = generate_dribbble_imgproxy_url(original_image)
print(f"URL without explicit resize parameters (potentially serving original or optimized version):\n{url_no_resize}\n")
