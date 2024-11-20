import torch.nn as nn
import torch.nn.functional as F
import torch
import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(project_root)

from mamba.vmamba import Backbone_VMAMBA2
from inference.models.grasp_model import GraspModel, ResidualBlock

class GenerativeResnet(GraspModel):
    def __init__(self, input_channels=4, output_channels=1, channel_size=32, dropout=False, prob=0.0):
        super(GenerativeResnet, self).__init__()
        num_embedding = 128

        # Initialize the VMAMBA backbone
        self.vmamba = Backbone_VMAMBA2(
            in_chans=input_channels, patch_size=2, linear_attn_duality=True, embed_dim=num_embedding
        ).cuda()

        # Decoder (upsampling layers)
        self.up1 = nn.ConvTranspose2d(1024, 512, kernel_size=4, stride=2, padding=1)
        self.up2 = nn.ConvTranspose2d(1024, 256, kernel_size=4, stride=2, padding=1)  # Concatenate with encoder layer
        self.up3 = nn.ConvTranspose2d(512, 128, kernel_size=4, stride=2, padding=1)
        self.up4 = nn.ConvTranspose2d(256, 256, kernel_size=4, stride=2, padding=1)
        self.up5 = nn.ConvTranspose2d(256, channel_size, kernel_size=4, stride=2, padding=1)

        # Final convolution layers
        self.pos_output = nn.Conv2d(channel_size, output_channels, kernel_size=1)
        self.cos_output = nn.Conv2d(channel_size, output_channels, kernel_size=1)
        self.sin_output = nn.Conv2d(channel_size, output_channels, kernel_size=1)
        self.width_output = nn.Conv2d(channel_size, output_channels, kernel_size=1)

        # Dropout layers
        self.dropout = dropout
        self.dropout_pos = nn.Dropout(p=prob)
        self.dropout_cos = nn.Dropout(p=prob)
        self.dropout_sin = nn.Dropout(p=prob)
        self.dropout_wid = nn.Dropout(p=prob)

    def forward(self, x_in):
        # Encoder
        enc1, enc2, enc3, enc4 = self.vmamba(x_in)
        
        # Decoder with skip connections
        x = F.gelu(self.up1(enc4))
        x = torch.cat([x, enc3], dim=1)  # Concatenate with encoder layer

        x = F.gelu(self.up2(x))
        x = torch.cat([x, enc2], dim=1)  # Concatenate with encoder layer

        x = F.gelu(self.up3(x))
        x = torch.cat([x, enc1], dim=1)  # Concatenate with encoder layer

        x = F.gelu(self.up4(x)) 
        x = F.gelu(self.up5(x)) 

        # Final output layers
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
    model = model.to(device)  # Ensure the model is on the same device as the inputs

    # Create a dummy input tensor with the correct shape and move it to the GPU
    input_tensor = torch.randn(8, input_channels, 224, 224).to(device)

    # Run a forward pass
    with torch.no_grad():  # Disable gradient computation for testing
        pos_output, cos_output, sin_output, width_output = model(input_tensor)

    # Print the output shapes to verify
    print("Position output shape:", pos_output.shape)
    print("Cosine output shape:", cos_output.shape)
    print("Sine output shape:", sin_output.shape)
    print("Width output shape:", width_output.shape)

