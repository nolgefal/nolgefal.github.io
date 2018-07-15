#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <math.h>
#include <iostream>
using namespace cv;
using namespace std;

struct license_plate {
  Mat hidden_img;
  Mat crop_img;
};

license_plate detect_plate(string path) {
    license_plate group_img;    
    Mat origin_img;
    Mat dst_img;
    Mat temps_img;
    
    // load image from PATH
    origin_img = cv::imread(path , CV_LOAD_IMAGE_COLOR);    
    resize(origin_img, origin_img, Size(800, origin_img.size().height * 800 / origin_img.size().width));
    origin_img.copyTo(group_img.hidden_img);
    origin_img.copyTo(dst_img);

    cvtColor(dst_img, temps_img, COLOR_RGB2GRAY);
    bilateralFilter (temps_img, dst_img, 11, 17, 17);
    medianBlur(dst_img, dst_img, 5);
    adaptiveThreshold (dst_img, dst_img, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 43, 6);

    // find Contours
    vector<vector<Point> > contours;
    vector<Vec4i> hierarchy;
    findContours(dst_img, contours, hierarchy, RETR_TREE, CHAIN_APPROX_SIMPLE);

    for ( int i = 0; i < contours.size(); i++ )
    {
        double area = contourArea(contours[i]);        
        if (area > 2200 && area < 16000) {       
            CvRect roi = boundingRect(Mat(contours[i]));            
            if (roi.height>0 && float(roi.width)/roi.height > 1.69 && float(roi.width)/roi.height < 2.1)
            {    
                // cout << "Area " << area << endl;
                GaussianBlur(group_img.hidden_img(roi), group_img.hidden_img(roi), Size(0, 0), 10);
                rectangle(origin_img, roi, Scalar(0, 0, 255 ), 5);
                group_img.crop_img = origin_img(roi);
                break;
            }
        }
    }

    return group_img;
}

int main( int argc, char** argv ) {  
    string img_path = "./data/11.jpg";
    license_plate group_img;
    
    try {
        group_img = detect_plate(img_path);
    }catch(int e){
        cout << "An exception occurred. Exception Nr. " << e << '\n';
    };

    namedWindow("Hidden Display window", WINDOW_AUTOSIZE );
    imshow("Hidden Display window", group_img.hidden_img );
  
    namedWindow("Crop Display window", WINDOW_AUTOSIZE );
    imshow("Crop Display window", group_img.crop_img );
  
    waitKey(0);
    return 0;
}
