Report3 - FashionMNIST and Clothing Classification
==================================================

 

Fashion-MNIST
-------------

`Fashion-MNIST` is a dataset of [Zalando](https://jobs.zalando.com/tech/)'s
article images—consisting of a training set of 60,000 examples and a test set of
10,000 examples. Each example is a 28x28 grayscale image, associated with a
label from 10 classes. We intend `Fashion-MNIST` to serve as a direct **drop-in
replacement** for the original [MNIST
dataset](http://yann.lecun.com/exdb/mnist/) for benchmarking machine learning
algorithms. It shares the same image size and structure of training and testing
splits.

Here's an example how the data looks (*each class takes three-rows*):

![](doc/img/fashion-mnist-sprite.png)

Why we made Fashion-MNIST
-------------------------

The original [MNIST dataset](http://yann.lecun.com/exdb/mnist/) contains a lot
of handwritten digits. Members of the AI/ML/Data Science community love this
dataset and use it as a benchmark to validate their algorithms. In fact, MNIST
is often the first dataset researchers try. *"If it doesn't work on MNIST, it
won't work at all"*, they said. *"Well, if it does work on MNIST, it may still
fail on others."*

 

Task
----

Build and train a CNN classification model with Fashion-MNIST dataset. Build a
web crawler and collect clothing (i.e. T-shirt, shoes...) images from taobao.
Then use the trained model to classify the collect images
