FROM python:3.9-slim

Tells Docker to download a pre-packaged, minimal Linux environment that already has Python 3.9 installed. You don't have to install Linux or Python yourself—Docker does it in seconds.

WORKDIR /app

Creates a folder named /app inside that Linux container and switches into it. All future commands will run from inside this folder.

COPY . /app

Takes all the files from your GitHub repository (like Junaid.py) and copies them straight into the /app folder inside the container.

CMD ["python", "Junaid.py"]

Specifies the final command executed when the container boots up. It literally tells the container: "Open terminal and run python Junaid.py."
