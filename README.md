# CountingWFlies
Algorithm to count Whitefly using digital image analysis

## Installation Instructions
To run this code, ensure you have Python 3.7 or higher installed. Additionally, install the matplotlib and NumPy libraries using the following command: pip install matplotlib numpy.

## Usage
Before running the whitefly counting algorithm, you have to manually adjust several parameters: *percentile* and *percentileBlue*
To run the whitefly counting algorithm, execute the following command: python whitefly_counter.py --input image.jpg. The code will process the input image and provide the count of whiteflies detected.

## Algorithm Details
The algorithm scans the digital image using a wings-size moving window. The window goes over the image looking for whiteflies. Wings are detected based on their color. The algorithm takes advantage of the contrast between the white wings and the background and matches the densities of the RGB color channels' intensity within the moving window with those within the reference wings.

## Performance and Limitations

## Sample Input and Output

## License
GNU General Public License v3

## Contact Information
Juanmi Requena, juanmimullor@mail.com
