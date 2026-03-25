import qrcode
x=qrcode.QRCode()
msg="QR CODE GENERATOR PROGRAM EXECUTED SUCCESSFULLY!!!!"
x.add_data(msg)
x.make(fit=True)
res=x.make_image(fill_color="black",back_color="white")
res.save("theerthiya.png")
print("CREATED SUCCESSFULLY")