
import jwt
from datetime import datetime, timedelta

# Define a secret key for your refresh tokens (should be different from access token secret)
REFRESH_TOKEN_SECRET = "your-refresh-token-super-secret-key"


def create_refresh_token(user_id: str) -> str:
    """
    Creates a JWT refresh token for a given user ID.
    """
    # Set a longer expiration time for the refresh token (e.g., 30 days)
    expires_delta = timedelta(days=30)
    expire = datetime.utcnow() + expires_delta

    # Define the payload for the refresh token
    to_encode = {"sub": user_id, "exp": expire}

    # Encode the token
    encoded_jwt = jwt.encode(to_encode, REFRESH_TOKEN_SECRET, algorithm="HS256")
    return encoded_jwt


# Example usage:
user_identifier = "example_user_id_123"
refresh_token = create_refresh_token(user_identifier)
print(f"Generated Refresh Token: {refresh_token}")

# To decode and verify (for demonstration)
try:
    decoded_payload = jwt.decode(refresh_token, REFRESH_TOKEN_SECRET, algorithms=["HS256"])
    print(f"Decoded Refresh Token Payload: {decoded_payload}")
except jwt.ExpiredSignatureError:
    print("Refresh token has expired.")
except jwt.InvalidTokenError:
    print("Invalid refresh token.")