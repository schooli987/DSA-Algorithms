class BubbleSort:
    def __init__(self, data):
        self.data = data

    def Bubble(self, sort_order="Ascending"):

        if isinstance(self.data, dict):
            items = list(self.data.items())  
        elif isinstance(self.data, tuple):
            items = list(self.data)
        else:
            items = self.data[:]

        n = len(items)
        iterations = 0

        if isinstance(self.data, dict):
            for i in range(n):
                swapped = False
                iterations += 1
                for j in range(0, n - i - 1):
                    v1, v2 = items[j][1], items[j + 1][1]

                    # Try numeric comparison, else string
                    try:
                        v1_num = float(v1)
                        v2_num = float(v2)
                    except (ValueError, TypeError):
                        v1_num = str(v1)
                        v2_num = str(v2)

                    if sort_order == "Ascending":
                        if v1_num > v2_num:
                            items[j], items[j + 1] = items[j + 1], items[j]
                            swapped = True
                    elif sort_order == "Descending":
                        if v1_num < v2_num:
                            items[j], items[j + 1] = items[j + 1], items[j]
                            swapped = True

                if not swapped:
                    break
            return dict(items), iterations

        elif isinstance(self.data, (list, tuple)):
            for i in range(n):
                swapped = False
                iterations += 1
                for j in range(0, n - i - 1):
                    try:
                        v1 = float(items[j])
                        v2 = float(items[j + 1])
                    except (ValueError, TypeError):
                        v1 = str(items[j])
                        v2 = str(items[j + 1])

                    if sort_order == "Ascending":
                        if v1 > v2:
                            items[j], items[j + 1] = items[j + 1], items[j]
                            swapped = True
                    elif sort_order == "Descending":
                        if v1 < v2:
                            items[j], items[j + 1] = items[j + 1], items[j]
                            swapped = True
                if not swapped:
                    break
            return (tuple(items) if isinstance(self.data, tuple) else items), iterations

        

        else:
            raise TypeError("Unsupported data type for sorting")
