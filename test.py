from list_dataloaders import ListDataloaders
import torch

# create sample dataloaders

def create_dataloader(num_samples, shift_offset=0):
    # create a dataloader with num_samples samples - random numbers between 0 and 1
    # shift_offset is used to shift all the samples by a constant value
    dataset = torch.utils.data.TensorDataset(torch.rand(num_samples, 1))
    # shift the samples by a constant value
    dataset.tensors = (dataset.tensors[0] + shift_offset,)
    # create a dataloader with batch size 1
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=1)
    return dataloader


dataloaders = [create_dataloader(5, shift_offset=0), create_dataloader(50, shift_offset=1), create_dataloader(500, shift_offset=2)]

# create a ListDataloaders object
list_dataloaders = ListDataloaders(dataloaders, verbose=True)

# iterate over the ListDataloaders object
for i, (x,) in enumerate(list_dataloaders):
    print(f"Dataloader index: {round(x.item())}, sample index: {i}")