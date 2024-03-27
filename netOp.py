import torch
import torch.nn as nn
import math

class dehaze_net(nn.Module):

	def __init__(self):
		super(dehaze_net, self).__init__()

		self.relu = nn.ReLU(inplace=True)
	
		self.e_conv1 = nn.Conv2d(3,3,1,1,0,bias=True) 
		self.e_conv2 = nn.Conv2d(3,3,3,1,1,bias=True) 
		self.e_conv3 = nn.Conv2d(6,3,5,1,2,bias=True) 
		self.e_conv4 = nn.Conv2d(6,3,7,1,3,bias=True) 
		self.e_conv5 = nn.Conv2d(12,3,3,1,1,bias=True)
		self.max_pool1 = nn.MaxPool2d(kernel_size=1, stride=2)
		self.max_pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
		self.max_pool3 = nn.MaxPool2d(kernel_size=4, stride=2)
		self.e_conv11 = nn.Conv2d(1,1,3,1,1,bias=True)
		self.e_conv22 = nn.Conv2d(1,1,3,1,1,bias=True)
		self.e_conv33 = nn.Conv2d(1,1,3,1,1,bias=True)

	def forward(self, x):
		source = []
		source.append(x)

		x1 = self.relu(self.e_conv1(x))
		x2 = self.relu(self.e_conv2(x1))

		concat1 = torch.cat((x1,x2), 1)
		x3 = self.relu(self.e_conv3(concat1))

		concat2 = torch.cat((x2, x3), 1)
		x4 = self.relu(self.e_conv4(concat2))

		concat3 = torch.cat((x1,x2,x3,x4),1)
		x5 = self.relu(self.e_conv5(concat3))
		#
		xx1 = self.max_pool1(x5)
		xx2 = self.max_pool2(x5)
		xx3 = self.max_pool3(x5)
		x6 = self.relu(self.e_conv11(xx1))
		x7 = self.relu(self.e_conv22(xx2))
		x8 = self.relu(self.e_conv33(xx3))
		concat4 = torch.cat((xx1,xx2,xx3),1)

		x9 = self.relu(self.e_conv1(concat4))
		clean_image = self.relu((x9 * x) - x9 + 1)
		
		return clean_image

		


			

			
			






