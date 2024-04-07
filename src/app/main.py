from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

# Azure Key Vault URI and secret name
key_vault_uri = "https://kv-apix-dev-ae-01.vault.azure.net/"
secret_name = "react-api-dummy-token"

# Use the managed identity of the Azure Container Instance for authentication
credential = DefaultAzureCredential()

# Create a SecretClient using the Key Vault URI and credential
client = SecretClient(vault_url=key_vault_uri, credential=credential)

# Retrieve the secret value from the Key Vault
secret_value = client.get_secret(secret_name).value
print(f"Secret Value: {secret_value}")

# Example usage of the secret (replace with your application logic)
# For demonstration purposes, this example simply prints the secret value
print("Hello from Azure Key Vault!")
print(f"The secret value is: {secret_value}")

# Keep the container running
input("Press Enter to exit...")
