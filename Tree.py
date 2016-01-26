import math as m
class Node:
    def __init__(self, att, val):
        self.attribute = att
        self.value = val
        self.left = None
        self.right = None

class DecisionTree():
    def __init__(self):
        self.list_attributes = None
        self.root = None

    def fit(self, df):
        self.root = self._fit(df)

    # need more optimization
    def _fit(self, df):
        list_RMI = []
        for a in list(df):
            values = df[a].unique()
            max_RMI = 0
            max_c = values[0]
            for c in values:
                df['temp'] = 1 if df[df[a]<c] else 2
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
        best_attr = list_RMI[0]
        df1 = df[df[best_attr[1]] <= best_attr[2]]
        df2 = df[df[best_attr[1]] > best_attr[2]]
        n = Node(best_attr[1], best_attr[2])
        if best_attr[0] > 0.1 and df1.shape[0] > 0 and df2.shape[0] > 0:
            n.left = self.fit(df1)
            n.right = self.fit(df2)
        return n