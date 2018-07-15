#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <math.h>
#include <iostream>
using namespace cv;
using namespace std;

Mat detect_plate(string path) {
    Mat origin_img;
    Mat dst_img;
    Mat temps_img;
    
    // load image from PATH
    origin_img = cv::imread(path , CV_LOAD_IMAGE_COLOR);                                                
    resize(origin_img, origin_img, Size(800, origin_img.size().height * 800 / origin_img.size().width));
    origin_img.copyTo(dst_img);
    cvtColor(dst_img, temps_img, COLOR_RGB2GRAY);    
    medianBlur(temps_img, dst_img, 7);
    bilateralFilter (temps_img, dst_img, 11, 15, 15);
    // medianBlur(dst_img, dst_img, 9);
    adaptiveThreshold (dst_img, dst_img, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 23, 6);

    namedWindow("TT", WINDOW_AUTOSIZE );
    imshow("TT", dst_img);

    // find Contours
    vector<vector<Point> > contours;
    vector<Vec4i> hierarchy;
    findContours(dst_img, contours, hierarchy, RETR_TREE, CHAIN_APPROX_SIMPLE);

    for ( int i = 0; i < contours.size(); i++ )
    {
        double area = contourArea(contours[i]);  
        if (area > 1200 && area < 16000) 
        {         
            CvRect roi = boundingRect(Mat(contours[i])); 
            rectangle(origin_img, roi, Scalar(0, 255, 0), 2);   
            if (roi.y > (dst_img.size().height / 3.5) && roi.height>10 && float(roi.width)/roi.height > 1 && float(roi.width)/roi.height < 2.5)            
            {    
                rectangle(origin_img, roi, Scalar(0, 0, 255 ), 2);                              
                vector<vector<Point> > roi_contours;
                findContours(dst_img(roi), roi_contours, hierarchy, RETR_LIST, CHAIN_APPROX_SIMPLE);

                int count = 0;
                for ( int i = 0; i < roi_contours.size(); i++ )
                {
                    if (contourArea(roi_contours[i]) > 50)
                    {
                        CvRect roi1 = boundingRect(Mat(roi_contours[i]));            
                        if (roi1.height>8 and roi1.height < 50 && float(roi1.width)/roi1.height < 1.1)
                        {
                            count++;
                        }
                    }
                }
                if (count > 3)
                {
                    GaussianBlur(origin_img(roi), origin_img(roi), Size(0, 0), 10);
                    // break;
                }
            }
        }
    }

    return origin_img;
}

int main( int argc, char** argv ) {  
    string img_path = "./data/x1.jpg";
    Mat img;
    img = detect_plate(img_path);
    
    namedWindow("Hidden Display window", WINDOW_AUTOSIZE );
    imshow("Hidden Display window", img);
  
    waitKey(0);
    return 0;
}
//1, 2, 3, 6, 7, 8, 9, 10, 13, 
//0, 4, 5, 11, 12, 14