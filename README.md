# PhotoQR
High resolution photo as a background of a QR code

### Demo
[Image](images/IMG_20190125_221718.jpg)

### Prerequisites
- Pillow
- qrcode

### How to use
```
  python3 pqr.py [data string] [image path]
```

### Outputs
- qr-overlay.png
  - Transparent overlay file. Would be useful with other image editing softwares
- qr.png
  - Resulted image file containing a QR code with photo background
