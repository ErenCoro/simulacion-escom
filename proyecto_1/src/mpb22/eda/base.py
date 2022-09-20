from abc import ABC, abstractmethod



class DatasetSummary(ABC):
 
    def list_features(self):
        raise NotImplementedError("This method hasn't been implemented yet")


    def list_labels(self):
        raise NotImplementedError("This method hasn't been implemented yet")

    def count_categorical(self):
        raise NotImplementedError("This method hasn't been implemented yet")


    def count_numerical(self):
        raise NotImplementedError("This method hasn't been implemented yet")       


    def statistics(self):
        raise NotImplementedError("This method hasn't been implemented yet")        


    def histogram(self, feature, bins = 10):
        raise NotImplementedError("This method hasn't been implemented yet")

