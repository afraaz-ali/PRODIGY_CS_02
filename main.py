import tkinter as tk


from PIL import Image

from tkinter import filedialog


def encrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    pixels = img.load()  # Load pixel data

    # Swap and modify pixel values
    for i in range(0, img.size[0], 2):  # Iterate over width
        for j in range(img.size[1]):  # Iterate over height
            # Ensure even index to swap with the next pixel (i + 1)
            if i + 1 < img.size[0]:
                # Swap pixel values with the next pixel
                pixels[i, j], pixels[i + 1, j] = pixels[i + 1, j], pixels[i, j]

            # Add the key value to each pixel component (R, G, B)
            r, g, b = pixels[i, j]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[i, j] = (r, g, b)

    img.save(output_image_path)


def decrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    pixels = img.load()  # Load pixel data

    # Reverse the swap and modify pixel values
    for i in range(0, img.size[0], 2):  # Iterate over width
        for j in range(img.size[1]):  # Iterate over height
            # Subtract the key value to each pixel component (R, G, B)
            r, g, b = pixels[i, j]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[i, j] = (r, g, b)

            # Ensure even index to swap with the next pixel (i + 1)
            if i + 1 < img.size[0]:
                # Reverse the swap with the next pixel
                pixels[i, j], pixels[i + 1, j] = pixels[i + 1, j], pixels[i, j]

    img.save(output_image_path)


def select_image_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.update()  # Ensure the dialog box is shown
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    return file_path


def main():
    print("Welcome to the Simple Image Encryption Tool")
    mode = input("Do you want to encrypt or decrypt an image? (enter 'encrypt' or 'decrypt'): ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
        return

    image_path = select_image_file()
    if not image_path:
        print("No image selected.")
        return

    key = int(input("Enter the encryption key (an integer value): "))

    if mode == 'encrypt':
        output_image_path = 'encrypted_image.png'
        encrypt_image(image_path, output_image_path, key)
        print(f"Image encrypted and saved as {output_image_path}")
    else:
        output_image_path = 'decrypted_image.png'
        decrypt_image(image_path, output_image_path, key)
        print(f"Image decrypted and saved as {output_image_path}")


if __name__ == "__main__":
    main()
