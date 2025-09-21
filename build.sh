#!/bin/bash

# This script provides manual build instructions for Vercel.

# Exit immediately if a command exits with a non-zero status.
set -e

# --- 1. Build Frontend ---
echo "--- Building Frontend ---"
# Navigate into the client directory
cd client
# Install npm dependencies
npm install
# Build the Next.js application
npm run build
# Navigate back to the root directory
cd ..


# --- 2. Install Backend Dependencies ---
echo "--- Installing Backend Dependencies ---"
# Navigate into the server directory
cd server
# Upgrade pip and install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt


echo "--- Build Script Finished Successfully ---"
