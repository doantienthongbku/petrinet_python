from random import choice
from petri_net import Place, PetriNet, Transition, In, Out

# initialize list of token
M0 = [1, 2, 3, 2]
ps = [Place(m) for m in M0]

# create graph of PetriNet
"""
Example:
---------------<--------------------
|                                  |
|--> P0 --> *T1* --> P1 --> *T2* --|
             |              /  \
             |             /    \---> P3
             P2 ----------/
"""
ts = dict(
    t1=Transition(
        [In(ps[0])],
        [Out(ps[1]), Out(ps[2])]
    ),
    t2=Transition(
        [In(ps[1]), In(ps[2])],
        [Out(ps[3]), Out(ps[0])]
    )
)

print(ts.keys())

num_fires = 3
# random fire in dict of transitions
firing_sequence = [choice(list(ts.keys())) for _ in range(num_fires)]

# Or you can hand-choice transition will be fire (length = num_fires)
# firing_sequence = ['t1', 't2', 't1']

network = PetriNet(ts)
network.run(firing_sequence, ps)
