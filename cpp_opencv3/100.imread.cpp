
#include <opencv2/opencv.hpp>

int main(void)
{
  cv::Mat src_img;
  src_img = cv::imread("img001.png", 1);

//  if(src_img.empty()) return -1;
//
//  cv::namedWindow("Image", CV_WINDOW_AUTOSIZE|CV_WINDOW_FREERATIO);
//  cv::imshow("Image", src_img);
//  cv::waitKey(0);
}


