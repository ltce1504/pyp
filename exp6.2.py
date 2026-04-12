class event:
    def __init__(self, eid, nm, dt):
        self.eid = eid
        self.dt = dt
        self.nm = nm

    def dis(self):
        print("\nEvent Details")
        print("ID:", self.eid)
        print("Name:", self.nm)
        print("Date:", self.dt)


class mevent(event):
    def __init__(self, eid, nm, dt):
        super().__init__(eid, nm, dt)
        self.p1 = []
        self.p2 = []

    def addp(self, p, i):
        if i == 1:
            self.p1.append(p)
            print(self.p1)
        elif i == 2:
            self.p2.append(p)
            print(self.p2)

        print(f'{p} participant registered successfully')

    def disp(self, i):
        if i == 1:
            if self.p1:
                print('Participants for Tech Quiz:\n')
                for p in self.p1:
                    print(p)
            else:
                print('No participant for Tech Quiz')

        elif i == 2:
            if self.p2:
                print('Participants for Musical Chair:\n')
                for p in self.p2:
                    print(p)
            else:
                print('No participant for Musical Chair')

    def dise(self, n, d):
        print('\nAvailable Events:')
        for i in range(len(n)):
            print(i + 1, n[i], d[i])


# Event datahoice : 
a = ['Tech Quiz', 'Musical Chair']
d = ['29/04/2026', '30/04/2026']

# Create ONE object only
e = mevent(0, "", "")

# Main loop
while True:
    e.dise(a, d)
    c = int(input('\nEnter event Choice : '))

    if c not in [1, 2]:
        print('Only 2 events, enter 1 or 2')
        continue

    print('\n1.Add participant \n2.Display Participant\n3.Exit')
    ch = int(input('Enter choice : '))

    if ch == 1:
        s = input('Enter name : ')
        e.addp(s, c)

    elif ch == 2:
        e.disp(c)

    elif ch == 3:
        print("Exiting program...")
        break

    else:
        print('You have entered wrong choice')





