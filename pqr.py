
if __name__ == '__main__':
  from sys import argv

  import qrcode
  q=qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=3,border=0) #border default = 4
  q.add_data(argv[1])
  q.make(fit=True)
  qr = q.make_image().convert('RGBA')
  
  from PIL import Image
  bg = Image.open(argv[2]).convert('RGBA')
  ratio = int(bg.width/qr.width)
  out_frame_width = 4*3*ratio

  qrpx = qr.load()
  for x in range(qr.width):
    for y in range(qr.height):
      if (x%3 == 1 and y%3 == 1) or \
          (y < 24 and (x<24 or x>86)) or \
          (y > 86 and x < 24) or \
          18 <= x <= 20 or \
          18 <= y <= 20 or \
          (84 <= x <= 98 and 84 <= y <= 98) :
            continue
      qrpx[x,y] = (0,0,0,0)

  qr_with_frame = Image.new('RGBA',tuple(map(lambda v:v*ratio+out_frame_width*2, qr.size)),color=(255,)*4)
  qr = qr.resize(tuple(map(lambda v:v*ratio, qr.size)))
  qr_with_frame.paste(qr.copy(), (out_frame_width,)*2)
  qr_with_frame.save('qr-overlay.png')

  bg = bg.resize(qr.size, Image.LANCZOS)
  bg_with_frame = Image.new('RGBA',qr_with_frame.size, color=(255,)*4)
  bg_with_frame.paste(bg, (out_frame_width,)*2)
  bg_with_frame.alpha_composite(qr_with_frame)
  bg_with_frame.save('qr.png')
  bg_with_frame.show()
