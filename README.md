# auto_face_pixelator
Facial detection x Pixelator (Mosaic)

# Idea
While I was writting my blog, I realized it was troublesome to apply mosaic effect to people's faces in my photos.
Why not automate it?

# How it works
Detect face and apply mosaic effect in Realtime & Flask Web App

# Installation
Get Docker of you don't have.
Run "docker build . -t auto_mosaic"  
Run "docker run -d -p 5000:5000 auto_mosaic"  
Access to "0.0.0.0:5000" on your browser

# Exsample
If it runs successfully, it should look like this.
![Screenshot](screenshot.png)

# Milestones
1. Locally implement auto face -- done　　
2. Dockernize -- done　　
3. Probably make API -- done　　
