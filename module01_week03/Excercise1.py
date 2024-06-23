import torch
import torch.nn as nn

class Softmax(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, data):
        exp_x = torch.exp(data)
        return exp_x / torch.sum(exp_x)


class softmax_stable(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, data):
        c = torch.max(data)
        exp_x = torch.exp(data - c)
        return exp_x / torch.sum(exp_x)

data = torch.Tensor([1,2,3])
softmax = Softmax ()
output1 = softmax ( data )
print(output1)

softmax_stable = softmax_stable ()
output2 = softmax_stable ( data )
print(output2)

