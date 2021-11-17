from random import choice
import petri_net

# create list of token
M0 = [1, 2, 3, 2]
ps = [petri_net.Place(m) for m in M0]

# create graph of PetriNet
"""
Sample:
---------------<---------------
|                             |
|--> P0 --> T1 --> P1 --> T2--|
            \           /  \
             \         /    \---> P3
              P2 -----/
"""
ts = dict(
    t1=petri_net.Transition(
        [petri_net.In(ps[0])],
        [petri_net.Out(ps[1]), petri_net.Out(ps[2])]
    ),
    t2=petri_net.Transition(
        [petri_net.In(ps[1]), petri_net.In(ps[2])],
        [petri_net.Out(ps[3]), petri_net.Out(ps[0])]
    )
)

firing_sequence = [choice(list(ts.keys())) for _ in range(10)]

network = petri_net.PetriNet(ts)
network.run(firing_sequence, ps)
