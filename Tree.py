import math as m
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

    # need more optimization
    def fit(self, df):
        list_RMI = []
        for a in list(df):
            values = df[a].unique()
            max_RMI = 0
            max_c = values[0]
            for c in values:
                df['temp'] = 1 if df[a]<c else 2
                sum = 0
                total_count = df.shape[0]
                for i in range(df.shape[0]):
                    attr = df['temp'][i]
                    dec = df['DECISION'][i]
                    attr_count = df[df['temp'] >= attr].shape[0]
                    dec_count = df[df['DECISION'] >= dec].shape[0]
                    both_count = df[df['temp'] >= attr & df['DECISION'] >= dec].shape[0]
                    l = m.log((attr_count*dec_count)/(total_count*both_count))
                    sum += l
                sum = -sum
                sum /= total_count
                if sum > max_RMI:
                    max_RMI = sum
                    max_c = c
            list_RMI.append([max_RMI, a, max_c])
        list_RMI.sort(key=lambda x: x[0], reverse=True)
