import qrcode

def banner_qr():
    # Display a simple text banner
    print("""
     ██████╗ ██████╗        ██████╗██╗     ██╗
    ██╔═══██╗██╔══██╗      ██╔════╝██║     ██║
    ██║   ██║██████╔╝█████╗██║     ██║     ██║
    ██║▄▄ ██║██╔══██╗╚════╝██║     ██║     ██║
    ╚██████╔╝██║  ██║      ╚██████╗███████╗██║
     ╚══▀▀═╝ ╚═╝  ╚═╝       ╚═════╝╚══════╝╚═╝

    [+] By: Mr.ShadowX
    [+] Github: https://github.com/PhantomZero-X
    [+] Version: 1.0
    [+] Link to QR Code Generator!
    """)
    
    link = input("Enter the link: ")
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(link)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

    print("QR code generated successfully")

if __name__ == "__main__":
    banner_qr()