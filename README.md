# CountingWFlies
Algorithm to count Whitefly using digital image analysis

## Installation Instructions
To run this code, ensure you have Python 3.7 or higher installed. Additionally, install the matplotlib and NumPy libraries using the following command: pip install matplotlib numpy.

## Usage
To run the whitefly counting algorithm, execute the following command: python whitefly_counter.py --input image.jpg. The code will process the input image and provide the count of whiteflies detected.

## Algorithm Details
The algorithm scans the digital image using a wings-size moving window. The window goes over the image looking for whiteflies. Wings are detected based on their color. The algorithm takes advantage of the contrast between the white wings and the background and matches the densities of the RGB color channels' intensity within the moving window with those within the reference wings.
The adjustable parameters are boxHalfRef (window size / 2), percentile (_p_th percentile used as a threshold in the red and green channels of the reference wings), percentileBlue (_p_th percentile used as a threshold in the blue channel of the reference wings), and buffer (distance around the window used to set the wing pixels as NA after being counted). 

## Performance and Limitations
The algorithm takes about two minutes to run on a 1520 x 1300 pixel image with 87% accuracy.
The main limitation is that the parameters have to be manually set.

## Sample Input and Output
<img src="FigGitHub.png" width="680" height="300">

## License
GNU General Public License v3

## Contact Information
Juanmi Requena, juanmimullor@mail.com
