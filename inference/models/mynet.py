import torch.nn as nn
import torch.nn.functional as F
import torch
import os
import sys
# from mamba.vmamba import Backbone_VMAMBA2
# Add project root to path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(project_root)

from mamba.vmamba import Backbone_VMAMBA2
import torch

from inference.models.grasp_model import GraspModel, ResidualBlock




class GenerativeResnet(GraspModel):

    def __init__(self, input_channels=4, output_channels=1, channel_size=32, dropout=False, prob=0.0):
        super(GenerativeResnet, self).__init__()
        num_embedding = 128
        self.vmamba = Backbone_VMAMBA2(in_chans=input_channels, linear_attn_duality=True, ssd_expansion=2, embed_dim=num_embedding).cuda()
        self.conv1 = nn.ConvTranspose2d(
            in_channels=num_embedding * 8,       # Number of input channels
            out_channels=num_embedding * 4,  # Half the number of channels
            kernel_size=4,                     # Kernel size to help with upsampling
            stride=2,                          # Stride to double the height and width
            padding=1                          # Padding to ensure output dimensions are doubled
        )
        self.conv2 = nn.ConvTranspose2d(
            in_channels=num_embedding * 4,       # Number of input channels
            out_channels=num_embedding * 2,  # Half the number of channels
            kernel_size=4,                     # Kernel size to help with upsampling
            stride=2,                          # Stride to double the height and width
            padding=1                          # Padding to ensure output dimensions are doubled
        )
        self.conv3 = nn.ConvTranspose2d(
            in_channels=num_embedding * 2,       # Number of input channels
            out_channels=num_embedding ,  # Half the number of channels
            kernel_size=4,                     # Kernel size to help with upsampling
            stride=2,                          # Stride to double the height and width
            padding=1                          # Padding to ensure output dimensions are doubled
        )
        self.bn3 = nn.BatchNorm2d(channel_size * 4)

        # Residual blocks
        self.res1 = ResidualBlock(channel_size * 4, channel_size * 4)
        self.res2 = ResidualBlock(channel_size * 4, channel_size * 4)
        self.res3 = ResidualBlock(channel_size * 4, channel_size * 4)
        self.res4 = ResidualBlock(channel_size * 4, channel_size * 4)
        self.res5 = ResidualBlock(channel_size * 4, channel_size * 4)

        # Transpose convolutions to upsample back to input size
        self.conv4 = nn.ConvTranspose2d(channel_size * 4, channel_size * 2, kernel_size=4, stride=2, padding=1,
                                        output_padding=1)
        self.bn4 = nn.BatchNorm2d(channel_size * 2)

        self.conv5 = nn.ConvTranspose2d(channel_size * 2, channel_size, kernel_size=4, stride=2, padding=2,
                                        output_padding=1)
        self.bn5 = nn.BatchNorm2d(channel_size)

        self.conv6 = nn.ConvTranspose2d(channel_size, channel_size, kernel_size=9, stride=1, padding=4)

        # Output layers for grasping parameters
        self.pos_output = nn.Conv2d(in_channels=channel_size, out_channels=output_channels, kernel_size=2)
        self.cos_output = nn.Conv2d(in_channels=channel_size, out_channels=output_channels, kernel_size=2)
        self.sin_output = nn.Conv2d(in_channels=channel_size, out_channels=output_channels, kernel_size=2)
        self.width_output = nn.Conv2d(in_channels=channel_size, out_channels=output_channels, kernel_size=2)

        # Dropout configuration
        self.dropout = dropout
        self.dropout_pos = nn.Dropout(p=prob)
        self.dropout_cos = nn.Dropout(p=prob)
        self.dropout_sin = nn.Dropout(p=prob)
        self.dropout_wid = nn.Dropout(p=prob)

        for m in self.modules():
            if isinstance(m, (nn.Conv2d, nn.ConvTranspose2d)):
                nn.init.xavier_uniform_(m.weight, gain=1)

    def forward(self, x_in):
        # Get feature maps from VMAMBA backbone
        ys = self.vmamba(x_in)
        last_output = ys[-1]
        print(ys[0].shape)
        print(ys[1].shape)
        print(ys[2].shape)
        print(ys[3].shape)
        x = F.gelu(self.conv1(last_output))
        x = F.gelu(self.conv2(x))
        x = F.gelu(self.conv3(x))
        # Pass through residual blocks
        x = self.res1(x)
        x = self.res2(x)
        x = self.res3(x)
        x = self.res4(x)
        x = self.res5(x)

        # Upsample to original input dimensions
        x = F.relu(self.bn4(self.conv4(x)))
        x = F.relu(self.bn5(self.conv5(x)))
        x = self.conv6(x)  # Final layer to maintain original dimensions
        
        # Apply dropout if enabled and generate output channels
        if self.dropout:
            pos_output = self.pos_output(self.dropout_pos(x))
            cos_output = self.cos_output(self.dropout_cos(x))
            sin_output = self.sin_output(self.dropout_sin(x))
            width_output = self.width_output(self.dropout_wid(x))
        else:
            pos_output = self.pos_output(x)
            cos_output = self.cos_output(x)
            sin_output = self.sin_output(x)
            width_output = self.width_output(x)

        return pos_output, cos_output, sin_output, width_output

    
if __name__ == "__main__":
    # Initialize the model with sample parameters
    input_channels = 4  # This is based on the model setup
    output_channels = 1  # Expected output channels for each of the output layers
    channel_size = 32  # Channel size for internal layers
    dropout = True  # Enable dropout to test that path

    model = GenerativeResnet(input_channels=input_channels, output_channels=output_channels, 
                            channel_size=channel_size, dropout=dropout, prob=0.2)

    # Move the model to GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    # Create a dummy input tensor with the correct shape
    # Assuming an input resolution (adjust if needed), e.g., 128x128
    input_tensor = torch.randn(8, input_channels, 224, 224).to(device)

    # Run a forward pass
    with torch.no_grad():  # Disable gradient computation for testing
        pos_output, cos_output, sin_output, width_output = model(input_tensor)

    # Print the output shapes to verify
    print("Position output shape:", pos_output.shape)
    print("Cosine output shape:", cos_output.shape)
    print("Sine output shape:", sin_output.shape)
    print("Width output shape:", width_output.shape)
