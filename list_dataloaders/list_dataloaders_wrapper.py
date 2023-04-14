import random

class ListDataloaders:
    """
    This class is a wrapper for a list of dataloaders. It allows to iterate over the dataloaders in a random order.
    """
    def __init__(self, dataloaders, verbose=False, weight_by_num_samples=True):
        """
        :param dataloaders: list of dataloaders
        :param verbose: boolean
        :param weight_by_num_samples: boolean, if True, the probability of choosing a dataloader is proportional to the
        number of samples in the dataloader
        """
        self.dataloaders = dataloaders
        self.num_dataloaders = len(dataloaders)
        self.counters = [0] * self.num_dataloaders
        self.num_samples = [len(dataloader) for dataloader in dataloaders]
        self.num_samples_total = sum(self.num_samples)
        self.iterators = [iter(dataloader) for dataloader in dataloaders]

        self.verbose = verbose
        self.weight_by_num_samples = weight_by_num_samples

        if verbose:
            print(f"num_dataloaders: {self.num_dataloaders}")
            print(f"num_samples_total: {self.num_samples_total}")
            print(f"num_samples: {self.num_samples}")

    def __iter__(self):
        return self

    def __next__(self):
        # randomly choose a dataloader among the ones that have not finished
        try:
            if self.weight_by_num_samples: # weight by the number of samples in the dataloader
                probabilities = [self.num_samples[i] - self.counters[i] for i in range(self.num_dataloaders)]
                dataloader_index = random.choices(range(self.num_dataloaders), weights=probabilities, k=1)[0]
            else:
                dataloader_index = random.choice([i for i in range(self.num_dataloaders) if self.counters[i] < self.num_samples[i]])
        except (IndexError, ValueError):
            if self.verbose:
                print ("The dataloaders are empty, restarting them")
            self.counters = [0] * self.num_dataloaders
            self.iterators = [iter(dataloader) for dataloader in self.dataloaders]
            raise StopIteration
        self.counters[dataloader_index] += 1
        return next(self.iterators[dataloader_index])

    def __len__(self):
        return self.num_samples_total