# ASCII Image Converter

## Introduction
This project converts images into ASCII art and optionally saves the ASCII output as a transparent PNG using the Pillow (PIL) library.

## Features
- Converts images to grayscale ASCII representations.
- Adjustable width and scale factor to maintain aspect ratio.
- Saves ASCII output as text and optionally as a transparent PNG.
- Uses custom or default fonts for rendering ASCII into an image.

## Installation
### Prerequisites
Ensure you have Python installed along with the required dependencies:

1. Install Python (3.x recommended)
2. Install dependencies:
   ```sh
   pip install pillow
   ```

## Usage
### Convert Image to ASCII
Run the script by providing an image path:
```sh
python ascii_converter.py
```
This will generate ASCII art and save it as `ascii_art.txt`.

### Save ASCII Art as PNG
To convert the ASCII output into a transparent PNG:
```sh
python ascii_converter.py
```
This will save the result as `ascii_art.png`.

## Configuration
Modify the script to adjust:
- **New Width**: Change `new_width` to control the ASCII image width.
- **Scale Factor**: Tweak `scale_factor` to adjust vertical proportions.
- **Font & Size**: Set `font_path` and `font_size` when saving as PNG.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contribution
Feel free to submit issues or pull requests to improve functionality!

## Disclaimer
This project is intended for artistic and educational purposes. Ensure you have the right to use the images you process.

## This is a sample image. (PLEASE VIEW IN LIGHT MODE)
<img src="https://github.com/roshaanmehar/ASCII-Art/blob/main/ascii_art.png" alt="sample ascii art" height="300">

## This is how it should look like in text:



                                 ###  ######                                    
                                 ###     ##                                     
                                ####    ###      ##                             
                             ## #########@#########                             
                              ######@@############# #                           
                              ###########   ###### ##                           
                               ###########   ###                                
                                  #########                                     
                                   ######    #                                  
                                  ## ######      #                              
                                 #####           ##                             
                                 #######        ####                            
                                 ########      #####                            
                                 ##@@###    #######                             
                                  #@@# #####  #####                             
                     ####         ##@#        ####                              
                     ####          #@#      # ####                              
                     #####          #@#    #  ###                               
                      ###           #@#      ###                                
                                     #@      @##                                
                                     #@#    @@#                                 
                                      @#   #@##                                 
                                      #@  #@@#                                  



- You can change the characters in the image.
- You can change the height using the ```` auto_scale ```` attribute.
- Have fun with it!
