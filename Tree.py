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
        self.epsilon_REMT = 0.05
        self.epsilon_CART = 0.1

    def fit(self, df, method = 'REMT'):
        self.list_attributes = list(df)
        del self.list_attributes[-1]
        if method == 'REMT':
            self.root = self._fit(df)
        elif method == 'CART':
            self.root = self._fit_classic(df)

    # need more optimization
    def _fit(self, df, parent = None):
        max_RMI = 0
        max_c = -1
        max_a = None
        for a in self.list_attributes:
            values = df[a].unique()
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
                if sum > max_RMI:
                    max_RMI = sum
                    max_c = c
                    max_a = a

        df = df.drop(['temp'], axis = 1)

        if max_a is None:
            n = Node()
            count = []
            class_df = df['DECISION'].unique()
            for i in range(len(class_df)):
                t = df[df['DECISION'] == class_df[i]].shape[0]
                count.append([class_df[i], t])
            count.sort(key=lambda x: x[1])  #TODO: Find the median in case there is 2 or more
            n.label = count[len(count)/2][0]
            return n


        df1 = df[df[max_a] <= max_c]
        df2 = df[df[max_a] > max_c]

        class_df1 = df1['DECISION'].unique()
        n = Node(max_a, max_c)
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


        if max_RMI > self.epsilon_REMT:
            if left and df1.shape[0] > 0:
                n.left = self._fit(df1, 'left')
            if right and df2.shape[0] > 0:
                n.right = self._fit(df2, 'right')
        if max_RMI <= self.epsilon_REMT:
            count = []
            class_df = df['DECISION'].unique()
            for i in range(len(class_df)):
                t = df[df['DECISION'] == class_df[i]].shape[0]
                count.append([class_df[i], t])
            count.sort(key=lambda x: x[1])  #TODO: Find the median in case there is 2 or more
            n.label = count[len(count)/2][0]

        return n

    def test(self, df):
        n = df.shape[0]
        result = [0] * n
        i = 0
        for row in df.iterrows():
            index, data = row
            rec = data.tolist()
            if self._test(self.root, rec):
                result[i] = 1
            i+=1
        return result

    def _test(self, node, rec):
        if node.label is not None:
            return rec[-1] == node.label
        else:
            index = self.list_attributes.index(node.attribute)
            if rec[index] <= node.value:
                return self._test(node.left, rec)
            else:
                return self._test(node.right, rec)

    def _fit_classic(self, df):
        distinct_decision = df['DECISION'].unique()
        n = df.shape[0]
        sum = 0
        for de in distinct_decision:
            count = df[df['DECISION']==de].shape[0]
            sum -= (float(count)/n)*m.log(float(count)/n, 2)
        entropy_before = sum
        max_gain = 0
        max_c = -1
        max_a = None
        for a in self.list_attributes:
            values = df[a].unique()
            for c in values:
                df1 = df[df[a] <= c]
                df2 = df[df[a] > c]

                distinct_decision1 = df1['DECISION'].unique()
                n1 = df1.shape[0]
                entropy_left = 0
                if n1>0:
                    for de in distinct_decision1:
                        count = df1[df1['DECISION']==de].shape[0]
                        entropy_left -= (float(count)/n1)*m.log(float(count)/n1, 2)


                distinct_decision2 = df2['DECISION'].unique()
                n2 = df2.shape[0]
                entropy_right = 0
                if n2>0:
                    for de in distinct_decision2:
                        count = df2[df2['DECISION']==de].shape[0]
                        entropy_right -= (float(count)/n2)*m.log(float(count)/n2, 2)


                entropy_after = (float(n1)/n)*entropy_left + (float(n2)/n)*entropy_right
                gain = entropy_before - entropy_after
                if gain>max_gain:
                    max_gain = gain
                    max_c = c
                    max_a = a
        n = Node(max_a, max_c)
        df1 = df[df[max_a] <= max_c]
        df2 = df[df[max_a] > max_c]

        class_df1 = df1['DECISION'].unique()
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

        if max_gain > self.epsilon_CART and df1.shape[0] > 0 and df2.shape[0] > 0:
            if left:
                n.left = self._fit_classic(df1)
            if right:
                n.right = self._fit_classic(df2)

        if max_gain <= self.epsilon_CART:
            count = []
            class_df = df['DECISION'].unique()
            for i in range(len(class_df)):
                t = df[df['DECISION'] == class_df[i]].shape[0]
                count.append([class_df[i], t])
            count.sort(key=lambda x: x[1])  #TODO: Find the median in case there is 2 or more
            n.label = count[len(count)/2][0]

        return n