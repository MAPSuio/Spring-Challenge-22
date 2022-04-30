class BFS:

    def __init__(self):
        self.graph = dict()
        self.visited = set()
        self.queue = []


    def addEdge(self, u, v):
        try:
            self.graph[u].append(v)
        except:
            self.graph[u] = list()
            self.graph[u].append(v)
    
        try:
            self.graph[v].append(u)
        except:
            self.graph[v] = list()
            self.graph[v].append(u)


    def BFS(self, s):
        try:
            self.graph[s]
        except:
            return None

        self.queue.append(s)
        self.visited.add(s)

        while self.queue:
            curr = self.queue.pop(0)
            for neighbour in self.graph[curr]:
                if neighbour not in self.visited:
                    self.queue.append(neighbour)
                    self.visited.add(neighbour)

        return self.hashStuff(self.visited)


    def hashStuff(self, s):
        return "".join(map(str, sorted(s)))


def main():
    g = BFS()

    o = open("test.txt", "r")
    folk, _ = map(int, o.readline().split(" ")) # trenger ikke andre variabelen, sjekker bare resten av filen

    for i in o.readlines():
        k = i.strip().split()
        g.addEdge(int(k[0]), int(k[1]))

    s = set()
    for i in range(folk + 1):
        tmp = g.BFS(i)
        if tmp:
            s.add(int(tmp))


    print(len(s))



if __name__ == "__main__":
    main()