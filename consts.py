"""Setup constants, ymmv."""

import torch
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

cifar10_mean = [0.4914672374725342, 0.4822617471218109, 0.4467701315879822]  
cifar10_std = [0.24703224003314972, 0.24348513782024384, 0.26158785820007324]  

cifar100_mean = [0.5071598291397095, 0.4866936206817627, 0.44120192527770996]
cifar100_std = [0.2673342823982239, 0.2564384639263153, 0.2761504650115967]

mnist_mean = (0.13066373765468597,)
mnist_std = (0.30810782313346863,)

imagenet_mean = [0.485, 0.456, 0.406]
imagenet_std = [0.229, 0.224, 0.225]

tiny_imagenet_mean = [0.485, 0.456, 0.406]  
tiny_imagenet_std = [0.229, 0.224, 0.225]  

gtsrb_mean = [0.3403, 0.3121, 0.3214]
gtsrb_std = [0.2724, 0.2608, 0.2669]
