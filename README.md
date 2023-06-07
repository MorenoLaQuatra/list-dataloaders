# List dataloaders

This repository contains an hyper-simple wrapper class that allows to iterate over a list of dataloaders in a transparent way.

## Installation

```bash
pip install list-dataloaders
```

or directly from the repository:

```bash
pip install git+https://github.com/MorenoLaQuatra/list-dataloaders.git
```

## Usage

```python
from list_dataloaders import ListDataLoaders

list_dataloaders = []
train_dl1 = DataLoader(...)
train_dl2 = DataLoader(...)
train_dl3 = DataLoader(...)
list_dataloaders.append(train_dl1)
list_dataloaders.append(train_dl2)
list_dataloaders.append(train_dl3)

train_dls = ListDataLoaders(list_dataloaders)

for batch in train_dls:
    print(batch)
```

## Options and parameters

The main class `ListDataLoaders` has the following parameters:
- `dataloaders`: the list of dataloaders to iterate over
- `verbose`: if *True*, prints the number of samples in each dataloader (default: *False*)
- `weight_by_num_samples`: if *True*, the probability of sampling a dataloader is proportional to the number of samples in the dataloader (default: *True*)

## License

This project is licensed under the terms of the MIT license.

## Issues

If you encounter any problems, please [file an issue](https://github.com/MorenoLaQuatra/list-dataloaders/issues/new) along with a detailed description.