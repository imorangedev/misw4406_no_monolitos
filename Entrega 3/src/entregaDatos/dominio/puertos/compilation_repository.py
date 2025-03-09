from abc import ABC, abstractmethod

class CompilationRepositoryPort(ABC):
    @abstractmethod
    def find_by_property(self, property_name: str, value):
        pass
