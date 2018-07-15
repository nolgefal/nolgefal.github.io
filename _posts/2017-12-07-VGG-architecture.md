---
layout: post
title: "VGG Architecture"
description: "Kiến trúc của mô hình VGG"
category: javascript
---

### Intro
Một trong những mô hình Deep Learning được nghiên cứu và ứng dụng nhiều nhất trong **Transfer Learning** là VGG. Bài này chúng ta sẽ đi sâu về VGG để giải thích được tại sao VGG lại được ưa chuộng đến như vậy.

***

VGG có thể được chia làm 2 phần dựa theo **logical block**

### Convolutional Block

Model VGG pre-trained được train trên tập Imagenet với 1,000 classes.
Convolutional Blocks chứa nhiều convolutional layers. 
Những layers đầu tiên chứa các features ở tầng thấp như: lines, curves.
Những layers cuối chứa các features ở tầng cao hơn như: hand, leg, eye, .. more..

![alt text](https://raw.githubusercontent.com/lhlong/lhlong.github.io/master/public/img/vgg-architecture-01.png "VGG low layer")
![alt text](https://raw.githubusercontent.com/lhlong/lhlong.github.io/master/public/img/vgg-architecture-02.png "VGG high layer")

Như bạn thấy từ những hình trên, các đặc trưng (features) được trích xuất bởi các convolutional layers có thể được sử dụng cho nhiều vấn đề về nhận diện ảnh. Lưu ý, các features trên không nên áp dụng cho các đầu vào là các ảnh hoạt hình, các ảnh lĩnh vực y tế.

Convolutional Layer đưa ra 2 thuộc tính quan trọng:
- Số lượng parameters ít hơn số **Fully Connected layer**. Ví dụ, Convolutional Layer có kích thước bộ filter là 3\*3\*64 thì chỉ cần 576 parameters.
- Convolutional layer tiêu tốn rất nhiều thời gian để tính toán giá trị của các paramaters.

### Fully Connected Block

Chứa Dense layer (in Keras) hoặc Linear layer (in pyTorch) với **Dropout**. Số lượng parameter trong FC cũng rất lớn nhưng tốn ít thời gian tính toán hơn Convolutional block.



### Fine tune VGG using pre-convoluted features

Chúng ta thường sử dụng lại các parameters của Convolutional Block và chỉ cần train lại các lớp FC trong mô hình pre-trained VGG này.
Trước khi train lại các layer FC, ta sẽ **fine tune** (tinh chỉnh) lại một số layer cuối của block này cho phù hợp với output của bài toán.
