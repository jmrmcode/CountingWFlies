# CountingWFlies
A simple algorithm to count Whitefly using a digital image.

## Installation Instructions
To run this code, ensure you have Python 3.7 or higher installed. Additionally, install the matplotlib and NumPy libraries using the following command: pip install matplotlib numpy.

## Usage
To run the whitefly counting algorithm, first download _countWfly_GH.py_ and _input_image-jpg_ then, execute the following command on the terminal: python3 abosolute-path-to-countWfly_GH.py abosolute-path-to-the-input_image.jpg abosolute-path-to-the-output_image.jpg
The script will print the index of the pixel being processed, update the number of whiteflies detected on the screen, and finally, it will print the total number of whitefly and save the image with black squares on the detected flies.

## Algorithm Details
The algorithm scans the digital image using a wings-size moving window. The window goes over the image looking for whiteflies. Wings are detected based on their color. The algorithm takes advantage of the contrast between the white wings and the background and matches the densities of the RGB color channels' intensity within the moving window with those within the reference wings.
The adjustable parameters are boxHalfRef (window size / 2), percentile (_p_th percentile used as a threshold in the red and green channels of the reference wings), percentileBlue (_p_th percentile used as a threshold in the blue channel of the reference wings), and buffer (distance around the window used to set the wing pixels as NA after being counted). 

## Performance and Limitations
The algorithm takes about two minutes to run on a 1520 x 1300 pixel image with 87% accuracy.
The main limitation is that the parameters have to be manually set.

## Input and Output
<img src="FigGitHub.png" width="680" height="300">

## License
GNU General Public License v3

## Contact Information
Juanmi Requena, juanmimullor@mail.com
