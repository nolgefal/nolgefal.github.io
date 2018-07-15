---
layer: post
title: "Google Colaboratory"
description: "Jupyter notebook online from Google"
category: machine-learning
---

#Notes

Go to: [https://colab.research.google.com](https://colab.research.google.com)

- để sử dụng lệnh trên cmd, gõ ! trước câu lệnh
    - !ls
    - !pip install -q keras

- upload file lên colaboratory như sau:

```python
from google.colab import files
uploaded = files.upload()

with open("filename.type", 'w') as f:
    f.write(uploaded[uploaded.keys()[0]])
```