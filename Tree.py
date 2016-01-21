class Tree:
    def __init__(self):
        self.attribute = None
        self.left = None
        self.right = None

class DecisionTree(Tree):
    def __init__(self):
        self.list_attributes = None
        self.df = None
        super(DecisionTree, self).__init__()

    def fit(self, dataframe):
        self.df = dataframe
        for a in self.list_attributes:
            values = self.df[a].unique()
            for c in values:
