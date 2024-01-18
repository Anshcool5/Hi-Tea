from PIL import Image, ImageDraw, ImageFont

def generate_stamp_card(stamp_count):
    # Load the base stamp card image
    #res = Image.new("RGBA", (220, 220), (255, 255, 255))
    base_image_path = "res/stampCard.png"
    base_image = Image.open(base_image_path)

    # Create a drawing object
    draw = ImageDraw.Draw(base_image)

    # Set font and size for stamp count text
    #font = ImageFont.truetype("arial.ttf", 30)

    # Set position for stamp count text
    text_position = (150, 50)

    # Set stamp image and position
    stamp_image_path = "res/stamp.png"
    stamp_position = (50, 150)

    # Draw stamp count text on the image
    #draw.text(text_position, f"Stamps: {stamp_count}", font=font, fill="black")

    # Add stamps to the image based on the stamp count
    stamp = Image.open(stamp_image_path).convert("RGBA")
    
    for _ in range(stamp_count):
        
        base_image.paste(stamp, stamp_position, stamp)

        # Update stamp position for the next stamp
        stamp_position = (stamp_position[0] + 60, stamp_position[1])

    # Save the modified image
    base_image.save("updated_stampCard.png")

# Example: Update stamp count based on a variable
current_stamp_count = 3
generate_stamp_card(current_stamp_count)
