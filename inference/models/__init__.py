def get_network(network_name):
    network_name = network_name.lower()
    # Original GR-ConvNet
    if network_name == 'grconvnet':
        from .grconvnet import GenerativeResnet
        return GenerativeResnet
    # Configurable GR-ConvNet with multiple dropouts
    elif network_name == 'grconvnet2':
        from .grconvnet2 import GenerativeResnet
        return GenerativeResnet
    # Configurable GR-ConvNet with dropout at the end
    elif network_name == 'grconvnet3':
        from .grconvnet3 import GenerativeResnet
        return GenerativeResnet
    # Inverted GR-ConvNet
    elif network_name == 'grconvnet4':
        from .grconvnet4 import GenerativeResnet
        return GenerativeResnet
    elif network_name == 'mynet':
        from .mynet import GenerativeResnet
        return GenerativeResnet
    elif network_name == 'mynet3':
        from .mynet3 import GenerativeResnet
        return GenerativeResnet
    elif network_name == 'mynet4':
        from .mynet4 import GenerativeResnet
        return GenerativeResnet
    elif network_name == 'tiny':
        from .me5400_tiny import GenerativeResnet
        return GenerativeResnet
    elif network_name == 'small':
        from .me5400_small import GenerativeResnet
        return GenerativeResnet
    elif network_name == 'base':
        from .me5400_base import GenerativeResnet
        return GenerativeResnet
    elif network_name == 'large':
        from .me5400_large import GenerativeResnet
        return GenerativeResnet
    elif network_name == 's1':
        from .me5400_s1 import GenerativeResnet
        return GenerativeResnet
    elif network_name == 'swin':
        from .swin import SwinTransformerSys
        return SwinTransformerSys
    else:
        raise NotImplementedError('Network {} is not implemented'.format(network_name))
