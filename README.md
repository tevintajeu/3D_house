# 3D House Project with Pycairo

## Overview
Our project showcases a 3D house illustration created using Pycairo, a powerful 2D graphics library for Python.
The goal of this project is to demonstrate how Pycairo can be used creatively to render 3D-like structures and visual effects within a 2D context. This is achieved by carefully layering shapes and adding depth through lighting, shading, and perspective techniques.

Our project is ideal for anyone interested in computer graphics, particularly those looking to expand their skills in creating complex visuals with simple geometry and artistic effects.

## Key Features of the project
- 3D Illusion Using 2D Techniques: Uses layered shapes, shading, and perspective adjustments to create a 3D effect.
- Modular Design: Components like walls, roof, windows, and doors are designed as modular elements, making it easy to modify individual parts.
- Adjustable Color Scheme and Dimensions: The colors, shapes, and dimensions of the house elements can be customized to explore different architectural styles and aesthetics.
- Optimized Performance: Pycairo is lightweight, making the rendering efficient even with detailed vector graphics.

## Why our Project is Useful
Our project serves as both an educational and artistic exploration. It provides insights into:
- Graphics Programming Concepts: Learn about basic principles of 3D representation, lighting, shading, and depth by working within a 2D framework.
- Practical Pycairo Skills: Dive deeper into Pycairo functions for path creation, transformations, gradients, and fills.
- Customizability for Artists and Designers: Easily modify the shapes, colors, and other parameters to create unique 3D house designs without needing a full 3D graphics engine.

Our project can also be used as a learning tool in educational settings, such as in computer graphics or programming classes, to teach students about 2D and 3D design techniques with practical coding.

## How to Get Started with the Project

### Prerequisites
Ensure you have:
- Python 3.6+ installed.
- Pycairo: Install using the command:
      pip install pycairo

##Steps on how to install and access the project
  -Clone the repository to your local machine
     cd 3D 
  -Run the main script
     python 3D_house.py
     
##Project Structure
3d_house.py: The main script where the Pycairo functions are defined and executed to create the house.
config.py (optional): A configuration file for advanced users, where you can define color palettes, dimensions, and shadow properties for easy customization.
assets/ (optional): Directory for storing reference images, icons, or textures that you might want to incorporate.

##Project Walkthrough
The script creates the 3D house by breaking down the structure into several key elements:

Base Structure: A simple rectangular prism forms the main body of the house, drawn using rectangles and polygons.
Roof: The triangular and trapezoidal shapes that form the roof are layered on top of the base structure, with shading applied to give it a pitched effect.
Windows and Door: Rectangular shapes are used with color fills to resemble windows, with added borders and shadows to give depth.
Lighting and Shadows: Shadows are added strategically to give an illusion of sunlight from a specific direction, enhancing the 3D appearance.

##Advanced Customizations
Adjusting Perspective: Modify coordinates to create different perspectives or angles.
Custom Colors: Use custom RGB values to change colors for each element. This is done within the script by altering the color variables.
Adding Textures: For a more realistic effect, consider adding subtle textures by drawing tiny patterns or gradients to simulate materials like bricks or tiles.

##Where Users Can Get Help with Your Project
If you encounter any issues or have questions, support is available:

GitHub Issues: Report bugs or request features in the Issues section.
PyCairo Documentation: Refer to the official PyCairo documentation for detailed information on using the library.
Community Support: You can also look for advice on Python graphics communities like Stack Overflow or Reddit.
