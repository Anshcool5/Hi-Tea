from PIL import Image, ImageDraw, ImageFont

def generate_stamp_card(stamp_count):
    # Load the base stamp card image
    #res = Image.new("RGBA", (220, 220), (255, 255, 255))
    base_image_path = "res/stampCard.png"
    base_image = Image.open(base_image_path)

    # Set stamp image and position
    stamp_image_path = "res/stamp.png"
    stamp_position = (70, 40)

    # Add stamps to the image based on the stamp count
    stamp = Image.open(stamp_image_path).convert("RGBA")
    
    for i in range(stamp_count):
        
        if i == 5:
            stamp_position = (70, 100)
        base_image.paste(stamp, stamp_position, stamp)

        # Update stamp position for the next stamp
        stamp_position = (stamp_position[0] + 70, stamp_position[1])

    # Save the modified image
    base_image.save("updated_stampCard.png")

# Example: Update stamp count based on a variable
current_stamp_count = 5
generate_stamp_card(current_stamp_count)
