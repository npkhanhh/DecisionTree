import math as m
class Node:
    def __init__(self, att = None, val = None):
        self.attribute = att
        self.value = val
        self.label = None
        self.left = None
        self.right = None

class DecisionTree():
    def __init__(self):
        self.list_attributes = None
        self.root = None

    def fit(self, df):
        self.list_attributes = list(df)
        del self.list_attributes[-1]
        self.root = self._fit(df)

    # need more optimization
    def _fit(self, df, parent = None):
        list_RMI = []
        for a in self.list_attributes:
            values = df[a].unique()
            max_RMI = 0
            max_c = values[0]
            for c in values:
                df.loc[(df[a]<=c), 'temp'] = 1
                df.loc[(df[a]>c), 'temp'] = 2
                sum = 0
                total_count = df.shape[0]
                for i in [1, 2]:
                    distinct_decision = df[df['temp'] == i]['DECISION'].unique()
                    for j in distinct_decision:
                        group_count = df[(df['temp'] == i) & df['DECISION'] == j].shape[0]
                        attr_count = df[df['temp'] >= i].shape[0]
                        dec_count = df[df['DECISION'] >= j].shape[0]
                        both_count = df[(df['temp'] >= i) & (df['DECISION'] >= j)].shape[0]
                        l = m.log(float((attr_count*dec_count))/(total_count*both_count))
                        l*=group_count
                        sum+=l
                sum = -sum
                sum /= total_count
                # for i in range(df.shape[0]):
                #     attr = df['temp'][i]
                #     dec = df['DECISION'][i]
                #     attr_count = df[df['temp'] >= attr].shape[0]
                #     dec_count = df[df['DECISION'] >= dec].shape[0]
                #     both_count = df[(df['temp'] >= attr) & (df['DECISION'] >= dec)].shape[0]
                #     if total_count*both_count == 0 or attr_count*dec_count == 0:
                #         l = 1
                #     else:
                #         l = m.log(float((attr_count*dec_count))/(total_count*both_count))
                #     sum += l
                #     print i
                # sum = -sum
                # sum /= total_count
                if sum > max_RMI:
                    max_RMI = sum
                    max_c = c
            list_RMI.append([max_RMI, a, max_c])
        df.drop(['temp'], axis = 1)
        list_RMI.sort(key=lambda x: x[0], reverse=True)
        best_attr = list_RMI[0]
        df1 = df[df[best_attr[1]] <= best_attr[2]]
        df2 = df[df[best_attr[1]] > best_attr[2]]

        class_df1 = df1['DECISION'].unique()
        n = Node(best_attr[1], best_attr[2])
        left = right = True
        if len(class_df1) == 1:
            n_left = Node()
            n_left.label = class_df1[0]
            n.left = n_left
            left = False

        class_df2 = df2['DECISION'].unique()
        if len(class_df2) == 1:
            n_right = Node()
            n_right.label = class_df2[0]
            n.right = n_right
            right = False


        if best_attr[0] > 0.1 and df1.shape[0] > 0 and df2.shape[0] > 0:
            if left:
                n.left = self._fit(df1, 'left')
            if right:
                n.right = self._fit(df2, 'right')
        elif best_attr[0] <= 0.1:
            count = []
            for i in range(len(class_df1)):
                t = df1[df1['DECISION'] == class_df1[i]].shape[0]
                count.append([class_df1[i], t])
            count.sort(key=lambda x: x[1], reverse=True)
            n.label = count[len(count)/2][0]

        return n