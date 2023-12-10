import qrcode as qr

img= qr.make("https://pixabay.com/images/search/happy%20birthday/") 
img.save("demo.jpg")